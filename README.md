# cookthebooks

Quickly translate gnucash files to ledger format. Translates a gnucash file with over 500 transactions in around .3 seconds on a modern machine.

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
