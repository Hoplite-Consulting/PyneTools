# Pyne Tools

This is a collection of tools that work well with the [Pyne](https://www.github.com/hoplite-consulting/pyne) Nessus Parser.

Written by [Oliver Scotten](https://www.github.com/oliv10).

### Requirements
- Python 3.10.4 or greater

### Usage
- Optional Install requirements
```
pip3 install -r requirements.txt
```

```
usage: pynetools.py [-h] [-A] [-U] [--pyne] [--vulnage] [--epss-cli] [--crackpot-cli] PATH

 ______                   _______            _      
(_____ \                 (_______)          | |     
 _____) )   _ ____   ____ _       ___   ___ | | ___ 
|  ____/ | | |  _ \ / _  ) |     / _ \ / _ \| |/___)
| |    | |_| | | | ( (/ /| |____| |_| | |_| | |___ |
|_|     \__  |_| |_|\____)\______)___/ \___/|_(___/ 
       (____/                                       

PyneTools 2.0.0

An installer and updater for the collection of tools that work well with the Pyne Nessus Parser.

positional arguments:
  PATH            path to store tools

options:
  -h, --help      show this help message and exit
  -A, --ALL       install all tools
  -U, --UPDATE    update installed tools (this will update ALL tools)
  --pyne          install pyne
  --vulnage       install vulnage
  --epss-cli      install epss-cli
  --crackpot-cli  install crackpot-cli
```
