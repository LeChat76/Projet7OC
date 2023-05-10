import datetime

def optimizedReport(result):
    print("Actions :", result[0])
    print("Rendement max : " + str(round(result[1], 2)) + "€.")
    print("Cout total : " + str(result[2]) + "€.")  

def bruteforceReport(actions, actionsCost, bestGain, start, i, binary_index_R):
    print("Choix des actions à acheter pour un meilleur rendement : \n" + str(actions[:-2]) + ".")
    print("Cout des achats : " + str(actionsCost) + "€.")
    print("Gain avec cette combinaison : " + str(bestGain) + "€.")
    print("Duree de traitement : " + str(datetime.datetime.now() - start)[:10])
    print("(i = " + str(i) + " / binary_index = " + str(binary_index_R) + ")")