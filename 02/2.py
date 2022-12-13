# A, X Rock, B, Y paper, C, Z Scissors
win = ['A Y', 'B Z', 'C X']
lose = ['A Z', 'B X', 'C Y']
tie = ['A X', 'B Y', 'C Z']
hand_score = {'X': 1, 'Y': 2, 'Z': 3}
game_score = {
    **{game: 6 for game in win},
    **{game: 3 for game in tie},
    **{game: 0 for game in lose},
}

with open('2/input') as handle:
    games = [line.strip() for line in handle.readlines()]

total_score = 0
for game in games:
    total_score += game_score[game] + hand_score[game[-1]]

print(total_score)

# theirs -> outcome -> yours
move_map = {
    'rock': {'win': 'paper', 'tie': 'rock', 'lose': 'scissors'},
    'paper': {'win': 'scissors', 'tie': 'paper', 'lose': 'rock'},
    'scissors': {'win': 'rock', 'tie': 'scissors', 'lose': 'paper'},
}
char_to_move = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
char_to_outcome = {'X': 'lose', 'Y': 'tie', 'Z': 'win'}
move_score = {'rock': 1, 'paper': 2, 'scissors': 3}
game_score = {'win': 6, 'tie': 3, 'lose': 0}

# games = [
#     'A X',  # 0 + 3 = 3
#     'A Y',  # 1 + 3 = 4
#     'A Z',  # 2 + 6 = 8
#     'B X',  # 1 + 0 = 1
#     'B Y',  # 2 + 3 = 5
#     'C X',  # 2 + 0 = 2
#     'C Y',  # 3 + 3 = 6
#     'C Z',  # 1 + 6 = 7
# ]

total_score = 0
for game in games:
    their_move_char, outcome_char = game.split(' ')
    their_move, outcome = char_to_move[their_move_char], char_to_outcome[outcome_char]
    print(move_score[move_map[their_move][outcome]], game_score[outcome])
    total_score += game_score[outcome] + move_score[move_map[their_move][outcome]]

print(total_score)
