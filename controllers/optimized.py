import sys
sys.path.append("..")
from functions import GetActionsValues
from constantes import MAX_INVEST


class porteFolio:
    def __init__(self, cost, profit): 
        self.cost = int(cost)
        self.profit = int(profit)
        self.ratio = self.profit // self.cost

    def __lt__(self, nextObj):
        return self.ratio < nextObj.ratio
  
def getMaxValue(actionsCosts, actionsProfits, MAX_INVEST): 
    actionsSorted = []

    for i in range(len(actionsCosts)): 
        actionsSorted.append(porteFolio(actionsCosts[i], actionsProfits[i]))

    actionsSorted.sort(reverse = True)

    finalProfit = 0

    for action in actionsSorted: 
        cost = int(action.cost) 
        profit = int(action.profit) 
        if MAX_INVEST - cost >= 0: 
            MAX_INVEST -= cost 
            finalProfit += profit

    return finalProfit 

actionsValues = GetActionsValues(sys.argv[1])
actionsCostsList = actionsValues[1]
actionsProfitsList = actionsValues[2]
valeurMax = getMaxValue(actionsCostsList, actionsProfitsList, MAX_INVEST) 
print("Rendement max =", valeurMax) 