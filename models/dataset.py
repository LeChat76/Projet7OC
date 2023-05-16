import sys


def GetActionsValues(datasetFile):
  ''' return all informations about actions '''
  ''' output : 3 lists '''
  actionsNamesList = []
  actionsCostsList = []
  actionsProfitsList = []
  actionsGainsList = []
  dataset = open(datasetFile, "r")
  lines = dataset.readlines()
  dataset.close()
  for line in lines[1:]:
    line_list = line.split(",")
    actionName = line_list[0]
    actionCost = int(line_list[1])
    actionProfit = int(line_list[2])
    actionsNamesList.append(actionName)
    actionsCostsList.append(actionCost)
    actionsProfitsList.append(actionProfit)
    actionsGainsList.append(actionCost * actionProfit / 100)
  return(actionsNamesList, actionsCostsList, actionsProfitsList, actionsGainsList)

def testArgv(argv, scriptName):
  if len(sys.argv) == 1 or len(sys.argv) >2 :
    print("Mauvaise syntaxe.\nExemple (depuis le dossier controllers) : python .\\" + scriptName + ".py ..\datas\dataset.csv ")
    sys.exit()
  else:
    try:
      with open(sys.argv[1]): pass
    except IOError:
      print("Le fichier semble ne pas exister, merci de vérifier.")
      sys.exit()