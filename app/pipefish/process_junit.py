"""
Utility functions for processing JUnit XML reports
"""

import collections

import defusedxml.cElementTree as ET

TestSuite = collections.namedtuple('TestSuite', [
    'cases', 'errors', 'failures', 'skips', 'collected', 'timetxt',
])


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
        timetxt = '{0} seconds'.format(
            suite.attrib.get('time', '')
        )
        suiteobj = TestSuite(
            cases, errors, failures, skips, collected, timetxt,
        )
        return _process_junit_cases(suiteobj)
    raise Exception('Failed to process JUnit XML')


def _process_junit_cases(suite):
    """
    Produce Markdown from provided case details
    """
    if suite.errors == 0 and suite.failures == 0:
        if suite.collected == 0:
            return _no_tests_collected(suite)
        return _all_tests_passed(suite)
    return _test_issues(suite)


def _no_tests_collected(suite):
    """
    Report for empty results
    """
    return 'No test cases found to run (ran in {0}).'.format(
        suite.timetxt,
    )


def _all_tests_passed(suite):
    """
    Report for no failures or errors.
    """
    return (
        'All tests passed ({0} tests collected, {1} tests skipped, ran in'
        ' {2}).'.format(
            suite.collected, suite.skips, suite.timetxt,
        )
    )


def _test_issues(suite):  # pylint:disable=unused-argument
    """
    Report details of issues found
    """
    return 'issues'
