



import math


class Bullet:
    def __init__(self,
            x, y, z,
            angle_y, angle_x,
            type,
            speed):
        
        self.x = x
        self.y = y
        self.z = z

        self.angle_y = angle_y
        self.angle_x = angle_x

        self.type = type
        self.speed = speed
        self.collider = None

        self.points = [
            {"x":-5, "y":0, "z":0},
            {"x":-5, "y":0, "z":20},
            {"x":5, "y":0, "z":0},
            {"x":5, "y":0, "z":20},
        ]

        self.faces = [
            {"ind0":1, "ind1":0, "ind2":2, "color":(0, 169, 0), "face_angle_h":0, "face_angle_v":0},
            {"ind0":1, "ind1":3, "ind2":2, "color":(0, 189, 0), "face_angle_h":0, "face_angle_v":0},

        ]


        for point in self.points:
            point["x"] += -x
            point["y"] += -y
            point["z"] += -z
    def update(self):
        # self.x += math.cos(math.radians(self.angle_y)) * self.speed
        # self.z += math.sin(math.radians(self.angle_y)) * self.speed

        for point in self.points:
            point["x"] += -math.sin(math.radians(self.angle_y)) * self.speed
            point["z"] += math.cos(math.radians(self.angle_y)) * self.speed

    def rotate_y(self, angle):
        # self.rotation_y += 0.1

        for point in self.points:
            x = point["x"]
            z = point["z"]

            
            

            dist_x = -self.x - x 
            dist_z = -self.z - z

            distanse_to_camera_XZ = math.sqrt(
                ((-self.x - x)**2) + ((-self.z - z)**2)
            )
            
            angleRadians_XZ = math.atan2(dist_x, dist_z)
            angleDegrees_XZ = angleRadians_XZ * (180 / math.pi)

            
            point["x"] = math.sin(math.radians((angleDegrees_XZ - 180) - angle)) * distanse_to_camera_XZ + -self.x
            point["z"] = math.cos(math.radians((angleDegrees_XZ + 180) - angle)) * distanse_to_camera_XZ + -self.z
    
    def rotate_x(self, angle):
        # self.rotation_y += 0.1

        for point in self.points:
            z = point["z"]
            y = point["y"]

            
            

            dist_z = -self.z - z
            dist_y = -self.y - y

            distanse_to_camera_XZ = math.sqrt(
                ((-self.z - z)**2) + ((-self.y - y)**2)
            )
            
            angleRadians_XZ = math.atan2(dist_y, dist_z)
            angleDegrees_XZ = angleRadians_XZ * (180 / math.pi)

            
            point["z"] = math.sin(math.radians((angleDegrees_XZ - 180) - angle)) * distanse_to_camera_XZ + -self.z
            point["y"] = math.cos(math.radians((angleDegrees_XZ + 180) - angle)) * distanse_to_camera_XZ + -self.y