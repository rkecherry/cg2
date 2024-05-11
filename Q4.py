import matplotlib.pyplot as plt

# Define window boundaries
X_MIN, X_MAX = 50, 200
Y_MIN, Y_MAX = 50, 200

def clip_polygon(polygon):
    output_list = polygon

    for edge in [[(X_MIN, Y_MIN), (X_MAX, Y_MIN)],
                 [(X_MAX, Y_MIN), (X_MAX, Y_MAX)],
                 [(X_MAX, Y_MAX), (X_MIN, Y_MAX)],
                 [(X_MIN, Y_MAX), (X_MIN, Y_MIN)]]:
        input_list = output_list
        output_list = []

        (x1, y1), (x2, y2) = edge

        for i in range(len(input_list)):
            p1 = input_list[i]
            p2 = input_list[(i + 1) % len(input_list)]

            # Check if the current edge of the polygon is inside the window
            if is_inside_window(p1, p2, x1, y1, x2, y2):
                if not is_inside_window(p1, p2, *edge[1], *edge[0]):
                    # Calculate intersection point
                    intersection = compute_intersection_point(p1, p2, x1, y1, x2, y2)
                    output_list.append(intersection)
                output_list.append(p2)
            elif is_inside_window(p1, p2, *edge[1], *edge[0]):
                # Calculate intersection point
                intersection = compute_intersection_point(p1, p2, x1, y1, x2, y2)
                output_list.append(intersection)

    return output_list

def is_inside_window(p1, p2, x1, y1, x2, y2):
    return (x2 - x1) * (p1[1] - y1) - (y2 - y1) * (p1[0] - x1) < 0 or \
           (x2 - x1) * (p2[1] - y1) - (y2 - y1) * (p2[0] - x1) < 0

def compute_intersection_point(p1, p2, x1, y1, x2, y2):
    # Calculate the intersection point
    if p1[0] == p2[0]:
        slope_edge = float('inf')
    else:
        slope_edge = (p2[1] - p1[1]) / (p2[0] - p1[0])

    if x1 == x2:
        slope_clip = float('inf')
    else:
        slope_clip = (y2 - y1) / (x2 - x1)

    if slope_edge != slope_clip:
        if slope_edge == float('inf'):
            intersection_x = p1[0]
            intersection_y = slope_clip * (intersection_x - x1) + y1
        elif slope_clip == float('inf'):
            intersection_x = x1
            intersection_y = slope_edge * (intersection_x - p1[0]) + p1[1]
        else:
            intersection_x = (slope_edge * p1[0] - slope_clip * x1 + y1 - p1[1]) / (slope_edge - slope_clip)
            intersection_y = slope_edge * (intersection_x - p1[0]) + p1[1]

        return int(intersection_x), int(intersection_y)
    else:
        return p2

def main():
    num_vertices = int(input("Enter the number of vertices of the polygon: "))
    polygon = []
    for i in range(num_vertices):
        x = int(input("Enter x-coordinate of vertex {}: ".format(i + 1)))
        y = int(input("Enter y-coordinate of vertex {}: ".format(i + 1)))
        polygon.append((x, y))

    clipped_polygon = clip_polygon(polygon)

    plt.figure()
    plt.plot([X_MIN, X_MAX, X_MAX, X_MIN, X_MIN], [Y_MIN, Y_MIN, Y_MAX, Y_MAX, Y_MIN], 'k-')
    plt.title('Sutherland-Hodgman Polygon Clipping')
    plt.gca().set_aspect('equal', adjustable='box')

    plt.plot(*zip(*polygon), 'r-', label='Original Polygon')
    plt.plot(*zip(*clipped_polygon), 'b-', label='Clipped Polygon')

    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
