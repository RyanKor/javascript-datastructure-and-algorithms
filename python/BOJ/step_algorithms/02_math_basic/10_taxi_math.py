import sys, math

n = int(sys.stdin.readline())

p = math.pi

circle_pi = p*n**2

taxi = 2*n**2

print('%.6f'%circle_pi,'%.6f'%taxi,end="\n")