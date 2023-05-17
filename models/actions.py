class porteFolio:
    def __init__(self, name, cost, profit): 
        self.name = name
        self.cost = float(cost)
        self.profit = float(profit)
        self.gain = self.cost * (self.profit / 100 )
        self.ratio = (self.cost * (self.profit / 100)) + self.profit

    def __lt__(self, nextObj):
        return self.ratio < nextObj.ratio
    