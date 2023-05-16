from constantes import COMBINATIONS_ACTIONS_LIST, NB_BIN1_MAX, NB_ACTIONS
import os, platform, sys

def GetActionsCost(bin_selection, actionsCostsList):
  ''' return actions's costs from binary list '''
  ''' output : INTEGER '''
  combination_cost = 0
  for i,bin in enumerate(bin_selection):
    if bin == "1":
      combination_cost += int(actionsCostsList[i])
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

def Clean():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
