import sys, os, datetime
start = datetime.datetime.now()
sys.path.append("..")
from constantes import MAX_INVEST
from functions import Clean
from models.dataset import GetActionsValues, testArgv
from views.reports import optimizedReport


testArgv(sys.argv, "optimized")

class porteFolio:
    def __init__(self, name, cost, profit): 
        self.name = name
        self.cost = int(cost)
        self.profit = int(profit)
        self.ratio = (self.cost * (self.profit / 100)) + self.profit

    def __lt__(self, nextObj):
        return self.ratio < nextObj.ratio

def getMaxProfit(actionsNames, actionsCosts, actionsProfits, MAX_INVEST):
    ''' return max profit from actions's costs and profits '''
    ''' output : INTEGER '''
    
    actionsSorted = []

    for i in range(len(actionsCosts)):
        action = porteFolio(actionsNames[i], actionsCosts[i], actionsProfits[i])
        actionsSorted.append(action)
    
    actionsSorted.sort(reverse=True)

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
            # print(str(action.name) + " - " + str(action.profit))

    actionsNames = actionsNames[:-2]
    return actionsNames, finalProfit, MAX_INVEST - maxInvest, datetime.datetime.now() - start

Clean()
data_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
actionsValues = GetActionsValues(data_path)
actionsNamesList = actionsValues[0]
actionsCostsList = actionsValues[1]
actionsProfitsList = actionsValues[2]
optimizedReport(getMaxProfit(actionsNamesList, actionsCostsList, actionsProfitsList, MAX_INVEST))
