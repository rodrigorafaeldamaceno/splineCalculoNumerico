from pycubicspline.pycubicspline import *
import matplotlib.pyplot as plt


def plotXY(x, y):
    sp = Spline2D(x, y)
    s = np.arange(0, sp.s[-1], 0.1)

    print(s)
    print('\n\n\n')

    rx, ry, ryaw, rk = [], [], [], []

    for i_s in s:
        ix, iy = sp.calc_position(i_s)
        rx.append(ix)
        ry.append(iy)
        ryaw.append(sp.calc_yaw(i_s))
        rk.append(sp.calc_curvature(i_s))

    #flg, ax = plt.subplots(1)
    plt.plot(x, y, "xb")
    plt.plot(rx, ry, "-r")


def cabeca():
    # cabeca
    x = [0, -2, -4.5, -5, -5, -4.4, -2, 0,
         2, 4.5, 5, 5, 4.4, 2, 0]

    y = [7.8, 7.5, 6, 5, 2.5, 0, -3, -4,
         -3, 0, 2.5, 5, 6, 7.5, 7.8]
    print('Cabeca: ')

    plotXY(x, y)


def boca():
    x = [-3, -2.5,   0, 2.5,   3,
         2.5, 0, -2.5, -3]
    y = [0,   -0.5, -1.5,   -0.5, 0,
         -1, -2.5, -1, 0]

    print('Boca: ')
    plotXY(x, y)


def olhoEsquerdo():
    x = [-2, -3, -2, -1, -2]
    y = [5, 4.5, 3.8, 4.5, 5]

    print('Olho esquerdo: ')
    plotXY(x, y)
    irisEsquerda()


def irisEsquerda():
    x = [-2, -2.5, -2, -1.5, -2]
    y = [5, 4.5, 4, 4.5, 5]

    print('Iris esquerdo: ')
    plotXY(x, y)


def olhoDireito():
    x = [2, 3, 2, 1, 2]
    y = [5, 4.5, 3.7, 4.5, 5]

    print('Olho esquerdo: ')
    plotXY(x, y)
    irisDireita()


def irisDireita():
    x = [2, 2.5, 2, 1.5, 2]
    y = [5, 4.5, 4, 4.5, 5]

    print('Iris direita: ')
    plotXY(x, y)


def nariz():
    x = [-1, -1.5, 0, 1.5, 1]
    y = [2.8, 1.5, 0.5, 1.5, 2.8]

    print('Nariz: ')
    plotXY(x, y)


cabeca()
boca()
olhoEsquerdo()
olhoDireito()
nariz()

plt.grid(True)
plt.axis("equal")
plt.xlabel("x[m]")
plt.ylabel("y[m]")
plt.legend()

plt.show()
