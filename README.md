# Pair-Generator-CLI

This program generates all sets of round robin pairings from a given list.

## Installation

```bash
git clone https://github.com/colour-me-bibi/Pair-Generator-CLI.git
```

## Command Line Usage

```bash
# known input file to stdout
python3 pair-gen.py names.txt

# known input file to known output file
python3 pair-gen.py names.txt -o output.txt

# stdin to stdout
cat names.txt | python3 pair-gen.py

# stdin to known output file
cat names.txt | python3 pair-gen.py -o output.txt
```

## Example Command Line Output

```
--- Pairing Set 1 ---
    sally - None
      bob - jane

--- Pairing Set 2 ---
    sally - bob
     jane - None

--- Pairing Set 3 ---
    sally - jane
     None - bob
```

## Python Module Usage

```python
from pair-gen import generate_pairs

pairing_sets = generate_pairs(["sally", "bob", "jane"])

print(list(pairing_sets))

#  [
#      [('sally', 'bob'), ('jane', 'None')],
#      [('sally', 'jane'), ('None', 'bob')],
#      [('sally', 'None'), ('jane', 'sally')]
#  ]
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
