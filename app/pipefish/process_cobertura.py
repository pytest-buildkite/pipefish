"""
Utility functions for processing Cobertura Coverage XML reports
"""

import defusedxml.cElementTree as ET


def process_cobertura_xml(filepath):
    """
    Converts a Cobertura Coverage XML file into a Markdown Report.
    """
    doc = ET.parse(filepath)
    result = []
    for coverage in doc.iter('coverage'):
        coverage_percent = 100.0 * float(coverage.get('line-rate', '0'))
        lines_covered = coverage.get('lines-covered', '0')
        lines_valid = coverage.get('lines-valid', '0')
        result.append('Coverage is %.2f%% (%s lines of %s total).' % (
            coverage_percent, lines_covered, lines_valid,
        ))
        return '\n\n'.join(result)
    raise Exception('Failed to process Cobertura Coverage XML')
