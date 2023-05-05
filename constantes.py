import os

### GLOBALS CONSTANTES VALUES ###
DATA_PATH = os.path.join(os.path.dirname(__file__), "datas")
DATASET_FILE = DATA_PATH + "\\dataset_bruteforce.csv"
NB_ACTIONS = 20
COMBINATIONS_ACTIONS_LIST = []
PROFITS_ACTIONS_LIST = []
MAX_INVEST = 500
NB_ONE_MAX = 16

### get value of the dataset file
ACTIONS_NAMES_LIST = []
ACTIONS_COSTS_LIST = []
ACTIONS_PROFITS_LIST = []
dataset = open(DATASET_FILE, "r")
lines = dataset.readlines()
dataset.close()
for line in lines:
  line_list = line.split(",")
  ACTIONS_NAMES_LIST.append(line_list[0])
  ACTIONS_COSTS_LIST.append(line_list[1])
  ACTIONS_PROFITS_LIST.append(line_list[2])
# delete titles
ACTIONS_NAMES_LIST.pop(0)
ACTIONS_COSTS_LIST.pop(0)
ACTIONS_PROFITS_LIST.pop(0)
