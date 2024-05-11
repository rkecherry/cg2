import numpy as np
import matplotlib.pyplot as plt

def hermite_curve(P0, P1, R0, R1, num_points=100):
    t = np.linspace(0, 1, num_points)
    H = np.array([[2, -2, 1, 1],
                  [-3, 3, -2, -1],
                  [0, 0, 1, 0],
                  [1, 0, 0, 0]])
    T = np.array([t**3, t**2, t, np.ones(num_points)])
    G = np.array([P0, P1, R0, R1])
    return np.dot(G, np.dot(H, T))

def bezier_curve(P0, P1, P2, P3, num_points=100):
    t = np.linspace(0, 1, num_points)
    B = np.array([(-1*t**3 + 3*t**2 - 3*t + 1),
                  (3*t**3 - 6*t**2 + 3*t),
                  (-3*t**3 + 3*t**2),
                  (t**3)])
    P = np.array([P0, P1, P2, P3])
    return np.dot(P.T, B)

def plot_curve(points, title):
    plt.figure()
    plt.plot(points[0], points[1], label='Curve')
    plt.scatter(points[0], points[1], color='r', label='Control Points')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    P0 = np.array([float(input("Enter x-coordinate of P0: ")), float(input("Enter y-coordinate of P0: "))])
    P1 = np.array([float(input("Enter x-coordinate of P1: ")), float(input("Enter y-coordinate of P1: "))])
    if input("Do you want to specify tangent vectors for Hermite curve? (yes/no): ").lower() == 'yes':
        R0 = np.array([float(input("Enter x-coordinate of R0: ")), float(input("Enter y-coordinate of R0: "))])
        R1 = np.array([float(input("Enter x-coordinate of R1: ")), float(input("Enter y-coordinate of R1: "))])
        points_hermite = hermite_curve(P0, P1, R0, R1)
        plot_curve(points_hermite, 'Hermite Curve')
    else:
        P2 = np.array([float(input("Enter x-coordinate of P2: ")), float(input("Enter y-coordinate of P2: "))])
        P3 = np.array([float(input("Enter x-coordinate of P3: ")), float(input("Enter y-coordinate of P3: "))])
        points_bezier = bezier_curve(P0, P1, P2, P3)
        plot_curve(points_bezier, 'Bezier Curve')

if __name__ == "__main__":
    main()
