

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

    @staticmethod
    def extract_python_code(text: str) -> str:
        if "```python\n" in text:
            return text.split("```python\n")[1].split("```")[0]
        else:
            return text

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
        with open(filename, "w") as f:
            f.write(code)

    @staticmethod
    def prepend_line_to_file(filename, line):
        with open(filename, "r") as f:
            content = f.read()
        with open(filename, "w") as f:
            f.write(line.strip() + "\n" + content)

    def run_pytest(self, test_file, result_file):
        with open(result_file, "w") as f:
            cmd = ["pytest", test_file]
            process = subprocess.run(cmd, stdout=f, stderr=f)
            if process.returncode != 0:
                print(f"pytest failed with exit code: {process.returncode}")
            else:
                print(f"pytest ran successfully. The results are saved in {result_file}")

if __name__ == "__main__":
    generator = CodeGenerator("humaneval.json")
    data_sample = generator.data[1:10]

    for data in data_sample:
        signature = data["prompt"]
        filename = data["prompt"].split("def ")[1].split("(")[0]
        function_name = filename

        code = generator.extract_python_code(generator.openai_request(
            system_message="You are a Python writing assistant...",
            user_message=f"Implement in python: {signature}")
        )
        generator.save_code(code, f"{filename}.py")

        tests = generator.extract_python_code(generator.openai_request(
            system_message="You are a Python writing assistant...",
            user_message=f"Write pytest unit tests in python for a function with given signature: {signature}, write just the tests, not the implementation")
        )
        generator.save_code(tests, f"test_{filename}.py")

        generator.prepend_line_to_file(f"test_{filename}.py", f"from grug_coder.{filename} import {function_name}")
        generator.run_pytest(f"test_{filename}.py", f"{filename}.txt")
