#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: April 29, 2025

# Years 1000-2000 program


def main():
    to_print = []
    for i in range(1000, 2005, 5):
        for n in range(5):
            if n + i <= 2000:
                to_print.append(i + n)

        print(to_print)
        to_print = []


if __name__ == "__main__":
    main()
