from constantes import ACTIONS_COSTS_LIST, NB_ACTIONS

def GetActionsCost(bin_selection=""):
  ''' return actions cost from booleen list '''
  combination_costs = 0
  for i,bin in enumerate(bin_selection):
    if bin == "1":
        combination_costs = combination_costs + int(ACTIONS_COSTS_LIST[i])
        if combination_costs >= 500:
          return "combination > 500"
  return combination_costs

def GetActionsReturn(bin_selection=""):
  ''' return actions return from booleen list '''
  pass

def DecToBin(dec):
  binary = bin(dec)
  binary = binary[2:]
  binary = str((int(NB_ACTIONS) - len(binary)) * "0") + str(binary)
  return binary[::-1]
