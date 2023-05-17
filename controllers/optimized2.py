import sys, os, datetime
start = datetime.datetime.now()
sys.path.append("..")
from memory_profiler import profile
from functions import Clean
from constantes import MAX_INVEST, OPTIMIZED2_LOG_FILE
from models.dataset import GetActionsValues, testArgv
from models.actions import porteFolio
from views.reports import optimizedReport

o2=open(OPTIMIZED2_LOG_FILE,'w+')

testArgv(sys.argv, "optimized")

@profile(stream=o2)
def getMaxProfit(MAX_INVEST, actionsList):
    n = len(actionsList)
    table = [["0" for x in range(MAX_INVEST + 1)] for x in range(n + 1)]

    for i in range(len(actionsList) + 1):
        cost = actionsList[i - 1].cost
        gain = actionsList[i - 1].gain
        for j in range(MAX_INVEST + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif cost <= j:
                if gain + table[i - 1][j - int(cost)] > table[i - 1][j]:
                    table[i][j] = gain + table[i - 1][j - int(cost)]
                else:
                    table[i][j] = table[i - 1][j]
            else:
                table[i][j] = table[i - 1][j]

    actionsToBuy = []
    actionsCost = 0

    # Retracing the actions selected
    j = MAX_INVEST
    for i in range(n, 0, -1):
        name = actionsList[i - 1].name
        cost = actionsList[i - 1].cost
        if table[i][int(j)] != table[i - 1][int(j)]:
            actionsToBuy.append(name)
            actionsCost += cost
            j -= cost

    actionsVar = ", ".join(actionsToBuy)

    return actionsVar, table[n][MAX_INVEST], actionsCost, datetime.datetime.now() - start

data_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
actionsValues = GetActionsValues(data_path)

actionsList = []

for name, cost, profit in zip(actionsValues[0], actionsValues[1], actionsValues[2]):
    action = porteFolio(name, cost, profit)
    actionsList.append(action)

Clean()

optimizedReport(getMaxProfit(MAX_INVEST, actionsList))