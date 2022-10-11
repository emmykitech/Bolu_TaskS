from random import choice


team_one = []
team_two = []
final_match = []

club = {
    'avl': 'AVL',
    'ars': 'ARS',
    'bha': 'BHA',
    'bre': 'BRE',
    'che': 'CHE',
    'cry': 'CRY',
    'eve': 'EVE',
    'lei': 'LEI',
    'liv': 'LIV',
    'lu': 'LU',
    'mci': 'MCI',
    'mu': 'MU',
    'nor': 'NOR',
    'nu':  'NU',
    'sou': 'SOU',
    'tot': 'TOT',
    'wat': 'WAT',
    'whu': 'WHU',
    'wol': 'WOL',
    'bur': 'BUR'
}


def prediction(accept_dict):
    for name in accept_dict.values():
        team_one.append(name)
        team_two.append(name)

    count = 0
    num_of_pred = int(input(f"Enter amount of prediction needed: "))
    while count < num_of_pred:
        alpha1 = (choice(team_one))
        alpha2 = (choice(team_two))
        # combinutpu from alpha1 and alpha2 to make a list
        comb = [alpha1, alpha2]

        if (comb not in final_match) and comb[0] != comb[1]:
            count += 1
            final_match.append(comb)

        elif (comb in final_match):
            continue

    for match in final_match:
        print(f"{match[0]} vs {match[1]}")


prediction(club)
