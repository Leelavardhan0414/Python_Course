class computer:
    def __init__(self, ram, ssd, cpu):
        self.ram = ram
        self.cpu = cpu
        self.ssd = ssd

    def configu(self):
        # return (f"cpu:{self.cpu},ram: {self.ram}, ssd: {self.ssd}")
        print("configu", self.cpu, self.ram, self.ssd)


com1 = computer("16GB", "1TB", "i7")
com2 = computer("64GB", "2TB", "i9")
# print(com1.configu())
# print(com2.configu())
com1.configu()
com2.configu()
