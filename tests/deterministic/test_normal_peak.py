import pytest
import numpy
from sequgen.deterministic.normal_peak import normal_peak


def test_without_height_or_unit_integral():
    t_predict = numpy.linspace(-2.5, 2.5, 11)
    location = 0.0
    actual = normal_peak(t_predict, location)
    expected_height_max = 1 / numpy.sqrt(2 * numpy.pi)
    actual_height_max = actual[t_predict == 0.][0]
    assert actual_height_max == pytest.approx(expected_height_max), "Expected maximum height at t=0"


def test_with_unit_integral():
    t_predict = numpy.linspace(-2.5, 2.5, 11)
    location = 0.0
    actual = normal_peak(t_predict, location, unit_integral=True)
    expected_height_max = 1 / numpy.sqrt(2 * numpy.pi)
    actual_height_max = actual[t_predict == 0.][0]
    assert actual_height_max == pytest.approx(expected_height_max), "Expected maximum height at t=0"


def test_with_height():
    t_predict = numpy.linspace(-2.5, 2.5, 11)
    location = 0.0
    actual = normal_peak(t_predict, location, height=1.0)
    expected_height_max = 1.0
    actual_height_max = actual[t_predict == 0.][0]
    assert actual_height_max == pytest.approx(expected_height_max), "Expected maximum height at t=0"


def test_with_height_and_unit_integral():
    location = 0.0
    t_predict = numpy.linspace(-2.5, 2.5, 11)
    with pytest.raises(AssertionError) as excinfo:
        normal_peak(t_predict, location, height=1.0, unit_integral=True)
    assert "Either define height or set unit_integral to True, but not both." in str(excinfo.value)


def test_with_location25():
    t_predict = numpy.linspace(0, 5, 11)
    location = 2.5
    actual = normal_peak(t_predict, location=location)
    expected_height_max = 1 / numpy.sqrt(2 * numpy.pi)
    actual_height_max = actual[t_predict == location][0]
    assert actual_height_max == pytest.approx(expected_height_max), "Expected maximum height at t=2.5"
    expected = numpy.array([0.0175, 0.0539, 0.1295, 0.2419, 0.3520, 0.3989,
                            0.3520, 0.2419, 0.1295, 0.05399, 0.0175])
    assert actual == pytest.approx(expected, abs=0.0001)


