"""
Test modules for pipefish __main__
"""

import pytest


def test_main():
    """
    GIVEN the pipefish.__main__ module entry point WHEN calling
    main without correct arguments THEN the call raises a SystemExit with an
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


def test_main_junit():
    """
    GIVEN the pipefish.__main__ module entry point WHEN calling
    main selecting junit processing THEN the call processes the sample
    junit file.
    """
    # Setup
    from pipefish.__main__ import main
    import mock
    samplepath = 'samplepath'
    fake_docopt = mock.patch(
        'pipefish.__main__.docopt', return_value={
            '--junit': samplepath
        }
    )
    fake_process = mock.patch(
        'pipefish.__main__.process_junit_xml', return_value='',
    )
    with fake_docopt, fake_process as mock_process:
        # Exercise
        main()
    # Verify
    mock_process.assert_called_with(samplepath)
