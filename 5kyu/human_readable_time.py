# https://www.codewars.com/kata/52685f7382004e774f0001f7
import pytest


def make_readable(seconds):
    hours = int(seconds / 3600)
    str_h = str(hours)
    if hours == 0:
        ret_h = "00"
    if hours < 10:
        ret_h = "0" + str_h
    else:
        ret_h = str_h

    seconds -= hours * 3600
    minutes = int(seconds / 60)
    str_m = str(minutes)
    if minutes == 0:
        ret_m = "00"
    if minutes < 10:
        ret_m = "0" + str_m
    else:
        ret_m = str_m

    seconds -= minutes * 60
    str_s = str(seconds)
    if seconds == 0:
        ret_s = "00"
    if seconds < 10:
        ret_s = "0" + str_s
    else:
        ret_s = str_s

    ret_str = ret_h + ":" + ret_m + ":" + ret_s
    return ret_str


@pytest.mark.parametrize("s, expected_result", [
    (65, "00:01:05"),
    (3599, "00:59:59"),
    (359999, "99:59:59"),
    (86400, "24:00:00"),
    (0, "00:00:00")
])
def test_make_readable(s, expected_result):
    assert make_readable(s) == expected_result
