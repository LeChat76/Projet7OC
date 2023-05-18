class porteFolio:
    def __init__(self, name, cost, profit, actionsContainFloat): 
        self.name = name
        self.cost = int(cost)
        self.profit = int(profit)
        if actionsContainFloat:
            self.gain = self.cost * (self.profit / 10000)
        else:
            self.gain = self.cost * (self.profit / 100 )
        self.ratio = (self.cost * (self.profit / 100)) + self.profit

    def __lt__(self, nextObj):
        return self.ratio < nextObj.ratio
    