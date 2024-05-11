import numpy as np
import matplotlib.pyplot as plt

def translate(tx, ty, tz):
    return np.array([[1, 0, 0, tx],
                     [0, 1, 0, ty],
                     [0, 0, 1, tz],
                     [0, 0, 0, 1]])

def scale(sx, sy, sz):
    return np.array([[sx, 0, 0, 0],
                     [0, sy, 0, 0],
                     [0, 0, sz, 0],
                     [0, 0, 0, 1]])

def rotate_x(theta):
    theta_rad = np.radians(theta)
    cos_theta = np.cos(theta_rad)
    sin_theta = np.sin(theta_rad)
    return np.array([[1, 0, 0, 0],
                     [0, cos_theta, -sin_theta, 0],
                     [0, sin_theta, cos_theta, 0],
                     [0, 0, 0, 1]])

def rotate_y(theta):
    theta_rad = np.radians(theta)
    cos_theta = np.cos(theta_rad)
    sin_theta = np.sin(theta_rad)
    return np.array([[cos_theta, 0, sin_theta, 0],
                     [0, 1, 0, 0],
                     [-sin_theta, 0, cos_theta, 0],
                     [0, 0, 0, 1]])

def rotate_z(theta):
    theta_rad = np.radians(theta)
    cos_theta = np.cos(theta_rad)
    sin_theta = np.sin(theta_rad)
    return np.array([[cos_theta, -sin_theta, 0, 0],
                     [sin_theta, cos_theta, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

def perspective_projection(d):
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 1/d, 0]])

def parallel_projection():
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 1]])

def transform_points(points, transformation_matrix):
    homogeneous_points = np.column_stack((points, np.ones(len(points))))
    transformed_points = np.dot(homogeneous_points, transformation_matrix.T)
    return transformed_points[:, :-1]

def plot_3d_object(points, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x, y, z = zip(*points)
    ax.scatter(x, y, z)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)

    plt.show()

def main():
    num_points = int(input("Enter the number of points of the 3D object: "))
    points = []
    for i in range(num_points):
        x = float(input("Enter x-coordinate of point {}: ".format(i + 1)))
        y = float(input("Enter y-coordinate of point {}: ".format(i + 1)))
        z = float(input("Enter z-coordinate of point {}: ".format(i + 1)))
        points.append([x, y, z])

    # Apply transformations
    tx = float(input("Enter translation along x-axis: "))
    ty = float(input("Enter translation along y-axis: "))
    tz = float(input("Enter translation along z-axis: "))
    translation_matrix = translate(tx, ty, tz)

    sx = float(input("Enter scaling along x-axis: "))
    sy = float(input("Enter scaling along y-axis: "))
    sz = float(input("Enter scaling along z-axis: "))
    scaling_matrix = scale(sx, sy, sz)

    angle_x = float(input("Enter rotation angle about x-axis in degrees: "))
    rotation_matrix_x = rotate_x(angle_x)

    angle_y = float(input("Enter rotation angle about y-axis in degrees: "))
    rotation_matrix_y = rotate_y(angle_y)

    angle_z = float(input("Enter rotation angle about z-axis in degrees: "))
    rotation_matrix_z = rotate_z(angle_z)

    # Apply transformations one by one and plot the results
    transformations = [translation_matrix, scaling_matrix, rotation_matrix_x, rotation_matrix_y, rotation_matrix_z]
    transformation_names = ['Translation', 'Scaling', 'Rotation about X', 'Rotation about Y', 'Rotation about Z']

    for transformation, name in zip(transformations, transformation_names):
        transformed_points = transform_points(points, transformation)
        plot_3d_object(transformed_points, name)

    # Apply parallel and perspective projection
    d = float(input("Enter distance from the viewer to the projection plane for perspective projection: "))
    perspective_matrix = perspective_projection(d)
    parallel_matrix = parallel_projection()

    perspective_projection_points = transform_points(points, perspective_matrix)
    plot_3d_object(perspective_projection_points, "Perspective Projection")

    parallel_projection_points = transform_points(points, parallel_matrix)
    plot_3d_object(parallel_projection_points, "Parallel Projection")

if __name__ == "__main__":
    main()
