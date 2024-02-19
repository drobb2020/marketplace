# Supporting Files for a Django Project

I'm sure everyone has their own list of support files that they add to every new Django project, here are mine.

## .flake8

flake8 is a tool designed to enforce the style guide recommendations. As such it is opinionated and can throw numerous errors that you may or may not be interested in. To control it's behavior a configuration file is necessary:

```sh
    [flake8]
    max-line-length = 119
    max-complexity = 10
    select = B,C,E,F,W,T4,B9
    exclude =
        migrations,
        __pycache__,
        manage.py,
        settings.py,
```

- You must specify [flake8] as this is considered an INI file
- The default max line length is 80, I usually adjust it to 119, the same value needs to be reflected in the .ruff.toml file.
- It's a good idea to exclude files from flake8 operations, these are the files you typically don't want to change or modify.

## .ruff.toml

Ruff is the modern replacement for flake8. I actually no longer use flake8, I only install Black and ruff. Here is the current content of my ruff.toml file:

```sh
select = ["E", "F"]
ignore = []

fixable = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "I",
    "N",
    "Q",
    "S",
    "T",
    "W",
    "ANN",
    "ARG",
    "BLE",
    "COM",
    "DJ",
    "DTZ",
    "EM",
    "ERA",
    "EXE",
    "FBT",
    "ICN",
    "INP",
    "ISC",
    "NPY",
    "PD",
    "PGH",
    "PIE",
    "PL",
    "PT",
    "PTH",
    "PYI",
    "RET",
    "RSE",
    "RUF",
    "SIM",
    "SLF",
    "TCH",
    "TID",
    "TRY",
    "UP",
    "YTT"
]
unfixable = []

exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".pytype",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    "venv",
    "__pypackages__",
    "__pycache__",
    "migrations",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "venv",
    "settings.py",
]

line-length = 119

dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

target-version = "py311"
```

## .gitignore

Anyone who is serious about coding and development has a github account and regularly commits their code to github. You should have a .gitignore file to prevent unnecessary files from being committed and stored on github. I use gitignore.io to generate the .gitignore file for my Django projects, and it looks like this:

```sh
# Created by https://www.toptal.com/developers/gitignore/api/django,macos,visualstudiocode
# Edit at https://www.toptal.com/developers/gitignore?templates=django,macos,visualstudiocode

### Django ###
*.log
*.pot
*.pyc
__pycache__/
local_settings.py
db.sqlite3
db.sqlite3-journal
media

# If your build process includes running collectstatic, then you probably don't need or want to include staticfiles/
# in your Git repository. Update and uncomment the following line accordingly.
# <django-project-name>/staticfiles/

### Django.Python Stack ###
# Byte-compiled / optimized / DLL files
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
staticfiles/

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo

# Django stuff:
journal_models.png
django_project/testing_settings.py

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
 .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

### macOS ###
# General
.DS_Store
.AppleDouble
.LSOverride

# Icon must end with two \r
Icon


# Thumbnails
._*

# Files that might appear in the root of a volume
.DocumentRevisions-V100
.fseventsd
.Spotlight-V100
.TemporaryItems
.Trashes
.VolumeIcon.icns
.com.apple.timemachine.donotpresent

# Directories potentially created on remote AFP share
.AppleDB
.AppleDesktop
Network Trash Folder
Temporary Items
.apdisk

### macOS Patch ###
# iCloud generated files
*.icloud

### VisualStudioCode ###
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
!.vscode/*.code-snippets

# Local History for Visual Studio Code
.history/

# Built Visual Studio Code Extensions
*.vsix

### VisualStudioCode Patch ###
# Ignore all local history of files
.history
.ionide

# End of https://www.toptal.com/developers/gitignore/api/django,macos,visualstudiocode
```

## .env - Django Environment Variables

An .env file is used to conceal sensitive information from the general public. The .env file should contain at least the following information:

```sh
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
EMAIL_HOST=your_email_provider_address
EMAIL_USER=sender_email_address
EMAIL_PASSWORD=sender_email_password
DB_NAME=database name
DB_USER=database admin user
DB_PASS=admin password
DB_HOST=host name
DB_PORT=port
```

## .markdownlint.json

If you are writing markdown files with your projects, you should at least provide a README.md file having a markdownlint.json file is invaluable to suppress annoying errors.

```sh
{
  "MD004": false,
  "MD013": false,
  "MD034": false,
  "MD041": false,
  "no-inline-html": {
    "allowed_elements": [
      "img",
      "h1",
      "h3",
      "br",
      "div",
      "p",
      "a",
      "ul",
      "li",
      "details",
      "summary",
      "ol",
      "strong"
    ]
  }
}
```

## LICENSE.txt

Again if you plan to allow public access to your code you need to select an appropriate license that the public need to honor. For myself I use the MIT software License.

```sh
MIT License

Copyright (c) 2024 David Robb

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## README.md

At a minimum you should always provide a readme file with every project you commit to github. My default readme is fairly long so I'm not going to provide the full document here, please see the readme attached to this project.

You can check out my [README Template](https://github.com/drobb2020/drobb-README-template) here.
