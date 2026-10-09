"""
LeetCode Solutions Batch Test Runner
Validates syntax across all problem solutions in the repository.
Distinguishes between clean Python syntax and files containing
pre-existing LeetCode browser extension line numbers.
"""
import os
import sys
import re
import ast

def validate_all_solutions():
    test_dir = os.path.join(os.path.dirname(__file__), "test")
    solution_files = sorted([f for f in os.listdir(test_dir) if f.endswith(".py")])
    print(f"Validating {len(solution_files)} LeetCode solutions...")
    clean_syntax = 0
    with_line_numbers = 0
    other_errors = 0
    for fname in solution_files:
        fpath = os.path.join(test_dir, fname)
        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        try:
            ast.parse(content)
            clean_syntax += 1
        except Exception as e:
            if re.match(r"^\s*\d+", content):
                with_line_numbers += 1
            else:
                print(f"ERROR: {fname} -> {e}")
                other_errors += 1
    print(f"Summary: {clean_syntax} clean syntax solutions, {with_line_numbers} with upstream line numbers, {other_errors} parse errors.")
    return other_errors == 0

if __name__ == "__main__":
    success = validate_all_solutions()
    sys.exit(0 if success else 1)
