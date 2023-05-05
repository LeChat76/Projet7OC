import os

### GLOBALS CONSTANTES VALUES ###
DATA_PATH = os.path.join(os.path.dirname(__file__), "datas")
ACTIONS_COSTS_FILE = DATA_PATH + "\\actions_costs.txt"
ACTIONS_RETURNS_FILE = DATA_PATH + ("\\actions_returns.txt")
ACTIONS_NAMES_FILE = DATA_PATH + ("\\actions_names.txt")
NB_ACTIONS = 20
COMBINATIONS_ACTIONS_LIST = []
RETURNS_ACTIONS_LIST = []
MAX_INVEST = 500
NB_ONE_MAX = 16

### creation of list from ACTIONS_COSTS_FILE ###
ACTIONS_COSTS_LIST = []
actions_costs_file = open(ACTIONS_COSTS_FILE, "r")
actions_costs_temp = actions_costs_file.readlines()
actions_costs_file.close()
for line in actions_costs_temp:
  ACTIONS_COSTS_LIST.append(line.strip('\n'))

### creation of list from ACTIONS_RETURNS_FILE ##
ACTIONS_RETURNS_LIST = []
actions_returns_file = open(ACTIONS_RETURNS_FILE, "r")
actionsCostsTemp = actions_returns_file.readlines()
actions_returns_file.close()
for line in actionsCostsTemp:
  ACTIONS_RETURNS_LIST.append(line.strip('\n'))

### creation of list from ACTIONS_NAMES_FILE ###
ACTIONS_NAMES_LIST = []
actions_costs_file = open(ACTIONS_NAMES_FILE, "r")
actions_costs_temp = actions_costs_file.readlines()
actions_costs_file.close()
for line in actions_costs_temp:
  ACTIONS_NAMES_LIST.append(line.strip('\n'))