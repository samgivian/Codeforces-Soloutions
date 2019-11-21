a =int(input())
m=0
for r in range(0,a):
    b=input()
    if(b=="Tetrahedron"):
        m=m+4
    elif(b=="Cube"):
        m=m+6
    elif(b=="Octahedron"):
        m=m+8
    elif(b=="Dodecahedron"):
        m=m+12
    elif(b=="Icosahedron"):
        m=m+20
print(m)
