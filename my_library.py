import pandas as pd
import numpy as np
from math import sqrt
from math import log
import math
from decimal import Decimal, ROUND_HALF_UP

import matplotlib.pyplot as plt
from mnk import *


color_combo_s = [
    ('#000000', '#E69F00', '#56B4E9'),  # Черный, оранжевый, голубой
    ('#009E73', '#D55E00', '#CC79A7'),  # Зеленый, оранжево-красный, розовый
    ('#0072B2', "#F0B642", '#CC79A7'),  # Синий, желтый, розовый
    ('#D55E00', '#009E73', '#56B4E9'),  # Оранжевый, зеленый, голубой
    ('#56B4E9', '#E69F00', '#009E73'),  # Голубой, оранжевый, зеленый
    ('#CC79A7', '#0072B2', "#45F042"),  # Розовый, синий, желтый
    ("#9D0A96", '#D55E00', '#009E73'),  # Желтый, оранжевый, зеленый
    ('#E69F00', '#56B4E9', '#CC79A7'),  # Оранжевый, голубой, розовый
    ('#009E73', '#0072B2', '#D55E00'),  # Зеленый, синий, оранжевый
    ('#CC79A7', "#4245F0", '#56B4E9')   # Розовый, желтый, голубой
]

def get_xy_from_file(file_name, x_name, y_name, separator=","):
    linear_data = pd.read_csv(file_name, sep=separator)
    x_es, y_es = list(linear_data[x_name]), list(linear_data[y_name])
    return (x_es, y_es)

def get_all_columns_from_file(file_name, separator=","):
    sp = []
    file = pd.read_csv(file_name, sep=separator)
    columns = file.columns.tolist()
    for column_name in columns:
        sp.append(list(file[column_name]))
    return sp


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
                        line_color = '',
                        point_color='',
                        krest_color='',
                        size=3,
                        color_number=0):
    #Если добавить y_es, то 
    if (not point_color) or (not krest_color) or (not line_color):
        line_color, point_color, krest_color = color_combo_s[color_number % len(color_combo_s)]
    if len(x_err) == 0:
        x_err = [0 for i in x_es]
    if len(y_err) == 0:
        y_err = [0 for i in x_es]
    new_y_es = [k * x + b for x in x_es]
    plt.plot(np.array(x_es), np.array(new_y_es), label=label, color=line_color)
    if len(y_es) > 0:
        plt.errorbar(x_es, y_es, xerr=x_err, yerr=y_err, 
                    fmt='o',  # формат маркера (o - кружок)
                    color=point_color,
                    ecolor=krest_color,  # цвет крестов погрешностей
                    markersize=size)



def set_end(x_label='x', y_label='y', title='', show_origin=False):
    if show_origin:
        plt.xlim(left=0) # Граница x начинается с 0
        plt.ylim(bottom=0) # Граница y начинается с 0
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid()
    plt.legend()
    plt.show()


def my_round(number, ndigits=0):
    # лучше чем round(), который действует по банковскому принципу
    exp = Decimal("1." + "0" * ndigits) if ndigits > 0 else Decimal("1")
    if ndigits == 0:
        return int(float(Decimal(str(number)).quantize(exp, rounding=ROUND_HALF_UP)))
    else:
        return float(Decimal(str(number)).quantize(exp, rounding=ROUND_HALF_UP))


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
