from datetime import datetime
from functools import wraps


def logger_with_params(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)

        with open('../log.txt', 'a', encoding='utf-8') as f:
            curent_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f'{curent_time}: {function.__name__}(args={args}, kwargs={kwargs}) => {result}\n')

        return result
    return wrapper
