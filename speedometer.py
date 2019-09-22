
class SpeedometerSolver:

    def __init__(self, filename):
        file = open(filename, "r")
        self.n = int(file.readline())
        self.T = int(file.readline())
        self.distances = list(map(int, file.readline().rstrip('\n').split()))
        self.speeds = list(map(int, file.readline().strip('\n').split()))
        file.close()

        self.c = []
        self.threshold = 1e-7

    def solve_equation(self, c):
        s = 0
        for di, si in zip(self.distances, self.speeds):
            s += di / (c + si)
        return s - self.T

    def solve_derivative(self, c):
        s = 0
        for di, si in zip(self.distances, self.speeds):
            s -= di / ((c + si)*(c + si))
        return s

    def test_solution(self, c):
        time = 0
        for di, si in zip(self.distances, self.speeds):
            time += di / (si + c)
        return self.T - time

    def delta(self, iteration):
        return abs(self.c[iteration]-self.c[iteration-1])

    def newtons_method(self, c0):
        self.c = []
        self.c.insert(0, c0)
        i = 0;

        while True:
            i += 1;
            self.c.insert(i, self.c[i-1] - (self.solve_equation(self.c[i-1]) / self.solve_derivative(self.c[i-1])))
            print("Iteration {0} -> {1}".format(i, self.c[i]))
            if self.delta(i) < self.threshold:
                print("Solution found: {}".format(self.c[i]))
                if self.c[i] >= -min(self.speeds):
                    print(" satisfies positive speed constraint!")
                else:
                    print(" does NOT satisfies positive speed constraint!")
                break
            elif (i > 1) and (self.delta(i) >= self.delta(i-1)):
                print("The solution does not converge: try with a different initial value")
                break

    def run(self, initial_guess, threshold=1e-7):
        self.threshold = threshold
        self.newtons_method(initial_guess)
        print("Time error: {0}".format(self.test_solution(self.c.pop())))


if __name__ == "__main__":
    solver = SpeedometerSolver('input.txt')
    solver.run(-0.4, threshold=1e-29)
