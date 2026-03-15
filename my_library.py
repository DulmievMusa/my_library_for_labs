import pandas as pd
import numpy as np
from math import sqrt
from math import log
import math

import matplotlib.pyplot as plt
from mnk import *



def get_xy_from_file(file_name, x_name, y_name):
    linear_data = pd.read_csv(file_name)
    x_es, y_es = list(linear_data[x_name]), list(linear_data[y_name])
    return (x_es, y_es)


def info_paint_graph_from_xy(x_es, y_es, color='r', label='', linestyle='-', marker='.', markersize=1):
    """styles = ['-', '--', '-.', ':', '-', '--']
    markers = ['.', '.', '.', '.', 'v', 's']
    markersize = 6
    colors = ['b', 'g', 'r', 'm', 'c', 'y']"""
    plt.plot(np.array(x_es), np.array(y_es), color=color, label=label,
                linestyle=linestyle, marker=marker, markersize=markersize)

def info_paint_dots_from_xy(x_es, y_es):
    plt.scatter(x_es, y_es)
    

def get_ln_from_sp(sp):
    return [log(i) for i in sp]


def calc_sigma_different_numbers_of_values(sp, O):
    #sp = [(sigma/value), (sigma, value) ...]
    summ = 0
    for element in sp:
        summ += (element[0]/element[1]) ** 2
    sqrt_summ = sqrt(summ)
    sigma = sqrt_summ * O
    return sigma


def get_round_sp(sp, accuracy):
    return [round(i, accuracy) for i in sp]


def paint_line_function(k, b, x_es, y_es=[], x_err=[], y_err=[], label='',
                         marker_color='red',
                         krest_color='black',
                         size=3):
    #Если добавить y_es, то 
    if len(x_err) == 0:
        x_err = [0 for i in x_es]
    if len(y_err) == 0:
        y_err = [0 for i in x_es]
    new_y_es = [k * x + b for x in x_es]
    plt.plot(np.array(x_es), np.array(new_y_es), label=label)
    if len(y_es) > 0:
        plt.errorbar(x_es, y_es, xerr=x_err, yerr=y_err, 
                    fmt='o',  # формат маркера (o - кружок)
                    color=marker_color,
                    ecolor=krest_color,  # цвет крестов погрешностей
                    markersize=size,)



def set_end(xlabel='x', ylabel='y', title=''):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid()
    plt.legend()
    plt.show()





def create_table(i_es, u_es, q_es, sigma_q_es, epsilon_q_es, r_es, sigma_r_es, epsilon_r_es):
    
    vstavka = ""
    for i in range(10):
        vstavka += f""" {i_es[i]}  & {u_es[i]} & {r_es[i]} & {sigma_r_es[i]} & {epsilon_r_es[i]} & {q_es[i]} & {sigma_q_es[i]} & {epsilon_q_es[i]} \\\\
\\hline \n"""


    text = f"""\\begin{'{table}'}[H]
\\begin{'{center}'}
\\begin{'{tabular}'}{'{|c|c|c|c|c|c|c|c|}'}
\\hline
\\rule{'{0pt}'}{'{12pt}'}
I, мА & U, мВ & R, Ом & $\\sigma_\\text{'{R}'}$, Ом & $\\varepsilon_\\text{'{R}'}, \\% $ & Q, мВт & $\\sigma_\\text{'{Q}'}$, мВт & $\\varepsilon_\\text{'{Q}'}, \\% $\\\\
\\hline
{vstavka}
\\end{'{tabular}'}
\\end{'{center}'}
\\caption{'{40°C}'}
\\end{'{table}'}"""
    return text