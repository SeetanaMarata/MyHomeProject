import os
import time
from pathlib import Path

import pytest

from decorators import log


def test_log_stdout_success(capsys: pytest.CaptureFixture) -> None:
    """Тест успешного выполнения с выводом в консоль"""

    @log()
    def add(a: int, b: int) -> int:
        return a + b

    result = add(1, 2)
    assert result == 3
    captured = capsys.readouterr()
    assert captured.out == "add ok\n"


def test_log_stdout_error(capsys: pytest.CaptureFixture) -> None:
    """Тест ошибки с выводом в консоль"""

    @log()
    def divide(a: int, b: int) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert captured.out == "divide error: ZeroDivisionError. Inputs: (1, 0), {}\n"


def test_log_file_success(tmp_path: Path) -> None:
    """Тест успешного выполнения с записью в файл"""
    filename = os.path.join(tmp_path, "log.txt")

    @log(filename=filename)
    def multiply(a: int, b: int) -> int:
        return a * b

    result = multiply(3, 4)
    assert result == 12

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == "multiply ok\n"


def test_log_file_error(tmp_path: Path) -> None:
    """Тест ошибки с записью в файл"""
    filename = os.path.join(tmp_path, "log.txt")

    @log(filename=filename)
    def fail_func() -> None:
        raise ValueError("Custom error")

    with pytest.raises(ValueError):
        fail_func()

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == "fail_func error: ValueError. Inputs: (), {}\n"


def test_log_with_kwargs(tmp_path: Path) -> None:
    """Тест функции с именованными аргументами"""
    filename = os.path.join(tmp_path, "log.txt")

    @log(filename=filename)
    def greet(name: str, greeting: str = "Hello") -> str:
        return f"{greeting}, {name}!"

    result = greet("Alice", greeting="Hi")
    assert result == "Hi, Alice!"

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == "greet ok\n"


def test_log_multiple_calls(tmp_path: Path) -> None:
    """Тест нескольких вызовов с накоплением логов"""
    filename = os.path.join(tmp_path, "log.txt")
    call_count = 0

    @log(filename=filename)
    def counter() -> int:
        nonlocal call_count
        call_count += 1
        return call_count

    counter()
    counter()
    counter()

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == "counter ok\n" * 3


def test_log_without_filename(capsys: pytest.CaptureFixture) -> None:
    """Тест явного указания filename=None"""

    @log(filename=None)
    def echo(text: str) -> str:
        return text

    result = echo("Test")
    assert result == "Test"
    captured = capsys.readouterr()
    assert captured.out == "echo ok\n"


def test_log_file_encoding(tmp_path: Path) -> None:
    """Тест обработки юникод-символов"""
    filename = os.path.join(tmp_path, "log.txt")

    @log(filename=filename)
    def russian_greet() -> str:
        return "Привет"

    russian_greet()

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == "russian_greet ok\n"


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
    ],
)
def test_log_with_parameters(capsys: pytest.CaptureFixture, a: int, b: int, expected: int) -> None:
    """Параметризованный тест с различными входными данными"""

    @log()
    def add(a: int, b: int) -> int:
        return a + b

    assert add(a, b) == expected
    captured = capsys.readouterr()
    assert captured.out == "add ok\n"


def test_log_performance(capsys: pytest.CaptureFixture) -> None:
    """Тест производительности декоратора"""

    @log()
    def fast_function() -> None:
        pass

    start = time.perf_counter()
    fast_function()
    duration = time.perf_counter() - start

    # Проверяем что выполнение заняло менее 1 миллисекунды
    assert duration < 0.001

    # Дополнительная проверка, что вывод был записан
    captured = capsys.readouterr()
    assert captured.out == "fast_function ok\n"
