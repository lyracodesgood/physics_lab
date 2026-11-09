import math as m

g = 9.8 #m/s

#energy
def find_KE(mass,v):
    return (mass*v**2)/2

def v_from_KE(mass, KE):
    return m.sqrt((2*KE)/(mass))

def find_PEg(mass,h):
    return mass * g * h

#vector addition
def add_comps(Dx,Dy):
    return (m.sqrt(Dx**2 + Dy**2))

def get_angle(Dx,Dy):
    return m.degrees(m.atan2(Dy, Dx))