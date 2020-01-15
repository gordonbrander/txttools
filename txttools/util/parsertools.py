def add_file_argument(parser):
    parser.add_argument("-f", "--file", type=str, default="-", help="Input file (- for stdin)")
    return parser


def add_output_argument(parser):
    parser.add_argument("-o", "--output", type=str, default="-", help="Output file (- for stdout)")
    return parser


def add_arguments(parser):
    return add_file_argument(add_output_argument(parser))