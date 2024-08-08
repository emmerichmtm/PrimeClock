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
        for prime in [2, 3]:
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

    def add_clocks(self, clock1, clock2):
        new_clock = PrimeClock(clock1.prime)
        new_clock.s = (clock1.s + clock2.s) % clock1.prime
        new_clock.m = clock1.m + clock2.m + (1 if new_clock.s == 0 else 0)
        new_clock.outputs = [0] * len(clock1.outputs)
        for i in range(len(clock1.outputs)):
            if i < len(clock2.outputs):
                new_clock.outputs[i] = clock1.outputs[i] + clock2.outputs[i]
            else:
                new_clock.outputs[i] = clock1.outputs[i]
        return new_clock

    def multiply_clocks(self, clock1, clock2):
        new_clock = PrimeClock(clock1.prime)
        new_clock.s = (clock1.s * clock2.s) % clock1.prime
        new_clock.m = clock1.m * clock2.m
        new_clock.outputs = [clock1.outputs[i] + clock2.outputs[i] for i in range(len(clock1.outputs))]
        return new_clock

    def add_states(self, state1, state2):
        result = []
        for clock1, clock2 in zip(state1, state2):
            result.append(self.add_clocks(clock1, clock2))
        return result

    def multiply_states(self, state1, state2):
        result = []
        for clock1, clock2 in zip(state1, state2):
            result.append(self.multiply_clocks(clock1, clock2))
        return result

    def get_current_state(self):
        return [clock for clock in self.clocks]

if __name__ == "__main__":
    max_iterations = 30
    clockwork = Clockwork()
    clockwork.run(max_iterations)
    
    # Example of addition and multiplication
    print("\nAdding states:")
    state1 = clockwork.get_current_state()
    state2 = clockwork.get_current_state()
    addition_result = clockwork.add_states(state1, state2)
    addition_outputs = [clock.outputs[-1] for clock in addition_result]
    print(addition_outputs)

    print("\nMultiplying states:")
    multiplication_result = clockwork.multiply_states(state1, state2)
    multiplication_outputs = [clock.outputs[-1] for clock in multiplication_result]
    print(multiplication_outputs)
