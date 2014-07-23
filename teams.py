# Copyright © 2014 Bart Massey
# Additions made by Kainoa Gaddis (c)
# Randomly partition people into teams.

# Given a team size n and a number m of team members,
# print out the teams one per line. If m is
# not evenly divisible by n, assign the "extra" members
# evenly to other teams.

from random import randrange

# Team size
n = int(input("Team size? "))

# Number of participants
m = int(input("Number of participants? "))

# Given a list of participants, return
# teams as a list of lists of participants.
def make_teams(participants):
    # Set up counts and accumulator.
    teams = []
    l = len(participants)
    residue = l % n

    # Loop over teams.
    for _ in range(l // n):
        # Set up accumulator.
        members = []
        
        # Check for an extra person that needs a team.
        team_size = n
        if residue > 0:
            team_size += 1
            residue -= 1
        
        # Loop over team members.
        for _ in range(team_size):
            i = randrange(len(participants))
            members += [participants[i]]
            del participants[i]
        
        # Remember the new team.
        teams += [members]

    return teams
            
# Create dictionary to print teams to make them easier to find
def print_teams(teams):
    team_numbers = {}
    num = 1
    for i in teams:
        team_numbers[num] = i
        num += 1

    # Print team numbers for individuals for quick look up
    print("\nCorresponding teams for the individuals")
    for j in range (1, m + 1):
        for k in team_numbers:
            if j in team_numbers[k]:
                print(j, ":", k)

    # Print teams by team number
    print("\nTeams listed in order of team numbers.")
    for k in team_numbers:
        print("Team", str(k) + ":", team_numbers[k])
     
# Produce and print the teams.
teams = make_teams(list(range(1, m + 1)))
print_teams(teams)

input("\n\nPress enter to exit")
