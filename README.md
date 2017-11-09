# cookthebooks

Simple Python3 program to quickly translate gnucash files to ledger format. Translates a gnucash file with over 500 transactions in around .3 seconds on a modern machine.

## Getting Started
Install the optional dependency for conversion of currency codes to Unicode currency symbols, e.g. GBP becomes £.

```
$ sudo python3 -m pip install money
```

Then clone the git repo:
```
$ git clone https://github.com/colemannugent/cookthebooks
$ cd cookthebooks/
```

Then all you need to is:
```
$ ./cookthebooks.py /path/to/your/file.gnucash
```
By default the program will output all of the converted ledger syntax to STDOUT and all errors or other messages to STDERR for easy redirection to files or other programs.

Note that this program may not work with all versions of GnuCash as there is no published information about the structure of the GnuCash files (that I can find anyway). It works beautifully on my Arch Linux machine running GnuCash 2.7.1.

## Usage
```
usage: cookthebooks.py [-h] [-o OUTFILE] file

Convert gnucash files to ledger files

positional arguments:
  file                  Path to the gnucash file to convert

optional arguments:
  -h, --help            show this help message and exit
  -o OUTFILE, --outfile OUTFILE
                        Output to a file instead of standard output
```

## Implemented
- Basic tranlation from the gnucash format to the ledger format
- Memo lines for splits are preserved as comments
- Unicode currency symbol support

## Not Yet Implemented
- Scheduled transactions
- Budgets
- Slot parsing for splits
- Cleared transactions

## Dependencies
- Python3 (tested with Python 3.6.3)
- money: https://pypi.python.org/pypi/money/

## Goals
- Pre-generate accounts at top of ledger file and impose assertions: http://ledger-cli.org/3.0/doc/ledger3.html#Command-Directives
- Talk about the display() function in the documentation
	- Maybe even have a command line switch to show the contents of the root account
- Check type of account (bank, expense, income) to determine the sign of the entry
	- There might be info in the XML account about the type
- Create a test suite of a few gnucash files
- Add screenshots or maybe a video
