from constantes import MAX_INVEST

def Optimized():
  from constantes import ACTIONS_PROFITS_LIST, ACTIONS_COSTS_LIST, ACTIONS_NAMES_LIST
  profitsList = []
  for profit, cost in zip(ACTIONS_PROFITS_LIST, ACTIONS_COSTS_LIST):
    profitRound = round((int(profit) / int(cost)), 2)
    profitsList.append(profitRound)

  profitsList, ACTIONS_COSTS_LIST, ACTIONS_PROFITS_LIST, ACTIONS_NAMES_LIST = zip(*sorted(zip(profitsList, ACTIONS_COSTS_LIST, ACTIONS_PROFITS_LIST, ACTIONS_NAMES_LIST), reverse=True))

  soldRemain = MAX_INVEST
  totalProfit = 0
  actionsList = ""
  for cost, profit, actionName in zip(ACTIONS_COSTS_LIST, ACTIONS_PROFITS_LIST, ACTIONS_NAMES_LIST):
    if soldRemain - int(cost) >= 0:
      totalProfit += (int(profit)/100) * int(cost)
      soldRemain -= int(cost)
      actionsList += actionName + ", "
  print("Choix des actions à acheter pour un meilleur rendement : \n" + str(actionsList[:-2]) + ".")
  print("Cout des achats : " + str(MAX_INVEST - soldRemain) + "€.")
  print("Gain avec cette combinaison : " + str(round(totalProfit, 2)) + "€.")

    