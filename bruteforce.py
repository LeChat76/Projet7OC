from functions import DecToBin, GetActionsCost, ReturnCombination, TestIfInfTo16
from functions import GetActionsReturn
from constantes import COMBINATIONS_ACTIONS_LIST, MAX_INVEST

def Bruteforce():
    ''' main script to analyse all combinations '''
    bestGain = 0
    for i in range(1, 2 ** 20):
      binary_index = DecToBin(i)
      if TestIfInfTo16(binary_index):
        if GetActionsCost(binary_index) <= MAX_INVEST:
          gain = GetActionsReturn(binary_index)
          if gain > bestGain:
            bestGain = gain
            # create list with combination of actions to buy
            ReturnCombination(str(binary_index))
        # if i == 500000:
        #   break

    print("Choix des actions à acheter pour un meilleur rendement : \n" +
          str(COMBINATIONS_ACTIONS_LIST) + "\n" +
          "Gain total théorique avec cette combinaison : " + str(bestGain))