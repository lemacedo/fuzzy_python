import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt

def make_variables():
    # x_in1 = ctrl.Antecedent(np.arange(0, 11, 1),'variancia')
    # x_in2 = ctrl.Antecedent(np.arange(0, 11, 1),'distorsao')
    # x_in3 = ctrl.Antecedent(np.arange(0, 11, 1),'curtose')
    # x_in4 = ctrl.Antecedent(np.arange(0, 11, 1),'entropia')
    # x_out = ctrl.Consequent(np.arange(0, 1, 1),'nota')

    x_in1 = np.arange(0, 1.1, 0.1)
    x_in2 = np.arange(0, 1.1, 0.1)
    x_in3 = np.arange(0, 1.1, 0.1)
    x_in4 = np.arange(0, 1.1, 0.1)
    x_out = np.arange(0, 1, 1)

    # x_in1['aut'] = fuzz.trimf(x_in1, [0, 0, 5])
    # x_in1['fal'] = fuzz.trimf(x_in1, [0, 5, 10])
    x_in1_lo = fuzz.trimf(x_in1, [0, 0, 0.5])
    x_in1_md = fuzz.trimf(x_in1, [0.5, 0.5, 1])
    x_in1_hi = fuzz.trimf(x_in1, [0.5, 1, 1])

    # x_in2['aut'] = fuzz.trimf(x_in2, [0, 0, 4])
    # x_in2['fal'] = fuzz.trimf(x_in2, [0, 4, 10])
    x_in2_lo = fuzz.trimf(x_in2, [0, 0, 0.5])
    x_in2_md = fuzz.trimf(x_in2, [0.5, 0.5, 1])
    x_in2_hi = fuzz.trimf(x_in2, [0.5, 1, 1])

    # x_in3['aut'] = fuzz.trimf(x_in3, [0, 0, 6])
    # x_in3['fal'] = fuzz.trimf(x_in3, [0, 6, 10])
    x_in3_lo = fuzz.trimf(x_in3, [0, 0, 0.5])
    x_in3_md = fuzz.trimf(x_in3, [0.5, 0.5, 1])
    x_in3_hi = fuzz.trimf(x_in3, [0.5, 1, 1])

    # x_in4['aut'] = fuzz.trimf(x_in4, [0, 0, 5])
    # x_in4['fal'] = fuzz.trimf(x_in4, [0, 5, 10])
    x_in4_lo = fuzz.trimf(x_in4, [0, 0, 0.5])
    x_in4_md = fuzz.trimf(x_in4, [0.5, 0.5, 1])
    x_in4_hi = fuzz.trimf(x_in4, [0.5, 1, 1])

    x_out_fal = fuzz.trimf(x_out, [0.5, 1, 1])
    x_out_aut = fuzz.trimf(x_out, [0, 0.5, 0.5])

    # x_out['fal'] = fuzz.trimf(x_out, [5, 10, 10])
    # x_out['aut'] = fuzz.trimf(x_out, [0, 5, 5])

    # x_in1['fal'] = fuzz.interp_membership(x_in1, x_in1['fal'], 5)
    # x_in1['aut'] = fuzz.interp_membership(x_in1, x_in1['aut'], 5)
    # x_in2['fal'] = fuzz.interp_membership(x_in1, x_in1['fal'], 7)
    # x_in2['aut'] = fuzz.interp_membership(x_in1, x_in1['aut'], 7)

    # regra1  = ctrl.Rule(x_in1_lo | x_in2_lo | x_in3_lo, x_out_aut)
    # regra2  = ctrl.Rule(x_in1_lo | x_in2_hi | x_in3_lo, x_out_aut)

    # regra1  = ctrl.Rule(x_in1['aut'] | x_in2['aut'] | x_in3['aut'] | x_in4['aut'], x_out['aut'])
    # regra2  = ctrl.Rule(x_in1['aut'] | x_in2['aut'] | x_in3['aut'] | x_in4['fal'], x_out['aut'])
    # regra3  = ctrl.Rule(x_in1['aut'] | x_in2['aut'] | x_in3['aut'] | x_in4['aut'], x_out['fal'])
    # regra4  = ctrl.Rule(x_in1['aut'] | x_in2['aut'] | x_in3['aut'] | x_in4['fal'], x_out['aut'])
    # regra5  = ctrl.Rule(x_in1['aut'] | x_in2['fal'] | x_in3['aut'] | x_in4['aut'], x_out['fal'])
    # regra6  = ctrl.Rule(x_in1['aut'] | x_in2['fal'] | x_in3['aut'] | x_in4['fal'], x_out['fal'])
    # regra7  = ctrl.Rule(x_in1['aut'] | x_in2['fal'] | x_in3['fal'] | x_in4['aut'], x_out['fal'])
    # regra8  = ctrl.Rule(x_in1['aut'] | x_in2['fal'] | x_in3['fal'] | x_in4['fal'], x_out['fal'])
    # regra9  = ctrl.Rule(x_in1['fal'] | x_in2['aut'] | x_in3['aut'] | x_in4['aut'], x_out['fal'])
    # regra10 = ctrl.Rule(x_in1['fal'] | x_in2['aut'] | x_in3['aut'] | x_in4['fal'], x_out['fal'])
    #
    # x_in1.view()

    # nota_ctrl = ctrl.ControlSystem([regra1, regra2])
    # nota = ctrl.ControlSystemSimulation(nota_ctrl)
    #
    # nota.input['x_in1'] = 0.3
    # nota.input['x_in2'] = 0.3
    #
    # nota.compute()
    # print(nota.output['x_out'])
    # x_out.view(sim=nota)
    # print(x_out)

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

    for ax in (ax0,ax1,ax2,ax3):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

    plt.tight_layout()
    plt.show()

    x_in1_level_lo = fuzz.interp_membership(x_in1, x_in1_lo, 6.5)
    x_in1_level_md = fuzz.interp_membership(x_in1, x_in1_md, 6.5)
    x_in1_level_hi = fuzz.interp_membership(x_in1, x_in1_hi, 6.5)

    x_in2_level_lo = fuzz.interp_membership(x_in2, x_in2_lo, 9.8)
    x_in2_level_md = fuzz.interp_membership(x_in2, x_in2_md, 9.8)
    x_in2_level_hi = fuzz.interp_membership(x_in2, x_in2_hi, 9.8)

make_variables()