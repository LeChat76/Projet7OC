from functions import DecToBin, GetActionsCost

def Bruteforce():
    for i in range(2 ** 20):
      print (GetActionsCost(DecToBin(i)))
      if i == 5000:
        break