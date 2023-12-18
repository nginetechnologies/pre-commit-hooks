from __future__ import annotations

import argparse
import sys

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    errorLocations = {}

    for filename in args.filenames:
        with open(filename, 'r', encoding="utf8", errors='ignore') as file:
            for lineIndex, line in enumerate(file):
                if "#pragma clang optimize off" in line:
                    if filename not in errorLocations:
                        errorLocations[filename] = []
                    errorLocations[filename].append(lineIndex)


    if len(errorLocations.keys()) > 0:
        print("Found clang pragma in the following locations: ")
        for key, values in errorLocations.items():
            if len(values) > 1:
                lines = ", ".join(str(value) for value in values)
                print(f"{key} - lines {lines}")
            else:
                print(f"{key} - line {values[0]}")
        return 1

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
