<p align="center">
 <img alt="logo" src="https://user-images.githubusercontent.com/119883313/236204342-478f1a02-6a75-48de-a54a-038db856562e.png">
</p>

# Projet7OC
Algorithms for calculating best bank returns.
This project is detailed in the file 'AlgoInvest&Trade.pdf'.

## Installation
```sh
"git clone https://github.com/LeChat76/Projet7OC.git"
"cd Projet7OC"
Create virtual environment :
* "python -m venv .venv"
* activate environment :
    * for Linux "source .venv/bin/activate"
    * for Windows ".\.venv\Scripts\activate"
Install needed library by typing : "pip install -r requirements.txt"
```

## Step 1 : bruteforce algorithm
### Knapsack01 with bruteforce algorithm :
 * python bruteforce.py datas\dataset.csv

## Step 2 : optimization
### Knapsack01 with gluttonous algorithm : 
 * python optimized.py datas\dataset.csv
### Knapsack01 with dynamic algorithm : 
 * python optimized2.py datas\dataset.csv

## Step 3 : backtesting
### Bruteforce is not used because computing time is too long
### Knapsack01 with gluttonous algorithm : 
    * python optimized.py datas\dataset1_Python+P7.csv
    * python optimized.py datas\dataset2_Python+P7.csv
### Knapsack01 with dynamic algorithm : 
    * python optimized2.py datas\dataset1_Python+P7.csv
    * python optimized2.py datas\dataset2_Python+P7.csv

