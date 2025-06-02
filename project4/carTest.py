from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
from math import pow, sqrt

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData()
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData, maxItr = 200, hiddenLayerList = hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData, maxItr = 200,hiddenLayerList = hiddenLayers)

#for i in range(5):
#    print("Pen Testing " + str(i))
#    testPenData()
#    print("Car Testing " + str(i))
#    testCarData()




for i in range(1):
    testAccus = []
    for j in range(5):
        print("Car Testing with " + str(5*i) + " hidden layer perceptrons")
        testAccus.append(testCarData([i * 5])[1])

    print("Summary:")
    print("Standard Deviation: " + str(stDeviation(testAccus)))
    print("Average: " + str(average(testAccus)))
    print("Max Accuracy: " + str(max(testAccus)) + "\n")



