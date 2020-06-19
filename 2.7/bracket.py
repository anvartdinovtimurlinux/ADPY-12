from stack import Stack


def is_balanced_brackets(items):
    opening_brackets = {'[': 0, '{': 1, '<': 2, '(': 3}
    closing_brackets = [']', '}', '>', ')']
    stack = Stack()

    for item in items:
        if item not in ['[', '{', '<', '(', ']', '}', '>', ')']:
            return 'В строке есть символы помимо скобок'

        if item in opening_brackets:
            stack.push(item)
        elif stack.size():
            if closing_brackets[opening_brackets[stack.peek()]] == item:
                stack.pop()
            else:
                return 'Небалансированно'
        else:
            return 'Небалансированно'

    return 'Небалансированно' if stack.size() else 'Сбалансированно'


brackets_list = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}',
    '}{}',
    '{{[(])]}}',
    '[[{())}]',
]

for brackets in brackets_list:
    print(is_balanced_brackets(brackets))
