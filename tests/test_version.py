from sequgen.__version__ import __version__


def test_version():
    expected = "0.1.0"
    assert __version__ == expected
