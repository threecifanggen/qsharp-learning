import numpy as np

Qubit = np.ndarray

i_ = np.complex(0, 1)

# Ket
KET_0: Qubit = np.array([[1], [0]])
KET_1: Qubit = np.array([[0], [1]])

KET_PLUS: Qubit = 1 / np.sqrt(2.0) * (KET_0 + KET_1)
KET_MINUS: Qubit = 1 / np.sqrt(2.0) * (KET_0 - KET_1)

KET_CLOCK: Qubit = 1 / np.sqrt(2.0) * np.array([[1], [np.complex(0, 1)]])
KET_ANTICLOCK: Qubit = 1 / np.sqrt(2.0) * np.array([[1], [-np.complex(0, 1)]])

# Bra
BRA_0 = KET_0.T
BRA_1 = KET_1.T

BRA_PLUS = KET_PLUS.T
BRA_MINUS = KET_MINUS.T

BRA_CLOCK = KET_CLOCK.T
BRA_ANTICLOCK = KET_ANTICLOCK.T

# One-Qubit Gate
IDENTITY_GATE: Qubit = np.eye(2, 2)
H = HADAMARD = 1 / np.sqrt(2.0) * np.array([[1, 1], [1, -1]])
X = SIGMA_X = np.array([[0, 1], [1, 0]])
Y = SIGMA_Y = np.array([[0, -i_], [i_, 0]])
Z = SIGMA_Z = np.array([[1, 0], [0, -1]])
S: Qubit = np.array([[1, 0], [0, np.exp(i_ * np.pi / 2.0)]])
T: Qubit = np.array([[1, 0], [0, np.exp(i_ * np.pi / 4.0)]])
S_DRAGGER = S.conjugate().transpose()
T_DRAGGER = T.conjugate().transpose()

# Two-Qubits Gate
CNOT = np.array(
    [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
    ]
)