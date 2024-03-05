#---imports---#
import random 
import array #to allow me to .append
import time #time used to make it more readable by giving people time to proccess
import os #used to clear screen
#---variables---#
loop = True
TeamSpaces = 5
SinglePlayerSpaces = 10
TotalSpaces = 0
TotalEvents = 0
#---arrays---#
TeamName = []
TeamScore = []
TeamEventsParticipateIn = []
Events = []
EventType = []
Positions = ['first','second','third']
PositionScore = [10, 7, 5]
#---METHODS---#
    #--Event Creation--#
def EventCreate(Events,EventType):
    print('Creating an event:')
    time.sleep(0.5)
    EventName = input('Please enter the name of your event:\n')
    Events.append(EventName)
    EventTypeDef = input('Please enter what type of event this event is: (Academic/Sporting)\n')
    EventType.append(EventTypeDef)
    #--Team Creation--#
def TeamCreate(TeamName,TeamEventsParticipateIn,TotalSpaces,SinglePlayerSpaces,TeamSpaces):
    print('Creating a team')
    time.sleep(0.5)
    TeamNameInput = input('Please enter the name of your team:\n')
    EventParticipate = input('Please enter whether the team is being entered for one event or six:\n')
    time.sleep(1)
    SingleOrTeam = input('Is this team single player? (y/n)\n')
    if SingleOrTeam.lower() == 'y' and SinglePlayerSpaces > 0:
        print('Team Saved')
        TeamName.append(TeamNameInput)
        TeamEventsParticipateIn.append(EventParticipate)
        TotalSpaces=TotalSpaces+1
        SinglePlayerSpaces=SinglePlayerSpaces-1
        return TeamSpaces, SinglePlayerSpaces, TotalSpaces
    elif SingleOrTeam.lower() == 'n' and TeamSpaces > 0:
        print('Team Saved')
        TeamName.append(TeamNameInput)
        TeamEventsParticipateIn.append(EventParticipate)
        TotalSpaces=TotalSpaces+1
        TeamSpaces=TeamSpaces-1
        return TeamSpaces, SinglePlayerSpaces, TotalSpaces
    elif SinglePlayerSpaces == 0 or TeamSpaces == 0:
        print('There are no longer any spaces of this team type.')
    else:
        print('Invalid input')
        return TeamSpaces, SinglePlayerSpaces, TotalSpaces
    #--Team Placements--#
def PlaceTeam(Events, TeamName, TeamScore, Positions, PositionScore):
    print('Team Placements')
    time.sleep(0.5)
    for i, val in enumerate(Events):  
        print(f'Event {i} = {val}')
        for x, val in enumerate(TeamName):
            score = input(f"Please enter {TeamName[x]}'s place in {Events[i]} (in words)\n")
            for y, val in enumerate(Positions):
                if score.lower == Positions[y]:
                    if(len(TeamScore) <= x):
                        TeamScore[x] = TeamScore[x]+PositionScore[y]
                        print(f'{TeamName[x]} score is now {TeamScore[x]}')
                    else:
                        TeamScore.append(PositionScore[y])
                        print(f'{TeamName[x]} score is now {TeamScore[x]}')
                else:
                    print('No score added')
    #--Score Output--#
def OutputScore(TeamName,TeamScore):
    print('Score output')
    for x, val in enumerate(TeamName):
        time.sleep(0.25)
        print(f"{TeamName[x]}'s score is {TeamScore[x]}\n")
    #--Program Output--#
def ProgramRun():
    choice = int(input("\nPress 1 to create events\nPress 2 to create teams\nPress 3 to calculate the teams score\nPress 4 to output the team rankings\nPress 5 to exit the program\nPress 6 to clear the screen\n\n"))
    if choice == 1:
        EventCreate(Events,EventType)
    elif choice == 2:
        TeamCreate(TeamName,TeamEventsParticipateIn,TotalSpaces,SinglePlayerSpaces,TeamSpaces)
    elif choice == 3:
        PlaceTeam(Events, TeamName, TeamScore, Positions, PositionScore)
    elif choice == 4:
        OutputScore(TeamName, TeamScore)
    elif choice == 5:
        print('Program exiting')
        time.sleep(1.5)
        exit()
    elif choice == 6:
        print('Clearing screen')
        time.sleep(0.75)
        os.system('cls')
    else:
        print('Invalid choice')
    
#---Run Program---#
print("Welcome to the program")
while loop == True:
    ProgramRun()