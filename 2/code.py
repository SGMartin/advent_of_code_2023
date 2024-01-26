import re

with open("example.txt", "r") as fil:
    games = [g.rstrip() for g in fil.readlines()]

## remove prefix
games = [re.sub("^Game \d+: ", "", game) for game in games]
games = [re.sub(";", ",", game) for game in games]

games_best = {}
games_worst = {}

template = {"blue":0, "red":0, "green":0}

for i,game in enumerate(games):
    highest_result,lowest_result = {},{}
    highest_result.update(template)
    lowest_result.update(template)

    boxes = game.split(",")

    for box in boxes:
        if "green" in box:
            colour = "green"
        elif "red" in box:
            colour = "red"
        else:
            colour = "blue"
        
        val = int(re.findall(r"\d+", box)[0])

        if highest_result[colour] < val:
            highest_result[colour] = val
        
        if lowest_result[colour] == 0 or lowest_result[colour] > val:
            lowest_result[colour] = val
        
    games_best[i + 1] = highest_result
    games_worst[i + 1] = lowest_result


def sum_valid(games: dict) -> int:
    valid_ids = []

    for k,val in games.items():
        if val["green"] <= 13 and val["blue"] <= 14 and val["red"] <= 12:
            valid_ids.append(k)
    
    return sum(valid_ids)




print(f"Part 1 answer is: {sum_valid(games_best)}")
