import particle as pr
import random


def initialize(par_num,Lx,Ly,max_mass):
    for i in range(par_num):
        mass=random.randint(1, max_mass)
        vx=0.0
        vy=0.0
        x=random.uniform(-Lx, Lx)
        y=random.uniform(-Ly, Ly)
        part=pr.Particle(mass,x,y,vx,vy)
        pr.par_list.append(part)
     
    return pr.par_list

# pr.par_list=initialize(4, 10, 10, 20)
# print pr.par_list
# print pr.par_list[1].mass,pr.par_list[1].x


  

