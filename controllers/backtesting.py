import sys, os, datetime
start = datetime.datetime.now()
sys.path.append("..")
from models.dataset import GetActionsValues, testArgvBacktesting

testArgvBacktesting(sys.argv)

actionsValues = GetActionsValues(sys.argv[1])
actionsChoice = GetActionsValues(sys.argv[2])
cost, profit = 0

def CombinationResult(actionsValues, actionsChoice):
    for actionChoice in actionsChoice:
        if actionChoice in actionsValues:
            cost += actionChoice[1]
            profit += actionChoice[2]
            





CombinationResult(actionsValues, actionsChoice)

