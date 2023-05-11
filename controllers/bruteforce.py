import datetime
import sys
sys.path.append("..")
from functions import DecToBin, GetActionsCost, ReturnCombination, TestIfInfToBinMax, GetActionsProfit, Clean
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
for i in range(1, 2 ** 20):
  binary_index = DecToBin(i)
  if TestIfInfToBinMax(binary_index):
    if GetActionsCost(binary_index, actionsCostsList) <= MAX_INVEST:
      nbCombinaison += 1
      gain = GetActionsProfit(binary_index, actionsProfitsList, actionsCostsList)
      if gain > bestGain:
        bestGain = gain
        actionsCost = GetActionsCost(binary_index, actionsCostsList)
        # create list with combination of actions to buy
        ReturnCombination(binary_index, actionsNamesList)
        binary_index_R = binary_index
for action in COMBINATIONS_ACTIONS_LIST:
  actions += action + ", "

Clean()
bruteforceReport(actions, actionsCost, bestGain, start, i, binary_index_R, nbCombinaison)
