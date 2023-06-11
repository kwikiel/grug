import pytest
import responses
import black
from hypothesis import given
from hypothesis.strategies import text
from grug_coder.main import CodeGenerator

# We will test on these sample responses
SAMPLE_RESPONSE = {
    "id": "test",
    "object": "chat.completion",
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "Here is some python code: ```python\nprint('Hello, World!')\n```"
            }
        }
    ],
}

@responses.activate
@given(code=text())
def test_code_generator(code):
    responses.add(
        responses.POST,
        "https://api.openai.com/v1/chat/completions",
        json=SAMPLE_RESPONSE,
        status=200,
    )

    # Instantiate the class
    generator = CodeGenerator(file_path = "/home/kacper/grug_coder/grug_coder/humaneval.json")

    # Get the response from the mocked API
    generated_code = generator.openai_request("system message", "user message")

    # Extract the python code from the response
    extracted_code = generator.extract_python_code(generated_code)

    # Use black to check if the extracted code is well-formatted
    try:
        black.format_str(extracted_code, mode=black.FileMode())
    except black.NothingChanged:
        pass
    except Exception as e:
        pytest.fail(f"Black failed to format the code: {e}")

    # Try to execute the code and check if there are any syntax errors
    try:
        exec(extracted_code)
    except Exception as e:
        pytest.fail(f"Exec failed to run the code: {e}")
