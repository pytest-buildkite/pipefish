"""
Utility functions for processing JUnit XML reports
"""

import collections

import defusedxml.cElementTree as ET

TestSuite = collections.namedtuple('TestSuite', [
    'cases', 'errors', 'failures', 'skips', 'collected', 'timetxt',
])

TestCase = collections.namedtuple('TestCase', [
    'classname', 'filename', 'line', 'name', 'timetxt', 'failures',
])

TestFailure = collections.namedtuple('TestFailure', [
    'message', 'full',
])


def process_junit_xml(filepath):
    """
    Converts a JUnit XML file into a Markdown Report.
    """
    doc = ET.parse(filepath)
    for suite in doc.iter('testsuite'):
        cases = _collect_cases(suite)
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


def _collect_cases(suite):
    """
    Read ElementTree Test Cases
    """
    result = []
    for case in suite.iter('testcase'):
        classname = case.attrib.get('classname', '')
        filename = case.attrib.get('file', '')
        line = case.attrib.get('line', '')
        name = case.attrib.get('name', '')
        timetxt = '{0} seconds'.format(
            case.attrib.get('time', '')
        )
        failures = []
        for failurekind in ('failure', 'error'):
            for failure in case.iter(failurekind):
                message = failure.get('message', '')
                full = failure.text
                failures.append(TestFailure(message, full))
        result.append(TestCase(
            classname, filename, line, name, timetxt, failures,
        ))
    return result


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
    msg = []
    if suite.errors > 0:
        msg.append('{0} test(s) had errors'.format(
            suite.errors
        ))
    if suite.failures > 0:
        msg.append('{0} test(s) had failures'.format(
            suite.failures
        ))
    result = ["{0} (ran in {1}).".format(
        ' and '.join(msg), suite.timetxt,
    )]
    for case in suite.cases:
        if not case.failures:
            continue
        result.extend(
            _markdown_block(failure.full) for failure in case.failures
        )
    return '\n\n'.join(result)


def _markdown_block(text):
    """
    Escape a block of text for markdown and use the fixed width markedown
    syntax.
    """
    result = []
    for line in text.splitlines():
        result.append('> {0}'.format(
            line.replace(
                '\\', '\\\\'
            ).replace(
                '_', '\\_'
            ).replace(
                '<', '\\<'
            ).replace(
                '>', '\\>'
            )
        ))
    return '\n'.join(result)
