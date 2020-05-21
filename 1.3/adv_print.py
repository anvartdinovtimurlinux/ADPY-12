def get_chunked_text(text, line_length):
    if line_length:
        chunked_text_list = []
        counter = 0
        for word in text.split():
            counter += len(word)
            if counter > line_length:
                chunked_text_list.append('\n')
                counter = len(word)
            elif chunked_text_list:
                chunked_text_list.append(' ')
                counter += 1
            chunked_text_list.append(word)
        chunked_text = ''.join(chunked_text_list)
    else:
        chunked_text = text
    return chunked_text


def adv_print(*args, **kwargs):
    import sys

    start = kwargs.get('start', '')
    end = kwargs.get('end', '\n')
    sep = kwargs.get('sep', ' ')
    file = kwargs.get('file', sys.stdout)
    flush = kwargs.get('flush', False)
    max_line = kwargs.get('max_line')
    in_file = kwargs.get('in_file')

    text_list = [str(piece) for piece in args]
    text = start + sep.join(text_list) + end
    text_to_print = get_chunked_text(text, max_line)

    if in_file:
        with open(in_file, 'w', encoding='utf-8') as f:
            f.write(text_to_print)

    print(text_to_print, file=file, flush=flush)


adv_print('Lorem ipsum dolor sit amet, consectetur adipiscing elit',
          'Lorem ipsum dolor sit amet',
          5,
          start='!!!!!',
          max_line=20,
          in_file='result.txt')
