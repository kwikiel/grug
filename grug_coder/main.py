import os
from typing import List
import openai
import subprocess
import json

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

openai.api_key = os.getenv("OPENAI_API_KEY")

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

    def apply_reflection(self, signature, previous_code, unit_test_results):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": """You are a Python writing assistant. You will be given your previous implementation of a function,
                a series of unit tests results, and your self-reflection on your previous implementation.
                Always return full implementation of the function with applied changes based on your reflection. Return it in python markdown format.
                """},
                {"role": "user", "content": f" Write robust fixed implementation of  {signature} the previous code is here {previous_code} and the result on the unit tests is {unit_test_results}"},
            ])  
        return (response["choices"][0]["message"]["content"])

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

        return process.returncode == 0, result_path

if __name__ == "__main__":
    generator = CodeGenerator(file_path = "humaneval.json")
    data_sample = generator.data[1:100]

    for data in data_sample:
        signature = data["prompt"]
        filename = data["prompt"].split("def ")[1].split("(")[0]
        function_name = filename
        code = ""

        if os.path.exists(f"solutions/{filename}.py"):
            print(f"Skipping {filename}.py because it already exists. Not generating new code.")
        else:
            response = generator.openai_request(
                system_message="You are a Python writing assistant...",
                user_message=f"Implement in python: {signature}")
            code = generator.extract_python_code(text = response)
            generator.save_code(code, f"{filename}.py")

        if os.path.exists(f"solutions/test_{filename}.py"):
            print(f"Skipping test_{filename}.py because it already exists. Not generating new code.")
        else:
            response = generator.openai_request(
                system_message="You are a Python writing assistant...",
                user_message=f"Write pytest unit tests in python for a function with given signature: {signature}, write just the tests, not the implementation.")
            tests = generator.extract_python_code(text = response)
            generator.save_code(tests, f"test_{filename}.py")
            generator.prepend_line_to_file(filename=f"test_{filename}.py", line = f"from {filename} import {filename}")

        success, result_path = generator.run_pytest(test_file = f"test_{filename}.py", result_file=f"{filename}.txt")

        iteration_count = 0
        while not success and iteration_count < 10:
            with open(result_path, "r") as f:
                unit_test_results = f.read()

            response = generator.apply_reflection(signature, code, unit_test_results)
            reflected_code = generator.extract_python_code(response)
            generator.save_code(reflected_code, f"{filename}.py")
            success, result_path = generator.run_pytest(test_file = f"test_{filename}.py", result_file=f"{filename}.txt")
            iteration_count += 1
            code = reflected_code