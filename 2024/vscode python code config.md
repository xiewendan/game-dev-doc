# 1. [TOC]

------------------------------------------------------------------------------

# 2. problem

Our project is using python in vscode. when commits, the checker has a lot of format error, i have take 10 miniutes to solve it. It disturb me.

------------------------------------------------------------------------------

# 3. idea

* auto formatter
* python static code checker
* quick navigate to the error position

------------------------------------------------------------------------------

# 4. solution

## 4.1. auto formatter

* autopep8(Microsoft): ahere to the pep8 style.
* black formatter(Microsoft): have more strict style then pep8

> i choose autopep8. as it only support python>=3.8, we have build python by ourself

## 4.2. python static code checker

* pylint(Microsoft):
* flake8(Microsoft)

> we can use both

## 4.3. quick navigate to the error position

* as the format of the output log, we can ctl + click to the file line column

  ~~~py
  # vscode
  relative path to workspace.py:line:column message
  abs path.py:line:column message

  # pycharm
  File "relative path to workspace", line no
  File "abs path to workspace", line no
  ~~~

## 4.4. some problem

* c++ lib cause 'reportMissingImports'
  * set stubpath in workspace in settings.json

    ~~~json
    # relative to workspace
    "python.analysis.stubPath": "typings",  
    ~~~

  * set python src in settings.json

    ~~~json
    "python.analysis.extraPaths": [
        "libsrc"
    ],
    ~~~
  
* pylint args not match our project

  ~~~json
  "pylint.args": [
  "--disable=E0015,W1514,W0012,E0013",
  "--max-line-length=100"

  ],
  ~~~

* flake8 args not match our project

  ~~~json
  "flake8.args": [
      "--max-line-length=100",
      "--ignore=W191,W503,E126,H301,H306"
  ],
  ~~~

* print-function check not exist in pylint

  ~~~s
  pip install print-funtion
  ~~~

  * as new version pylint plugin not support IAstroidChecker, you can comment related code in pylint_print.py

    ~~~py
    # from pylint.interfaces import IAstroidChecker

    # __implements__ = (IAstroidChecker,)
    ~~~

------------------------------------------------------------------------------

# 5. conlusion

after config, we will have the error prompt in the editor, i really satify
