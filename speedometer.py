
class SpeedometerSolver:

    def __init__(self, filename):
        file = open(filename, "r")
        self.n = int(file.readline())
        self.T = int(file.readline())
        self.distances = list(map(int, file.readline().rstrip('\n').split()))
        self.speeds = list(map(int, file.readline().strip('\n').split()))
        file.close()

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
        time = 0;
        for di, si in zip(self.distances, self.speeds):
            time += di / (si + c)
        return self.T - time

    def newtons_method(self, c0):
        self.c = c0
        for i in range(0, 10):
            self.c -= (self.solve_equation(self.c) / self.solve_derivative(self.c))
            print(self.c)

    def run(self, c0):
        self.newtons_method(c0)
        print("Time error: {0}".format(self.test_solution(self.c)))


if __name__ == "__main__":
    solver = SpeedometerSolver('input.txt')
    solver.run(-0.1)
