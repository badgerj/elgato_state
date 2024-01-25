# elgato_state

This is a program to help change the state of an elgato keylight

Example:
```
python elgato_state/elgato_state_on.py
python elgato_state/elgato_state_off.py
```

## Basis
This is based on the following code snippets:

* A
* B
```
## Features
- Currently only ssh is supported.

### General
- `python elgato_state/elgato_on.py`
- `python elgato_state/elgato_off.py`

### Self testing
- `tox` - run both flake8, plylint, and py3 pytest tests. This also installs all dependencies in .tox in a virtualenv
- `tox -e flake8` - for pep8/flake8 linting of the python files.
- `tox -e pylint` - for more detailed linting of the python files.
- `tox -e py3` - run unit tests against fake data to ensure things work as desired.

*or*

- `python3 -m venv ./.venv`
- `source ./.venv/bin/activate`
- `python -m pip install -r test-requirements.txt`

*then*

- `python -m pytest -v -s` - verbose and stdout

*or*

- `python -m pytest test/test_elgato_state.py::TestElgato::test_bad` - specific test

## Requirements

You will need to have python3 installed on your computer
-  [Python3 Installation](https://www.python.org/downloads/)
-  Monitorontrol 4.2.0 or higher
-  Sleepwatcher 2.2.1 or higher
-  brew install sleepwatcher
-  brew services start sleepwatcher

## Known Issues

None at this time

## Release Notes

- First release only for beta testing
- If you want to commit, please ensure you follow the commit message guidelines:
https://wiki.openstack.org/wiki/GitCommitMessages

## Credits

Thanks to my heros
-

### 1.0.0

Initial release of elgato_state

-----------------------------------------------------------------------------------------------------------

### For more information

* [Python3 Installation](https://www.python.org/downloads/)

**Enjoy!**
