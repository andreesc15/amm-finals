import random
import statistics
import math

#function to return whether a point is in the circle or not
def isInCircle(x,y):
    return ((x-1)**2 + (y-2)**2)<=25

#run one Monte Carlo simulation with a sample of n
def monteCarlo(sampleCount, showPoints = False, showResults = False):
    pointCount = 0
    for i in range(1,sampleCount+1):
        x, y = random.uniform(-4,6), random.uniform(-3,7) 
        #generate x, y coordinates through uniformly random number generator

        if(showPoints):
            print("pt-{}: ({:.3f},{:.3f}),{} within circle".format(i,x,y," not" if not isInCircle(x,y) else ""))
            #print all points if explicitly stated at the parameter

        if(isInCircle(x,y)): 
            #only add to accepted point counter if the point is within the circle
            pointCount+=1 

    if(showResults):
            print("{} points within the circle out of {} sample points. Approx area of circle: {}".format(pointCount, sampleCount, pointCount * 100.00 / sampleCount))
            #print results of the Monte Carlo simulation if explicitly stated at the parameter    
    return pointCount

def simulateMultipleMonteCarlo(sampleCount, simulationCount, showSimulation = False):
    simulatedArea = []
    for i in range(1,simulationCount+1):
        curr = monteCarlo(sampleCount)
        area = curr * 100.00 / sampleCount
        simulatedArea.append(area)

        if showSimulation:
            print("Sim. #{}: {}/{} points are within area of circle. Approx. area: {} ".format(i, curr, sampleCount, area))
    
    mean = statistics.mean(simulatedArea)
    stdev = statistics.stdev(simulatedArea)
    print("Average out of {} simulations of {} sample points: {:.4f} with standard deviation of {:.2f}".format(simulationCount, sampleCount, mean, stdev))
    return mean, stdev

def simulateBiggerSamples(n):
    for i in range(1,n):
        monteCarlo(10**i, showResults=True)


monteCarlo(5000,showResults=True)
