"""
Test modules for pipefish __main__
"""

import pytest


def test_main():
    """
    GIVEN the pipefish.__main__ module entry point WHEN calling
    main without correct arguments THEN the call raises a `SystemExit` with an
    return code of 1
    """
    # Setup
    from pipefish.__main__ import main
    import mock
    fake_docopt = mock.patch(
        'pipefish.__main__.docopt', return_value={}
    )
    with fake_docopt, pytest.raises(SystemExit) as excctxt:
        # Exercise
        main()
    # Verify
    assert excctxt.value.args[0] == 1  # nosec


@pytest.mark.parametrize("option,expect_call", [
    ('--junit', 'process_junit_xml'),
    ('--cobertura', 'process_cobertura_xml'),
])
def test_main_junit(option, expect_call):
    """
    GIVEN the pipefish.__main__ module entry point WHEN calling
    main selecting the specified processing THEN the call processes the sample
    file.
    """
    # Setup
    from pipefish.__main__ import main
    import mock
    samplepath = 'samplepath'
    fake_docopt = mock.patch(
        'pipefish.__main__.docopt', return_value={
            option: samplepath
        }
    )
    fake_process = mock.patch(
        'pipefish.__main__.%s' % (expect_call,), return_value='',
    )
    with fake_docopt, fake_process as mock_process:
        # Exercise
        main()
    # Verify
    mock_process.assert_called_with(samplepath)
