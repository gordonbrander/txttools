# txttools

Simple command-line scripts for manipulating text files.

Using:

```bash
git clone https://github.com/gordonbrander/txttools
cd txttools
pip3 install -e .
```

## Commands

- [txt_clean_whitespace](txttools/bin/clean_whitespace.py): clean up junk whitespace.
- [txt_combine](txttools/bin/combine.py): combine contents of files with a separator.
- [txt_ext](txttools/bin/ext.py): assign a new file extension to a batch of files.
- [txt_textiness](txttools/bin/textiness.py): filter chunks of text based on "textiness". Meant for cleaning out junk text after scraping.
- [txt_unwrap](txttools/bin/unwrap.py): unwrap text in a file.
- [txt_sep](txttools/bin/sep.py): add separators between each chunk of stdin

Do `<cmd> --help` for usage info on each.

TODO

- txt_filter_files: some way of filtering file names based on contents inside. Use for running reports, combining, etc.