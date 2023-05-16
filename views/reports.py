import datetime, sys
from memory_profiler import profile
sys.path.append("..")
bf=open('..\datas\memory_profiler_bruteforce.log','w+')

def optimizedReport(result):
    print("Choix des actions à acheter pour un meilleur rendement : \n" + str(result[0]) + ".")
    print("Cout des achats : " + str(result[2]) + "€.")  
    print("Gain avec cette combinaison : " + str(format(result[1], '.2f') + "€."))
    print("Duree de traitement :" ,result[3])

@profile(stream=bf)
def bruteforceReport(actions, actionsCost, bestGain, start):
    print("Choix des actions à acheter pour un meilleur rendement : \n" + str(actions[:-2]) + ".")
    print("Cout des achats : " + str(actionsCost) + "€.")
    print("Gain avec cette combinaison : " + str(bestGain) + "€.")
    print("Duree de traitement : " + str(datetime.datetime.now() - start)[:10])
