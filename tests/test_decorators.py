import os
from pathlib import Path
from typing import Any, Callable

import pytest

from decorators import log


def test_log_stdout_success(capsys: pytest.CaptureFixture) -> None:
    @log()
    def add(a: int, b: int) -> int:
        return a + b

    add(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "add ok\n"


def test_log_stdout_error(capsys: pytest.CaptureFixture) -> None:
    @log()
    def divide(a: int, b: int) -> float:
        return a / b

    try:
        divide(1, 0)
    except ZeroDivisionError:
        pass

    captured = capsys.readouterr()
    assert captured.out == "divide error: ZeroDivisionError. Inputs: (1, 0), {}\n"


def test_log_file_success(tmp_path: Path) -> None:
    filename = os.path.join(tmp_path, "log.txt")

    @log(filename=filename)
    def multiply(a: int, b: int) -> int:
        return a * b

    multiply(3, 4)

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == "multiply ok\n"


def test_log_file_error(tmp_path: Path) -> None:
    filename = os.path.join(tmp_path, "log.txt")

    @log(filename=filename)
    def fail_func() -> None:
        raise ValueError("Custom error")

    try:
        fail_func()
    except ValueError:
        pass

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == "fail_func error: ValueError. Inputs: (), {}\n"
