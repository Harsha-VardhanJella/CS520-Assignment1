To run the tests with coverage for any problem, use the following command from the project directory:
Example for problem 5
pytest -s Tests/test_problem5_eval.py \
    --cov=Codes/chatgpt/COT \
    --cov-branch \
    --cov-report=term-missing \
    --disable-warnings

Make sure you are in the correct path before running:

...\Umass\assignment1\problem5>
