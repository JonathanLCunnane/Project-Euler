def createArray(dimension):
    array = []
    for i in range(dimension):
        array.append([])
        for j in range(dimension):
           array[i].append(i+j) 
    return array
def routes(dimensionarray):
    tracer = [0,0]
    dimension = len(dimensionarray)
    routes = 0
    while tracer != [dimension, dimension]:
        for i in range(dimension):
            for j in range(i-1, i+1):
                for k in range(i-1, i+1):
                    try:
                        if dimensionarray[j][k] > dimensionarray[tracer[0]][tracer[1]]:
                            tracer = [i+j,i+k]
                            routes += 1
                    except:
                        continue
    return routes

print(routes(createArray(3)))