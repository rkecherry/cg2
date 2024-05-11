import numpy as np
import matplotlib.pyplot as plt

def translate(tx, ty):
    return np.array([[1, 0, tx],
                     [0, 1, ty],
                     [0, 0, 1]])

def scale(sx, sy):
    return np.array([[sx, 0, 0],
                     [0, sy, 0],
                     [0, 0, 1]])

def rotate(theta):
    theta_rad = np.radians(theta)
    cos_theta = np.cos(theta_rad)
    sin_theta = np.sin(theta_rad)
    return np.array([[cos_theta, -sin_theta, 0],
                     [sin_theta, cos_theta, 0],
                     [0, 0, 1]])

def reflect(axis):
    if axis.lower() == 'x':
        return np.array([[1, 0, 0],
                         [0, -1, 0],
                         [0, 0, 1]])
    elif axis.lower() == 'y':
        return np.array([[-1, 0, 0],
                         [0, 1, 0],
                         [0, 0, 1]])

def shear(kx, ky):
    return np.array([[1, kx, 0],
                     [ky, 1, 0],
                     [0, 0, 1]])

def transform_points(points, transformation_matrix):
    homogeneous_points = np.column_stack((points, np.ones(len(points))))
    transformed_points = np.dot(homogeneous_points, transformation_matrix.T)
    return transformed_points[:, :-1]

def main():
    num_points = int(input("Enter the number of points: "))
    points = []
    for i in range(num_points):
        x = float(input("Enter x-coordinate of point {}: ".format(i + 1)))
        y = float(input("Enter y-coordinate of point {}: ".format(i + 1)))
        points.append([x, y])

    # Apply transformations
    tx = float(input("Enter translation along x-axis: "))
    ty = float(input("Enter translation along y-axis: "))
    translation_matrix = translate(tx, ty)

    sx = float(input("Enter scaling along x-axis: "))
    sy = float(input("Enter scaling along y-axis: "))
    scaling_matrix = scale(sx, sy)

    theta = float(input("Enter rotation angle in degrees: "))
    rotation_matrix = rotate(theta)

    axis = input("Enter axis for reflection (x/y): ")
    reflection_matrix = reflect(axis)

    kx = float(input("Enter shear factor along x-axis: "))
    ky = float(input("Enter shear factor along y-axis: "))
    shear_matrix = shear(kx, ky)

    # Apply transformations one by one and plot the results
    transformations = [translation_matrix, scaling_matrix, rotation_matrix, reflection_matrix, shear_matrix]
    transformation_names = ['Translation', 'Scaling', 'Rotation', 'Reflection', 'Shear']

    plt.figure(figsize=(10, 8))
    plt.title('2D Object Transformations')

    for i, (transformation, name) in enumerate(zip(transformations, transformation_names), 1):
        transformed_points = transform_points(points, transformation)
        plt.subplot(2, 3, i)
        plt.plot(*zip(*points), marker='o', linestyle='-', color='b', label='Original')
        plt.plot(*zip(*transformed_points), marker='o', linestyle='-', color='r', label='Transformed')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(name)
        plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
