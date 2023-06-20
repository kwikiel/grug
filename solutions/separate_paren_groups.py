from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separates a string containing multiple groups of nested parentheses into a list
    of separate strings.

    Args:
        paren_string: A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of the separate groups of nested parentheses.

    Examples:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
    """
    # Remove all spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Use regex to match all balanced groups of parentheses and check if they are balanced
    matches = []
    pattern = r"\(([^()]*)\)"
    start = 0
    while True:
        match = re.search(pattern, paren_string[start:])
        if not match:
            break

        group = match.group()
        if group.count("(") != group.count(")"):
            return []
        matches.append(group)
        start += match.end()

    return matches
