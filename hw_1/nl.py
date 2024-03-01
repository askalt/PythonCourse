#!/usr/bin/env python3
from gettext import ngettext
import click

# The idea was taken from https://stackoverflow.com/questions/56351195/how-to-specify-a-default-value-for-argument-list-processed-by-click


class FileDefaultToStdin(click.Argument):
    def __init__(self, *args, **kwargs):
        kwargs['type'] = click.File('r')
        # Allow any number of arguments.
        # We will validate arguments number in process_value().
        kwargs['nargs'] = -1
        super().__init__(*args, **kwargs)

    def process_value(self, ctx, args):
        if len(args) > 1:
            ctx.fail(
                ngettext(
                    "Got unexpected extra argument ({args})",
                    "Got unexpected extra arguments ({args})",
                    len(args)-1,
                ).format(args=" ".join(map(str, args[1:])))
            )
        return super().process_value(ctx, args or ("-", ))


@click.command()
@click.argument("file_args", cls=FileDefaultToStdin)
def main(file_args):
    (file,) = file_args
    line_num = 1
    while (line := file.readline()) != "":
        print("%6s\t%s" % (line_num, line.strip("\n")))
        line_num += 1


if __name__ == "__main__":
    main()
