import os
import openai
import os
import subprocess
# Load your API key from an environment variable or secret management service

openai.api_key = "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"

import re

import json

data = []

# Opening JSON file
with open('humaneval.json', 'r') as file:
    for line in file:
        data.append(json.loads(line))


def extract_python_code(text: str) -> str:
    if "```python\n" in text:
        return text.split("```python\n")[1].split("```")[0]
    else:
        return text


def run_pytest(test_file, result_file):
    with open(result_file, 'w') as f:
        # pytest command
        cmd = ['pytest', test_file]

        # Running the pytest command
        process = subprocess.run(cmd, stdout=f, stderr=f)
        
        # Checking the return code from pytest
        if process.returncode != 0:
            print(f"pytest failed with exit code: {process.returncode}")
        else:
            print(f"pytest ran successfully. The results are saved in {result_file}")


def generate_implementation(signature):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    stop = ["``` ", "```\n"],
    messages=[
                {"role": "system", "content": """You are a Python writing assistant. You will be given your previous implementation of a function,
                a series of unit tests results, and your self-reflection on your previous implementation. Apply the
                necessary changes below by responding only with the improved body of the function. Do not include comments 
            """},
        {"role": "user", "content": f"Implement in python: {signature}"},
    ])

    print("DEBUG generate_implementation START")
    print(response)
    print("DEBUG generate_implementation END")

    return (response["choices"][0]["message"]["content"])

def generate_tests(signature):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
                {"role": "system", "content": """You are a Python writing assistant. You will be given your previous implementation of a function,
                a series of unit tests results, and your self-reflection on your previous implementation. Apply the
                necessary changes below by responding only with the improved body of the function. Do not include comments Follow ALL the following rules:
                - ONLY EVER RESPOND WITH CODE IN PYTHON MARKDOWN BLOCKS, AND NOTHING ELSE
                - write the tests only in pytest
                - NEVER include code comments."""},
        {"role": "user", "content": f"Write pytest unit tests in python for a function with given signature: {signature}, write just the tests, not the implementation"},
    ])  
    return (response["choices"][0]["message"]["content"])

def apply_reflection(signature, previous_code, unit_test_results):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
                {"role": "system", "content": """You are a Python writing assistant. You will be given your previous implementation of a function,
                a series of unit tests results, and your self-reflection on your previous implementation. Apply the
                necessary changes below by responding only with the improved body of the function. Do not include comments Follow ALL the following rules:
                - ONLY EVER RESPOND WITH CODE IN PYTHON MARKDOWN BLOCKS, AND NOTHING ELSE
                - NEVER include code comments."""},
        {"role": "user", "content": f" Write robust fixed implementation of  {signature} the previous code is here {previous_code} and the result on the unit tests is {unit_test_results}"},
    ])  
    return (response["choices"][0]["message"]["content"])


# Save the generated code to a file
def save_code(code, filename):
    with open(filename, "w") as f:
        f.write(code)


def prepend_line_to_file(filename, line):
    # Open the file in read mode, read the contents
    with open(filename, 'r') as f:
        content = f.read()

    # Now open the file in write mode, prepend the line, and write
    with open(filename, 'w') as f:
        f.write(line.strip() + '\n' + content)


if __name__ == "__main__":
    data_sample = data[1:10]
    for data in data_sample:
        signature = data['prompt']
        filename = data["prompt"].split("def ")[1].split("(")[0]
        function_name = filename


        # First run: 
        # Generate code
        # Generate tests
        # Run tests
        # Apply reflection

        # Another run 
        # Read code from file
        # Execute tests
        # Apply reflection



        code = extract_python_code(generate_implementation(signature))
        print(code)

        # # Save code
        save_code(code, f"{filename}.py")

        # # Generate tests
        tests = extract_python_code(generate_tests(signature))
        print(tests)

        # # Save tests
        save_code(tests, f"test_{filename}.py")

        prepend_line_to_file(f"test_{filename}.py", f"from grug_coder.{filename} import {function_name}")


        run_pytest(f"test_{filename}.py", f"{filename}.txt")


        # with open(f"{filename}.py", 'r') as f:
        #     code = f.read()
        #     with open(f"{filename}.txt", 'r') as f2:
        #         tests_results = f2.read()
        #         fixed_code = apply_reflection(signature, code, tests_results)
        #         print(fixed_code)
        #         save_code(extract_python_code(fixed_code), f"{filename}.py")



        # Run tests
        #os.system("pytest tests.py")





