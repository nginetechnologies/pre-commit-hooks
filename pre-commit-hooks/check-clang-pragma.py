from __future__ import annotations

import argparse
import sys

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    for filename in args.filenames:
        with open(filename, 'r') as file:
            for lineIndex, line in enumerate(file):
                if "#pragma clang optimize off" in line:
                    print(f"Found clang pragma in {filename} on line {lineIndex + 1}")
                    return 1
    
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
