import datetime, sys
from constantes import BRUTEFORCE_LOG_FILE
sys.path.append("..")

def optimizedReport(result):
    print("Choix des actions à acheter pour un meilleur rendement : \n" + str(result[0]) + ".")
    print("Cout des achats : " + str(format(result[2], '.2f') + "€.")  )
    print("Gain avec cette combinaison : " + str(format(result[1], '.2f') + "€."))
    print("Duree de traitement :" ,result[3])

def bruteforceReport(actions, actionsCost, bestGain, start):
    print("Choix des actions à acheter pour un meilleur rendement : \n" + str(actions[:-2]) + ".")
    print("Cout des achats : " + str(actionsCost) + "€.")
    print("Gain avec cette combinaison : " + str(bestGain) + "€.")
    print("Duree de traitement : " + str(datetime.datetime.now() - start)[:10])

def displayMsg(message):
    print(message)
