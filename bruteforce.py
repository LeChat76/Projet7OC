from functions import DecToBin, GetActionsCost, ReturnCombination
from constantes import COMBINATIONS_ACTIONS_LIST

def Bruteforce():
    ''' main script to analyse all combinations '''
    combinations_list = []
    for i in range(400000, 2 ** 20):
      result = GetActionsCost(DecToBin(i))
      if GetActionsCost(str(result)) < 500:
         print(result)
         ReturnCombination(str(DecToBin(i)))
      if i == 400500:
        break
    print(COMBINATIONS_ACTIONS_LIST)