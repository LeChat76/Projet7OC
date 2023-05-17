import datetime, sys
sys.path.append("..")
from functions import DecToBin, GetActionsCost, ReturnCombination, GetActionsProfit, Clean
from constantes import COMBINATIONS_ACTIONS_LIST, MAX_INVEST
from models.dataset import GetActionsValues, testArgv
from views.reports import bruteforceReport

''' main script to analyse all combinations '''
testArgv(sys.argv, "bruteforce")

bestGain = 0
actions = ""
nbCombinaison = 0
actionsValues = GetActionsValues(sys.argv[1])
actionsNamesList = actionsValues[0]
actionsCostsList = actionsValues[1]
actionsProfitsList = actionsValues[2]
start = datetime.datetime.now()
for i in range(1, 2 ** len(actionsNamesList)):
  binary_index = DecToBin(i)
  if GetActionsCost(binary_index, actionsCostsList) <= MAX_INVEST:
    gain = GetActionsProfit(binary_index, actionsProfitsList, actionsCostsList)
    if gain > bestGain:
      bestGain = gain
      actionsCost = GetActionsCost(binary_index, actionsCostsList)
      # create list of combination of actions to buy
      ReturnCombination(binary_index, actionsNamesList)
for action in COMBINATIONS_ACTIONS_LIST:
  actions += action + ", "

Clean()
bruteforceReport(actions, actionsCost, bestGain, start)
