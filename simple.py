import sympy

class PrimeClock:
    def __init__(self, prime):
        self.prime = prime
        self.s = 0
        self.m = 0
        self.outputs = [0]  # positive_outputs

    def next(self, t):
        self.s += 1
        if self.s == self.prime:
            self.s = 0
            self.m += 1
        if self.s == 0:
                output = 1 + self.outputs[self.m]
        else:
                output = 0
        self.outputs.append(output)
        return output

class Clockwork:
    def __init__(self, max_iterations):
        self.t = 0
        self.clocks = []
        for prime in sympy.primerange(2, max_iterations):
            self.clocks.append(PrimeClock(prime))

    def next(self):
        digits = [clock.next(self.t) for clock in self.clocks]
        self.t += 1
        return digits, self.t

    def run(self, max_iterations):
        for _ in range(max_iterations):
            digits, t = self.next()
            print(f"{t}\t" + "\t".join(map(str, digits)))

if __name__ == "__main__":
    max_iterations = 30
    clockwork = Clockwork(max_iterations)
    clockwork.run(max_iterations)
