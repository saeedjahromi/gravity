import particle as pr
import initialize as ini
import force as frc
# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# import string



# Defining the Initial condition

lx=10
ly=10
par_num=6
max_mass=10
dt=0.04
rc=0.1
max_iter=200



# pr.par_list=ini.initialize(par_num, lx, ly, max_mass)
p1=pr.Particle(100,0,0,0,0)
p2=pr.Particle(1,5.0,0,0,-2)
p3=pr.Particle(1,-5.0,0,0,-4)
p4=pr.Particle(1,-9.0,0,0,4)
pr.par_list=[p1,p2,p3,p4]


pr.merged_par_list(pr.par_list, rc)
ini_pos=pr.get_pos(pr.par_list)

fig = plt.figure()
fig.set_dpi(100)
ax = plt.axes(xlim=(-2*lx,2*lx), ylim=(-2*ly,2*ly))


def pcolor():
    color="#%06x" % random.randint(0, 0xFFFFFF)
    return color

patch=[]
for i in range(len(ini_pos)):
    patch.append(plt.Circle((ini_pos[i][0],ini_pos[i][1]) ,0.5,fc=pcolor()))    
#     patch.append(plt.Circle((ini_pos[i][0],ini_pos[i][1]) ,pr.par_list[i].mass/8.0,fc=pcolor()))

def anim_init():    
    for i in range(len(ini_pos)):
        patch[i].center=(ini_pos[i][0],ini_pos[i][1])
        ax.add_patch(patch[i])
    return patch    



def animate(i):
    frc.update_particle_list(pr.par_list, dt)
#     pr.merged_par_list(pr.par_list, rc)
    pos_list=pr.get_pos(pr.par_list)
    for i in range(len(pos_list)):
        patch[i].center=(pos_list[i][0],pos_list[i][1])
    return patch
    

def trace_path(i):
    patch=[]
    frc.update_particle_list(pr.par_list, dt)
#     pr.merged_par_list(pr.par_list, rc)
    pos_list=pr.get_pos(pr.par_list)
    for i in range(len(ini_pos)):
        patch.append(plt.Circle((pos_list[i][0],pos_list[i][1]) ,0.5,fc=pcolor()))
    
    for i in range(len(pos_list)):
        patch[i].center=(pos_list[i][0],pos_list[i][1])
        ax.add_patch(patch[i])
    return patch



anim=animation.FuncAnimation(fig, animate, init_func=anim_init, frames=max_iter, interval=20 , blit=True)
# anim.save('/home/jahromi/Desktop/im.gif', writer='imagemagick', fps=15)
plt.show()



