import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps

    x = x1
    y = y1
    points = [(round(x), round(y))]

    for _ in range(steps):
        x += x_increment
        y += y_increment
        points.append((round(x), round(y)))

    return points

def main():
    # Input from user
    x1 = int(input("Enter x-coordinate of the first point: "))
    y1 = int(input("Enter y-coordinate of the first point: "))
    x2 = int(input("Enter x-coordinate of the second point: "))
    y2 = int(input("Enter y-coordinate of the second point: "))

    # Plotting the line using DDA algorithm
    line_points = dda_line(x1, y1, x2, y2)
    x_values, y_values = zip(*line_points)

    # Plot the line
    plt.plot(x_values, y_values, marker='o')
    plt.title('DDA Line Drawing Algorithm')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == "__main__":
    main()
