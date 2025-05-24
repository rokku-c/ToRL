import re

boxed_pattern = re.compile(r"\\boxed\{((?:[^{}]|\\{|\\}|(?:\{(?:[^{}]|\\{|\\}|(?:\{(?:[^{}]|\\{|\\}|(?:\{[^{}]*\}))*\}))*\}))*\})")
def extract_answer(solution_str):
    matches = boxed_pattern.findall(solution_str)
    if not matches: return -1.0
    pred = matches[-1][:-1]
    return pred