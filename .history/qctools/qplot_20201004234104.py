from typing import List, NoReturn, Tuple
from itertools import cycle

import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import iplot

import numpy as np


def sphere_trace() -> go.Trace:
    u = np.linspace(0, 2*np.pi, 30)
    v = np.linspace(0, 2*np.pi, 30)
    u, v = np.mgrid[0:2*np.pi:100j, 0:2*np.pi:100j]
    # u,v = np.meshgrid(v,u)
    # u = u.flatten()
    # v = v.flatten()

    x = np.sin(u) * np.cos(v)
    y = np.sin(u) * np.sin(v)
    z = np.cos(u)

    # x, y, z = np.meshgrid(x, y, z)
    # print(x, y, z)
    # x = x.flatten()
    # y = y.flatten()
    # z = z.flatten()
    # print(x[:5], y[:5], z[:5])
    return go.Surface(
            x = x,
            y = y,
            z = z,
            opacity=0.1,
            surfacecolor="pink"
    )

def bloch_fig_for_one_qubit(qubit, name="Qubit") -> go.Figure:
    x, y, z = get_bloch_coordinates(qubit)
    line = go.Scatter3d( 
        x = [0,x],
        y = [0,y],
        z = [0,z],
        marker = dict(
            size = 1,
            color = "rgb(84,48,5)"
        ),
        line = dict(
            color = "rgb(84,48,5)",
            width = 6
        ),
        showlegend = False
    )
    scatter =  go.Scatter3d( 
        x = [x],
        y = [y],
        z = [z],
        marker = dict(
            size = 8,
            color = "rgb(84,48,5)"
        ),
        mode = "markers",
        name = name
    )
    fig = go.Figure(
        data = [
            sphere,
            scatter,
            line
            ],
        layout=go.Layout(
            scene = {
                'xaxis_title': r'|-> ==> |+>',
                'yaxis_title': r'|↺> ==> |↻>',
                'zaxis_title': r'|0> ==> |1>'
            }
        )
    )
    return fig

def get_bloch_coordinates(qubit: np.ndarray) -> Tuple[float, float, float]:
    def get_x(qubit):
        qubit_x = 1. / np.sqrt(2.0) * np.array([[1, 1], [1, -1]]) @ qubit
        prob_0 = (qubit_x.item(0) * qubit_x.item(0).conjugate()).real
        prob_1 = (qubit_x.item(1) * qubit_x.item(1).conjugate()).real
        return prob_0 - prob_1
    def get_y(qubit):
        qubit_y = 1. / np.sqrt(2.0) * np.array([[1, 1], [1, -1]]) @ np.array([[1, 0], [0, -np.complex(0, 1)]]) @ qubit
        prob_0 = (qubit_y.item(0) * qubit_y.item(0).conjugate()).real
        prob_1 = (qubit_y.item(1) * qubit_y.item(1).conjugate()).real
        return prob_0 - prob_1
    def get_z(qubit):
        qubit_z = qubit
        prob_0 = (qubit_z.item(0) * qubit_z.item(0).conjugate()).real
        prob_1 = (qubit_z.item(1) * qubit_z.item(1).conjugate()).real
        return prob_0 - prob_1
    return (get_x(qubit), get_y(qubit), get_z(qubit))

def bloch_fig_for_qubits(qubits: List[np.array]) -> go.Figure:
    traces = []
    color_generator = cycle(px.colors.qualitative.Dark24)
    for i, qubit in enumerate(qubits):
        color = next(color_generator)
        x, y, z = get_bloch_coordinates(qubit)
        line = go.Scatter3d( 
            x = [0,x],
            y = [0,y],
            z = [0,z],
            marker = dict(
                size = 1,
                color = color
            ),
            line = dict(
                color = color,
                width = 6
            ),
            showlegend = False
        )
        scatter =  go.Scatter3d( 
            x = [x],
            y = [y],
            z = [z],
            marker = dict(
                size = 8,
                color = color,
            ),
            mode = "markers",
            name = f"Qubit_{i+1}"
        )
        traces.append(line)
        traces.append(scatter)
    fig = go.Figure(
        data = [sphere_trace()] + traces,
        layout=go.Layout(
            scene = {
                'xaxis_title': r'|-> ==> |+>',
                'yaxis_title': r'|↺> ==> |↻>',
                'zaxis_title': r'|0> ==> |1>'
            }
        )
    )
    return fig

def plot_bloch_for_one_qubit(qubit, name="Qubit") -> NoReturn:
    iplot(bloch_fig_for_one_qubit(qubit, name="Qubit"))
    

def plot_bloch_for_qubits(qubits: List[np.array]) -> NoReturn:
    iplot(bloch_fig_for_qubits(qubits))
