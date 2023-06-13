from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    for group in paren_string.split():
        depth = current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                depth = max(depth, current_depth)
            elif char == ')':
                current_depth -= 1
        depths.append(depth)
    return depths
