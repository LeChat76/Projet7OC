import sys, os, datetime, psutil, platform
start = datetime.datetime.now()

class porteFolio:
    ''' create action object '''
    def __init__(self, name, cost, profit, actionsContainFloat): 
        self.name = name
        self.cost = float(cost)
        # if cost <= 0 (so I guess it's a mistake), I modify cost by 0 to bypass this action in the script
        if self.cost <= 0:
            self.cost = 0
        self.profit = float(profit)
        if actionsContainFloat:
            self.gain = self.cost * (self.profit / 10000)
        else:
            self.gain = self.cost * (self.profit / 100 )
        self.ratio = (self.cost * self.profit / 100) + self.profit

    def __lt__(self, nextObj):
        return self.ratio < nextObj.ratio

def Clean():
    '''
    clear screen, check OS to launch good command
    '''
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")

def getMemoryUsage():
    '''
    extract memory usage
    '''
    process = psutil.Process()
    memoryInfo = process.memory_info()
    memoryUsageMb = memoryInfo.rss / (1024 * 1024)
    return memoryUsageMb

def optimizedReport(result):
    memoryUsed = getMemoryUsage()
    print("Choix des actions à acheter pour un meilleur rendement : \n", str(result[0]) + ".")
    print("Cout des achats :", str(format(result[2], '.2f') + "€."))
    print("Gain avec cette combinaison :", str(format(result[1], '.2f') + "€."))
    print("Duree de traitement :" ,result[3])
    print("Utilisation de la mémoire :", str(format(memoryUsed, '.2f') + "Mo"))

def testArgv(argv, scriptName):
  ''' test if arguments are correct '''  
  if len(argv) == 1 or len(argv) >2 :
    print("Mauvaise syntaxe.\nExemple python : " + scriptName + ".py datas\dataset.csv ")
    sys.exit()
  else:
    try:
      with open(sys.argv[1]): pass
    except IOError:
      print(f"Le fichier '{sys.argv[1]}' semble ne pas exister, merci de vérifier.")
      sys.exit()

def GetActionsValues(datasetFile):
  ''' return all informations about actions '''
  ''' output : 3 lists '''
  actionsNamesList = []
  actionsCostsList = []
  actionsProfitsList = []
  dataset = open(datasetFile, "r")
  lines = dataset.readlines()
  dataset.close()
  for line in lines[1:]:
    line_list = line.split(",")
    actionName = line_list[0]
    actionCost = float(line_list[1])
    actionProfit = float(line_list[2])
    actionsNamesList.append(actionName)
    actionsCostsList.append(actionCost)
    actionsProfitsList.append(actionProfit)
  return(actionsNamesList, actionsCostsList, actionsProfitsList)

def isFloat(actionsList):
  '''
  test if some cost or profit are in float type because unable to manage table in that case
  input : LIST
  output : BOOLEAN
  '''
  for actionCost in actionsList[1]:
    actionCost = str(actionCost)
    if "." in actionCost:
      decAfterPoint = actionCost.split('.')[1]
      if any(chiffre != '0' for chiffre in decAfterPoint):
        return True
  for actionProfit in actionsList[2]:
    actionProfit = str(actionProfit)
    if "." in actionProfit:
      decAfterPoint = actionProfit.split('.')[1]
      if any(chiffre != '0' for chiffre in decAfterPoint):
        return True
  return False

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

    # seek all values (gains) changed. "Changed" meaning action bought so : added to actionsVar
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

# check if file argument exists and if can be accessed
testArgv(sys.argv, "optimized")

# retrieving all datas in dataset file
data_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
actionsValues = GetActionsValues(data_path)

# return True if action's cost in actionsValues contains at less one Float
actionsContainFloat = (isFloat(actionsValues))

maxInvest = 500

if actionsContainFloat:
    maxInvest = maxInvest * 100

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
    try:
        Clean()
        # executing script getMaxProfit + reporting
        optimizedReport(getMaxProfit(maxInvest, actionsObjList, actionsContainFloat))
    except KeyboardInterrupt:
        print("\n\nFin du script par l'utilisateur.\n")
