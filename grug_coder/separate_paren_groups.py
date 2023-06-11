from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = []
    for char in paren_string:
        if char == ' ':
            continue
        elif char == '(':
            stack.append('')
        elif char == ')':
            top = stack.pop()
            if stack:
                stack[-1] += top + char
            else:
                result.append(top + char)
        else:
            if not stack:
                result.append(char)
            else:
                stack[-1] += char
    return result