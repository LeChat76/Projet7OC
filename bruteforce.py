from functionsBruteforce import DecToBin, GetActionsCost, ReturnCombination, TestIfInfTo16
from functionsBruteforce import GetActionsProfit
from constantes import COMBINATIONS_ACTIONS_LIST, MAX_INVEST
import datetime

def Bruteforce():
    ''' main script to analyse all combinations '''
    bestGain = 0
    actions = ""
    start = datetime.datetime.now()
    for i in range(1, 2 ** 20):
      binary_index = DecToBin(i)
      if TestIfInfTo16(binary_index):
        if GetActionsCost(binary_index) <= MAX_INVEST:
          gain = GetActionsProfit(binary_index)
          if gain > bestGain:
            bestGain = gain
            actionsCost = GetActionsCost(binary_index)
            # create list with combination of actions to buy
            ReturnCombination(str(binary_index))
            binary_index_R = binary_index
        # if i == 10:
        #   break
    for action in COMBINATIONS_ACTIONS_LIST:
      actions += action + ", "
    print("Choix des actions à acheter pour un meilleur rendement : \n" +
          str(actions[:-2]) + ".")
    print("Cout des achats : " + str(actionsCost) + "€.")
    print("Gain avec cette combinaison : " + str(bestGain) +
         "€.")
    print("Duree de traitement : " + str(datetime.datetime.now() - start)[:10])
    print("(i = " + str(i) + " / binary_index = " + str(binary_index_R) + ")")
