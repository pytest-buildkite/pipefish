"""
Test modules for pipefish process_junit
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
    (
        'junit_issues.xml',
        '2 test(s) had failures (ran in 0.097 seconds).\n'
        '\n'
        '\n'
        '```\n'
        'def test_zero():\n'
        '        """\n'
        '        Test an exception\n'
        '        """\n'
        '>       _ = 0 / 0\n'
        'E       ZeroDivisionError: division by zero\n'
        '\n'
        'app/test/test_demo.py:19: ZeroDivisionError\n'
        '```\n'
        '\n'
        '\n'
        '\n'
        '```\n'
        'def test_bad_assert():\n'
        '        """\n'
        '        Test assertion fail\n'
        '        """\n'
        '>       assert 1 + 1 == 3\n'
        'E       assert (1 + 1) == 3\n'
        '\n'
        "'''\n"
        'code snippet\n'
        "'''\n"
        '\n'
        'app/test/test_demo.py:42: AssertionError\n'
        '```\n'
    ),
    (
        'junit_errors.xml',
        '1 test(s) had errors (ran in 0.097 seconds).\n'
        '\n'
        '\n'
        '```\n'
        'Got an error.\n'
        '```\n'
    ),
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


def test_invalid_xml():
    """
    GIVEN a sample JUnit XML containing non-junit XML WHEN calling
    process_junit_xml THEN the call raises an Exception indicating failure to
    process.
    """
    # Setup
    from pipefish.process_junit import process_junit_xml
    samplepath = os.path.join(
        os.path.dirname(get_basedir()), 'data', 'junit_invalid.xml'
    )
    # Exercise
    with pytest.raises(Exception) as excctxt:
        # Exercise
        process_junit_xml(samplepath)
    # Verify
    assert excctxt.value.args[0] == 'Failed to process JUnit XML'  # nosec
