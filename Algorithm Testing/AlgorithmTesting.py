import networkx as nx

DAYSOFTHEWEEK = {0 : "monday"}#, 1 : "tuesday", 2 : "wednesday", 3 : "thursday", 4 : "friday"}

POSSIBLETIMES = [[800 + (n // 4) * 100  + (15 * (n % 4)) for n in range(0, 48)] for _ in DAYSOFTHEWEEK]

class Meeting:
    def __init__(self, startTime=800, endTime=2000, dayOfWeek=0, peopleInMeeting=None):
        self.startTime = startTime
        self.endTime = endTime
        self.dayOfWeek = dayOfWeek
        self.peopleInMeeting = peopleInMeeting

class potentialMeeting:
    def __init__(self, duration=60, peopleInMeeting=[]):
        self.duration = duration
        self.peopleInMeeting = peopleInMeeting
    
class person:
    name = ''
    def __init__(self, name):
        self.name = name

def dateTimeToIndex(day, time):
    index = POSSIBLETIMES[0].index(time)
    return 100  * day + index

def indexToDateTime(index):
    return index // 100, POSSIBLETIMES[index // 100][index % 100]

def magicAlgorithm(people, meetingsAlreadyInExistence, meetingsToBeScheduled, scheduledMeetings=[], G = nx.Graph()):

    if len(meetingsToBeScheduled) == 0:
        return True, scheduledMeetings
    
    if nx.is_empty(G):
        # Fill in Bipartite Graph
        for i, day in enumerate(POSSIBLETIMES):
            for time in day:
                index = dateTimeToIndex(i, time)
                G.add_node(index, bipartite=0)
                for p in people:
                    G.add_node(p.name, bipartite=1)
                    G.add_edge(p.name, index)

        # Remove edges if people are busy
        for m in meetingsAlreadyInExistence:
            startIndex = dateTimeToIndex(m.dayOfWeek, m.startTime)
            endIndex = dateTimeToIndex(m.dayOfWeek, m.endTime)
            for p in m.peopleInMeeting:
                for i in range(startIndex, endIndex):
                    G.remove_edge(p.name, i)
    
    GraphCopy = G.copy()
        
    # pick a meeting to start scheduling (meetingsToBeScheduled is nonempty)
    scheduledCopy = scheduledMeetings.copy()

    # Find a time for the new meeting, and update Graph
    newMeeting = meetingsToBeScheduled[0]

    # Contains the set of all free time indexes for every person in the newMeeting
    freeTimeCollection = [[key for _, key in enumerate(value)] for _, value in enumerate([GraphCopy[p.name] for p in newMeeting.peopleInMeeting])]

    # Make it a list and sort it
    intersectingTimes = list(set(freeTimeCollection[0]).intersection(*freeTimeCollection[1:]))
    intersectingTimes.sort()

    # If it is impossible to schedule a meeting
    if len(intersectingTimes) == 0:
        return False, scheduledMeetings
    
    # Try all possible free times
    else:  
        # For all the times that everyone is free
        for i in intersectingTimes:
            start = i
            delta = (newMeeting.duration + 14) // 15

            # Get all the sets of free time indexes
            j = [i for i in range(start, start + delta)]

            # If a whole meeting block is actually free
            if len(set(intersectingTimes).intersection(set(j))) == len(j):

                # Set up the data for the new meeting
                day, startTime = indexToDateTime(j[0])
                _, endTime = indexToDateTime(j[-1] + 1)
                peopleInThisNewerMeeting = newMeeting.peopleInMeeting
                temp = Meeting(startTime, endTime, day, peopleInThisNewerMeeting)
                scheduledCopy = scheduledMeetings.copy()
                scheduledCopy.append(temp)
                newMeetingsToBeScheduled = meetingsToBeScheduled.copy()
                newMeetingsToBeScheduled.pop(0)

                # remove edges from graph and return copy as appropriate for newMeeting
                startIndex = j[0]
                endIndex = j[-1] + 1
                for p in temp.peopleInMeeting:
                    for idx in range(startIndex, endIndex):
                        GraphCopy.remove_edge(p.name, idx)


                success, output = magicAlgorithm(people, meetingsAlreadyInExistence, newMeetingsToBeScheduled, scheduledCopy, GraphCopy)
                if success:
                    return success, output

    # If it was impossible to schedule a meeting
    return False, []

# People
mal = person('Malcolm Reynolds')
zoe = person('Zoe Washburne')
wash = person('Hoban Washburne')
inara = person('Inara Serra')
kaylee = person('Kaywinet Lee Frye')
jayne = person('Jayne Cobb')
book = person('Derrial Book')
simon = person('Simon Tam')
river = person('River Tam')

persons = [mal, zoe, wash, inara, kaylee, jayne, book, simon, river]

# Adding Mike a.k.a. the leader
mike = person('Mike Ingram')
completePeople = persons.copy()
completePeople.append(mike)

# Existing meetings
piloting = Meeting(800, 1230, 0, [mal, zoe, wash])
infirmary = Meeting(1100, 1300, 0, [simon, river, book, inara])
hr = Meeting(1300, 1400, 0, [mal, zoe, jayne])
maint = Meeting(1330,1400, 0, [kaylee, book])
armory = Meeting(1400,1500,0,[mal, zoe, jayne, book])
ambassador = Meeting(1400, 1500, 0, [inara])
moon = Meeting(1500, 1600, 0, [mal, inara, jayne, kaylee, simon])

meetings = [piloting, infirmary, hr, maint, armory, ambassador, moon]

# Individual meetings with mike for 45 minutes
potentialMeetings = [potentialMeeting(45, [mike, m]) for m in persons]

# Group meetings with mike for an hour
potentialMeetings.append(potentialMeeting(60, completePeople))

# Run the algorithm
success, output = magicAlgorithm(completePeople, meetings, potentialMeetings)

if not success:
    print("it didn't work!")
for thing in output:
    print([x.name for x in thing.peopleInMeeting], thing.startTime, thing.endTime)
