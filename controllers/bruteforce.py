import datetime, sys
sys.path.append("..")
from functions import DecToBin, GetActionsCost, ReturnCombination, GetActionsProfit, Clean, isFloat
from constantes import COMBINATIONS_ACTIONS_LIST, MAX_INVEST
from models.dataset import GetActionsValues, testArgv
from models.actions import porteFolio
from views.reports import bruteforceReport

# check if file argument exists and if can be accessed
testArgv(sys.argv, "bruteforce")

def getMaxProfit(actionsObjList):
  ''' return max profit from dataset '''

  Clean()

  start = datetime.datetime.now()
  bestGain = 0
  actions = ""

  for i in range(1, 2 ** len(actionsObjList)):
    
    # generate "binary selection"
    binary_index = DecToBin(i)
    
    # test if combination of actions's costs is less than MAX_INVEST
    if GetActionsCost(binary_index, actionsObjList) <= MAX_INVEST:
      gain = GetActionsProfit(binary_index, actionsObjList)
    
      # test if gain of this combination is better than old better combination's gain
      if gain > bestGain:
        bestGain = gain
        actionsCost = GetActionsCost(binary_index, actionsObjList)
        ReturnCombination(binary_index, actionsObjList)

  # generate actions to buy list
  for action in COMBINATIONS_ACTIONS_LIST:
    actions += action.name + ", "

  if actionsContainFloat:
     actionsCost = actionsCost / 100
     bestGain = bestGain /100

  return actions, actionsCost, bestGain, start

actionsValues = GetActionsValues(sys.argv[1])
actionsNamesList = actionsValues[0]
actionsCostsList = actionsValues[1]
actionsProfitsList = actionsValues[2]
actionsObjList = []

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
        maxProfit = getMaxProfit(actionsObjList)
        bruteforceReport(maxProfit[0], maxProfit[1], maxProfit[2], maxProfit[3])
    except KeyboardInterrupt:
        print("\n\nFin du script par l'utilisateur.\n")
