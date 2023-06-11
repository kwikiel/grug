import subprocess
import sys

def test_script():
    # Define command and arguments
    command = [sys.executable, '-m', 'pytest', 'test_below_zero.py']
    
    # Run the command
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Print output and error (if any)
    print("Output:\n", result.stdout.decode())
    print("Error (if any):\n", result.stderr.decode())

    # Return the test result
    if result.returncode == 0:
        print("All tests passed successfully.")
    else:
        print("Some tests failed.")

if __name__ == "__main__":
    test_script()
