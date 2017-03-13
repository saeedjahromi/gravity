from __future__ import division
import numpy as np

class Particle():
    def __init__(self,mas,x,y,vx,vy):
        self.mass=mas
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        
    def __str__ (self):
        return "(%s, %s, %s, %s, %s)" % (self.mass, self.x, self.y, self.vx, self.vx)    
        

par_list=[]

def merge_particle(part1,part2):
    massT=part1.mass+part2.mass
    vxT=(part1.mass*part1.vx+part2.mass*part2.vx)/massT
    vyT=(part1.mass*part1.vy+part2.mass*part2.vy)/massT
    xT=(part1.x+part2.x)/2
    yT=(part1.y+part2.y)/2  
    prt3=Particle(massT,xT,yT,vxT,vyT)
    return prt3
    
def merged_par_list(par_list,rc):
    prnum=len(par_list)
    for i in range(prnum):
        for j in range(i+1,prnum):
            m1=par_list[i].mass
            m2=par_list[j].mass             
            if (m1>0 and m2>0):    
                x1=par_list[i].x
                y1=par_list[i].y            
                x2=par_list[j].x
                y2=par_list[j].y                            
                r=np.sqrt((x2-x1)**2+(y2-y1)**2)                     
                if (r<rc):
                    merged_par=merge_particle(par_list[i],par_list[j])
                    zero_par=Particle(0,x1,y1,0,0)
                    par_list[i]=merged_par
                    par_list[j]=zero_par
             
    return par_list
    
    
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


