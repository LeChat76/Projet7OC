import sys


def GetActionsValues(datasetFile):
  ''' return all informations about actions '''
  ''' output : 3 lists '''
  actionsNamesList = []
  actionsCostsList = []
  actionsProfitsList = []
  dataset = open(datasetFile, "r")
  lines = dataset.readlines()
  dataset.close()
  for line in lines[1:]:
    line_list = line.split(",")
    actionName = line_list[0]
    actionCost = float(line_list[1])
    actionProfit = float(line_list[2])
    actionsNamesList.append(actionName)
    actionsCostsList.append(actionCost)
    actionsProfitsList.append(actionProfit)
  return(actionsNamesList, actionsCostsList, actionsProfitsList)

def testArgv(argv, scriptName):
  if len(argv) == 1 or len(argv) >2 :
    print("Mauvaise syntaxe.\nExemple (depuis le dossier controllers) : python .\\" + scriptName + ".py ..\datas\dataset.csv ")
    sys.exit()
  else:
    try:
      with open(sys.argv[1]): pass
    except IOError:
      print("Le fichier semble ne pas exister, merci de vérifier.")
      sys.exit()
