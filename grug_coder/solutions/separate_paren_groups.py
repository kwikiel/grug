from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    groups = []
    current_group = ""
    
    for ch in paren_string.replace(" ", ""):
        
        if ch == "(":
            stack.append(ch)
            current_group += ch
            
        else:
            stack.pop()
            current_group += ch
            
            if not stack:
                groups.append(current_group)
                current_group = ""
    
    return groups
