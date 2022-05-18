# -*- coding: utf-8 -*-
"""

The Contacts class is the graph-based implementation of a professional network (for example, a network such as Linkedin).
In particular, the vertices of the network are the people and the edges are the possible connections between them.
Each person is represented by his or her name and phone number. Implement the function getSuggestions that 
takes a person and a minimum number of jumps (minjumps) and returns a list with all the people connected to that person 
by minjunmps"""

import sys


class Person():

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def __str__(self):
        str_person = "Name: {}; Phone number: {}".format(self.name, self.phone_number)
        return str_person

    def __hash__(self):
        """returns integers that are used to compare dictionary keys"""
        return hash((self.name, self.phone_number))


class Contacts():

    def __init__(self):
        # vertices
        self._vertices = {}

    def addPerson(self, person: Person):
        """adds a new person in the dictionary vertices"""
        self._vertices[person] = []
        # self.connections[person] = []

    def addConnection(self, person1, person2):
        """adds an edge between two people"""
        if person1 not in self._vertices.keys():
            print(str(person1) + ' does not exist!!!')
            return
        if person2 not in self._vertices.keys():
            print(str(person2) + ' does not exist!!!')
            return

        self._vertices[person1].append(person2)
        self._vertices[person2].append(person1)

    def areConnected(self, person1, person2):
        """checks if person1 and person2 are connected"""
        if person1 not in self._vertices.keys():
            print(str(person1) + ' does not exist!!!')
            return
        if person2 not in self._vertices.keys():
            print(str(person2) + ' does not exist!!!')
            return

        return person2 in self._vertices[person1]

    def minDistance(self, distances, visited):
        """returns the vertex (index) with the mininum distance. We 
        only consider the set of vertices that have not been visited"""
        # Initilaize minimum distance for next node 
        min = sys.maxsize

        # returns the vertex with minimum distance from the non-visited vertices
        for i in self._vertices:
            if distances[i] <= min and visited[i] == False:
                min = distances[i]
                min_index = i
        return min_index

    def dijkstra(self, origin):
        """"takes a vertex v and calculates its mininum path 
        to the rest of vertices by using the Dijkstra algoritm"""

        # we use a Python list of boolean to save those nodes that have already been visited
        # Mark all the vertices as not visited 
        visited = {}
        for v in self._vertices.keys():
            visited[v] = False

        # this list will save the previous vertex
        previous = {}
        for v in self._vertices.keys():
            previous[v] = -1

        # This array will save the accumulate distance from v to each node
        distances = {}
        for v in self._vertices.keys():
            distances[v] = sys.maxsize

        # The distance from v to itself is 0
        distances[origin] = 0

        for n in range(len(self._vertices)):
            # Pick the vertex with the minimum distance vertex.
            # u is always equal to v in first iteration 
            u = self.minDistance(distances, visited)
            # Put the minimum distance vertex in the shotest path tree
            visited[u] = True

            # Update distance value of the u's adjacent vertices only if the current  
            # distance is greater than new distance and the vertex in not in the shotest path tree 
            for i in self._vertices[u]:
                if visited[i] == False and distances[i] > distances[u] + 1:
                    distances[i] = distances[u] + 1
                    previous[i] = u

                    # finally, we print the minimum path from v to the other vertices

        # self.printSolution(distances,previous,origin)
        return distances, previous

    def getSuggestions(self, person, minjumps):
        """"takes a person and a minimum number of jumps minjumps and returns a list with all the people 
             connected to person by minjunmps"""
        distances, previous = self.dijkstra(person)
        result = []
        for v in distances.keys():
            if distances[v] < sys.maxsize and distances[v] == minjumps:
                result.append(v)

        return result


if __name__ == '__main__':

    # Create delivery points
    pA = Person('Isa', 666889900)  # A
    pB = Person('Ana', 666887700)
    pC = Person('Bea', 555887755)
    pD = Person('Cris', 333224411)
    pE = Person('Joe', 444887766)
    pF = Person('JoseL', 222776644)
    pG = Person('Leo', 322776644)
    pH = Person('Fran', 388776644)
    pI = Person('Mia', 388776644)
    pJ = Person('Ruth', 388776644)
    pK = Person('Blas', 388776644)

    graph = Contacts()
    persons = [pA, pB, pC, pD, pE, pF, pG, pH, pI, pJ, pK]
    for p in persons:
        graph.addPerson(p)

    graph.addConnection(pA, pB)  # Isa<->Ana
    graph.addConnection(pA, pC)  # Isa<->Bea
    graph.addConnection(pA, pD)  # Isa<->Cris

    graph.addConnection(pB, pG)  # Ana<->Leo

    graph.addConnection(pC, pD)  # Bea<->Cris

    graph.addConnection(pD, pE)  # Cris<->Joe
    graph.addConnection(pD, pF)  # Cris<->JoseL
    graph.addConnection(pD, pH)  # Cris<->Fran

    graph.addConnection(pF, pI)  # JoseL<->Mia

    graph.addConnection(pG, pI)  # Leo<->Mia

    graph.addConnection(pI, pJ)  # Mia<->Ruth

    graph.addConnection(pJ, pK)  # Ruth<->Blas

    # print(graph)
    suggestions = graph.getSuggestions(pA, 2)
    for s in suggestions:
        print(s.name, end=' ')
    print()


