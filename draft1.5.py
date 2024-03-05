import random #imports
#assign variables and declare arrays
loop = True
Team_Name = [''] * 15
Team_Score = [0] * 15
Num_Of_Events = [0] * 15
points = [5, 3, 1]
positions = ['first', 'second', 'third']
TeamSpaces = 5
SinglePlayerSpaces = 10
TotalSpaces = 0
events = ['event 1', 'event 2', 'event 3', 'event 4', 'event 5', 'event 6']
EventType = ['Academic Event', 'Sport Event']
TeamPosition = ''
#define the function that runs the code, adds teams and collates their score
def ScoreSystemProccess(Team_Name, Team_Score, Num_Of_Events, points, positions, TeamSpaces, SinglePlayerSpaces, TotalSpaces, EventType, TeamPosition):
    while TotalSpaces < 15: 
        SinglePlayerConfirm = input(f"Is team {TotalSpaces + 1} single player? y/n ")
        SinglePlayerConfirm = SinglePlayerConfirm.lower() # use .lower() to catch responses regardless of case sensitivity
        if SinglePlayerConfirm == 'y':
            if SinglePlayerSpaces > 0: #ensures that there is enough spaces within that category of team
                teamname = input("Please enter the team name: \n")
                Team_Name[TotalSpaces] = teamname
                print(f"The team {Team_Name[TotalSpaces]} has been saved")
                SinglePlayerSpaces -= 1
                TotalSpaces += 1
            else:
                print("Unfortunately there are no more single player team spaces remaining")
        elif SinglePlayerConfirm == 'n':
            if TeamSpaces > 0: #ensures that there is enough spaces within that category of team
                teamname = input("Please enter the team name: \n")
                Team_Name[TotalSpaces] = teamname
                print(f"The team {Team_Name[TotalSpaces]} has been saved")
                TeamSpaces -= 1
                TotalSpaces += 1
            else:
                print("Unfortunately there are no more multiplayer team spaces remaining")
        else:
            print("invalid input")
        if TotalSpaces < 15:
            OnlyOneEvent = input(f"Is team {TotalSpaces} entering into only one event? y/n ")
            OnlyOneEvent = OnlyOneEvent.lower()
            if OnlyOneEvent == 'y':
                print(f"Event 1 is a {random.choice(EventType)}")  #uses random to assign either academic or althletic event
                for x in range(TotalSpaces): 
                    TeamPosition = input(f"Please enter {Team_Name[x]} position in the tournament: \n").lower()
                    for y in range(len(positions)):  
                        if TeamPosition == positions[y]:
                            print(f'{points[y]} added')
                        else:
                            Team_Score[x] += 0
                            print(f'0 points added')
            elif OnlyOneEvent == 'n':
                for i in range(6):
                    print(f"Event {i + 1} is a {random.choice(EventType)}")  #uses random to assign either academic or althletic event
                    for x in range(TotalSpaces): 
                        TeamPosition = input(f"Please enter {Team_Name[x]} position in the tournament: \n").lower()
                        for y in range(len(positions)):  
                            if TeamPosition == positions[y]:
                                Team_Score[x] += points[y]  
                                print(f'{points[y]} added')
                            else:
                                Team_Score[x] += 0
                                print(f'0 points added')
            else:
                print('Invalid input') #error cathcing
        
    for x in range(TotalSpaces):  
        print(f"Team {Team_Name[x]} has {Team_Score[x]} points.\n")


while loop == True: #repeats constantly
    print("Welcome to the Scoring system")
    confirm = input("Would you like to use the system? (y/n) ")
    if confirm.lower() == 'y':
        ScoreSystemProccess(Team_Name, Team_Score, Num_Of_Events, points, positions, TeamSpaces, SinglePlayerSpaces, TotalSpaces, EventType, TeamPosition) #calls function
        confirm = input("\nWould you like to use the system again? (y/n) ")
        if confirm.lower() != 'y':
            loop = False #stops from repeating
    elif confirm.lower() == 'n': #stops from repeating
        print("System Closing. \n Thank you")
        loop = False
    else:
        print("invalid input")#error catching
