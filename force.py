import math as math
# import random

# class Particle (object):
#     """Paticle module"""
#     def __init__ (self, mass=1.0, x=0.0, y=0.0, vx=0.0, vy=0.0):
#         self.mass = mass
#         self.x = x
#         self.y = y
#         self.vx = vx
#         self.vy = vy
#         
#     def __str__ (self):
#         return "(%s, %s, %s, %s, %s)" % (self.mass, self.x, self.y, self.vx, self.vy)

def Acceleration (particles):
    G = 1
    AccList_x = []
    AccList_y = []
    nParticle = len(particles) 
    for iParticle in range (0, nParticle):
        ax = ay = 0.0
        if(particles[iParticle].mass > 1.0e-7):
            for jParticle in range (0, nParticle):
                if(iParticle != jParticle):
                    dx = particles[iParticle].x - particles[jParticle].x
                    dy = particles[iParticle].y - particles[jParticle].y
                    r = math.sqrt(dx*dx + dy*dy)
                    r2 = r**2
                    xhat = dx/r
                    yhat = dy/r
                    ax = ax - G*particles[jParticle].mass*xhat/r2
                    ay = ay - G*particles[jParticle].mass*yhat/r2
            AccList_x.append(ax)
            AccList_y.append(ay)
        else:
            AccList_x.append(0.0)
            AccList_y.append(0.0)
    return AccList_x, AccList_y

def UpdateVelocity (particles, TimeStep):
    ax, ay = Acceleration (particles)
    nParticle = len(particles)
    for iParticle in range(0, nParticle):
        if(particles[iParticle].mass>1.0e-7):
            particles[iParticle].vx = particles[iParticle].vx + ax[iParticle]*TimeStep
            particles[iParticle].vy = particles[iParticle].vy + ay[iParticle]*TimeStep
        else:
            particles[iParticle].vx = particles[iParticle].vy = 0.0
    return particles

def UpdatePosition (particles, TimeStep):
    nParticle = len(particles)
    for iParticle in range(0, nParticle):
        particles[iParticle].x += particles[iParticle].vx*TimeStep
        particles[iParticle].y += particles[iParticle].vy*TimeStep
    return particles

def update_particle_list (particles, dt):
    particles=UpdateVelocity (particles, dt)
    particles=UpdatePosition (particles, dt)
    return particles

# def MakeLogFile (particles, step=1):
#     LogFile = open('LogFile.out', 'w')
#     LogFile.write ("%d\t" % len(particles))
#     LogFile.write ("%d\n\n" % step)
#     for iParticle in range(0, len(particles)):
#         LogFile.write ("%14.10f\t"% particles[iParticle].mass)
#         LogFile.write ("%14.10f\t"% particles[iParticle].x)
#         LogFile.write ("%14.10f\t"% particles[iParticle].y)
#         LogFile.write ("%14.10f\t"% particles[iParticle].vx)
#         LogFile.write ("%14.10f\n"% particles[iParticle].vy)
# 
#     LogFile.close()
#     return 0
#     
# def TimeEvaluation (particles, dt, nt, SaveLogFile=50, SaveXYZFile=100):
#     nParticle = len(particles)
#     OutputFile = open('OutputFile-2.xyz', 'w')
#     for step in range (1, nt):
#         update_particle_list (particles, dt)
#         
#         if(step%SaveLogFile == 0):
#             MakeLogFile (particles, step)
# 
#         if(step%SaveXYZFile == 0):
#             OutputFile.write ("%d\n" % nParticle)
#             OutputFile.write ("MD\n")
#             for iParticle in range(0, nParticle):
# #               OutputFile.write ("%d\t"% (iParticle + 1))
#                 OutputFile.write ("Ar\t")
#                 OutputFile.write ("%12.8f\t"% particles[iParticle].x)
#                 OutputFile.write ("%12.8f\t"% particles[iParticle].y)
#                 OutputFile.write ("%12.8f\n"% 0.0)
# 
#     OutputFile.close()
#     return 0
#     
# def InitializeParticle (nParticle=1, 
#                         origin_x=0.0, origin_y=0.0, 
#                         corner_x=10.0, corner_y=10.0,
#                         LengthScale = 1.0,
#                         VelocityScale=1.0,
#                         MassScale=1.0,
#                         restart=False):
#     
#     particles = []
#     if(restart == False):
#         InitializeParticle = open('InitializeParticle.out', 'w')
#         InitializeParticle.write ("%d\n" % nParticle)
#         for iParticle in range(0, nParticle):
#             InitializeParticle.write ("%d\t" % (iParticle+1))
#             # Mass
#             mass = MassScale*random.uniform(0.0, 1.0)
#             InitializeParticle.write ("%14.10f\t" % mass)
#             
#             # Position
#             xpar = LengthScale*random.uniform(origin_x, corner_x)
#             ypar = LengthScale*random.uniform(origin_y, corner_y)
#             
#             InitializeParticle.write ("%14.10f\t" % xpar)
#             InitializeParticle.write ("%14.10f\t" % ypar)
#             
#             # Velocity
#             vxpar = random.uniform(0.0, 1.0)
#             vypar = random.uniform(0.0, 1.0)
#             dv = math.sqrt(vxpar*vxpar + vypar*vypar)
#             vxpar = VelocityScale*vxpar/dv
#             vypar = VelocityScale*vypar/dv
#             InitializeParticle.write ("%14.10f\t" % vxpar)
#             InitializeParticle.write ("%14.10f\n" % vypar)
#             
#             particle = Particle (mass, xpar, ypar, vxpar, vypar)
#             particles.append (particle)
#             
#         InitializeParticle.close ()
#     else:
#         LogFile = open('LogFile.out', 'r')
#         
#         LogFile.close ()
#     return particles

# 
# par = InitializeParticle (10)
# TimeEvaluation (par, 0.01, 1000)