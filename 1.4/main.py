import loggers.logger_without_params as logger1
# from logger_with_params import logger_with_params as logger2


@logger1.logger_without_params
def summator(*args):
    return sum(args)


if __name__ == '__main__':
    print(summator(1, 2, 3, 4))
    print(summator(1, 2, 3, 4, 5))
    print(summator(1, 2, 3, 4, 5, 6))
