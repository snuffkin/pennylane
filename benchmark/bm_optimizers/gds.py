# Copyright 2020 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Gradient descent optimizer benchmark.
"""
import pennylane as qml

from .base_benchmark import BaseBenchmark


class Benchmark(BaseBenchmark):
    """Gradient descent optimizer benchmark."""

    name = "Gradient descent optimizer"
    optimizer = qml.GradientDescentOptimizer()
