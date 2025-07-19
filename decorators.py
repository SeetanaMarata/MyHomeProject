import functools

def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
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

def _write_log(message, filename):
    if filename:
        with open(filename, 'a') as f:
            f.write(message)
    else:
        print(message, end='')