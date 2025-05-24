# Copyright 2024 Bytedance Ltd. and/or its affiliates
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# from . import gsm8k, math, prime_math, prime_code


def _default_compute_score(data_source, solution_str, ground_truth, extra_info=None, sandbox_fusion_url=None, concurrent_semaphore=None):
    if data_source.lower() in ["math", 'guru', "math500", "aime24", "aime25", "hmmt25", "olympiadbench", "scibench"]:
        from . import math_verify
        res = math_verify.compute_score(solution_str, ground_truth)
    elif data_source.lower() in ["crossthinker", 'gpqa', 'supergpqa']:
        from . import choice
        res = choice.compute_score(solution_str, ground_truth)
    elif data_source.lower() == "arcagi":
        from . import grid
        res = grid.compute_score(solution_str, ground_truth)
    else:
        from . import math_verify
        res = math_verify.compute_score(solution_str, ground_truth)

    if isinstance(res, dict):
        return res
    elif isinstance(res, (int, float, bool)):
        return float(res)
    else:
        return float(res[0])
