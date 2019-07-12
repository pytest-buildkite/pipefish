"""
Utility functions for processing Cobertura Coverage XML reports
"""

import defusedxml.cElementTree as ET


def get_coverage_from_cobertura_xml(filepath):
    """
    Reads just the coverage percentage from the Cobertura Coverage XML file.
    """
    doc = ET.parse(filepath)
    for coverage in doc.iter('coverage'):
        coverage_percent = 100.0 * float(coverage.get('line-rate', '0'))
        return coverage_percent
    raise Exception('Failed to process Cobertura Coverage XML')


def process_cobertura_xml(filepath, minimum_coverage=None):
    """
    Converts a Cobertura Coverage XML file into a Markdown Report.
    """
    doc = ET.parse(filepath)
    result = []
    for coverage in doc.iter('coverage'):
        coverage_percent = 100.0 * float(coverage.get('line-rate', '0'))
        lines_covered = coverage.get('lines-covered', '0')
        lines_valid = coverage.get('lines-valid', '0')
        coverage_minimum_statement = ''
        if minimum_coverage is not None:
            coverage_minimum_statement = get_coverage_minimum_statement(
                coverage_percent, minimum_coverage
            )
        result.append('Coverage is %.2f%%%s (%s lines of %s total).' % (
            coverage_percent, coverage_minimum_statement,
            lines_covered, lines_valid,
        ))
        return '\n\n'.join(result)
    raise Exception('Failed to process Cobertura Coverage XML')


def get_coverage_minimum_statement(coverage_percent, minimum_coverage):
    """
    Check if the coverage is above the minimum required coverage and return a
    statement to this effect.
    """
    if coverage_percent >= minimum_coverage:
        return ' meets minimum of %.2f%%' % (minimum_coverage,)
    return ' is below minimum of %.2f%%' % (minimum_coverage,)
