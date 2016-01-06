IB Unfuck (GIT)
===============

This script will revert all the unneeded changes caused by Interface Builder. For example `<animations />` tags, `+-1` changes on `<rect />`, `<point />`, `<size />`.

<img src="https://cloud.githubusercontent.com/assets/232113/11322350/338255e0-909c-11e5-8e91-9a92372e6226.gif" />

Install
-------

```bash
$ brew install https://raw.githubusercontent.com/Reflejo/ib-unfuck-git/master/Formula/ib-unfuck-git.rb
```

Usage
-------

Important: Make sure your changes are still in unstaged state only then this will remove the unwanted changes.

Run `ibunfuck` command from your repository directory to remove the unwanted changes.