import os
import sys


def main():
    usage()


def usage():
    with open(f"{os.path.dirname(__file__)}/usage.md", "rt") as f:
        print(f.read(), file=sys.stderr, flush=True)
