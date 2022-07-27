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
usage: pynetools.py [-h] [-A] [--pyne] [--vulnage] [--epss] [--crackpot] path

 ______                   _______            _      
(_____ \                 (_______)          | |     
 _____) )   _ ____   ____ _       ___   ___ | | ___ 
|  ____/ | | |  _ \ / _  ) |     / _ \ / _ \| |/___)
| |    | |_| | | | ( (/ /| |____| |_| | |_| | |___ |
|_|     \__  |_| |_|\____)\______)___/ \___/|_(___/ 
       (____/                                       

PyneTools 1.0.1

An installer and updater for the collection of tools that work well with the Pyne Nessus Parser.

positional arguments:
  path        path to store tools

options:
  -h, --help  show this help message and exit
  -A, --ALL   install all tools
  --pyne      install pyne
  --vulnage   install vulnage
  --epss      install epss cli
  --crackpot  install crackpot cli
```
