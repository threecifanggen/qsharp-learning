from typing import Callable, Union
from functools import reduce

import numpy as np
from . import const

Qubit = np.ndarray

def measure(bra: Qubit) -> Callable[[Qubit], np.float]:
    """测量

    Args:
        bra (Qubit): 测量的方向

    Returns:
        Callable[[Qubit], np.float]: 科里化的函数，带入ket后返回值
    """
    def helper(ket: Qubit):
        return ((bra @ ket) ** 2).sum()
    return helper


def to_bra(ket: Qubit) -> Qubit:
    """从ket转为bra

    Args:
        ket (Qubit): 需要转换的Qubit

    Returns:
        Qubit: 返回值
    """
    return ket.T


def to_ket(bra: Qubit) -> Qubit:
    """从ket转为bra

    Args:
        bra (Qubit): 需要转换的Qubit

    Returns:
        Qubit: 返回值
    """
    return bra.T


q_dict = {
    "0": const.KET_0,
    "1": const.KET_1,
    "+": const.KET_PLUS,
    "-": const.KET_MINUS,
    ">": const.KET_CLOCK,
    "<": const.KET_ANTICLOCK,
}


def ket(qubit_sign: Union[str, int]) -> Qubit:
    """从字符串定义Qubit

    Args:
        qubit_sign (str): 待处理的字符串，仅支持
            （0， 1， +， -， >, <）。

    Returns:
        Qubit: 返回Qubit
    """
    if len(str(qubit_sign)) == 1:
        return q_dict[qubit_sign]
    else:
        return reduce(lambda x, y: np.kron(x, q_dict[y]), list(qubit_sign[1:]), q_dict[qubit_sign[0]])
    
def bra(qubit_sign: Union[int,str]) -> Qubit:
    """从字符串定义Qubit bra

    Args:
        qubit_sign (str): s

    Returns:
        Qubit: 返回值
    """
    return ket(qubit_sign).T
