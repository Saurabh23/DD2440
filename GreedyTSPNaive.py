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
#define function to compute euclidian distance for 2 points
def dist(c1,c2):
    return int(math.floor(math.sqrt(math.pow(c1[0]-c2[0],2)+math.pow(c1[1]-c2[1],2)))) #should also round up?

#read data
coords = []
n = int(raw_input())
for x in range(0,n):
    line = raw_input()
    splitline = line.split(" ")
    coords.append([float(splitline[0]),float(splitline[1]),x])


tour = [0] #init tour (output)
#startingpoint = coords[0] #startingpoint = coordinates of index zero (this is also the last point)
currentpoint = coords[0]
del coords[0] #remove index 0 as we won't have to compute distance to index 0 anymore (I guess this can happen faster)
best = 1000000000


while len(coords) > 0:
    for i in xrange(0,len(coords)):

        #if current(previous) best is slower than the new one, update best
        if best > dist(currentpoint,coords[i]):
            best = dist(currentpoint,coords[i])
            best_id = coords[i][2]
            best_index = i


    tour.append(coords[best_index][2])
    currentpoint = coords[best_index]
    del coords[best_index]
    best = 1000000000

for i in tour:
    print i
