class porteFolio:
    def __init__(self, name, cost, profit, actionsContainFloat): 
        self.name = name
        self.cost = float(cost)
        self.profit = float(profit)
        if actionsContainFloat:
            self.gain = self.cost * (self.profit / 10000)
        else:
            self.gain = self.cost * (self.profit / 100 )
        self.ratio = (self.cost * (self.profit / 100)) + self.profit
        # self.ratio = self.profit + (self.cost * self.profit)

    def __lt__(self, nextObj):
        return self.ratio < nextObj.ratio
    