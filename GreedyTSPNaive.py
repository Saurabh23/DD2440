import math
import sys
#input
'''
#test solution
input = "10 95.0129 61.5432 23.1139 79.1937 60.6843 92.1813 48.5982 73.8207 89.1299 17.6266 76.2097 40.5706 45.6468 93.5470 1.8504 91.6904 82.1407 41.0270 44.4703 89.3650"
#split on spaces
splitput = input.split(" ")
n = 10
#n = int(splitput[0])
coords = range(0,n)
for i in xrange(0,n):
    coords[i] = [float(splitput[i*2+1]),float(splitput[i*2+2]),i]
    #print coords[i]
'''

#actual solution
i = 0
coords = []
for line in sys.stdin:
    if i == 0:
        n = line
    if i != 0:
        splitline = line.split(" ")
        coords.append([float(splitline[0]),float(splitline[1]),i])
    i += 1





#define function to compute euclidian distance for 2 points
def dist(c1,c2):
    return int(math.floor(math.sqrt(math.pow(c1[0]-c2[0],2)+math.pow(c1[1]-c2[1],2)))) #should also round up?

#print dist(coords[0],coords[8])

#set index 0 as starting point
tour = [0]
startingpoint = coords[0]
currentpoint = coords[0]
#remove index 0 as we won't have to compute distance to index 0 anymore
del coords[0]


#while len(coords) > 1:
best = dist(currentpoint,coords[1])
current_best = coords[1]
while len(coords) > 0:
    for i in xrange(0,len(coords)):
        #best = min(best,dist(currentpoint,coords[i]))

        #if current(previous) best is slower than the new one, update best
        if best > dist(currentpoint,coords[i]):
            best = dist(currentpoint,coords[i])
            best_id = coords[i][2]
            best_index = i

    tour.append(coords[best_index][2])
    #print tour
    currentpoint = coords[best_index]
    #print currentpoint
    del coords[best_index]
    best = 10000000

for i in tour:
    print i

'''
for i in tour:
    sys.stdout
'''
