import datetime, sys
sys.path.append("..")
from functions import getMemoryUsage

def optimizedReport(result):
    memoryUsed = getMemoryUsage()
    print("Choix des actions à acheter pour un meilleur rendement : \n", str(result[0]) + ".")
    print("Cout des achats :", str(format(result[2], '.2f') + "€."))
    print("Gain avec cette combinaison :", str(format(result[1], '.2f') + "€."))
    print("Duree de traitement :" ,result[3])
    print("Utilisation de la mémoire :", str(format(memoryUsed, '.2f') + "Mo"))



def bruteforceReport(actions, actionsCost, bestGain, start):
    memoryUsed = getMemoryUsage()
    print("Choix des actions à acheter pour un meilleur rendement : \n" + str(actions[:-2]) + ".")
    print("Cout des achats :", str(format((actionsCost), '.2f') + "€."))
    print("Gain avec cette combinaison :", str(bestGain) + "€.")
    print("Duree de traitement :", (str(datetime.datetime.now() - start)[:10]))
    print("Utilisation de la mémoire :", str(format(memoryUsed, '.2f')) + "Mo.")

def displayMsg(message):
    print(message)
