import particle as pr
import initialize as ini
import force as frc
import matplotlib.pyplot as plt
import matplotlib.animation as animation



# Defining the Initial condition

lx=10
ly=10
par_num=6
max_mass=20
dt=0.01
rc=0.1
max_iter=1000

pr.par_list=ini.initialize(par_num, lx, ly, max_mass)
pr.merged_par_list(pr.par_list, rc)
ini_pos=pr.get_pos(pr.par_list)

fig = plt.figure()
fig.set_dpi(100)
ax = plt.axes(xlim=(-lx,lx), ylim=(-ly,ly))

patch=[]
for i in range(len(ini_pos)):
    patch.append(plt.Circle((ini_pos[i][0],ini_pos[i][1]) ,0.3,fc='b'))

def anim_init():    
    for i in range(len(ini_pos)):
        patch[i].center=(ini_pos[i][0],ini_pos[i][1])
        ax.add_patch(patch[i])
    return patch    



def animate(i):
    frc.update_particle_list(pr.par_list, dt)
    pr.merged_par_list(pr.par_list, rc)
    pos_list=pr.get_pos(pr.par_list)
    for i in range(len(pos_list)):
        patch[i].center=(pos_list[i][0],pos_list[i][1])
    return patch
    


anim=animation.FuncAnimation(fig, animate, init_func=anim_init, frames=max_iter, interval=20 , blit=True)
plt.show()
 



# for t in range(max_iter):
#     print "Iteration %d" % t
#     frc.update_particle_list(pr.par_list, dt)
#     pr.merged_par_list(pr.par_list, rc)    
#     pos_list=pr.get_pos(pr.par_list)
#     print  
#     OutputFile.write ("%d\n" % par_num)
#     OutputFile.write ("MD\n")
#     for i in range(par_num):
# #         OutputFile.write ("Ar  %12.8f  %12.8f  %12.8f \n" % pr.par_list[i].x, pr.par_list[i].y, 0.0)
#         OutputFile.write('{} {} {} {}\n'.format('Ar', pr.par_list[i].x, pr.par_list[i].y, 0.0))
#         OutputFile.write ("%12.8f\t"% pr.par_list[i].x)
#         OutputFile.write ("%12.8f\t"% pr.par_list[i].y)
#         OutputFile.write ("%12.8f\n"% 0.0)


      

