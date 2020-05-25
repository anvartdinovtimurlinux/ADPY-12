import hashlib
from loggers.logger_without_params import logger_without_params as logger1
from loggers.logger_with_params import logger_with_params as logger2


@logger1
def md5_generator(path_to_file,):
    with open(path_to_file, 'r', encoding='utf-8') as f:
        for line in f:
            result = hashlib.md5(line.encode())
            yield result.hexdigest()


@logger2('log2.txt')
def sha256_generator(path_to_file,):
    with open(path_to_file, 'r', encoding='utf-8') as f:
        for line in f:
            result = hashlib.sha256(line.encode())
            yield result.hexdigest()


if __name__ == '__main__':
    print('Результат работы алгоритма MD5:')
    for i, line in enumerate(md5_generator('original_text.txt'), 1):
        print('{}) {}'.format(i, line))

    print('Результат работы алгоритма SHA-256:')
    for i, line in enumerate(sha256_generator('original_text.txt'), 1):
        print('{}) {}'.format(i, line))
