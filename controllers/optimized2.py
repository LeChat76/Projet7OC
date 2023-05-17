import sys, os, datetime
start = datetime.datetime.now()
sys.path.append("..")
from memory_profiler import profile
o2=open('..\datas\memory_profiler_optimized2.log','w+')
from functions import Clean, TestIfFloat
from constantes import MAX_INVEST
from models.dataset import GetActionsValues, testArgv
from views.reports import optimizedReport, displayMsg

testArgv(sys.argv, "optimized")
actionsValues = GetActionsValues(sys.argv[1])
if TestIfFloat(actionsValues):
    Clean()
    displayMsg("Dataset contains floats, unable to use with tables.")
    exit()

@profile(stream=o2)
def portfolio(MAX_INVEST, costs, gains, actions):
    n = len(costs)
    table = [["0" for x in range(MAX_INVEST + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        cost = costs[i - 1]
        gain = gains[i - 1]
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
        if table[i][int(j)] != table[i - 1][int(j)]:
            actionsToBuy.append(actions[i - 1])
            actionsCost += costs[i - 1]
            j -= costs[i - 1]

    actionsVar = ", ".join(actionsToBuy)

    return actionsVar, table[n][MAX_INVEST], actionsCost, datetime.datetime.now() - start

data_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
actionsValues = GetActionsValues(data_path)
actionsNamesList = actionsValues[0]
# actionsNamesList = ['Action-1', 'Action-2', 'Action-3', 'Action-4', 'Action-5', 'Action-6', 'Action-7', 'Action-8', 'Action-9', 'Action-10', 'Action-11', 'Action-12', 'Action-13', 'Action-14', 'Action-15', 'Action-16', 'Action-17', 'Action-18', 'Action-19', 'Action-20']
actionsCostsList = actionsValues[1]
# actionsCostsList = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114]
actionsProfitsList = actionsValues[2]
# actionsProfitsList = [5, 10, 15, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1, 3, 8, 12, 14, 21, 18]
actionsGainsList = actionsValues[3]
# actionsGainsList = [1.0, 3.0, 7.5, 14.0, 10.2, 20.0, 1.54, 2.86, 6.24, 9.18, 7.14, 9.9, 8.74, 0.14, 0.54, 0.64, 0.48, 1.4, 5.04, 20.52]

Clean()

optimizedReport(portfolio(MAX_INVEST, actionsCostsList, actionsGainsList, actionsNamesList))