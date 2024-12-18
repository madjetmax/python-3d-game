import pygame
import math
import numpy as np

def project_point_3d_to_2d(x, y, z, screen_width, screen_height, fov, z_near=0.1):
    """
    Projects a 3D point (x, y, z) onto a 2D screen in Pygame, with correct handling for negative z-values.
    """
    f = screen_width / (2 * math.tan(math.radians(fov) / 2))
    z_safe = z + z_near
    if z_safe == 0:
        return None  # Avoid division by zero

    if z_safe > 0:
        x_prime = (x * f) / z_safe + screen_width / 2
        y_prime = (-y * f) / z_safe + screen_height / 2
    else:
        x_prime = (x * f) * z_safe + screen_width / 2
        y_prime = (-y * f) * z_safe + screen_height / 2

    return int(x_prime), int(y_prime)

def rotate_point(point, rotation_matrix):
    """
    Rotates a 3D point using a given rotation matrix.
    """
    return np.dot(rotation_matrix, point)

def create_rotation_matrix(rx, ry, rz):
    """
    Creates a composite rotation matrix for rotations around x, y, z axes.
    """
    cx, cy, cz = math.cos(rx), math.cos(ry), math.cos(rz)
    sx, sy, sz = math.sin(rx), math.sin(ry), math.sin(rz)

    rotation_x = np.array([
        [1, 0, 0],
        [0, cx, -sx],
        [0, sx, cx],
    ])

    rotation_y = np.array([
        [cy, 0, sy],
        [0, 1, 0],
        [-sy, 0, cy],
    ])

    rotation_z = np.array([
        [cz, -sz, 0],
        [sz, cz, 0],
        [0, 0, 1],
    ])

    return np.dot(rotation_z, np.dot(rotation_y, rotation_x))

def draw_cube(screen, cube_points, edges, camera_position, camera_rotation, screen_width, screen_height, fov):
    """
    Draws a 3D cube on the Pygame screen using perspective projection.
    """
    rotation_matrix = create_rotation_matrix(*camera_rotation)
    projected_points = []

    for x, y, z in cube_points:
        # Translate point relative to camera
        translated_point = np.array([x - camera_position[0], y - camera_position[1], z - camera_position[2]])

        # Rotate point relative to camera's rotation
        rotated_point = rotate_point(translated_point, rotation_matrix)

        # Project the rotated point
        projection = project_point_3d_to_2d(rotated_point[0], rotated_point[1], rotated_point[2], screen_width, screen_height, fov)
        projected_points.append(projection)

    # Draw edges if both points are projectable
    for start, end in edges:
        p1 = projected_points[start]
        p2 = projected_points[end]
        if p1 is not None and p2 is not None:
            try:
                pygame.draw.line(screen, (255, 255, 255), p1, p2, 2)
            except Exception:
                pass
# Pygame setup
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("3D Cube Projection with Camera Movement and Rotation")

# Cube definition
cube_points = [
    (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),  # Back face
    (-1, -1,  1), (1, -1,  1), (1, 1,  1), (-1, 1,  1),  # Front face
]
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Back face
    (4, 5), (5, 6), (6, 7), (7, 4),  # Front face
    (0, 4), (1, 5), (2, 6), (3, 7),  # Connecting edges
]

# Camera variables
camera_position = np.array([0.0, 0.0, -5.0])  # Start behind the cube
camera_rotation = [0.0, 0.0, 0.0]  # Rotation angles (x, y, z)

# Field of view
fov = 90

# Movement and rotation speed
move_speed = 0.1
rotate_speed = 0.05

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # Move forward
        camera_position[2] += move_speed
    if keys[pygame.K_s]:  # Move backward
        camera_position[2] -= move_speed
    if keys[pygame.K_a]:  # Move left
        camera_position[0] -= move_speed
    if keys[pygame.K_d]:  # Move right
        camera_position[0] += move_speed
    if keys[pygame.K_q]:  # Move up
        camera_position[1] += move_speed
    if keys[pygame.K_e]:  # Move down
        camera_position[1] -= move_speed
    if keys[pygame.K_LEFT]:  # Rotate left
        camera_rotation[1] -= rotate_speed
    if keys[pygame.K_RIGHT]:  # Rotate right
        camera_rotation[1] += rotate_speed
    if keys[pygame.K_UP]:  # Rotate up
        camera_rotation[0] -= rotate_speed
    if keys[pygame.K_DOWN]:  # Rotate down
        camera_rotation[0] += rotate_speed

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw cube
    draw_cube(screen, cube_points, edges, camera_position, camera_rotation, screen_width, screen_height, fov)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()