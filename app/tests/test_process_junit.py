"""
Test modules for pipefish __main__
"""

import os
import sys

import pytest


def get_basedir():
    """
    Locate the current directory of this file
    """
    return os.path.dirname(os.path.abspath(sys.modules[__name__].__file__))


@pytest.mark.parametrize("outcome_filename,expected_outcome", [
    ('junit_issues.xml', 'issues'),
    (
        'junit_notests.xml',
        'No test cases found to run (ran in 0.026 seconds).'
    ),
    (
        'junit_success.xml',
        'All tests passed (3 tests collected, 0 tests skipped,'
        ' ran in 0.146 seconds).'
    ),
])
def test_outcomes(outcome_filename, expected_outcome):
    """
    GIVEN a sample JUnit XML containing specified outcome WHEN calling
    process_junit_xml THEN the call returns markdown highlighting the
    expected outcome.
    """
    # Setup
    from pipefish.process_junit import process_junit_xml
    samplepath = os.path.join(
        os.path.dirname(get_basedir()), 'data', outcome_filename
    )
    # Exercise
    result = process_junit_xml(samplepath)
    # Verify
    assert result == expected_outcome  # nosec
