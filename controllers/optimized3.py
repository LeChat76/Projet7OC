import sys, os
sys.path.append("..")
from constantes import MAX_INVEST
from models.dataset import GetActionsValues, testArgv
from views.reports import optimizedReport

testArgv(sys.argv, "optimized")

def portfolio(MAX_INVEST, costs, gains):
    n = len(costs) # 20
    # creation of a table with 21 X (500 x 0)
    table = [[0 for x in range(MAX_INVEST + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(MAX_INVEST + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif costs[i - 1] <= j:
                table[i][j] = max(gains[i - 1] + table[i - 1][j - costs[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]
    
    return table[n][MAX_INVEST]

data_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
actionsValues = GetActionsValues(data_path)
actionsNamesList = actionsValues[0]
actionsCostsList = actionsValues[1]
actionsGainsList = actionsValues[3]

optimizedReport(["", portfolio(MAX_INVEST, actionsCostsList, actionsGainsList), ""])
