from __future__ import division

class Particle():
    def __init__(self,mas,x,y,vx,vy):
        self.mass=mas
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        

par_list=[]

def merge_particle(part1,part2):
    massT=part1.mass+part2.mass
    vxT=(part1.mass*part1.vx+part2.mass*part2.vx)/massT
    vyT=(part1.mass*part1.vy+part2.mass*part2.vy)/massT
    xT=(part1.x+part2.x)/2
    yT=(part1.y+part2.y)/2  
    prt3=Particle(massT,xT,yT,vxT,vyT)
    return prt3
    




