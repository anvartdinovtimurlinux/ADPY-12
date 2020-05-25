import loggers.logger_without_params as logger1
import loggers.logger_with_params as logger2


@logger1.logger_without_params
def summator(*args):
    return sum(args)

@logger2.logger_with_params('log2.txt')
def summator2(*args):
    return sum(args)


if __name__ == '__main__':
    print(summator(1, 2, 3, 4))
    print(summator(1, 2, 3, 4, 5))
    print(summator(1, 2, 3, 4, 5, 6))

    print(summator2(1, 2, 3, 4))
    print(summator2(1, 2, 3, 4, 5))
    print(summator2(1, 2, 3, 4, 5, 6))
    print(summator2(1, 2, 3, 4, 5, 6, 7))
