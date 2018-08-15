# Have I Been Pwned?
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![license](https://img.shields.io/github/license/marinko-peso/haveibeenpwned.svg)](https://github.com/marinko-peso/haveibeenpwned/blob/master/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![PyPI](https://img.shields.io/pypi/v/haveibeenpwned.svg)](https://pypi.org/project/haveibeenpwned/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/haveibeenpwned.svg)](https://pypi.org/project/haveibeenpwned/)
[![Last Commit](https://img.shields.io/github/last-commit/marinko-peso/haveibeenpwned.svg?maxAge=3600)](https://github.com/marinko-peso/haveibeenpwned/commits/master)

Check if you have an account that has been compromised in a data breach.
This package uses the awesome website https://haveibeenpwned.com/.


## Installation

Available via PyPi.
```
pip install haveibeenpwned
```


## Usage

Available as command with format:
```
haveibeenpwned here.is@the.email [options]
```
Options:
* ```-f``` [--full] get the full response not just status
* ```-h``` [--help]
* ```-v``` [--version]

As an import:
```python
from haveibeenpwned import pwned
from haveibeenpwned import pwned_full
```
* ```pwned``` returns Boolean
* ```pwned_full``` returns dict with Boolean status and additional data as a list


## License

MIT.
