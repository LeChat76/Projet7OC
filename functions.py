from constantes import COMBINATIONS_ACTIONS_LIST, NB_BIN1_MAX, NB_ACTIONS
# from controllers.optimized import porteFolio
import os, platform

def GetActionsCost(bin_selection, actionsCostsList):
  ''' return actions's costs from binary list '''
  ''' output : INTEGER '''
  combination_cost = 0
  for i,bin in enumerate(bin_selection):
    if bin == "1":
      combination_cost = combination_cost + int(actionsCostsList[i])
  return combination_cost

def GetActionsProfit(bin_selection, actionsProfitsList, actionsCostsList):
  ''' return actions's gain from binary list '''
  ''' output : INTEGER limited TO 2 decimals '''
  combination_profit = 0
  for i,bin in enumerate(bin_selection):
    if bin == "1":
      gain = ((int(actionsCostsList[i]) * int(actionsProfitsList[i])) / 100)
      combination_profit = combination_profit + gain
  return round(combination_profit, 2)

def ReturnCombination(bin_selection, actionsNamesList):
  ''' create list of combination from binary list '''
  ''' output : LIST of actions names '''
  COMBINATIONS_ACTIONS_LIST.clear()
  for i,bin in enumerate(bin_selection):
    if bin == "1":
      COMBINATIONS_ACTIONS_LIST.append(actionsNamesList[i])

def DecToBin(dec):
  ''' convert decimal in binary with 20 digits '''
  ''' output : BINARY '''
  binary = bin(dec)
  binary = binary[2:]
  binary = str((int(NB_ACTIONS) - len(binary)) * "0") + str(binary)
  return binary[::-1]

def TestIfInfToBinMax(bin_selection):
  ''' return True if bin_selection contains less than 16 x "1"
  and False if more than 16 x "1" '''
  nbOne = 0
  for digit in bin_selection:
    if digit == "1":
      nbOne += 1
  if nbOne > NB_BIN1_MAX:
    return False
  else:
    return True

def Clean():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")

def GetActionsValues(datasetFile):
  ''' return all informations about actions '''
  ''' output : 3 lists '''
  data_path = os.path.join(os.path.abspath(__file__), datasetFile)
  actionsNamesList = []
  actionsCostsList = []
  actionsProfitsList = []
  dataset = open(data_path, "r")
  lines = dataset.readlines()
  dataset.close()
  for line in lines:
    line_list = line.split(",")
    actionsNamesList.append(line_list[0])
    actionsCostsList.append(line_list[1])
    actionsProfitsList.append(line_list[2].rstrip('\n'))
  # delete titles
  actionsNamesList.pop(0)
  actionsCostsList.pop(0)
  actionsProfitsList.pop(0)
  return(actionsNamesList, actionsCostsList, actionsProfitsList)
