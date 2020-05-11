import networkx as nx
import matplotlib.pyplot as plt

daysOfTheWeek = { 0 : "monday", 1 : "tuesday", 2 : "wednesday", 3 : "thursday", 4 : "friday"}

possibleTimes = [ [ 800 + (n // 4) * 100  + (15 * (n % 4)) for n in range(0, 48) ] for _ in daysOfTheWeek ]

class Meeting:
    # peopleInMeeting = []
    # startTime = 800
    # endTime = 2000
    # dayOfWeek = 0
    # availableTime = False

    def __init__(self, startTime = 800, endTime = 2000, dayOfWeek=0, peopleInMeeting = []):
        self.startTime = startTime
        self.endTime = endTime
        self.dayOfWeek = dayOfWeek
        self.peopleInMeeting = peopleInMeeting

    
class person:
    name = ''
    def __init__(self, name):
        self.name = name


mal = person('Malcolm Reynolds')
zoe = person('Zoe Washburne')
wash = person('Hoban Washburne')
inara = person('Inara Serra')
kaylee = person('Kaywinet Lee Frye')
jayne = person('Jayne Cobb')
book = person('Derrial Book')
simon = person('Simon Tam')
river = person('River Tam')

persons = [mal] #, zoe, wash, inara, kaylee, jayne, book, simon, river]

piloting = Meeting(800, 1230, 0, [mal, zoe, wash])
infirmary = Meeting(1100, 1300, 0, [simon, river, book, inara])
hr = Meeting(1300, 1400, 0, [mal, zoe, jayne])
maint = Meeting(1330,1400, 0, [kaylee, book])
armory = Meeting(1400,1500,0,[mal, zoe, jayne, book])
ambassador = Meeting(1400, 1500, 0, [inara])
moon = Meeting(1500, 1600, 0, [mal, inara, jayne, kaylee, simon])

meetings = [piloting, infirmary, hr, maint, armory, ambassador, moon]

def dateTimeToIndex(day, time):
    index = possibleTimes[0].index(time)
    return 100  * day + index

def indexToTime(index):
    return possibleTimes[index // 100][index % 100]

# class edge:
#     def __init__(self, person, dayOfWeek, timeIndex):
#         self.person = person
#         self.dayOfWeek = dayOfWeek
#         self.timeIndex = timeIndex

def magicAlgorithm(people, meetingsAlreadyInExistence, meetingsToBeScheduled):

    # Fill in Bipartite Graph
    G = nx.Graph()

    for i, day in enumerate(possibleTimes):
        for time in day:
            index = dateTimeToIndex(i, time)
            G.add_node(index)
            for p in people:
                G.add_node(p.name)
                G.add_edge(p.name, index)
    

    nx.draw(G, with_labels=True)
    plt.show()

    
    #temp = edge(Alice, 0, timeToIndex(800))
    #edges = [temp]

    # # Remove edges if people are busy
    # for m in meetingsAlreadyInExistence:
    #     startIndex = timeToIndex(m.startTime)
    #     tEnd = m.endTime
        
    return(G)
    #return [meeting()]

print(magicAlgorithm(persons, meetings, []))