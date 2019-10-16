nclass computer():
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print('the config is ',self.cpu ,self.ram)
comp1=computer('i5',16)
comp2=computer('i7',32)
