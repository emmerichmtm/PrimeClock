class PrimeClock:
    def __init__(self, prime):
        self.prime = prime
        self.s = 0
        self.m = 0
        self.outputs = [0]  # positive_outputs

    def next(self):
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
    def __init__(self):
        self.t = 0
        self.clocks = []
        for prime in [2,3]:
            self.clocks.append(PrimeClock(prime))

    def next(self):
        digits = [clock.next() for clock in self.clocks]
        self.t += 1
        return digits, self.t

    def add_new_clock(self):
        new_prime = self.t
        new_clock = PrimeClock(new_prime)
        for _ in range(self.t):
            new_clock.next()
        self.clocks.append(new_clock)
        return new_clock.outputs[-1]

    def run(self, max_iterations):
        for _ in range(max_iterations):
            digits, t = self.next()
            if all(d == 0 for d in digits) and t > 2:
                new_output = self.add_new_clock()
                digits.append(new_output)
            print(f"{t}\t" + "\t".join(map(str, digits)))

if __name__ == "__main__":
    max_iterations = 30
    clockwork = Clockwork()
    clockwork.run(max_iterations)
