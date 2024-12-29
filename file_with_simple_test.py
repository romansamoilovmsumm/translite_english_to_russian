# Назовите файл как test_example.py или подобное
import test
import pytest


def test_print_aboba(capfd):
    test.print_aboba()
    out, err = capfd.readouterr()
    assert out == "aboba?\n"


@pytest.mark.xfail(reason="Expected to fail")
def test_ex_fail_print_aboba(capfd):
    test.print_aboba()
    out, err = capfd.readouterr()
    assert out == "aboba!\n"
