import pytest
from test_data import CROSS_DATA, CHESS_BOARD_DATA, REPORT_DATA, FACTORIAL_DATA, SNOWMAN_DATA, \
    SNOWBALL_DATA, HOURGLASS_DATA


def _data_args(data):
    if not data:
        return
    size = len(data[0])
    names = []
    for entry in data:
        name = []
        for arg in range(size - 1):
            name.append(str(entry[arg]))
        names.append(", ".join(name))
    return names


@pytest.mark.parametrize("arg, expected_output", CROSS_DATA, ids=_data_args(CROSS_DATA))
def test_task_1_cross(capfd, arg, expected_output):
    with capfd.disabled():
        from task_1 import cross
    cross(arg)
    actual_output, _ = capfd.readouterr()
    assert expected_output == actual_output


@pytest.mark.parametrize("arg1, arg2, expected_output", CHESS_BOARD_DATA, ids=_data_args(CHESS_BOARD_DATA))
def test_task_2_chessboard(capfd, arg1, arg2, expected_output):
    with capfd.disabled():
        from task_2 import chess_board
    chess_board(arg1, arg2)
    actual_output, _ = capfd.readouterr()
    assert expected_output == actual_output


@pytest.mark.parametrize("arg, expected_output", HOURGLASS_DATA, ids=_data_args(HOURGLASS_DATA))
def test_task_3_hourglass(capfd, arg, expected_output):
    with capfd.disabled():
        from task_3 import hourglass
    hourglass(arg)
    actual_output, _ = capfd.readouterr()
    assert expected_output == actual_output


@pytest.mark.parametrize("arg1, arg2, expected_output", SNOWBALL_DATA, ids=_data_args(SNOWBALL_DATA))
def test_task_4_snowball(capfd, arg1, arg2, expected_output):
    with capfd.disabled():
        from task_4 import snowball
    snowball(arg1, arg2)
    actual_output, _ = capfd.readouterr()
    assert expected_output == actual_output


@pytest.mark.parametrize("arg, expected_output", SNOWMAN_DATA, ids=_data_args(SNOWMAN_DATA))
def test_task_4_snowman(capfd, arg, expected_output):
    with capfd.disabled():
        from task_4 import snowman
    snowman(arg)
    actual_output, _ = capfd.readouterr()
    assert expected_output == actual_output


@pytest.mark.parametrize("arg, expected_output", FACTORIAL_DATA, ids=_data_args(FACTORIAL_DATA))
def test_task_5_factorial(capfd, arg, expected_output):
    with capfd.disabled():
        from task_5 import factorial
    result = factorial(arg)
    assert expected_output == result


def test_task_5_report(capfd):
    with capfd.disabled():
        from task_5 import report
    report()
    actual_output, _ = capfd.readouterr()
    assert REPORT_DATA == actual_output
