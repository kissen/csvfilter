CSVFILTER

    This is a Python script that allows you to filter CSV files by
    float value. CSV files are read from stdin, output is written to
    stdout.

USAGE

    csvfilter.py [-h] [-c IDX] [-H] [-s SEP] [-l VAL] [-L VAL] [-g VAL] [-G VAL]

ARGUMENTS AND FLAGS

    -h, --help         show this help message and exit
    -c IDX, --col IDX  zero-indexed column to filter on, defaults to 0
    -H, --skip-header  skip the first line (e.g. used for headers)
    -s SEP, --sep SEP  separator string, defaults to ","
    -l VAL, --leq VAL  only print values less than or equal to this value
    -L VAL, --lt VAL   only print values less than this value
    -g VAL, --geq VAL  only print values greater than or equal to this value
    -G VAL, --gt VAL   only print values greater than this value

EXAMPLE

    Say we have a CSV file that looks something like this.

	$ cat drinks.csv
	name; age; favorite_drink
	alice; 16; coffee
	bob; 32; mate
	celia; 24; water
	david; 1; milk

    You can use csvfilter to filter out everyone older than 16.

	$ ./csvfilter.py -c 1 -H -s ';' --gt 16
	bob; 32; mate
	celia; 24; water
