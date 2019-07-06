"""
Utility functions for processing JUnit XML reports
"""

import defusedxml.cElementTree as ET


def process_junit_xml(filepath):
    """
    Converts a JUnit XML file into a Markdown Report.
    """
    doc = ET.parse(filepath)
    for suite in doc.iter('testsuite'):
        cases = list(suite.iter('testcase'))
        errors = int(suite.attrib.get('errors', '0'))
        failures = int(suite.attrib.get('failures', '0'))
        skips = int(suite.attrib.get('skips', '0'))
        collected = int(suite.attrib.get('tests', '0'))
        timetxt = suite.attrib.get('time', '')
        return _process_junit_cases(
            cases, errors, failures, skips, collected, timetxt,
        )
    raise Exception('Failed to process JUnit XML')


def _process_junit_cases(cases, errors, failures, skips, collected, timetxt):
    """
    Produce Markdown from provided case details
    """
    if errors == 0 and failures == 0:
        if collected == 0:
            return _no_tests_collected(timetxt)
        return _all_tests_passed(collected, skips, timetxt)
    return _test_issues(cases, errors, failures, skips, collected, timetxt)


def _no_tests_collected(timetxt):
    """
    Report for empty results
    """
    return 'No test cases found to run (ran in {0} seconds).'.format(
        timetxt,
    )


def _all_tests_passed(collected, skips, timetxt):
    """
    Report for no failures or errors.
    """
    return (
        'All tests passed ({0} tests collected, {1} tests skipped, ran in'
        ' {2} seconds).'.format(
            collected, skips, timetxt,
        )
    )


def _test_issues(cases, errors, failures, skips, collected, timetxt):
    """
    """
    return 'issues'
