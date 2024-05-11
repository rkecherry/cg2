import matplotlib.pyplot as plt
import numpy as np

def scan_line_fill(polygon):
    min_y = min(y for _, y in polygon)
    max_y = max(y for _, y in polygon)

    scan_lines = []
    for y in range(min_y, max_y + 1):
        intersecting_points = []
        for i in range(len(polygon)):
            x1, y1 = polygon[i]
            x2, y2 = polygon[(i + 1) % len(polygon)]
            if y1 < y <= y2 or y2 < y <= y1:
                if y2 - y1 != 0:
                    intersect_x = int(x1 + (y - y1) * (x2 - x1) / (y2 - y1))
                    intersecting_points.append(intersect_x)

        intersecting_points.sort()
        scan_lines.append(intersecting_points)

    return scan_lines

def fill_polygon(polygon):
    scan_lines = scan_line_fill(polygon)

    filled_polygon = []
    for y, intersecting_points in enumerate(scan_lines):
        for i in range(0, len(intersecting_points), 2):
            start_x = intersecting_points[i]
            end_x = intersecting_points[i + 1]
            filled_polygon.extend([(x, y) for x in range(start_x, end_x + 1)])

    return filled_polygon

def main():
    num_vertices = int(input("Enter the number of vertices of the polygon: "))
    polygon = []
    for i in range(num_vertices):
        x = int(input("Enter x-coordinate of vertex {}: ".format(i + 1)))
        y = int(input("Enter y-coordinate of vertex {}: ".format(i + 1)))
        polygon.append((x, y))

    filled_polygon = fill_polygon(polygon)

    plt.figure()
    plt.title('Scan-Line Fill Algorithm')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.plot(*zip(*filled_polygon), 'k.')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
