import datetime

def optimizedReport(result):
    print("Actions :", result[0])
    print("Rendement max : " + str(format(result[1], '.2f') + "€."))
    print("Cout total : " + str(result[2]) + "€.")  

def bruteforceReport(actions, actionsCost, bestGain, start, i, binary_index_R, nbCombinaison):
    print("Choix des actions à acheter pour un meilleur rendement : \n" + str(actions[:-2]) + ".")
    print("Cout des achats : " + str(actionsCost) + "€.")
    print("Gain avec cette combinaison : " + str(bestGain) + "€.")
    print("Duree de traitement : " + str(datetime.datetime.now() - start)[:10])
    print("Nombre de combinaisons testées :", nbCombinaison)
    print("(i = " + str(i) + " / binary_index = " + str(binary_index_R) + ")")
