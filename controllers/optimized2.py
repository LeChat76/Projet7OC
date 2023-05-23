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
def getMaxProfit(maxInvest, actionsObjList, actionsContainFloat):
    ''' extract best combination of actions to buy '''
    n = len(actionsObjList)
    table = [[0 for x in range(maxInvest + 1)] for x in range(n + 1)]

    prevPercent = 0

    for i in range(n + 1):
        cost = actionsObjList[i - 1].cost

        # if cost < 0 (so I guess a mistake), I modify cost by 0
        if cost < 0:
            cost = 0
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
    if actionsContainFloat:
        action = porteFolio(actionName, actionCost * 100, actionProfit * 100, actionsContainFloat)
    else:
        action = porteFolio(actionName, actionCost, actionProfit, actionsContainFloat)
    actionsObjList.append(action)

Clean()

optimizedReport(getMaxProfit(maxInvest, actionsObjList, actionsContainFloat))
