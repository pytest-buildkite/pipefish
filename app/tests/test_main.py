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
        main()  # pylint: disable=assignment-from-no-return
    # Verify
    assert excctxt.value.args[0] == 1  # nosec
