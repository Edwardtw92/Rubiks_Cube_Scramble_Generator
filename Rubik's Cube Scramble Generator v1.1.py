import sys
import random

sc = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"] #20 moves scramble
# types of moves ["r", "l", "u", "d", "f", "b"]
r = ["R ", "R' ", "R2 "] 
l = ["L ", "L' ", "L2 "]
u = ["U ", "U' ", "U2 "]
d = ["D ", "D' ", "D2 "]
f = ["F ", "F' ", "F2 "]
b = ["B ", "B' ", "B2 "]
x = 0
rsc = ""

print("Thank you for using Rubik's Cube Scramble Generator v1.1 created created by Edward Chang")
rsc = str.lower(input("Press 'entre' to start"))

while rsc == "" :
    i = 0
    while i <= 19 :
        n1 = random.randint(0,5)
        n2 = random.randint(0,2)
        while n1 == x:
            n1 = random.randint(0,5)
        if n1 == 0 :
            sc[i] = r[n2]
        elif n1 == 1 :
            sc[i] = l[n2]
        elif n1 == 2 :
            sc[i] = u[n2]
        elif n1 == 3 :
            sc[i] = d[n2]
        elif n1 == 4 :
            sc[i] = f[n2]
        elif n1 == 5 :
            sc[i] = b[n2]
        x = n1
        i = i + 1

    print(sc[0] + sc[1] + sc[2] + sc[3] + sc[4] + sc[5] + sc[6] + sc[7] + sc[8] + sc[9] + sc[10] + sc[11] + sc[12] + sc[13] + sc[14] + sc[15] + sc[16] + sc[17] + sc[18] + sc[19])

    rsc = str.lower(input("Press 'entre' for a new scramble"))

print("See you")
sys.exit(0)
