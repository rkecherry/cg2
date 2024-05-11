import matplotlib.pyplot as plt

# Define region codes for Cohen-Sutherland algorithm
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

# Define the window boundaries
X_MIN, X_MAX = 50, 200
Y_MIN, Y_MAX = 50, 200

def compute_region_code(x, y):
    code = INSIDE
    if x < X_MIN:
        code |= LEFT
    elif x > X_MAX:
        code |= RIGHT
    if y < Y_MIN:
        code |= BOTTOM
    elif y > Y_MAX:
        code |= TOP
    return code

def cohen_sutherland_line_clipping(x1, y1, x2, y2):
    code1 = compute_region_code(x1, y1)
    code2 = compute_region_code(x2, y2)

    while True:
        if not (code1 | code2):
            # Both endpoints are inside the window, accept the line
            return [(x1, y1), (x2, y2)]
        elif code1 & code2:
            # Both endpoints are outside the window and on the same side, reject the line
            return []
        else:
            # Calculate intersection point
            code_out = code1 if code1 else code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (Y_MAX - y1) / (y2 - y1)
                y = Y_MAX
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (Y_MIN - y1) / (y2 - y1)
                y = Y_MIN
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (X_MAX - x1) / (x2 - x1)
                x = X_MAX
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (X_MIN - x1) / (x2 - x1)
                x = X_MIN

            # Update the endpoint outside the window
            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_region_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_region_code(x2, y2)

def main():
    x1 = int(input("Enter x-coordinate of the first point: "))
    y1 = int(input("Enter y-coordinate of the first point: "))
    x2 = int(input("Enter x-coordinate of the second point: "))
    y2 = int(input("Enter y-coordinate of the second point: "))

    plt.figure()
    plt.plot([X_MIN, X_MAX, X_MAX, X_MIN, X_MIN], [Y_MIN, Y_MIN, Y_MAX, Y_MAX, Y_MIN], 'k-')
    plt.title('Cohen-Sutherland Line Clipping')
    plt.gca().set_aspect('equal', adjustable='box')
    
    plt.plot([x1, x2], [y1, y2], 'r-', label='Original Line')

    clipped_line = cohen_sutherland_line_clipping(x1, y1, x2, y2)
    if clipped_line:
        plt.plot([clipped_line[0][0], clipped_line[1][0]], [clipped_line[0][1], clipped_line[1][1]], 'b-', label='Clipped Line')
    else:
        print("Line is completely outside the window, not plotted.")

    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
