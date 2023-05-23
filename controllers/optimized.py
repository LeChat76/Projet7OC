import sys, os, datetime
start = datetime.datetime.now()
sys.path.append("..")
from constantes import MAX_INVEST
from functions import Clean
from models.dataset import GetActionsValues, testArgv
from models.actions import porteFolio
from views.reports import optimizedReport

testArgv(sys.argv, "optimized")

actionsContainFloat = False

def getMaxProfit(MAX_INVEST, actionsObjList):
    ''' return max profit from actions's costs and profits '''
    actionsSorted = []
    finalProfit = 0
    maxInvest = MAX_INVEST
    actionsNames = ""

    # create list of action ordered by ratio profit + gain
    for action in actionsObjList:
        action = porteFolio(action.name, float(action.cost), action.profit, actionsContainFloat)
        actionsSorted.append(action)
    actionsSorted.sort(reverse=True)

    # gloutonous algorithm to add actions's cost one by one to reach MAX_INVEST
    for action in actionsSorted:
        cost = float(action.cost)
        profit = float(action.profit)
        if maxInvest - cost >= 0:
            maxInvest -= cost
            finalProfit += cost * profit / 100
            actionsNames += action.name + ", "

    actionsNames = actionsNames[:-2] # ([:-2] to remove ", " at the end of the last actions's list)

    return actionsNames, finalProfit, MAX_INVEST - maxInvest, datetime.datetime.now() - start

Clean()

# creation of actions's object list from dataset
data_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
actionsValues = GetActionsValues(data_path)

actionsObjList = []

for name, cost, profit in zip(actionsValues[0], actionsValues[1], actionsValues[2]):
    action = porteFolio(name, cost, profit, actionsContainFloat)
    if action.cost > 0: # remove error in dataset
        actionsObjList.append(action)

# executing script
maxProfit = getMaxProfit(MAX_INVEST, actionsObjList )

# reporting
optimizedReport(maxProfit)
