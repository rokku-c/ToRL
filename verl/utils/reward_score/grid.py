import numpy as np
from io import StringIO
from verl.utils.reward_score.utils import extract_answer
import ast
def parse_string_to_grid(s: str) -> np.ndarray:
    s = s.strip()  
    if s.startswith('[') and s.endswith(']'):
        try:
            list_data = ast.literal_eval(s)
            return np.array(list_data)
        except (ValueError, SyntaxError):
            pass

    try:
        return np.loadtxt(StringIO(s), delimiter=' ')
    except (ValueError, OSError):
        pass

    try:
        return np.loadtxt(StringIO(s), delimiter=',')
    except (ValueError, OSError):
        pass

    try:
        parts = s.replace(',', ' ').split() # 将逗号也替换为空格，然后统一分割
        if '\n' in s:
            first_line_parts = s.split('\n')[0].replace(',', ' ').split()
            ncols = len(first_line_parts)
        else:
            ncols = len(parts)

        if ncols > 0: # 确保不是空字符串
            return np.array([float(p) for p in parts]).reshape(-1, ncols)
        else:
            raise ValueError("No numbers found in string.")
    except ValueError:
        pass


def compute_score(prediction, ground_truth):
    prediction = extract_answer(prediction)
    prediction=parse_string_to_grid(str(prediction))
    ground_truth=parse_string_to_grid(str(ground_truth))
    if np.array_equal(prediction, ground_truth):
        return 1.0
    else:
        return -1.0
