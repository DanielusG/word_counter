# Count the number of characters in your code base

## Reason
When developing a large project, it might be interesting to see how much code has been written so far. For fun or research purposes, it doesn't matter, it can always be interesting data to know

## Usage
```bash
$ python3 count.py <path>
```

## Configuration
You can add some folders or files to the list of folders excluded from the count, this can be useful in case in the code base in addition to the code written by the developer there are configuration files or test texts that should not be counted

You can add files and folders to be excluded in the `.ignorecount` file (inspired by github's `.gitignore`)

## Example .ignorecount
```bash
bin/
config/
.gitignore
```