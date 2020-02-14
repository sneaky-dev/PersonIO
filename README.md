PersonIO
=======
[![Build Status](https://travis-ci.com/timlehr/PersonIO.svg?token=SCm6SLKCgY9E15GKSEUi&branch=master)](https://travis-ci.com/timlehr/PersonIO)

Python implementation of my Tech Task - with a cool name! 

## Requirements

- Python 2.7 / 3.x (tested with Py3.6)
- Python 2.7: pathlib2, six, future
- Python 3.x: six

## Usage

    $ python -m personio --help
    usage: __main__.py [-h] {list,print,write} ...
    
    Personal data IO tool.
    
    optional arguments:
      -h, --help          show this help message and exit
    
    Subcommands:
      {list,print,write}  Available subcommands
        list              List implementations
        print             Print data from file
        write             Write data to file

### 1. Print data
```
$ python -m personio print --help                                                               
usage: __main__.py print [-h] [-if INPUT_FORMAT] input_file printer

Prints data from an input file.

positional arguments:
  input_file            Input file containing the data set to be read.
  printer               Name of the printer to be used.

optional arguments:
  -h, --help            show this help message and exit
  -if INPUT_FORMAT, --input-format INPUT_FORMAT
                        Name of the format to be used for reading.

```
```
$ python -m personio print /Users/Tim/Documents/Github/PersonIO/sample_files/persons.json stdout

Read file with format 'JSON': '/Users/Tim/Documents/Github/PersonIO/sample_files/persons.json'
Print data using 'Stdout' printer ...
           last_name          first_name              street                city                 zip             country               phone
============================================================================================================================================
                Lehr                 Tim          Uferstr. 8              Haiger               35708                  DE    +49 151 61493316
              Rabbit               Peter    16/38 Driver Ave          Moore Park            NSW 2021                  AU     +61 2 9383 4800
          Brickowski              Emmett        Ordinary Ave          Bricksburg           LEGO 2014                  DK     +45 79 50 60 70
```

### 2. Write Data

```
$ python -m personio write --help
usage: __main__.py write [-h] [-if INPUT_FORMAT] [-of OUTPUT_FORMAT]
                         input_file output_file

Writes data to an output file.

positional arguments:
  input_file            Input file containing the data set to be read.
  output_file           Output file to write the data to.

optional arguments:
  -h, --help            show this help message and exit
  -if INPUT_FORMAT, --input-format INPUT_FORMAT
                        Name of the format to be used for reading.
  -of OUTPUT_FORMAT, --output-format OUTPUT_FORMAT
                        Name of the format to be used for writing.
```
```
$ python -m personio write /Users/Tim/Documents/Github/PersonIO/sample_files/persons.json /Users/Tim/TMP/persons2.json --output-format=PrettyJSON

Read file with format 'JSON': '/Users/Tim/Documents/Github/PersonIO/sample_files/persons.json'
Write data to file with format 'PrettyJSON': '/Users/Tim/TMP/persons2.json'
```
```
$ python -m personio write /Users/Tim/Documents/Github/PersonIO/sample_files/persons.json /Users/Tim/TMP/persons.csv                            

Read file with format 'JSON': '/Users/Tim/Documents/Github/PersonIO/sample_files/persons.json'
Write data to file with format 'CSV': '/Users/Tim/TMP/persons.csv'
```
### 3. List available formats / printers
```
$ python -m personio list --help  
usage: __main__.py list [-h] [--filter FILTER_LIST] type

Lists registered implementations.

positional arguments:
  type                  Type of implementation to list: formats, printers

optional arguments:
  -h, --help            show this help message and exit
  --filter FILTER_LIST
```
```
$ python -m personio list formats --filter extension=".json"

List results:
[<PrettyJSONFormat, Name: 'PrettyJSON' (Ext.: '.json', Priority: 0)>,
 <JSONFormat, Name: 'JSON' (Ext.: '.json', Priority: 100)>]
```

```
$ python -m personio list printers 
                         
List results:
[<HTMLPrinter, Name: 'HTML' (Priority: 0)>,
 <StdoutPrinter, Name: 'Stdout' (Priority: 0)>]
```
