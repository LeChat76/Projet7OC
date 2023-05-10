import sys
sys.path.append("..")
from functions import GetActionsValues
from constantes import MAX_INVEST


class porteFolio:
    def __init__(self, name, cost, profit): 
        self.name = name
        self.cost = int(cost)
        self.profit = int(profit)
        self.ratio = round((self.profit / self.cost), 2)

    def __lt__(self, nextObj):
        return self.ratio < nextObj.ratio

def getMaxProfit(actionsNames, actionsCosts, actionsProfits, MAX_INVEST):
    ''' return max profit from actions's costs and profits '''
    ''' output : INTEGER '''
    actionsSorted = []
    # actionsRatio = ""
    # actionsRatioSorted = ""
    # actionsCost = ""
    # actionsCostSorted = ""
    # actionsProfit = ""
    # actionsProfitSorted = ""

    for i in range(len(actionsCosts)):
        action = porteFolio(actionsNames[i], actionsCosts[i], actionsProfits[i])
        actionsSorted.append(action)
    #     actionsRatio += str(action.ratio) + " - "
    #     actionsCost += str(action.cost) + " - "
    #     actionsProfit += str(action.profit) + " - "

    # print(actionsCost)
    # print(actionsProfit)
    # print(actionsRatio)

    actionsSorted.sort(reverse = True)

    # print("******************************************************************")

    # for action in actionsSorted:
    #     actionsRatioSorted += str(action.ratio) + " - "
    #     actionsCostSorted += str(action.cost) + " - "
    #     actionsProfitSorted += str(action.profit) + " - "
    
    # print(actionsCostSorted)
    # print(actionsProfitSorted)
    # print(actionsRatioSorted)

    finalProfit = 0
    maxInvest = MAX_INVEST
    actionsNames = ""

    for action in actionsSorted:
        cost = int(action.cost)
        profit = int(action.profit)
        if maxInvest - cost >= 0:
            maxInvest -= cost 
            finalProfit += cost * profit / 100
            actionsNames += action.name + ", "

    actionsNames = actionsNames[:-2]
    return actionsNames, finalProfit, MAX_INVEST - maxInvest

actionsValues = GetActionsValues(sys.argv[1])
actionsNamesList = actionsValues[0]
actionsCostsList = actionsValues[1]
actionsProfitsList = actionsValues[2]
result = getMaxProfit(actionsNamesList, actionsCostsList, actionsProfitsList, MAX_INVEST) 

print("Actions à acheter : ", result[0])
print("Rendement max : " + str(round(result[1], 2)) + "€.")
print("Cout total : " + str(result[2]) + "€.")