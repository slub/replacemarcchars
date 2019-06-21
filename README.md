# replacemarcchars - replace binary MARC characters

replacemarcchars is a commandline command (Python3 program) that takes binary MARC records/lines (e.g. originally stored in a JSON value) as input and replace some characters in it to be really binary MARC compatible.

Following replace methods are available:
* **decimal**: replaces '#29;', '#30;', '#31;' with "\x1D", "\x1E", "\x1F"
* **unicode**: replaces '\u001d', '\u001e', '\u001f' with "\x1D", "\x1E", "\x1F"
* **hex**: replaces '\x1D', '\x1E', '\x1F' with "\x1D", "\x1E", "\x1F"

## Usage

```
replacemarcchars

optional arguments:
  -h, --help                                show this help message and exit
  -replace-method {decimal,unicode,hex}     method for character replacement (default: decimal)
```

* example:
    ```
    replacemarcchars < [BINARY MARC RECORDS/LINES FROM E.G. JSON VALUE] > [TRUE BINARY MARC]
    ```

## Run

* clone this git repo or just download the [replacemarcchars.py](replacemarcchars/replacemarccchars.py) file
* run ./replacemarcchars.py
* for a hackish way to use replacemarcchars system-wide, copy to /usr/local/bin

### Install system-wide via pip

* via pip:
    ```
    sudo -H pip3 install --upgrade [ABSOLUTE PATH TO YOUR LOCAL GIT REPOSITORY OF REPLACEMARCCHARS]
    ```
    (which provides you ```replacemarcchars``` as a system-wide commandline command)