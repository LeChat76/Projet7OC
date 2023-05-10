import datetime
import sys
sys.path.append("..")
from functions import DecToBin, GetActionsCost, ReturnCombination, TestIfInfToBinMax, GetActionsProfit, GetActionsValues
from constantes import COMBINATIONS_ACTIONS_LIST, MAX_INVEST

''' main script to analyse all combinations '''
if len(sys.argv) == 1 or len(sys.argv) >2 :
  print("Mauvaise syntaxe.\nExemple (depuis le dossier controllers) : python .\\bruteforce.py ..\datas\dataset.csv ")
  sys.exit()
else:
  try:
    with open(sys.argv[1]): pass
  except IOError:
    print("Le fichier semble ne pas exister, merci de vérifier.")
    sys.exit()
bestGain = 0
actions = ""
actionsValues = GetActionsValues(sys.argv[1])
actionsNamesList = actionsValues[0]
actionsCostsList = actionsValues[1]
actionsProfitsList = actionsValues[2]
start = datetime.datetime.now()
for i in range(1, 2 ** 20):
  binary_index = DecToBin(i)
  if TestIfInfToBinMax(binary_index):
    if GetActionsCost(binary_index, actionsCostsList) <= MAX_INVEST:
      gain = GetActionsProfit(binary_index, actionsProfitsList, actionsCostsList)
      if gain > bestGain:
        bestGain = gain
        actionsCost = GetActionsCost(binary_index, actionsCostsList)
        # create list with combination of actions to buy
        ReturnCombination(binary_index, actionsNamesList)
        binary_index_R = binary_index
for action in COMBINATIONS_ACTIONS_LIST:
  actions += action + ", "
print("Choix des actions à acheter pour un meilleur rendement : \n" +
      str(actions[:-2]) + ".")
print("Cout des achats : " + str(actionsCost) + "€.")
print("Gain avec cette combinaison : " + str(bestGain) +
      "€.")
print("Duree de traitement : " + str(datetime.datetime.now() - start)[:10])
print("(i = " + str(i) + " / binary_index = " + str(binary_index_R) + ")")