import unittest


class Test(unittest.TestCase):
    


    #provisional mark
    mark=0

    def setUp(self):
        print('\ninitializing data...\n')
        
        #Create delivery points
        self.pA=Person('Isa',666889900)             #A
        self.pB=Person('Ana',666887700)
        self.pC=Person('Bea',555887755)
        self.pD=Person('Cris',333224411)
        self.pE=Person('Joe',444887766)
        self.pF=Person('JoseL',222776644)
        self.pG=Person('Leo',322776644)
        self.pH=Person('Fran',388776644)
        self.pI=Person('Mia',388776644)
        self.pJ=Person('Ruth',388776644)
        self.pK=Person('Blas',388776644)

        
        self.persons=[self.pA,self.pB,self.pC,self.pD,self.pE,self.pF,self.pG,self.pH,self.pI,self.pJ,self.pK]
        
        self.graph=Contacts()
        
        for p in self.persons:
            self.graph.addPerson(p)
            
    
        self.graph.addConnection(self.pA,self.pB)      #Isa<->Ana
        self.graph.addConnection(self.pA,self.pC)      #Isa<->Bea
        self.graph.addConnection(self.pA,self.pD)      #Isa<->Cris

        self.graph.addConnection(self.pB,self.pG)      #Ana<->Leo

        self.graph.addConnection(self.pC,self.pD)      #Bea<->Cris


        self.graph.addConnection(self.pD,self.pE)      #Cris<->Joe
        self.graph.addConnection(self.pD,self.pF)      #Cris<->JoseL
        self.graph.addConnection(self.pD,self.pH)      #Cris<->Fran

        self.graph.addConnection(self.pF,self.pI)      #JoseL<->Mia

        self.graph.addConnection(self.pG,self.pI)      #Leo<->Mia


        self.graph.addConnection(self.pI,self.pJ)      #Mia<->Ruth

        self.graph.addConnection(self.pJ,self.pK)      #Ruth<->Blas

    def testz_printNota(self):
        print('\n\n*************************')
        print("\t Provisional mark:",Test.mark)  
        print('*************************')
        
    def test1_getSuggestions(self):
        print('Case 1: minimumJumps=1')
        result=self.graph.getSuggestions(self.pA,1)
        expected=[self.pB,self.pC,self.pD,self.pE,self.pF,self.pG,self.pH,self.pI,self.pJ,self.pK]
        
        #print('result:')
        #for p in result:
        #    print(p)

        #print('expected:')
        #for p in expected:
        #    print(p)
    
        self.assertEqual(len(result),len(expected))
        self.assertCountEqual(result,expected)
        print('\t\t mark += 3')
        Test.mark+=3
      
    def test2_getSuggestions(self):
        print('Case 2: minimumJumps=2')
        result=self.graph.getSuggestions(self.pA,2)
        expected=[self.pE,self.pF,self.pG,self.pH,self.pI,self.pJ,self.pK]
        
        #print('result:')
        #for p in result:
        #    print(p)

        #print('expected:')
        #for p in expected:
        #    print(p)
    
        self.assertEqual(len(result),len(expected))
        self.assertCountEqual(result,expected)
        print('\t\t mark += 4')
        Test.mark+=4

    def test3_getSuggestions(self):
        print('Case 3: minimumJumps=3')
        result=self.graph.getSuggestions(self.pA,3)
        expected=[self.pI,self.pJ,self.pK]
        
        #print('result:')
        #for p in result:
        #    print(p)

        #print('expected:')
        #for p in expected:
        #    print(p)
    
        self.assertEqual(len(result),len(expected))
        self.assertCountEqual(result,expected)
        print('\t\t mark += 4')
        Test.mark+=4

    def test4_getSuggestions(self):
        print('Case 4: minimumJumps=4')
        result=self.graph.getSuggestions(self.pA,4)
        expected=[self.pJ,self.pK]
        
        #print('result:')
        #for p in result:
        #    print(p)

        #print('expected:')
        #for p in expected:
        #    print(p)
    
        self.assertEqual(len(result),len(expected))
        self.assertCountEqual(result,expected)
        print('\t\t mark += 4')
        Test.mark+=4

    def test5_getSuggestions(self):
        print('Case 5: minimumJumps=5')
        result=self.graph.getSuggestions(self.pA,5)
        expected=[self.pK]
        
        #print('result:')
        #for p in result:
        #    print(p)

        #print('expected:')
        #for p in expected:
        #    print(p)
    
        self.assertEqual(len(result),len(expected))
        self.assertCountEqual(result,expected)
        print('\t\t mark += 4')
        Test.mark+=4

    def test6_getSuggestions(self):
        print('Case 6: minimumJumps=6')
        result=self.graph.getSuggestions(self.pA,6)
        expected=[]
        
        #print('result:')
        #for p in result:
        #    print(p)

        #print('expected:')
        #for p in expected:
        #    print(p)
    
        self.assertEqual(len(result),len(expected))
        self.assertCountEqual(result,expected)
        print('\t\t mark += 1')
        Test.mark+=1
    
#Comentar para usarlo en spyder
#unittest.main(argv=['first-arg-is-ignored'], exit=False)

#Descomenar para usarlo en Spyder
if __name__ == '__main__':
    unittest.main()

