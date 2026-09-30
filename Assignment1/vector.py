import math

class vector:

    def __init__(self, src=None):
        if src is None:
            self.elements = ()
        else:
            elements = tuple(src)

            for x in elements:
                if not isinstance(x, (int, float)):
                    raise TypeError("THE INPUT MUST BE A SCALAR")

            self.elements = elements

    def __repr__(self):
        return repr(self.elements)

    def __len__(self):
        return len(self.elements)

    def mean(self):
        return sum(self.elements) / len(self.elements)

    def demean(self):
        m = self.mean()
        return vector(x - m for x in self.elements)

    def std(self):
        dm = self.demean()
        return math.sqrt(
            sum(x * x for x in dm.elements) / len(dm)
        )