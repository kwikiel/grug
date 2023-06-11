from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    stack = []
    start = None
    for i, c in enumerate(paren_string):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if not stack:
                raise ValueError('Unexpected closing parenthesis')
            start = stack.pop()
            if not stack:
                groups.append(paren_string[start:i+1])
    if stack:
        raise ValueError('Unclosed parenthesis')
    return groups
