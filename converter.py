class Converter:
    def __int__(self):
        self.k = 0
        self.m = 0

    def miles_to_km(self, m=0):

        self.k = float(m) * 1.6
        return self.k

    def km_to_miles(self, k=0):

        self.m = float(k) * 0.62
        return self.m
