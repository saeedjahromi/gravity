# Modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#--------------------------------------------------------------


#--------------------------------------------------
#visulisation initializer
#--------------------------------------------------
fig = plt.figure()
fig.set_dpi(100)
ax = plt.axes(xlim=(0,50), ylim=(0,50))



def get_pos(plist):
	xlist = []
	ylist = []
	zlist = []
	for k in range(len(plist)):
		if plist[k].mass > 0:
			xlist.append(plist[k].x)
			ylist.append(plist[k].y)
	zlist = zip(xlist, ylist)
	return zlist

def animate(zlist):
	for i in range(len(zlist)):
		patch_1 = plt.Circle((pl_1.x,pl_1.y), 0.5, fc='r')	
		patch_2 = plt.Circle((pl_2.x,pl_2.y), 0.45, fc='g')

	



anim = 	animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=20, blit=True)

plt.show()







def plotPoints(ziplist):
	for i in range(len(ziplist)):
		plt.scatter(ziplist[i][0], ziplist[i][1])
	
	plt.show()