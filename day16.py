#!/usr/bin/env python
import numpy as np
import ast

class Node:
    def __init__(self, id, name, neighbors, value):
        self.id = id
        self.name = name
        self.neighbors = neighbors
        self.flow = value
        self.isOpen = 0
    def get_connections(self):
        return self.adjacent.keys()  
    def get_name(self):
        return self.name
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class AgencyMatrix:
    def __init__(self, maxId, graph):
        self.matrix = np.zeros((maxId,maxId)) 
        for nodeName in graph:
            node = graph[nodeName]
            for neighbor in node.neighbors:
                neighborNode = graph[neighbor]
                self.matrix[node.id, neighborNode.id] = 1
    def FloydWarshall(self):
        distance = self.matrix + (1-self.matrix)*1000
        # Adding vertices individually
        for k in range(self.matrix.shape[0]):
            for i in range(self.matrix.shape[0]):
                for j in range(self.matrix.shape[0]):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        self.floydWarshall = distance

def allPaths(graph, floydWarshallMatrix, valvesRemaining, time, currentValve="AA", paths={"AA": 30}):
    pathList = [paths]

    for valve in valvesRemaining:
        if graph[valve].flow < 1:
            continue
        timeLeft = time - (floydWarshallMatrix[graph[currentValve].id, graph[valve].id]+1) 
        if timeLeft < 2:
            continue
        newValvesRemaining = valvesRemaining[:]
        newValvesRemaining.remove(valve)
        dictValve = {valve:timeLeft}
        newPaths = dict(paths.items() + dictValve.items())
        pathList += allPaths(graph, floydWarshallMatrix, newValvesRemaining, timeLeft, currentValve=valve, paths=newPaths)
    return pathList

def score(graph, chosenValves):
    score = 0
    for valve in chosenValves.keys():
        score += graph[valve].flow * chosenValves[valve]
    return score

f = open("ressources/day16.txt", "r")
lines = f.readlines()
graph = {}
id = 0
for line in lines:
    instructions = line.replace("\n", "").replace("=", " ").replace(";", " ").replace(",", " ").split()
    name = instructions[1]
    flow = int(instructions[5])
    neighbors = instructions[10::]
    
    node = Node(id, name, neighbors, flow)
    graph[node.name] = node
    id += 1

adjencyMatrix = AgencyMatrix(id, graph)
adjencyMatrix.FloydWarshall()

valves = graph.keys()
valves.remove("AA")
allPathsPossible = allPaths(graph, adjencyMatrix.floydWarshall, valves, 30)
maxScore = 0
for path in allPathsPossible:
    newScore = score(graph, path)
    if newScore > maxScore:
        maxScore = newScore

print("Max released pressure is: {}".format(int(maxScore)))

valves = graph.keys()
valves.remove("AA")
allPathsPossible = allPaths(graph, adjencyMatrix.floydWarshall, valves, 26)
maxScoresPerValves = {}

for path in allPathsPossible:
    valves = path.keys()
    valves.sort()
    if len(valves) < 5:
        continue
    valves = str(valves)
    s = score(graph, path)
    if valves not in maxScoresPerValves:
        maxScoresPerValves[valves]=s
    elif s > maxScoresPerValves[valves]:
        maxScoresPerValves[valves] = s

maxScore = 0
for setOfValves1 in maxScoresPerValves:
    list1 = ast.literal_eval(setOfValves1)
    for setOfValves2 in maxScoresPerValves:
        list2 = ast.literal_eval(setOfValves2)
        intersection = [value for value in list1 if value in list2]
        if len(intersection) < 2:
            doubleScore = maxScoresPerValves[setOfValves1]+maxScoresPerValves[setOfValves2]
            if doubleScore > maxScore:
                maxScore = doubleScore
            
print("Max released pressure with an elephant is: {}".format(int(maxScore)))