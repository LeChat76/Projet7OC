import datetime, sys
sys.path.append("..")
from functions import DecToBin, GetActionsCost, ReturnCombination, GetActionsProfit, Clean
from constantes import COMBINATIONS_ACTIONS_LIST, MAX_INVEST, BRUTEFORCE_LOG_FILE
from models.dataset import GetActionsValues, testArgv
from views.reports import bruteforceReport

testArgv(sys.argv, "bruteforce")

actionsValues = GetActionsValues(sys.argv[1])
actionsNamesList = actionsValues[0]
actionsCostsList = actionsValues[1]
actionsProfitsList = actionsValues[2]

def getMaxProfit():
  ''' return max profit from dataset '''

  start = datetime.datetime.now()
  bestGain = 0
  actions = ""

  for i in range(1, 2 ** len(actionsNamesList)):
    
    # generate "binary selection"
    binary_index = DecToBin(i)
    
    # test if combination of actions's costs is less than MAX_INVEST
    if GetActionsCost(binary_index, actionsCostsList) <= MAX_INVEST:
      gain = GetActionsProfit(binary_index, actionsProfitsList, actionsCostsList)
    
      # test if gain of this combination is better than old better combination's costs
      if gain > bestGain:
        bestGain = gain
        actionsCost = GetActionsCost(binary_index, actionsCostsList)
        ReturnCombination(binary_index, actionsNamesList)

  # generate actions to buy list
  for action in COMBINATIONS_ACTIONS_LIST:
    actions += action + ", "

  return actions, actionsCost, bestGain, start

Clean()

maxProfit = getMaxProfit()

# reporting
bruteforceReport(maxProfit[0], maxProfit[1], maxProfit[2], maxProfit[3])
