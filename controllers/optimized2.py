import sys, os, datetime
start = datetime.datetime.now()
sys.path.append("..")
from memory_profiler import profile
from functions import Clean, isFloat
from constantes import MAX_INVEST, OPTIMIZED2_LOG_FILE
from models.dataset import GetActionsValues, testArgv
from models.actions import porteFolio
from views.reports import optimizedReport

o2=open(OPTIMIZED2_LOG_FILE,'w+')

testArgv(sys.argv, "optimized")

# @profile(stream=o2)
def getMaxProfit(max_Invest, actionsObjList, actionsContainFloat):
    n = len(actionsObjList)
    table = [["0" for x in range(max_Invest + 1)] for x in range(n + 1)]

    for i in range(len(actionsObjList) + 1):
        cost = actionsObjList[i - 1].cost
        gain = actionsObjList[i - 1].gain
        for j in range(MAX_INVEST + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif cost <= j:
                print(cost)
                print(gain)
                exit()
                if gain + table[i - 1][j - cost] > table[i - 1][j]:
                    table[i][j] = gain + table[i - 1][j - cost]
                else:
                    table[i][j] = table[i - 1][j]
            else:
                table[i][j] = table[i - 1][j]

    actionsToBuy = []
    actionsCost = 0

    # Retracing the actions selected
    j = MAX_INVEST
    for i in range(n, 0, -1):
        name = actionsObjList[i - 1].name
        cost = actionsObjList[i - 1].cost
        if table[i][int(j)] != table[i - 1][int(j)]:
            actionsToBuy.append(name)
            actionsCost += cost
            j -= cost

    actionsVar = ", ".join(actionsToBuy)

    if actionsContainFloat:
        return actionsVar, table[n][MAX_INVEST] / 100, actionsCost / 100, datetime.datetime.now() - start
    else:
        return actionsVar, table[n][MAX_INVEST], actionsCost, datetime.datetime.now() - start

data_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
actionsValues = GetActionsValues(data_path)

actionsContainFloat = (isFloat(actionsValues))

actionsObjList = []
maxInvest = MAX_INVEST

for name, cost, profit in zip(actionsValues[0], actionsValues[1], actionsValues[2]):
    if actionsContainFloat:
        action = porteFolio(name, cost * 100, profit * 100)
    else:
        action = porteFolio(name, cost, profit)
    actionsObjList.append(action)

if actionsContainFloat:
    maxInvest = MAX_INVEST * 100

Clean()

optimizedReport(getMaxProfit(maxInvest, actionsObjList, actionsContainFloat))