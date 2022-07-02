import timeit

original_setup = """
import numpy as np
from utils import load_json
from boards import OriginalBoard

puzzle = load_json('puzzle.json')['puzzle']

original = OriginalBoard(np.array(puzzle))
"""

original_test = """
original.is_valid
"""

original_time = (timeit.timeit(setup=original_setup, stmt=original_test, number=10000))
print(f"Original Code: {original_time:.4f}")


refactored_setup = """
from boards import RefactoredBoard
from utils import load_json
puzzle = load_json('puzzle.json')['puzzle']
refactored = RefactoredBoard(sum(puzzle, []))
"""

refactored_test = """
refactored.has_violations
"""

refactored_time = (timeit.timeit(setup=refactored_setup, stmt=refactored_test, number=10000))
print(f"Refactor Code: {refactored_time:.4f}")

percent_differance = (original_time - refactored_time) / original_time * 100
print(f"\nPrecnet Differance: {percent_differance:.2f}%")
