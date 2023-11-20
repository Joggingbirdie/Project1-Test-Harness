import os
import subprocess
import sys

def run_test(program, test_name):
    input_file = f"test/{program}.{test_name}.in"
    expected_output_file = f"test/{program}.{test_name}.out"
    expected_exit_status_file = f"test/{program}.{test_name}.status"

    # Run the program with STDIN input
    process = subprocess.Popen(["python", f"prog/{program}.py", input_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    actual_output, stderr = process.communicate()
    exit_status = process.returncode

    # Compare output with expected output
    with open(expected_output_file, 'r') as file:
        expected_output = file.read()

    if actual_output == expected_output and exit_status == 0:
        print(f"OK: {program} {test_name}")
    else:
        print(f"FAIL: {program} {test_name} (TestResult.OutputMismatch)")
        print(f"      expected:\n{expected_output}\n\n{' ' * 11}got:\n{actual_output}")

    # Compare exit status with expected exit status
    with open(expected_exit_status_file, 'r') as file:
        expected_exit_status = int(file.read().strip())

    if exit_status != expected_exit_status:
        print(f"FAIL: {program} {test_name} (TestResult.ExitStatusMismatch)")
        print(f"      expected: {expected_exit_status}\n{' ' * 11}got: {exit_status}")

def run_tests(program):
    test_files = [file for file in os.listdir('test') if file.startswith(f"{program}.") and file.endswith('.in')]

    for test_file in test_files:
        test_name = test_file[len(program) + 1:-3]  # Extract test name from filename (e.g., wc.basic)
        run_test(program, test_name)

def main():
    programs = ['wc', 'gron', 'csv']  # Add your choice program here
    total_tests, failed_tests, exit_status_mismatches = 0, 0, 0

    for program in programs:
        run_tests(program)

    print("\nSummary:")
    print(f"OK: {total_tests - failed_tests}")
    print(f"output mismatch: {failed_tests}")
    print(f"total: {total_tests}")

    if exit_status_mismatches > 0:
        sys.exit(1)  # Exit with non-zero status if there were exit status mismatches

if __name__ == "__main__":
    main()
