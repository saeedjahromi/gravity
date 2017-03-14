import math as math
import random

class _2D_Point(object):
    """2D points"""
    def __init__ (self, x=0., y=0.):
        self.x = x
        self.y = y

    def __str__ (self):
        return "(%s, %s)" % (self.x, self.y)

    def __add__ (self, another):
        point = _2D_Point()
        point.x = self.x + another.x
        point.y = self.y + another.y
        return point

    def __sub__ (self, another):
        point = _2D_Point()
        point.x = self.x - another.x
        point.y = self.y - another.y
        return point

    def scale (self, alpha=1.):
        point = _2D_Point()
        point.x = self.x*alpha
        point.y = self.y*alpha
        return point

    def dot (self, another):
        return self.x*another.x + self.y*another.y

    @property
    def dis (self):
        return math.sqrt(self.dot(self))

    @property
    def unit (self):
        return self.scale (1.0/self.dis)

class Particle (object):
    """paticle"""
    def __init__ (self, mass=1.0, pos=_2D_Point (0.0, 0.0), vel=_2D_Point (0.0, 0.0)):
        self.mass = mass
        self.pos = pos
        self.vel = vel
        
    def __str__ (self):
        return "(%s, %s, %s)" % (self.mass, self.pos, self.vel)

def Acceleration (particles):
    G = 1.0
    AccList = []
    nParticle = len(particles) 
    for iParticle in range (0, nParticle):
        acc = _2D_Point (0.0, 0.0)
        for jParticle in range (0, nParticle):
            if(iParticle != jParticle):
                rij = particles[iParticle].pos - particles[jParticle].pos
                r = rij.dis
                rhat = rij.unit
                r2 = r**2
                r3 = r**3
                k = 0.0
                aij = k/r3 - G*particles[jParticle].mass/r2
                acc = acc + rhat.scale(aij)
        AccList.append(acc)
            
    return AccList
    
def EulerUpdate (particles, TimeStep):
    nParticle = len(particles)
    acc = Acceleration (particles)
    # velocity update
    for iParticle in range(0, nParticle):
        particles[iParticle].vel = particles[iParticle].vel + acc[iParticle].scale(TimeStep)
    # position update
    for iParticle in range(0, nParticle):
        particles[iParticle].pos = particles[iParticle].pos + particles[iParticle].vel.scale(TimeStep)
        
    return 0


def VelocityVerletUpdate (particles, TimeStep):
    nParticle = len(particles)
    acc_old = Acceleration (particles)
    # update position
    for iParticle in range (0, nParticle):
        particles[iParticle].pos = particles[iParticle].pos + particles[iParticle].vel.scale(TimeStep) + acc_old[iParticle].scale(0.5*TimeStep**2)

    acc_new = Acceleration (particles)
    # update velocity
    for iParticle in range (0, nParticle):
        particles[iParticle].vel = particles[iParticle].vel + acc_old[iParticle].scale(0.5*TimeStep) + acc_new[iParticle].scale(0.5*TimeStep)
        
    return 0
    
def Update (particles, dt):
#   EulerUpdate (particles, dt)
    VelocityVerletUpdate (particles, dt)
    
    return 0

def TimeEvaluation (particles, dt, nt, SaveXYZFile=50):
    nParticle = len(particles)
    OutputFile = open('OutputFile-1.xyz', 'w')
    for step in range (1, nt):
        Update (particles, dt)
        if(step%SaveXYZFile == 0):
            OutputFile.write ("%d\n" % nParticle)
            OutputFile.write ("MD\n")
            for iParticle in range(0, nParticle):
                OutputFile.write ("Ar\t")
                OutputFile.write ("%12.8f\t"% particles[iParticle].pos.x)
                OutputFile.write ("%12.8f\t"% particles[iParticle].pos.y)
                OutputFile.write ("%12.8f\n"% 0.0)

    OutputFile.close()
    return 0

def InitializeParticle ():
    particles = []
    InitialFile = open('IntialFile.in', 'r')
    for Line in InitialFile:
        particle = line.split (Line)
        particles.append (particle)
    return particles
