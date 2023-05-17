import sys, os, datetime
start = datetime.datetime.now()
sys.path.append("..")
from memory_profiler import profile
from constantes import MAX_INVEST, OPTIMIZED_LOG_FILE
from functions import Clean
from models.dataset import GetActionsValues, testArgv
from models.actions import porteFolio
from views.reports import optimizedReport

o1=open(OPTIMIZED_LOG_FILE,'w+')

testArgv(sys.argv, "optimized")

actionsContainFloat = False

@profile(stream=o1)
def getMaxProfit(MAX_INVEST, actionsObjList):
    ''' return max profit from actions's costs and profits '''
    ''' output : INTEGER '''
    
    actionsSorted = []

    for action in actionsObjList:
        action = porteFolio(action.name, action.cost, action.profit, actionsContainFloat)
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

    actionsNames = actionsNames[:-2]
    return actionsNames, finalProfit, MAX_INVEST - maxInvest, datetime.datetime.now() - start

Clean()

data_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
actionsValues = GetActionsValues(data_path)

actionsObjList = []

for name, cost, profit in zip(actionsValues[0], actionsValues[1], actionsValues[2]):
    action = porteFolio(name, cost, profit, actionsContainFloat)
    actionsObjList.append(action)

optimizedReport(getMaxProfit(MAX_INVEST, actionsObjList ))
