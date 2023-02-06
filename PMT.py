import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

print("""                                                           
 .__   __.   ______     ______ .___________.     ___      ___   ___    .______   .___  ___. .___________.
|  \ |  |  /  __  \   /      ||           |    /   \     \  \ /  /    |   _  \  |   \/   | |           |
|   \|  | |  |  |  | |  ,----'`---|  |----`   /  ^  \     \  V  /     |  |_)  | |  \  /  | `---|  |----`
|  . `  | |  |  |  | |  |         |  |       /  /_\  \     >   <      |   ___/  |  |\/|  |     |  |     
|  |\   | |  `--'  | |  `----.    |  |      /  _____  \   /  .  \     |  |      |  |  |  |     |  |     
|__| \__|  \______/   \______|    |__|     /__/     \__\ /__/ \__\    | _|      |__|  |__|     |__|       ©                                                                                                                                                                               
""")

# Loading data :
DataFrame = df = pd.read_excel("Data_Input/Data_SP_Amine.xlsx")
print("listes des sondages :")
print(df["Code"].drop_duplicates(inplace=False))

print("Veuillez choisir le Sondage à traiter !")
Sondage: str = input("-->")
print("Traitement du Sondage " + Sondage + " en cours...")

# subplots variables :
font1 = {'family': 'arial', 'color': 'Black', 'size': 10}
font2 = {'family': 'arial', 'color': 'Black', 'size': 8}
Y = df.loc[df['Code'] == Sondage]['Profondeur']
X0 = df.loc[df['Code'] == Sondage]['EM']
X1 = df.loc[df['Code'] == Sondage]['Pl']
X2 = df.loc[df['Code'] == Sondage]['Pf']
X3 = df.loc[df['Code'] == Sondage]['EM/Pl']

Y_max = df['Profondeur'].max()
X0_max = df['EM'].max()
X1_max = df['Pl'].max()
X2_max = df['Pf'].max()
X3_max = df['EM/Pl'].max()


# round up function for X and Y axis
def round_up_y(n):
    return int(math.ceil(n / 5.0)) * 5


def round_up_x0(n):
    return int(math.ceil(n / 10.0)) * 10


def round_up_x1(n):
    return int(math.ceil(n / 100.0)) * 100


def round_up_x2(n):
    return int(math.ceil(n / 1000.0)) * 1000


X0_max = round_up_x2(int(X0_max))
X1_max = round_up_x0(int(X1_max))
X2_max = round_up_x0(int(X2_max))
X3_max = round_up_x1(int(X3_max))
Y_max = round_up_y(int(Y_max))

print(Y_max, X0_max, X1_max, X2_max, X3_max)


def sub_plot1():
    plt.subplot(1, 3, 1)
    plt.plot(X0, Y, color='Orange')
    plt.xlabel("Modules pressiométriques EM (Bars) ", fontdict=font2)
    plt.ylabel("Profondeur (m) ", fontdict=font2)
    ax = plt.gca()
    ax.xaxis.set_label_position('top')
    ax.xaxis.set_ticks_position('top')
    # make arrows
    ax.plot((1), (0), ls="", marker=">", ms=10, color="k",
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot((0), (0), ls="", marker="v", ms=10, color="k",
            transform=ax.get_xaxis_transform(), clip_on=False)

    plt.xlim(0, X0_max)
    plt.ylim(0, Y_max)
    ax.xaxis.set_ticks(np.arange(0, X0_max, X0_max / 5))
    ax.yaxis.set_ticks(np.arange(0, Y_max, 5))

    plt.gca().invert_yaxis()
    plt.grid(visible=True, which='major', color='black', linestyle='-', linewidth=0.2)
    plt.grid(visible=True, which='minor', color='gray', linestyle='-', alpha=0.2, linewidth=0.2)
    plt.minorticks_on()
    plt.legend(["EM"])


def sub_plot2():
    plt.subplot(1, 3, 2)
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    plt.plot(X1, Y, color='Red')
    #    plt.plot(X2, Y, color='Blue')
    plt.xlabel("Pressions limites Pl (Bars)", fontdict=font2)
    plt.ylabel("Profondeur (m) ", fontdict=font2)
    ax = plt.gca()
    ax.xaxis.set_label_position('top')
    ax.xaxis.set_ticks_position('top')
    # make arrows
    ax.plot((1), (0), ls="", marker=">", ms=10, color="k",
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot((0), (0), ls="", marker="v", ms=10, color="k",
            transform=ax.get_xaxis_transform(), clip_on=False)
    plt.xlim(0, X1_max)
    plt.ylim(0, Y_max)
    ax.xaxis.set_ticks(np.arange(0, X1_max, X1_max / 5))
    ax.yaxis.set_ticks(np.arange(0, Y_max, 5))
    plt.gca().invert_yaxis()
    plt.grid(visible=True, which='major', color='black', linestyle='-', linewidth=0.2)
    plt.grid(visible=True, which='minor', color='gray', linestyle='-', alpha=0.2, linewidth=0.2)
    plt.minorticks_on()
    plt.legend(["Pl"])


def sub_plot3():
    plt.subplot(1, 3, 3)
    plt.plot(X3, Y, color='Green')
    plt.xlabel("Rapports EM/Pl ", fontdict=font2)
    plt.ylabel("Profondeur (m) ", fontdict=font2)
    ax = axes = plt.gca()
    axes.xaxis.set_label_position('top')
    ax.xaxis.set_ticks_position('top')
    # make arrows
    ax.plot((1), (0), ls="", marker=">", ms=10, color="k",
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot((0), (0), ls="", marker="v", ms=10, color="k",
            transform=ax.get_xaxis_transform(), clip_on=False)
    plt.xlim(0, X3_max)
    plt.ylim(0, Y_max)
    ax.xaxis.set_ticks(np.arange(0, X3_max, X3_max / 5))
    ax.yaxis.set_ticks(np.arange(0, Y_max, 5))
    plt.gca().invert_yaxis()
    plt.grid(visible=True, which='major', color='black', linestyle='-', linewidth=0.2)
    plt.grid(visible=True, which='minor', color='gray', linestyle='-', alpha=0.2, linewidth=0.2)
    plt.minorticks_on()
    plt.legend(["EM/PL"])


def figure():
    sub_plot1()
    sub_plot2()
    sub_plot3()
    # subplots adjust set_up :
    cm = 1 / 2.54
    fig = plt.gcf()
    fig.size = (20 * cm, 10 * cm)
    fig.tight_layout(pad=1)
    fig.subplots_adjust(top=0.87)
    fig.set_size_inches(11.69, 8.27)

    plt.suptitle("Courbes pressiométriques du sondage " + Sondage + "", ha='center', fontdict=font1, y=0.97)
    plt.savefig("Data_Output/Courbes pressiométriques du sondage " + Sondage + ".pdf", format='pdf', dpi=120,
                orientation='portrait')


while True:
    if Sondage in df["Code"].values:
        figure()
        Sondage = input("-->")
        continue

    elif Sondage in ['EXIT', 'Exit', 'exit', 'QUIT', 'Quit', 'quit']:
        print("Goodbye!")
        break

    else:
        print("Réessayer!")
        Sondage = input("-->")
        continue