"""   
def InitializeParticle (nParticle=1, 
                        origin=_2D_Point (0.0, 0.0), 
                        corner=_2D_Point (10.0, 10.0),
                        LengthScale = 1.0,
                        VelocityScale=1.0,
                        MassScale=1.0,
                        restart=False):
    
    particles = []
    if(restart == False):
        InitializeParticle = open('InitializeParticle.out', 'w')
        InitializeParticle.write ("%d\n" % nParticle)
        for iParticle in range(0, nParticle):
            InitializeParticle.write ("%d\t" % (iParticle+1))
            # Mass
            mass = MassScale*random.uniform(0.0, 1.0)
            InitializeParticle.write ("%14.10f\t" % mass)
            
            # Position
            xpar = _2D_Point (random.uniform(origin.x, corner.x), 
                              random.uniform(origin.y, corner.y))
            xpar = xpar.scale (LengthScale)
            InitializeParticle.write ("%14.10f\t" % xpar.x)
            InitializeParticle.write ("%14.10f\t" % xpar.y)
            
            # Velocity
            vpar = _2D_Point (random.uniform(0.0, 1.0), random.uniform(0.0, 1.0))
            vpar = vpar.unit
            vpar = vpar.scale (VelocityScale)
            InitializeParticle.write ("%14.10f\t" % vpar.x)
            InitializeParticle.write ("%14.10f\n" % vpar.y)
            
            particle = Particle (mass, xpar, vpar)
            particles.append (particle)
            
        InitializeParticle.close ()
    else:
        LogFile = open('LogFile.out', 'r')
        
        LogFile.close ()
    return particles
"""

#Test of InitializeParticle
"""
print "------ Test of InitializeParticle"
par = InitializeParticle (10)
"""

par = []
# 1st example
#par.append (Particle(50.0, _2D_Point ( 0.0, 0.0), _2D_Point ( 0.0, 0.0)))
#par.append (Particle(1.0, _2D_Point ( 5.0, 0.0), _2D_Point ( 0.0, 2.0)))

# 2nd example
#par.append (Particle(50.0, _2D_Point ( 0.0, 0.0), _2D_Point ( 0.0, 0.0)))
#par.append (Particle(1.0, _2D_Point (5.0, 0.0), _2D_Point ( 0.0,-2.0)))
#par.append (Particle(1.0, _2D_Point (-5.0, 0.0), _2D_Point ( 0.0, 2.0)))

# 3rd example
par.append (Particle(100.0, _2D_Point ( 0.0, 0.0), _2D_Point ( 0.0, 0.0)))
par.append (Particle(1.0, _2D_Point (5.0, 0.0), _2D_Point ( 0.0,-2.0)))
par.append (Particle(1.0, _2D_Point (-5.0, 0.0), _2D_Point ( 0.0,-4.0)))

# 4th example
#par.append (Particle(50.0, _2D_Point (0.0,0.0), _2D_Point ( 0.0, 0.0)))
#par.append (Particle(1.0, _2D_Point (0.0, 5.0), _2D_Point ( 2.0, 0.0)))
#par.append (Particle(1.0, _2D_Point (5.0, 0.0), _2D_Point ( 0.0,-2.0)))
#par.append (Particle(1.0, _2D_Point (-5.0, 0.0), _2D_Point ( 0.0,-4.0)))

# 4th example
#par.append (Particle(50.0, _2D_Point (0.0,0.0), _2D_Point ( 0.0, 0.0)))
#par.append (Particle(1.0, _2D_Point (0.0, 5.0), _2D_Point ( 2.0, 0.0)))
#par.append (Particle(1.0, _2D_Point (5.0, 0.0), _2D_Point ( 0.0,-2.0)))
#par.append (Particle(1.0, _2D_Point (-5.0, 0.0), _2D_Point ( 0.0,-4.0)))

# 5th example
#par.append (Particle(50.0, _2D_Point (0.0,0.0), _2D_Point ( 0.0, 0.0)))
#par.append (Particle(1.0, _2D_Point (0.0, 5.0), _2D_Point ( 2.0, 0.0)))
#par.append (Particle(0.5, _2D_Point (5.0, 0.0), _2D_Point ( 0.0,-2.0)))
#par.append (Particle(0.25, _2D_Point (-5.0, 0.0), _2D_Point ( 0.0,-4.0)))
#par.append (Particle(0.25, _2D_Point (0.0,-5.0), _2D_Point ( 0.0,-4.0)))

# TimeEvaluation
print "------ Test of TimeEvaluation"
#TimeEvaluation (par, 0.001, 50000)
TimeEvaluation (par, 0.001, 31000)
