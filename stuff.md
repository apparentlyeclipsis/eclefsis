# Variables and Imports
```python
import random

plrStats = [
    # stores data like this:
    # [0, 5]
    # index-0 is points
    # index-1 is dice remaining
    
    # reason for this is modularity, so we can realistically like
    # as many players as we want w/o having like 300 variables
]
```

# Main functions
these are in order they appear within the program
```python
def check(results, dices):
    changes = [0, dices]
    # why are we doing it like this?
    # because we want to return multiple values
    # and also because this is how its stored in
    # the main gameplay loop
    for roll in results:
        # for each roll, add points
        changes[0] += roll
        if roll == 5 or roll == 2:
            changes[1] -= 1
            # if rolled 5 or 2
            # remove dice
    if changes[1] < dices:
        changes[0] = 0
        # if less dices than before,
        # reset points gained
    print(f"POINTS GAINED  > {changes[0]}")
    print(f"REMAINING DICE > {changes[1]}")
    # prints out changes so players know what they got
    
    return changes
    # returned array that has changes
```

```python
def roll(dices): # gurnoor
    rolls = []
    # store dice rolls temporarily
    for i in range(dices):
        rolls.append(random.randint(1, 6))
        # append rolls to temporary array
    print(f"ROLL RESULTS > {rolls}")
    # print what was rolled so people can see
    
    input("<CONTINUE> ")
    return check(rolls, dices) # return values after checking
```

```python
def play(players):      # arush
    for player in range(players):
        plrStats.append([0, 5])
        # adds stats for every player
    
    gameActive = True
    gameRound = 1
    while gameActive: #while players still have dice
        lostPlayers = 0
        print(f"ROUND #{gameRound} BEGINS")
        for player in range(len(plrStats)):
            if plrStats[player][1] > 0:
                # only continues if the player has dice
                # why? because what if you have 0 dice
                # you cant play without dice
                print(f"PLAYER {player+1}'s TURN")
                input("<ROLL> ")
                temp = roll(plrStats[player][1])
                # temporary array to hold results
                # why? because rolling twice would give you
                # different results
                plrStats[player][0] += temp[0]
                plrStats[player][1] = temp[1]
                # adds points gained
                # replaces dice value with current amount of dices
                print()
            else:
                lostPlayers += 1
                # this resets every loop so
                # we'd have whats theoretically the
                # most updated version
        gameRound += 1
        if lostPlayers == len(plrStats):
            gameActive = False
            # ends match!
            print(f"GAME OVER - LASTED {gameRound-2} ROUNDS")
    finalResults()
```

# Secondary Functions
```python
def finalResults():  # cole
    highestPoints = 0
    winner = 0
    for plr in range(len(plrStats)):
        # goes through data for every player,
        # checks how many points they have
        if plrStats[plr][0] > highestPoints:
            # the person with the highest points is
            # set to winner, and the next person
            # needs more points than the winnter
            winner = plr
            highestPoints = plrStats[plr][0]
    print(f"WINNER > PLAYER #{winner+1}")
    print(f"POINTS > {highestPoints}")
    print()
    
    print(f"ALL RESULTS:")
    for plr in range(len(plrStats)):
        print(f"PLAYER #{plr+1}: {plrStats[plr][0]}")
        # prints out points every player had
```

```python
def betterInput(inputType, question):
    while True:
        response = input(question)
        try:
            if inputType == "int":
                response = int(response)
            elif inputType == "float":
                response = float(response)
            
            return response
        except:
            print("ERROR")
```
