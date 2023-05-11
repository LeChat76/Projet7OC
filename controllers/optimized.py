import sys, os
sys.path.append("..")
from constantes import MAX_INVEST
from models.dataset import GetActionsValues, testArgv
from views.reports import optimizedReport


testArgv(sys.argv, "optimized")

class porteFolio:
    def __init__(self, name, cost, profit): 
        self.name = name
        self.cost = int(cost)
        self.profit = int(profit)
        # self.ratio = (self.profit / self.cost)
        self.ratio = (self.cost * self.profit / 100) / self.cost

    def __lt__(self, nextObj):
        return self.ratio < nextObj.ratio

def getMaxProfit(actionsNames, actionsCosts, actionsProfits, MAX_INVEST):
    ''' return max profit from actions's costs and profits '''
    ''' output : INTEGER '''
    actionsSorted = []
    # actionsRatio = "Ratios : "
    # actionsRatioSorted = "Ratios : "
    # actionsCost = "Costs : "
    # actionsCostSorted = "Costs : "
    # actionsProfit = "Profits : "
    # actionsProfitSorted = "Profits : "

    for i in range(len(actionsCosts)):
        action = porteFolio(actionsNames[i], actionsCosts[i], actionsProfits[i])
        actionsSorted.append(action)
    #     actionsRatio += str(action.ratio) + " - "
    #     actionsCost += str(action.cost) + " - "
    #     actionsProfit += str(action.profit) + " - "

    # print("*" * 150)
    # print("Liste extraite du dataset :")

    # print(actionsCost[:-2])
    # print(actionsProfit[:-2])
    # print(actionsRatio[:-2])

    actionsSorted.sort(reverse = True)

    # print("*" * 150)
    # print("Liste triée par ratio :")

    # for action in actionsSorted:
    #     actionsCostSorted += str(action.cost) + " - "
    #     actionsProfitSorted += str(action.profit) + " - "
    #     actionsRatioSorted += str(format(action.ratio, '.2f')) + " - "
    
    # print(actionsCostSorted[:-2])
    # print(actionsProfitSorted[:-2])
    # print(actionsRatioSorted[:-2])
    
    print("*" * 150)

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

data_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
actionsValues = GetActionsValues(data_path)
actionsNamesList = actionsValues[0]
actionsCostsList = actionsValues[1]
actionsProfitsList = actionsValues[2]
optimizedReport(getMaxProfit(actionsNamesList, actionsCostsList, actionsProfitsList, MAX_INVEST))
