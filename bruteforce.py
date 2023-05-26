import datetime, sys, psutil, platform, os

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

def testArgv(argv, scriptName):
  ''' test if arguments are correct '''  
  if len(argv) == 1 or len(argv) >2 :
    print("Mauvaise syntaxe.\nExemple python " + scriptName + ".py datas\dataset.csv ")
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

def ReturnCombination(bin_selection, actionsObjList):
  '''
  create list of combination from binary list
  input : BINARY number, LIST of all actions's objects
  output : LIST of actions's objects
  '''
  combinationActionsList = []
  # COMBINATIONS_ACTIONS_LIST.clear()
  for i,bin in enumerate(bin_selection):
    if bin == "1":
      combinationActionsList.append(actionsObjList[i])
  return combinationActionsList

def GetActionsCost(bin_selection, actionsObjList):
  '''
  return actions's costs from binary list
  input : BINARY number, LIST of all actions's objects
  output : INTEGER
  '''
  cost = 0
  for i,bin in enumerate(bin_selection):
    if bin == "1":
      cost += float(actionsObjList[i].cost)
  return cost

def GetActionsProfit(bin_selection, actionsObjList):
  '''
  return actions's gain from binary list
  input : BINARY number, LIST of all actions's objects
  output : FLOAT limited TO 2 decimals
  '''
  combination_profit = 0
  for i,bin in enumerate(bin_selection):
    if bin == "1":
      gain = ((int(actionsObjList[i].cost) * int(actionsObjList[i].profit)) / 100)
      combination_profit = combination_profit + gain
  return round(combination_profit, 2)

def isFloat(actionsList):
  '''
  test if some cost or profit are in float type
  because unable to manage table in that case
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

def DecToBin(dec, nbActions):
  '''
  convert decimal in binary
  input : INTEGER
  output : BINARY
  '''
  binary = bin(dec)
  binary = binary[2:]
  binary = str((int(nbActions) - len(binary)) * "0") + str(binary)
  return binary[::-1]

def bruteforceReport(actions, actionsCost, bestGain, start):
    memoryUsed = getMemoryUsage()
    print("Choix des actions à acheter pour un meilleur rendement : \n" + str(actions[:-2]) + ".")
    print("Cout des achats :", str(format((actionsCost), '.2f') + "€."))
    print("Gain avec cette combinaison :", str(bestGain) + "€.")
    print("Duree de traitement :", (str(datetime.datetime.now() - start)[:10]))
    print("Utilisation de la mémoire :", str(format(memoryUsed, '.2f')) + "Mo.")

def getMaxProfit(actionsObjList):
  ''' return max profit from dataset '''

  start = datetime.datetime.now()
  bestGain = 0
  actions = ""
  nbActions = len(actionsObjList)
  
  for i in range(1, 2 ** nbActions):
    
    # generate "binary selection"
    binary_index = DecToBin(i, nbActions)
    
    # test if combination of actions's costs is less than maxInvest
    if GetActionsCost(binary_index, actionsObjList) <= maxInvest:
      gain = GetActionsProfit(binary_index, actionsObjList)
    
      # test if gain of this combination is better than old better combination's gain
      if gain > bestGain:
        bestGain = gain
        actionsCost = GetActionsCost(binary_index, actionsObjList)
        combinationActionsList = ReturnCombination(binary_index, actionsObjList)

  # generate actions list to buy
  for action in combinationActionsList:
    actions += action.name + ", "

  if actionsContainFloat:
     actionsCost = actionsCost / 100
     bestGain = bestGain /100

  return actions, actionsCost, bestGain, start

testArgv(sys.argv, "bruteforce") # check if file argument exists and if can be accessed

actionsValues = GetActionsValues(sys.argv[1])
actionsNamesList = actionsValues[0]
actionsCostsList = actionsValues[1]
actionsProfitsList = actionsValues[2]
actionsObjList = []
maxInvest = 500

actionsContainFloat = (isFloat(actionsValues))

for name, cost, profit in zip(actionsValues[0], actionsValues[1], actionsValues[2]):
    action = porteFolio(name, cost, profit, actionsContainFloat)
    # check if action contains mistakes (cost <= 0)
    if action.cost <= 0:
        continue
    actionsObjList.append(action)

# reporting
if __name__ == '__main__':
    try:
        Clean()
        ''' execute main def '''
        maxProfit = getMaxProfit(actionsObjList)
        bruteforceReport(maxProfit[0], maxProfit[1], maxProfit[2], maxProfit[3])
    except KeyboardInterrupt:
        print("\n\nFin du script par l'utilisateur.\n")
