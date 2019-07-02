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

    # flg, ax = plt.subplots(1)
    plt.plot(x, y, "xb")
    plt.plot(rx, ry, "-r")


def rodaTraseira():
    x = [-2.5,
         -1.8,
         -2.5,
         -3.2,
         -2.5,

         -1.8,
         -2.5,
         -3.2,
         -2.5,
         ]

    y = [-0.35,
         -1.05,
         -1.85,
         -1.05,
         -0.35,

         -1.05,
         -1.85,
         -1.05,
         -0.35,
         ]

    print('Roda Traseira: ')
    plotXY(x, y)


def rodaDianteira():
    x = [2.6,
         1.9,
         2.6,
         3.3,
         2.6,

         1.9,
         2.6,
         3.3,
         2.6,
         ]

    y = [-0.35,
         -1.05,
         -1.85,
         -1.05,
         -0.35,

         -1.05,
         -1.85,
         -1.05,
         -0.35,
         ]

    print('Roda Dianteira: ')
    plotXY(x, y)


def corpoCarro():
    x = [-3.98,
         - 3.98,
         - 3.85,
         - 3.0,
         - 2,
         - 0.58,
         0.42,
         1.3,
         2.42,
         3.7,
         4.5,
         4.6]

    y = [-1.05,
         - 0.6,
         - 0.1,
         0.3,
         1.1,
         1.5,
         1.5,
         1.15,
         0.36,
         0.0,
         - 0.5,
         -1.1]

    print('Corpo Carro: ')
    chassi()
    plotXY(x, y)
    # chassi()


def chassi():
    x = [4.6,
         1.94,
         0.38,
         -0.64,
         -2.1,
         -3.98]

    y = [-1.1,
         -1.18,
         -1.18,
         -1.18,
         -1.18,
         -1.05]
    print('Chassi: ')
    plotXY(x, y)


def portaMalas():
    x = [0.58, 2]
    y = [1.38, 2]

    print('Porta Malas: ')
    plotXY(x, y)


def tetoCarro():
    x = [2.46, 3, 3, 3]
    y = [3.04, 4, 5, 6]

    print('Teto Carro: ')
    plotXY(x, y)
    # tetoCarro()


def paraBrisa():
    x = [7, 7.1, 7.2, 7.3, 7.4, 7.5]
    y = [2, 2.1, 2.2, 2.3, 2.4, 2.5]

    print('Para Brisa: ')
    plotXY(x, y)


def capoCarro():
    x = [8.62, 8.61, 8.60, 8.59, 8.58]
    y = [1.62, 1.63, 1.64, 1.65, 1.66]

    print('Capo Carro: ')
    plotXY(x, y)


def vidroDianteiro():
    x = [-0.3,
         0.8,
         1.8,
         0.8,
         -0.1,
         -0.3,
         ]
    y = [1.3,
         1.15,
         0.4,
         0.25,
         0.4,
         1.3
         ]

    print('Vidro Diant: ')
    plotXY(x, y)


def vidroTraseiro():
     x = [-0.5,
          -1.5,
          -2.35,
          -1.5,
          -0.5,
          -0.5
          ]
     y = [1.25,
          1.05,
          0.4,
          0.25,
          0.4,
          1.25
          ]

     print('Vidro Traseiro: ')
     plotXY(x, y)



rodaTraseira()
rodaDianteira()
corpoCarro()
vidroDianteiro()
vidroTraseiro()
# portaMalas()
# tetoCarro()
# paraBrisa()
# capoCarro()


plt.grid(True)
plt.axis("equal")
plt.xlabel("x[m]")
plt.ylabel("y[m]")
plt.legend()

plt.show()
