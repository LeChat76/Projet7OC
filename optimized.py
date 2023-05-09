from constantes import ACTIONS_COSTS_LIST, ACTIONS_PROFITS_LIST

profitsList = []
for profit, cost in zip(ACTIONS_PROFITS_LIST, ACTIONS_COSTS_LIST):
    profitRound = round((int(profit) / int(cost)), 2)
    profitsList.append(profitRound)

profitsList, ACTIONS_COSTS_LIST, ACTIONS_PROFITS_LIST = zip(*sorted(zip(profitsList, ACTIONS_COSTS_LIST, ACTIONS_PROFITS_LIST), reverse=True))

# print(profitsList)
# print(ACTIONS_COSTS_LIST)
# print(ACTIONS_PROFITS_LIST)


    