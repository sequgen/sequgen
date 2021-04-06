from sequgen.__version__ import __version__


def test_version():
    expected = "0.2.0"
    assert __version__ == expected
