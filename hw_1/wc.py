#!/usr/bin/env python3
import click
from sys import stdin


def stat(content):
    return [content.count("\n"), len(content.split()),
            len(bytes(content, "utf-8"))]


def fmt_as_wc(table):
    assert len(table) > 0, "table is empty"
    fmt = "{{0: >{}}}".format(len(str(table[-1][2])))

    return "\n".join(map(
        lambda row: " ".join(map(lambda i: fmt.format(i), row)),
        table
    ))


@click.command()
@click.argument("files", nargs=-1, type=click.File("r"))
def main(files):
    if len(files) == 0:
        print(fmt_as_wc([stat(stdin.read())]))
        return

    rows = []
    tot = [0, 0, 0, "total"]
    for file in files:
        stats = stat(file.read())
        stats.append(file.name)

        for i in range(3):
            tot[i] += stats[i]
        rows.append(stats)

    if len(files) > 1:
        rows.append(tot)
    print(fmt_as_wc(rows))


if __name__ == "__main__":
    main()
