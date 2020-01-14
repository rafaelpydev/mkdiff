from argparse import ArgumentParser, FileType, SUPPRESS


def parse_args(args=None, namespace=None):
    parse = ArgumentParser(
        prog="mkdiff",
        usage='mkdiff [OPTION]... [FILE1] [FILE2]...',
        description='Make a diff between FILE1 and FILE2',
        add_help=False,
    )

    # Positional args
    parse._positionals.title = 'Positional arguments'
    parse.add_argument(
        dest='file',
        metavar='[FILE1] [FILE2]',
        nargs=2,
        type=FileType('r'),
        help="Files to compare",
    )

    # Optional args
    parse._optionals.title = 'Optional arguments'

    parse.add_argument(
        '-f',
        dest='font_size',
        default=8,
        metavar="[font_size]",
        type=float,
        help='Specify font size (default is 8)',
    )

    parse.add_argument(
        '-h',
        '--help',
        action='help',
        default=SUPPRESS,
        help='Show this help message and exit.'
    )

    parse.add_argument(
        '-l',
        '--add-legend',
        action='store_true',
        dest='legend',
        help='Add legend'
    )

    parse.add_argument(
        '-o',
        dest='filename',
        type=str,
        metavar="[filename]",
        help="Output file name",
    )

    return parse.parse_args(args, namespace)
