# -*- coding: cp936 -*-
from numpy import *
from matplotlib.pyplot import *
#画线
plot([0, 1], [0, 1])
#plot(0,1)
title("a strait line")
xlabel("x value")
ylabel("y value")
savefig("draw_line.jpg")