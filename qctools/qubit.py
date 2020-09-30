from __future__ import annotations
from typing import Callable, List
from functools import reduce

import numpy as np
from numpy.lib.shape_base import kron

from .expection import NotAllowedShapeOfNumpyArray, SumOfPercentageIsNotOne


import numpy as np

# class Qubit:

#     def __init__(
#             self,
#             up: float,
#             down: float
#         ) -> Qubit:
#         self.up = up
#         self.down = down
#         self.nparray = np.array([[up], [down]])
    
#     def __repr__(self):
#         return f"Qubit({self.up}, {self.down})"

#     @staticmethod
#     def from_nparray(a: np.array) -> Qubit:
#         """numpy array转Qubit

#         Args:
#             a (np.array): 传入的array

#         Raises:
#             NotAllowedShapeOfNumpyArray: 不支持的array维度

#         Returns:
#             Qubit: Qubit
#         """
#         if a.shape != (2, 1):
#             raise NotAllowedShapeOfNumpyArray(
#                 "仅支持(2, 1)维度的numpy array转为Qubit"
#             )
#         else:
#             return Qubit(a[0, 0], a[1, 0])

#     @staticmethod
#     def compose(this: Qubit, that: Qubit) -> Callable[[float, float], Qubit]:
#         def helper(per1: float, per2: float) -> Qubit:
#             if np.abs(per1 + per2 - 1.0) < 1e-5:
#                 return Qubit.from_nparray(
#                     np.sqrt(per1) * this.nparray + np.sqrt(per2) * that.nparray
#                 )
#             else:
#                 raise SumOfPercentageIsNotOne("概率之和不为1")
#         return helper
    

# KET_0 = Qubit(1, 0)
# KET_1 = Qubit(0, 1)
# KET_PLUS = Qubit.from_nparray(1 / np.sqrt(2) * np.array([[1], [1]]))
# KET_MINUS = Qubit.from_nparray(1 / np.sqrt(2) * np.array([[1], [-1]]))
# KET_CLOCKWISE = Qubit.from_nparray(1 / np.sqrt(2) * np.array([[1], [np.complex(0, 1)]]))
# KET_ANTICLOCKWISE = Qubit.from_nparray(1 / np.sqrt(2) * np.array([[1], [-np.complex(0, 1)]]))


# class QuantumState:
#     def __init__(self, *q_list: List[Qubit]):
#         self.value = reduce(lambda x, y: np.kron(x, y.nparray), q_list[1:], q_list[0].nparray)