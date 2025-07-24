import functools
from typing import Any, Callable, Optional, TypeVar

T = TypeVar("T")


def log(filename: Optional[str] = None) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Декоратор для логирования вызовов функций

    :param filename: Имя файла для записи логов (None - вывод в консоль)
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            func_name = func.__name__
            try:
                result = func(*args, **kwargs)
                message = f"{func_name} ok\n"
                _write_log(message, filename)
                return result
            except Exception as e:
                error_type = type(e).__name__
                inputs = f"Inputs: {args}, {kwargs}"
                message = f"{func_name} error: {error_type}. {inputs}\n"
                _write_log(message, filename)
                raise

        return wrapper

    return decorator


def _write_log(message: str, filename: Optional[str]) -> None:
    """
    Вспомогательная функция для записи логов

    :param message: Сообщение для записи
    :param filename: Имя файла (None - вывод в консоль)
    """
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message)
    else:
        print(message, end="")
