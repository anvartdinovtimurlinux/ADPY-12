import hashlib


def md5_generator_from_file(path_to_file,):
    with open(path_to_file, 'r', encoding='utf-8') as f:
        for line in f:
            result = hashlib.md5(line.encode())
            yield result.hexdigest()


if __name__ == '__main__':
    for i, line in enumerate(md5_generator_from_file('result.txt'), 1):
        print('{}) {}'.format(i, line))
