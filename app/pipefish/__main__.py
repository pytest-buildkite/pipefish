"""
Module load handler for execution via python -m pipefish.

Usage:
    %(exename)s [options] [<args>...]
    %(exename)s (-h | --help)

Options:
    -h --help                  Show this screen
    --junit=<xmlpath>          Process JUnit XML to Markdown
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# {{{ Imports
# System Imports
import sys

# External Imports
from docopt import docopt

# Local Imports
from . import process_junit_xml

# }}}


def main():
    """
    Main Command Line entry point
    """
    args = docopt(__doc__ % {
        'exename': ''.join(sys.argv[0:1]),
    })
    if args.get('--junit') is not None:
        print(process_junit_xml(args['--junit']))
    else:
        print(
            'Please select a processing option either --junit or'
            ' --cobertura.',
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == '__main__':
    main()
