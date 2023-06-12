import os
from typing import List
import openai
import subprocess
import json

openai.api_key = "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"

def hello_world():
    return ("Hello, World!")

class CodeGenerator:
    def __init__(self, file_path, model="gpt-3.5-turbo"):
        self.data = []
        self.model = model
        self.load_json_dataset(file_path)

    def load_json_dataset(self, file_path):
        with open(file_path, "r") as file:
            for line in file:
                self.data.append(json.loads(line))

    def load_function_names(self) -> List[str]:
        function_names = []
        for obj in self.data:
            function_names.append(obj["prompt"].split("def ")[1].split("(")[0])
        return function_names

    @staticmethod
    def extract_python_code(text: str) -> str:
        # Extract code from backticks
        if "```python\n" in text:
            code = text.split("```python\n")[1].split("```")[0]
        elif "```\n" in text:
            code = text.split("```\n")[1].split("```")[0]
        elif "`" in text:
            code = text.split("`")[1]
        else:
            code = text


        return code


    def openai_request(self, system_message, user_message):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message},
            ],
        )
        return response["choices"][0]["message"]["content"]

    def save_code(self, code, filename):
        dir_path = os.path.join("solutions")
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        with open(os.path.join(dir_path, filename), "w") as f:
            f.write(code)

    def prepend_line_to_file(self, filename, line):
        dir_path = os.path.join("solutions")
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        
        with open(os.path.join(dir_path, filename), "r") as f:
            content = f.read()
        
        with open(os.path.join(dir_path, filename), "w") as f:
            f.write(line.strip() + "\n" + content)

    def run_pytest(self, test_file, result_file=None):
        dir_path = "solutions"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        if result_file is None:
            result_file = "results.txt"
        
        result_path = os.path.join(dir_path, result_file)

        with open(result_path, "w") as f:
            process = subprocess.run(["pytest", os.path.join(dir_path, test_file)], stdout=f, stderr=f)

        
        # Return True if tests passed successfully, otherwise False
        return process.returncode == 0
            


if __name__ == "__main__":
    generator = CodeGenerator(file_path = "/home/kacper/grug_coder/grug_coder/humaneval.json")
    data_sample = generator.data[0:10]

    import json

    data = []

    # Opening JSON file
    with open('/home/kacper/grug_coder/grug_coder/humaneval.json', 'r') as file:
        for line in file:
            data.append(json.loads(line))
    
    function_names = []
    for obj in data:
        function_names.append(obj["prompt"].split("def ")[1].split("(")[0])



    # Convert function_names to a list of dictionaries with the function name as the key

    function_names_dict = {
        x for x in function_names
    }
    
    print(function_names_dict)
    


    for data in data_sample:
        signature = data["prompt"]
        filename = data["prompt"].split("def ")[1].split("(")[0]
        function_name = filename

        # If the filename.py already exists, skip it
        if os.path.exists(f"solutions/{filename}.py"):
            print(f"Skipping {filename}.py because it already exists. Not generating new code.")
        
        else:


            code = generator.extract_python_code(text = generator.openai_request(
                system_message="You are a Python writing assistant...",
                user_message=f"Implement in python: {signature}")
            )
            generator.save_code(code, f"{filename}.py")

        # If the test_filename.py already exists, skip it
        if os.path.exists(f"solutions/test_{filename}.py"):
            print(f"Skipping test_{filename}.py because it already exists. Not generating new code.")

        else:
            tests = generator.extract_python_code(text = generator.openai_request(
                system_message="You are a Python writing assistant...",
                user_message=f"Write pytest unit tests in python for a function with given signature: {signature}, write just the tests, not the implementation.")
            )
            generator.save_code(tests, f"test_{filename}.py")


            generator.prepend_line_to_file(filename=f"test_{filename}.py", line = f"from {filename} import {filename}")


        # Save the results of the test run to the testing_results directory 
        #print(generator.run_pytest(test_file = f"test_{filename}.py", result_file=f"{filename}.txt"))
