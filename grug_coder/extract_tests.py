import json 

def extract_tests_from_line(data, line_number):
    # Ensure the line number is a valid index
    if line_number < 0 or line_number >= len(data):
        raise ValueError("Invalid line number")

    # Parse the JSON object at the specified line
    task = json.loads(data[line_number])

    # Extract the 'test' field from the JSON object
    test = task.get('example_test')

    # Write the test to a file
    with open('test_ground_truth_has_close_elements.py', 'w') as file:
        file.write(test)

import json

def extract_answers_from_line(data, line_number):
    # Ensure the line number is a valid index
    if line_number < 0 or line_number >= len(data):
        return False

    # Parse the JSON object at the specified line
    try:
        task = json.loads(data[line_number])
    except json.JSONDecodeError:
        return False

    # Extract the 'test' field from the JSON object
    test = task.get('example_test')
    if test is None:
        return False

    # Write the test to a file
    try:
        with open('test_ground_truth_has_close_elements.py', 'w') as file:
            file.write(test)
    except IOError:
        return False

    return True


def get_answers(data, number_of_answers):
    answers = [1 if extract_answers_from_line(data, x) else 0 for x in range(number_of_answers)]
    
    return answers

if __name__ == '__main__':
    with open('humaneval.json', 'r') as file:
        data = file.readlines()

    #print(data)
    #extract_tests_from_line(data, 0)
    #print(extract_answers_from_line(data, 0))
    #print(extract_answers_from_line(data, x) for x in range(163))
    result = get_answers(data, 163)
    print(result)