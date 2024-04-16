import sys
import math

def facto (**fact_):
    return math.factorial(fact_)

factori = facto(sys.argv[1])


print(f'El faltorial de numero es {factori}')
