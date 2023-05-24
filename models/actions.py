class porteFolio:
    def __init__(self, name, cost, profit, actionsContainFloat): 
        self.name = name
        self.cost = float(cost)
        # if cost <= 0 (so I guess it's a mistake), I modify cost by 0 to bypass this action in the script
        if self.cost <= 0:
            self.cost = 0
        self.profit = float(profit)
        if actionsContainFloat:
            self.gain = self.cost * (self.profit / 10000)
        else:
            self.gain = self.cost * (self.profit / 100 )
        self.ratio = (self.cost * self.profit / 100) + self.profit

    def __lt__(self, nextObj):
        return self.ratio < nextObj.ratio
    