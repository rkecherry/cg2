import matplotlib.pyplot as plt

def draw_circle(center_x, center_y, radius):
    x = 0
    y = radius
    p = 1 - radius

    points = set_points(center_x, center_y, x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        points.update(set_points(center_x, center_y, x, y))

    return points

def set_points(center_x, center_y, x, y):
    points = set()
    points.add((center_x + x, center_y + y))
    points.add((center_x - x, center_y + y))
    points.add((center_x + x, center_y - y))
    points.add((center_x - x, center_y - y))
    points.add((center_x + y, center_y + x))
    points.add((center_x - y, center_y + x))
    points.add((center_x + y, center_y - x))
    points.add((center_x - y, center_y - x))
    return points

def main():
    center_x = int(input("Enter the x-coordinate of the center: "))
    center_y = int(input("Enter the y-coordinate of the center: "))
    radius = int(input("Enter the radius of the circle: "))

    circle_points = draw_circle(center_x, center_y, radius)

    plt.figure()
    plt.axis('equal')
    plt.title('Mid-Point Circle Drawing Algorithm')
    plt.scatter(*zip(*circle_points), color='black')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
