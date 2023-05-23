# automatic-disk-collector

Collect evidence from a disk using different module



## Usage

```bash
dacru:git/automatic-disk-collector/ $ python3 main.py -h
usage: main.py [-h] -d DISK_PATH -o OUT_PATH

optional arguments:
  -h, --help            show this help message and exit
  -d DISK_PATH, --disk_path DISK_PATH
                        Path to the image of the disk
  -o OUT_PATH, --out_path OUT_PATH
                        Path to store results

```



## Module

To add a new module:

- create a new folder 

- create the module in this folder
  
  - The method named `run` will be call by the main program

- add `__init__.py` in this folder
  
  - `from .my_module import run`

Have a look on other module to have an example.



## Ignore a module

To ignore a module, just fill `ignored_modules` with the name of the module to ignore
