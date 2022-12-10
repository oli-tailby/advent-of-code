# Read input and split to nested array form
def strategy_input(filename):
    with open(filename) as f:
        rounds = f.read().splitlines()

    strategy = [r.split() for r in rounds]

    return strategy

# Calculate score from AOC rules given a relevant lookup
def calculate_score(lookup):
    score = 0
    for i in strategy:
        score += lookup[i[0]][i[1]]
    return score

strategy = strategy_input('input.txt')

# Part 1
score_lookup = {'A':{'X':4, 'Y':8, 'Z':3},
                'B':{'X':1, 'Y':5, 'Z':9},
                'C':{'X':7, 'Y':2, 'Z':6}}

calculate_score(score_lookup)

# Part 2
score_lookup_2 = {'A':{'X':3, 'Y':4, 'Z':8},
                  'B':{'X':1, 'Y':5, 'Z':9},
                  'C':{'X':2, 'Y':6, 'Z':7}}

calculate_score(score_lookup_2)
