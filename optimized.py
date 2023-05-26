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
    ''' display report fort optimized algorithm '''
    memoryUsed = getMemoryUsage()
    print("Choix des actions à acheter pour un meilleur rendement : \n", str(result[0]) + ".")
    print("Cout des achats :", str(format(result[2], '.2f') + "€."))
    print("Gain avec cette combinaison :", str(format(result[1], '.2f') + "€."))
    print("Duree de traitement :" ,result[3])
    print("Utilisation de la mémoire :", str(format(memoryUsed, '.2f') + "Mo"))

def testArgv(argv, scriptName):
  ''' test if arguments are correct '''
  if len(argv) == 1 or len(argv) >2 :
    print("Mauvaise syntaxe.\nExemple python .\\" + scriptName + ".py datas\dataset.csv ")
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

def getMaxProfit(maxInvestInit, actionsObjList):
    ''' return max profit from actions's costs and profits '''
    actionsSorted = []
    finalProfit = 0
    maxInvest = maxInvestInit
    actionsNames = ""

    # create list of actions ordered by ratio profit + gain
    for action in actionsObjList:
        action = porteFolio(action.name, float(action.cost), action.profit, actionsContainFloat)
        actionsSorted.append(action)
    actionsSorted.sort(reverse=True)

    # gloutonous algorithm to add actions's cost one by one to reach maxInvestInit
    for action in actionsSorted:
        cost = float(action.cost)
        profit = float(action.profit)
        if maxInvest - cost >= 0:
            maxInvest -= cost
            finalProfit += cost * profit / 100
            actionsNames += action.name + ", "

    actionsNames = actionsNames[:-2] # ([:-2] to remove ", " at the end of the last actions's list)

    return actionsNames, finalProfit, maxInvestInit - maxInvest, datetime.datetime.now() - start

# creation of actions's object list from dataset
data_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
actionsValues = GetActionsValues(data_path)

# check if file argument exists and if can be accessed
testArgv(sys.argv, "optimized")

actionsObjList = []
maxInvestInit = 500
actionsContainFloat = False

for name, cost, profit in zip(actionsValues[0], actionsValues[1], actionsValues[2]):
    action = porteFolio(name, cost, profit, actionsContainFloat)
    # check if action contains mistakes (cost <= 0)
    if action.cost <= 0:
        continue
    actionsObjList.append(action)

if __name__ == '__main__':
    try:
        Clean()
        # executing script getMaxProfit + reporting
        optimizedReport(getMaxProfit(maxInvestInit, actionsObjList ))
    except KeyboardInterrupt:
        print("\n\nFin du script par l'utilisateur.\n")
