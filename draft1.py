import random

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

def ScoreSystemProccess(Team_Name, Team_Score, Num_Of_Events, points, positions, TeamSpaces, SinglePlayerSpaces, TotalSpaces, EventType, TeamPosition):
    while TotalSpaces < 15:  # Change loop condition to ensure it doesn't exceed the length of the lists
        SinglePlayerConfirm = input(f"Is team {TotalSpaces + 1} single player? y/n ")
        SinglePlayerConfirm = SinglePlayerConfirm.lower()
        if SinglePlayerConfirm == 'y':
            if SinglePlayerSpaces > 0:
                teamname = input("Please enter the team name: \n")
                Team_Name[TotalSpaces] = teamname
                print(f"The team {Team_Name[TotalSpaces]} has been saved")
                SinglePlayerSpaces -= 1
                TotalSpaces += 1
            else:
                print("Unfortunately there are no more single player team spaces remaining")
        elif SinglePlayerConfirm == 'n':
            if TeamSpaces > 0:
                teamname = input("Please enter the team name: \n")
                Team_Name[TotalSpaces] = teamname
                print(f"The team {Team_Name[TotalSpaces]} has been saved")
                TeamSpaces -= 1
                TotalSpaces += 1
            else:
                print("Unfortunately there are no more multiplayer team spaces remaining")
        else:
            print("invalid input")
        if TotalSpaces < 15:  # Check if TotalSpaces is still less than 15 before attempting to add a team
            OnlyOneEvent = input(f"Is team {TotalSpaces + 1} entering into only one event? y/n ")
            OnlyOneEvent = OnlyOneEvent.lower()
            if OnlyOneEvent == 'y':
                Num_Of_Events[TotalSpaces] = 1
            else:
                Num_Of_Events[TotalSpaces] = 6     
        for i in range(6):
            print(f"Event {i + 1} is a {random.choice(EventType)}")  # Fix random.choice usage
            for x in range(TotalSpaces):  # Iterate over TotalSpaces
                if Num_Of_Events[x] == 1 and i > 1:
                    print(f"{Team_Name[x]} is only entered for one event")
                else:
                    TeamPosition = input(f"Please enter {Team_Name[x]} position in the tournament: \n").lower()
                    for y in range(len(positions)):  # Iterate over length of positions
                        if TeamPosition == positions[y]:
                            Team_Score[x] += points[y]  # Use shorthand increment operator
                        else:
                            Team_Score[x] += 0  # This line is redundant, can be removed
        for x in range(TotalSpaces):  # Iterate over TotalSpaces
            print(f"Team {Team_Name[x]} has {Team_Score[x]} points.\n")


while loop:
    print("Welcome to the Scoring system")
    confirm = input("Would you like to use the system? (y/n) ")
    if confirm.lower() == 'y':
        ScoreSystemProccess(Team_Name, Team_Score, Num_Of_Events, points, positions, TeamSpaces, SinglePlayerSpaces, TotalSpaces, EventType, TeamPosition)
        print('system in use')
        confirm = input("\nWould you like to use the system again? (y/n) ")
        if confirm.lower() != 'y':
            loop = False
    elif confirm.lower() == 'n':
        print("System Closing. \n Thank you")
        loop = False
    else:
        print("invalid input")
