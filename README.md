# Test executable application

## Install
```
sudo apt-get install python3-pip
sudo -H pip3 install git+https://github.com/catbinary/test_executable_app
```

## Help

```
/> print_date -h

usage: print_date [-h] [--days DAYS] {now,tomorrow,yesterday} ...

Test executable application print_date

positional arguments:
  {now,tomorrow,yesterday}
                        date type
    now                 print datetime.datetime.now()
    tomorrow            print datetime.datetime.now() + 1
    yesterday           print datetime.datetime.now() - 1

optional arguments:
  -h, --help            show this help message and exit
  --days DAYS           default = 0. equals now
```

## Usage

```
user#pc:/$ print_date
2018-01-24
user#pc:/$ print_date now
2018-01-24
user#pc:/$ print_date tomorrow
2018-01-25
user#pc:/$ print_date yesterday
2018-01-23
user#pc:/$ print_date --days -365
2017-01-24
user#pc:/$ print_date --days 31
2018-02-24
```