import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt

def make_variables():

    x_in1 = np.arange(0, 1.1, 0.1)
    x_in2 = np.arange(0, 1.1, 0.1)
    x_in3 = np.arange(0, 1.1, 0.1)
    x_in4 = np.arange(0, 1.1, 0.1)

    x_in1_lo = fuzz.trimf(x_in1, [0, 0, 0.5])
    x_in1_md = fuzz.trimf(x_in1, [0.5, 0.5, 1])
    x_in1_hi = fuzz.trimf(x_in1, [0.5, 1, 1])

    x_in2_lo = fuzz.trimf(x_in2, [0, 0, 0.5])
    x_in2_md = fuzz.trimf(x_in2, [0.5, 0.5, 1])
    x_in2_hi = fuzz.trimf(x_in2, [0.5, 1, 1])

    x_in3_lo = fuzz.trimf(x_in3, [0, 0, 0.5])
    x_in3_md = fuzz.trimf(x_in3, [0.5, 0.5, 1])
    x_in3_hi = fuzz.trimf(x_in3, [0.5, 1, 1])

    x_in4_lo = fuzz.trimf(x_in4, [0, 0, 0.5])
    x_in4_md = fuzz.trimf(x_in4, [0.5, 0.5, 1])
    x_in4_hi = fuzz.trimf(x_in4, [0.5, 1, 1])

    fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, figsize=(8, 9))

    ax0.plot(x_in1, x_in1_lo, 'b', linewidth=1.5, label='Baixo')
    ax0.plot(x_in1, x_in1_md, 'g', linewidth=1.5, label='Médio')
    ax0.plot(x_in1, x_in1_hi, 'r', linewidth=1.5, label='Alto')
    ax0.set_title('Variância Wavlet')
    ax0.legend()

    ax1.plot(x_in2, x_in2_lo, 'b', linewidth=1.5, label='Baixo')
    ax1.plot(x_in2, x_in2_md, 'g', linewidth=1.5, label='Medio')
    ax1.plot(x_in2, x_in2_hi, 'r', linewidth=1.5, label='Alto')
    ax1.set_title('Distorsão Wavlet')
    ax1.legend()

    ax2.plot(x_in3, x_in3_lo, 'b', linewidth=1.5, label='Baixo')
    ax2.plot(x_in3, x_in3_md, 'g', linewidth=1.5, label='Medio')
    ax2.plot(x_in3, x_in3_hi, 'r', linewidth=1.5, label='Alto')
    ax2.set_title('Curtose Wavlet')
    ax2.legend()

    ax3.plot(x_in4, x_in4_lo, 'b', linewidth=1.5, label='Baixo')
    ax3.plot(x_in4, x_in4_md, 'g', linewidth=1.5, label='Medio')
    ax3.plot(x_in4, x_in4_hi, 'r', linewidth=1.5, label='Alto')
    ax3.set_title('Entropia Wavlet')
    ax3.legend()

    for ax in (ax0, ax1, ax2, ax3):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

    plt.tight_layout()
    plt.show()

make_variables()