#!/bin/python3

import tracery
from tracery.modifiers import base_english
import json
import sys

def main():

    # Load in the list of filenames
    with open('files.json', 'r') as f:
        filenames = json.load(f)

    rules = dict()

    # Append the rules from each file to the main rules set
    for filename in filenames:
        with open(filename, 'r') as f:
            new_rules = json.load(f)
            rules.update(new_rules)

    # Build the grammar
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)

    # If we run with `python3 main.py coffee` then it will run the
    # #coffee# grammar, which is good for testing.
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            print(grammar.flatten(f"#{arg}#"))
    else:
        # Print out one of the options, with a procgen line delimiter
        print(grammar.flatten("\n#main#"))
        print(grammar.flatten("#linedrawing#"))

if __name__ == "__main__":
    main()
