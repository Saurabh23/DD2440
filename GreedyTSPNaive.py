import math

''' #input
10
95.0129 61.5432
23.1139 79.1937
60.6843 92.1813
48.5982 73.8207
89.1299 17.6266
76.2097 40.5706
45.6468 93.5470
1.8504 91.6904
82.1407 41.0270
44.4703 89.3650
'''
# Create adjacency matrix

# define function to compute euclidian distance for 2 points
def dist(c1,c2):
    return int(math.floor(math.sqrt(math.pow(c1[0]-c2[0], 2)+math.pow(c1[1]-c2[1],2)))) # should also round up?

#read data
coords = []
n = int(raw_input())
for x in range(0, n):
    line = raw_input()
    splitline = line.split(" ")
    coords.append([float(splitline[0]), float(splitline[1]), x])

mat = range(0, n)

# Populate adjacency matrix (simple)
for i in range(0, n):
    row = []
    for j in range(0, n):
        row.append(dist(coords[i], coords[j]))

    mat[i] = row

'''
# Print adjacency matrix #debug
for i in range(0, n):
    print mat[i]
'''

tour = [0]  # init tour (output)
del coords[0]  # remove index 0 as we won't have to compute distance to index 0 anymore (I guess this can happen faster)
best = 1000000000
currentpoint = 0
#for i in range(0,n):


for i in range(0,n-1):  # for every row in matrix
    for j in range(0,n):  # for every col in row (every distance of every edge adjacent to the vertex the row represents)
        if j not in tour and mat[currentpoint][j] != 0: #store n in dictionary (hashmap)
            # print j
            if best > mat[currentpoint][j]:
                best = mat[currentpoint][j]
                bestind = j

    tour.append(bestind)
    # print tour #debug
    currentpoint = bestind
    best = 1000000

for i in tour:
    print i
