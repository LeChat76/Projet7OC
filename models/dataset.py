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
  for line in lines:
    line_list = line.split(",")
    actionsNamesList.append(line_list[0])
    actionsCostsList.append(line_list[1])
    actionsProfitsList.append(line_list[2].rstrip('\n'))
  # delete titles
  actionsNamesList.pop(0)
  actionsCostsList.pop(0)
  actionsProfitsList.pop(0)
  return(actionsNamesList, actionsCostsList, actionsProfitsList)

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