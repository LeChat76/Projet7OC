import sys, os, datetime
start = datetime.datetime.now()
sys.path.append("..")
from functions import Clean, isFloat
from constantes import MAX_INVEST
from models.dataset import GetActionsValues, testArgv
from models.actions import porteFolio
from views.reports import optimizedReport

# check if file argument exists and if can be accessed
testArgv(sys.argv, "optimized")

def getMaxProfit(maxInvest, actionsObjList, actionsContainFloat):
    ''' extract best combination of actions to buy '''
    
    print("Creating matrix....")
    n = len(actionsObjList)
    table = [[0 for x in range(maxInvest + 1)] for x in range(n + 1)]
    
    prevPercent = 0

    for i in range(n + 1):
        cost = actionsObjList[i - 1].cost

        gain = actionsObjList[i - 1].gain
        percent = int(i / (n + 1) * 100)

        # generate a percent progressbar
        if percent != prevPercent:
            Clean()
            int(i / (n + 1) * 100)
            print("Computed : " + str(int(i / (n + 1) * 100)) + "%")
            prevPercent = percent

        # dynamic algorithm
        for j in range(maxInvest + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            # if ....
            elif cost <= j:
                if gain + table[i - 1][j - int(cost)] > table[i - 1][j]:
                    table[i][j] = gain + table[i - 1][j - int(cost)]
                else:
                    table[i][j] = table[i - 1][j]
            else:
                table[i][j] = table[i - 1][j]

    actionsToBuy = []
    actionsCost = 0

    # Retracing the actions selected for the report
    if actionsContainFloat:
        j = maxInvest
    else:
        j = MAX_INVEST
    
    # seek all values (gains) changed. Changed meaning action bought so : added to actionsVar
    for i in range(n, 0, -1):
        name = actionsObjList[i - 1].name
        cost = actionsObjList[i - 1].cost
        if table[i][int(j)] != table[i - 1][int(j)]:
            actionsToBuy.append(name)
            actionsCost += cost
            j -= cost

    # creating list of actions for the report
    actionsVar = ", ".join(actionsToBuy)

    # converting values when using float numbers
    if actionsContainFloat:
        return actionsVar, table[n][maxInvest] / 100, actionsCost / 100, datetime.datetime.now() - start
    else:
        return actionsVar, table[n][maxInvest], actionsCost, datetime.datetime.now() - start

# retrieving all datas in dataset file
data_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
actionsValues = GetActionsValues(data_path)

# return True if action's cost in actionsValues contains at less one Float
actionsContainFloat = (isFloat(actionsValues))

if actionsContainFloat:
    maxInvest = MAX_INVEST * 100
else:
    maxInvest = MAX_INVEST

actionsObjList = []

for actionName, actionCost, actionProfit in zip(actionsValues[0], actionsValues[1], actionsValues[2]):
    # check if action contains mistakes (cost <= 0)
    if actionCost <= 0:
        continue
    if actionsContainFloat:
        action = porteFolio(actionName, actionCost * 100, actionProfit * 100, actionsContainFloat)
    else:
        action = porteFolio(actionName, actionCost, actionProfit, actionsContainFloat)
    actionsObjList.append(action)

if __name__ == '__main__':
    Clean()
    try:
        # executing script getMaxProfit + reporting
        optimizedReport(getMaxProfit(maxInvest, actionsObjList, actionsContainFloat))
    except KeyboardInterrupt:
        print("\n\nFin du script par l'utilisateur.\n")
