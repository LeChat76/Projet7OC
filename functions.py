from constantes import COMBINATIONS_ACTIONS_LIST, NB_ACTIONS
import os, platform, psutil

def GetActionsCost(bin_selection, actionsObjList):
  ''' return actions's costs from binary list '''
  ''' output : INTEGER '''
  cost = 0
  for i,bin in enumerate(bin_selection):
    if bin == "1":
      cost += float(actionsObjList[i].cost)
  return cost

def GetActionsProfit(bin_selection, actionsObjList):
  ''' return actions's gain from binary list '''
  ''' output : INTEGER limited TO 2 decimals '''
  combination_profit = 0
  for i,bin in enumerate(bin_selection):
    if bin == "1":
      gain = ((int(actionsObjList[i].cost) * int(actionsObjList[i].profit)) / 100)
      combination_profit = combination_profit + gain
  return round(combination_profit, 2)

def ReturnCombination(bin_selection, actionsObjList):
  ''' create list of combination from binary list '''
  ''' output : LIST of actions names '''
  COMBINATIONS_ACTIONS_LIST.clear()
  for i,bin in enumerate(bin_selection):
    if bin == "1":
      COMBINATIONS_ACTIONS_LIST.append(actionsObjList[i])

def DecToBin(dec):
  ''' convert decimal in binary with 20 digits '''
  ''' output : BINARY '''
  binary = bin(dec)
  binary = binary[2:]
  binary = str((int(NB_ACTIONS) - len(binary)) * "0") + str(binary)
  return binary[::-1]

def Clean():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")

def isFloat(actionsList):
  ''' test if some cost or profit are in float type '''
  ''' because unable to manage table in that case '''
  ''' output : BOOLEAN '''
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

def getMemoryUsage():
    process = psutil.Process()
    memoryInfo = process.memory_info()
    memoryUsageMb = memoryInfo.rss / (1024 * 1024)
    return memoryUsageMb