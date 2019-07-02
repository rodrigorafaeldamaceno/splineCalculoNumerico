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

def teste():
     x= [2,4,5,12,19,25,34,43,47,50,55,60]
     y=[3,10,11,14.5,19.5,20,19.5,15,11,10,9,3]

     plotXY(x,y)

teste()
plt.grid(True)
plt.axis("equal")
plt.xlabel("x[m]")
plt.ylabel("y[m]")
plt.legend()

plt.show()