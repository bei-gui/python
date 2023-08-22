from Crypto.Util.number import*

class LCG:
    def __init__(self):
        self.a = 3939333498
        self.b = 3662432446
        self.m = 2271373817
        self.seed = 104984523

    def next(self):
        self.seed = (self.a*self.seed+self.b) % self.m
        return self.seed >> 16

    def output(self):
        print("a = {}nb = {}nm = {}".format(self.a, self.b, self.m))
        print("state1 = {}".format(self.next()))
        print("state2 = {}".format(self.next()))
lcg = LCG()
lcg.output()
cipher = 600017039001091357643174067454938198067935635401496485588306838343558125283178792619821966678282131419050878
cipher2 = long_to_bytes(cipher)
print(cipher2)
c = b''.join([long_to_bytes(cipher2[i] ^ (lcg.next() % 10))
            for i in range(len(cipher2))])
print(long_to_bytes(c))
