import sys, os
sys.path.append("..")
from constantes import MAX_INVEST
from models.dataset import GetActionsValues, testArgv
from views.reports import optimizedReport

testArgv(sys.argv, "optimized")

def portfolio(maxInvest, costs, gains):
    n = len(costs)
    table = [[0 for x in range(maxInvest + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(maxInvest + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif costs[i - 1] <= j:
                table[i][j] = max(gains[i - 1] + table[i - 1][j - costs[i - 1]], table[i - 1][j]
                )
            else:
                table[i][j] = table[i - 1][j]

    return table[n][maxInvest]

data_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
actionsValues = GetActionsValues(data_path)
actionsNamesList = actionsValues[0]
actionsCostsList = actionsValues[1]
actionsGainsList = actionsValues[3]
# actionsProfitsList = [1, 3, 7.5, 14, 10.2, 20, 1.54, 2.86, 6.24, 9.18, 7.14, 9.9, 8.74, 0.14, 0.54, 0.64, 0.48, 1.4, 5.04, 20.52]
# actionsProfitsList = [5, 10, 15, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1, 3, 8, 12, 14, 21, 18]
# actionsCostsList = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4,  10, 24, 114]
maxInvest = MAX_INVEST


optimizedReport(["", portfolio(maxInvest, actionsCostsList, actionsGainsList), ""])
# print(format(knapSack(maxInvest, actionsCostsList, actionsGainsList), '.2f') + "€")