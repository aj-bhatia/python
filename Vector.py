# Ajay Bhatia
"""
This module provides functions to perform standard vector operations.  Vectors
are represented as tuples of numbers (floats or ints).  Functions that take two 
vector arguments will raise a ValueError() exception if the two vectors are of
different dimensions.
"""

# import libraries
import math
import random
import sys

def add(u, v):
    """
    Return the vector sum u+v.
    """
    
    z = []
    if not (len(u) == len(v)):
        raise ValueError('incompatible vectors: '+str(u)+', '+str(v))
    # end if
    
    for i in range(len(u)):
        z.append(u[i]+v[i])
    # end for
    
    return tuple(z)
    
# end add()

def negate(u):
    """
    Return the negative of the vector u.
    """
    
    z = []
    for i in range(len(u)):
        z.append((u[i]*-2) + u[i])
    # end for
    
    return tuple(z)
    
# end negate()

def sub(u, v):
    """
    Return the vector difference u-v.
    """
    
    z = []
    if not (len(u) == len(v)):
        raise ValueError('incompatible vectors: '+str(u)+', '+str(v))
    # end if
    
    for i in range(len(u)):
        z.append(u[i]-v[i])
    # end for
    
    return tuple(z)
    
# end sub()

def scalarMult(c, u):
    """
    Return the scalar product cu  of the number c by the vector u.
    """
    
    z = []
    for i in range(len(u)):
        z.append(u[i]*c)
    # end for
    
    return tuple(z)
    
# end scalarMult()

def hadamard(u, v):
    """
    Return the Hadamard product of u with v.
    """
    
    z = []
    if not (len(u) == len(v)):
        raise ValueError('incompatible vectors: '+str(u)+', '+str(v))
    # end if
    
    for i in range(len(u)):
        z.append(u[i]*v[i])
    # end for
    
    return tuple(z)
    
# end hadamard()

def dot(u, v):
    """
    Return the dot product of u with v.
    """
    
    total = 0
    
    if not (len(u) == len(v)):
        raise ValueError('incompatible vectors: '+str(u)+', '+str(v))
    # end if
    
    z = hadamard(u,v)
    
    for i in range(len(z)):
        total += z[i]
    # end for
    
    return total
    
# end dot()

def length(u):
    """
    Return the (geometric) length of the vector u.
    """
    
    return math.sqrt(dot(u,u))
    
# end length()

def dim(u):
    """
    Return the dimension of the vector u.
    """
    
    return len(u)
    
# end dim()

def unit(v):
    """
    Return a unit (geometric length 1) vector in the direction of v.
    """
    
    return scalarMult((1/length(v)),v)
    
# end unit()

def angle(u,v):
    """
    Return the angle (in radians) between vectors u and v.
    """
    
    if not (len(u) == len(v)):
        raise ValueError('incompatible vectors: '+str(u)+', '+str(v))
    # end if
    
    z = unit(u)
    y = unit(v)
    return math.acos(dot(z,y))
    
# end angle()

def randVector(n, a, b):
    """
    Return a vector of dimension n whose components are random floats in the range [a,b).
    """
    
    u = []
    
    for i in range(n):
        u.append(random.uniform(a,b))
    # end for
    
    return tuple(u)
    
# end randomVector()