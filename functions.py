from constantes import COMBINATIONS_ACTIONS_LIST, NB_BIN1_MAX, NB_ACTIONS
import os, platform

def GetActionsCost(bin_selection, actionsCostsList):
  ''' return actions's costs from binary list '''
  ''' output : INTEGER '''
  cost = 0
  for i,bin in enumerate(bin_selection):
    if bin == "1":
      cost += float(actionsCostsList[i])
  return cost

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

def Clean():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")

def TestIfFloat(dataset):
  ''' check if dataset contains float '''
  ''' if yes, to use optimized2 and table, we can not have float so so we must multiply by nDec * 100 '''
  ''' output : BOOLEAN '''
  for cost, profit in zip(dataset[1], dataset[2]):
    cost = str(cost)
    profit = str(profit)
    if '.' in cost or '.' in profit:
      nbDecCost = len(cost) - cost.index('.') - 1
      if nbDecCost > 1:
        return True
      nbDecProfit = len(profit) - profit.index('.') - 1
      if nbDecProfit > 1:
        return True
  return False