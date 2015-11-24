from lxml import etree


class IBPlugin(object):
    """
    These processors will mark unnecessary xcode changes as invalid.

    Example: +-1 on rect values, `<animations />` tags, etc.
    """

    @classmethod
    def _xml_changes(klass, chunk):
        # Returns two arrays one for xml additions and other for removals
        try:
            plus = [etree.fromstring(str(line)[1:])
                    for line in chunk if line.is_removed]
            minus = [etree.fromstring(str(line)[1:])
                     for line in chunk if line.is_added]
            return plus, minus
        except etree.XMLSyntaxError:
            return [], []

    @classmethod
    def _is_valid_dimension(klass, hunk, tag, properties):
        minus, plus = klass._xml_changes(hunk)
        if any(x.tag != tag for x in minus + plus):
            return True

        if len(minus) == 1 and len(plus) == 1:
            mnode, pnode = minus[0], plus[0]
            if mnode.tag != pnode.tag or mnode.tag != tag or pnode.tag != tag:
                return True

            is_right_tag = mnode.tag == pnode.tag == tag
            diffs = [abs(float(mnode.attrib[p]) - float(pnode.attrib[p]))
                     for p in properties]
            return not is_right_tag or max(diffs) > 1.0

        return True

    @classmethod
    def process_animations(klass, hunk):
        """
        Marks all `<animations />` changes as invalid.
        """
        minus, plus = klass._xml_changes(hunk)
        return (minus or not plus or
                not all(n.tag == "animations" for n in plus))

    @classmethod
    def process_point(klass, hunk):
        """
        Marks all +- 1 changes on <point> tags invalid.
        """
        return klass._is_valid_dimension(hunk, "point", ['x', 'y'])

    @classmethod
    def process_size(klass, hunk):
        """
        Marks all +- 1 changes on <size> tags invalid.
        """
        return klass._is_valid_dimension(hunk, "size", ['width', 'height'])

    @classmethod
    def process_rect(klass, hunk):
        """
        Marks all +- 1 changes on <rect> tags invalid.
        """
        return klass._is_valid_dimension(hunk, "rect",
                                         ['x', 'y', 'width', 'height'])
