import itertools as it


def count_wins(dice1, dice2):
	assert len(dice1) == 6 and len(dice2) == 6
	dice1_wins, dice2_wins = 0, 0

	for i in range(6):
		for j in range(6):
			if dice1[i] < dice2[j]:
				dice2_wins += 1
			else:
				if dice1[i] > dice2[j]:
					dice1_wins += 1

	return (dice1_wins, dice2_wins)


def find_the_best_dice(dices):
	assert all(len(dice) == 6 for dice in dices)
	winner = []

	for i in range(len(dices) - 1):
		for j in range(i + 1, len(dices)):
			win1, win2 = count_wins(dices[i], dices[j])
			if win1 > win2:
				winner.append([i, j])
			else:
				if win2 > win1:
					winner.append([j, i])

	if len(winner) < len(dices) - 1:
		return winner

	new_win = []
	for i in range(len(winner)):
		new_win.append(winner[i][0])

	for i in range(len(dices)):
		count = 0
		for j in range(0, len(new_win)):
			if new_win[j] == i:
				count += 1
			if count == len(dices) - 1:
				return i
	return winner


dices =  [[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]
assert all(len(dice) == 6 for dice in dices)


strategy = dict()

if type(find_the_best_dice(dices)) == int:
  strategy["choose_first"] = True
  strategy["first_dice"] = find_the_best_dice(dices)
else:
  strategy["choose_first"] = False
  winner = find_the_best_dice(dices)
  for i in range(len(winner)):
    strategy[winner[i][1]] = winner[i][0]

print(strategy)