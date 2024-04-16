import sys
import math

def facto (**fact_):
    return math.factorial(fact_)

factori = int(sys.argv[1])
facto(factori)


print(f'El faltorial de numero es {factori}')
