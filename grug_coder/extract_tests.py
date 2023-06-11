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


if __name__ == '__main__':
    with open('humaneval.json', 'r') as file:
        data = file.readlines()

    extract_tests_from_line(data, 0)