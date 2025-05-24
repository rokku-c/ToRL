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

from verl.utils.reward_score.utils import extract_answer
def compute_score(model_output: str, ground_truth: str, timeout_score: float = 0) -> bool:
    model_output = extract_answer(model_output)
    if str(model_output).strip().lower() == str(ground_truth).strip().lower():
        return 1.0
    else:
        return -1.0
