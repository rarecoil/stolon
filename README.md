# stolon (alpha)

> This is currently an **alpha grade** project. It has not been tested on multiple dirty password lists. Please file issues and include your list data that is causing breakage. Better yet, file a pull request.

Stolon is a multithreaded password wordlist management script inspired by tooling such as [rurasort](https://github.com/bitcrackcyber/rurasort/) and [PACK](https://github.com/iphelix/pack). Stolon is written in Python 3. You can use Stolon to filter dirty wordlists or dumps into usable password lists.

## Usage

Stolon operates on incoming files and processes data either to stdout or an output file.

````bash
./stolon.py --filters=hashes input_file.txt
````

will read from `input_file.txt` and send cleaned data to stdout. To use an output file, specify `--outfile`.

### Using filters

Stolon uses filters to clean data. Filter chains are created in-order in comma-separated lists. To strip whitespace, hashes, and HTML data from lines, in that order:

````bash
./stolon.py --filters=whitespace,hashes,html input_file.txt
````

To see all available filters, use `--list-filters`.

## License

GNU GPL v3.
