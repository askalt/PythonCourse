#!/usr/bin/env python3
import click
from sys import stdin


def tail(lines, n):
    return lines[max(0, len(lines)-n):]


@click.command()
@click.argument("files", nargs=-1, type=click.File("r"))
def main(files):
    if len(files) == 0:
        print("".join(tail(stdin.readlines(), 17)), end="")
        return
    print_name = len(files) > 1
    for i, file in enumerate(files):
        if print_name:
            print(f"==> {file.name} <==")
        lines = file.readlines()
        print("".join(tail(lines, 10)),
              end="" if i == len(files)-1 else "\n")


if __name__ == "__main__":
    main()
