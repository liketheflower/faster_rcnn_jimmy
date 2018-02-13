# @ jimmy shen
# Feb 13, 2018
# this code is used to visualize the L1 loss function used in the fast RCNN 


import matplotlib.pyplot as plt

def vis_l1_loss(steps):
    xs = [0.001*_ for _ in xrange(steps)]
    ys = []
    ys_l2 = [0.5*_**2 for _ in xs]
    for x in xs:
        if x<=1:
          ys.append(0.5*x*x)
        else:
          ys.append(x-0.5)
    plt.plot(xs,ys,'g',label = r'$L_1$')
    plt.plot(xs, ys_l2,'r', label = r'$L_2$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$Loss$')
    plt.title(r'$L_1$'+' loss used in Fast RCNN vs '+r'$L_2$'+' loss'+r'$(0.5*x^2)$')
    plt.legend(loc='upper left',)
    plt.savefig("l1_l2_loss.png")
    plt.show()
if __name__ == "__main__":
    vis_l1_loss(6000)
