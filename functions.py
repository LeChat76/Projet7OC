from constantes import ACTIONS_PROFITS_LIST, ACTIONS_COSTS_LIST, NB_ACTIONS
from constantes import COMBINATIONS_ACTIONS_LIST, ACTIONS_NAMES_LIST, NB_BIN1_MAX
import os, platform

def GetActionsCost(bin_selection):
  ''' return actions's costs from binary list '''
  ''' return INTEGER '''
  combination_cost = 0
  for i,bin in enumerate(bin_selection):
    if bin == "1":
      combination_cost = combination_cost + int(ACTIONS_COSTS_LIST[i])
  return combination_cost

def GetActionsProfit(bin_selection):
  ''' return actions's gain from binary list '''
  ''' return INTEGER limited TO 2 decimals '''
  combination_profit = 0
  for i,bin in enumerate(bin_selection):
    if bin == "1":
      gain = ((int(ACTIONS_COSTS_LIST[i]) * int(ACTIONS_PROFITS_LIST[i])) / 100)
      combination_profit = combination_profit + gain
  return round(combination_profit, 2)

def ReturnCombination(bin_selection):
  ''' create list of combination from binary list '''
  ''' return LIST of actions names '''
  COMBINATIONS_ACTIONS_LIST.clear()
  for i,bin in enumerate(bin_selection):
    if bin == "1":
      COMBINATIONS_ACTIONS_LIST.append(ACTIONS_NAMES_LIST[i])

def DecToBin(dec):
  ''' convert decimal in binary with 20 digits '''
  ''' return BINARY '''
  binary = bin(dec)
  binary = binary[2:]
  binary = str((int(NB_ACTIONS) - len(binary)) * "0") + str(binary)
  return binary[::-1]

def TestIfInfTo16(bin_selection):
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