#!/usr/bin/python

import git
import sys
import tempfile
import unidiff

from cStringIO import StringIO
from plugins import IBPlugin


class UnfuckPatch(object):
    """
    Contains the logic to call plugins that reverts unnecessary changes
    to the repository.

    >>> unfuck = UnfuckPatch(".")
    >>> unfuck.clear()
    """
    default_processors = [
        IBPlugin.process_rect, IBPlugin.process_size, IBPlugin.process_point,
        IBPlugin.process_animations
    ]

    def __init__(self, path):
        self.repository = git.Repo(path)

    def _clear_patch(self, patch, processors):
        has_changes = False
        for i, patch_piece in enumerate(patch):
            length = len(patch_piece)
            for j, hunk in enumerate(patch_piece[::-1]):
                if not all(p(hunk) for p in processors):
                    continue

                del patch[i][length - j - 1]

            has_changes = has_changes or len(patch[i]) > 0

        return has_changes

    def clear(self, processors=None):
        """
        Starts the process of cleaning unnessesary changes using given
        processors if no processor is given, we'll use the default ones.

        Processors are functions that receive a hunk and return
        `True` or `False`, when any processor returns `False`, the hunk is
        reverted from the working tree.
        """
        processors = processors or self.default_processors
        index = self.repository.index
        patches = index.diff(None, create_patch=True, unified=0)
        for patch in patches:
            try:
                patch = unidiff.PatchSet(StringIO(patch.diff))
            except Exception, e:
                print "Unhandled error %s, continuing..." % str(e)
                continue

            if self._clear_patch(patch, processors):
                patchpath = tempfile.mktemp()
                open(patchpath, 'w').write(str(patch) + '\n')
                self.repository.git.execute(
                    ['git', 'apply', '--recount', '-R', '--unidiff-zero',
                     '--allow-overlap', patchpath]
                )


def main():
    repository_path = sys.argv[1] if len(sys.argv) == 2 else "."
    try:
        unfuck = UnfuckPatch(repository_path)
    except git.exc.InvalidGitRepositoryError:
        print "Error: Current path is not a git repository\n"
        print "Usage: %s <repository path>" % sys.argv[0]

    unfuck.clear()


if __name__ == "__main__":
    main()
