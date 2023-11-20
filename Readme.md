# Project: Command-line Utilities and Test Harness

## Project Information

- **Name: Zhenbin Zhang
- **Stevens Login:20018578

## Repository URL

[Link to the GitHub Repository](https://github.com/Joggingbirdie/Project1-Test-Harness)

## Project Details

### Time Spent

I estimate that I spent around 21 hours working on this project.

### Testing Methods

I tested the code using a data-driven approach, creating pairs of input and expected output files for each program. The test harness (`test.py`) reads these files, runs the programs, compares the output, and reports the results.

### Issues and Resolutions

- **Unresolved Bugs or Issues:** No unresolved bugs or issues at the time of submission.

### Difficult Issue Example

One challenging issue I encountered was related to handling edge cases in the flattening process of the `gron.py` program. Some JSON structures caused unexpected behavior. After careful debugging and refining the flattening algorithm, I was able to resolve the issue.

## Extensions Information

I implemented the following three extensions:

1. **More Advanced wc: Multiple Files**
   - **Evaluation:** CAs can evaluate this extension by running tests with multiple input files and checking if the total count is correct.

2. **More Advanced wc: Flags to Control Output**
   - **Evaluation:** CAs can evaluate this extension by running tests with different combinations of flags (e.g., `-l`, `-w`, `-c`) and ensuring the output matches expectations.

3. **More Advanced gron: Control the Base Object Name**
   - **Evaluation:** CAs can evaluate this extension by running tests with the `--obj` flag, providing different base object names, and checking if the output reflects the specified base object.

## Additional Notes

Feeling good after got these code done!
