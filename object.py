from copy import deepcopy
import math

objects = {
    "floor":{
        "points":[
            {"x":0, "y":0, "z":0},
            {"x":0, "y":0, "z":300},
            {"x":300, "y":0, "z":0},
            {"x":300, "y":0, "z":300},
            {"x":600, "y":0, "z":0},
            {"x":600, "y":0, "z":300},
            {"x":900, "y":0, "z":0},
            {"x":900, "y":0, "z":300},
            {"x":1200, "y":0, "z":0},
            {"x":1200, "y":0, "z":300},
            {"x":1500, "y":0, "z":0},
            {"x":1500, "y":0, "z":300},
            {"x":1800, "y":0, "z":0},
            {"x":1800, "y":0, "z":300},
            {"x":2100, "y":0, "z":0},
            {"x":2100, "y":0, "z":300},


            {"x":0, "y":0, "z":600},
            {"x":300, "y":0, "z":600},
            {"x":600, "y":0, "z":600},
            {"x":900, "y":0, "z":600},
            {"x":1200, "y":0, "z":600},
            {"x":1500, "y":0, "z":600},
            {"x":1800, "y":0, "z":600},
            {"x":2100, "y":0, "z":600},

            {"x":0, "y":0, "z":900},
            {"x":300, "y":0, "z":900},
            {"x":600, "y":0, "z":900},
            {"x":900, "y":0, "z":900},
            {"x":1200, "y":0, "z":900},
            {"x":1500, "y":0, "z":900},
            {"x":1800, "y":0, "z":900},
            {"x":2100, "y":0, "z":900},

        ],
        "faces":[
            {"ind0":1, "ind1":0, "ind2":2, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":1, "ind1":3, "ind2":2, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},

            {"ind0":4, "ind1":2, "ind2":3, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":4, "ind1":5, "ind2":3, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},

            {"ind0":6, "ind1":4, "ind2":5, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":6, "ind1":7, "ind2":5, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},

            {"ind0":8, "ind1":6, "ind2":7, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":8, "ind1":9, "ind2":7, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},

            {"ind0":10, "ind1":8, "ind2":9, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":10, "ind1":11, "ind2":9, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},


            {"ind0":12, "ind1":10, "ind2":11, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":12, "ind1":13, "ind2":11, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},


            {"ind0":14, "ind1":12, "ind2":13, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":14, "ind1":13, "ind2":15, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},


            {"ind0":3, "ind1":1, "ind2":16, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":3, "ind1":17, "ind2":16, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},

            {"ind0":5, "ind1":3, "ind2":17, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":5, "ind1":18, "ind2":17, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},

            {"ind0":7, "ind1":5, "ind2":18, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":7, "ind1":19, "ind2":18, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},

            {"ind0":9, "ind1":7, "ind2":19, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":9, "ind1":20, "ind2":19, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},

            {"ind0":11, "ind1":9, "ind2":20, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":11, "ind1":21, "ind2":20, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},

            {"ind0":13, "ind1":11, "ind2":21, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":13, "ind1":22, "ind2":21, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},

            {"ind0":15, "ind1":13, "ind2":22, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":15, "ind1":23, "ind2":22, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},

            {"ind0":17, "ind1":16, "ind2":24, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":17, "ind1":25, "ind2":24, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},

            {"ind0":18, "ind1":17, "ind2":25, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":18, "ind1":26, "ind2":25, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},

            {"ind0":19, "ind1":18, "ind2":26, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":19, "ind1":27, "ind2":26, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},

            {"ind0":20, "ind1":19, "ind2":27, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":20, "ind1":28, "ind2":27, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},

            {"ind0":21, "ind1":20, "ind2":28, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":21, "ind1":29, "ind2":28, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},

            {"ind0":22, "ind1":21, "ind2":29, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":22, "ind1":30, "ind2":29, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},

            {"ind0":23, "ind1":22, "ind2":30, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":23, "ind1":31, "ind2":30, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},
        ]
    },
    "wall":{
        "points":[
            # side 0
            {"x":0, "y":0, "z":0},
            {"x":0, "y":0, "z":300},
            {"x":0, "y":300, "z":0},
            {"x":0, "y":300, "z":300},

            {"x":0, "y":0, "z":600},
            {"x":0, "y":300, "z":600},

            {"x":0, "y":0, "z":900},
            {"x":0, "y":300, "z":900},

            {"x":0, "y":0, "z":1200},
            {"x":0, "y":300, "z":1200},

            # side 1
            {"x":50, "y":0, "z":0},
            {"x":50, "y":0, "z":300},
            {"x":50, "y":300, "z":0},
            {"x":50, "y":300, "z":300},

            {"x":50, "y":0, "z":600},
            {"x":50, "y":300, "z":600},

            {"x":50, "y":0, "z":900},
            {"x":50, "y":300, "z":900},


            {"x":50, "y":0, "z":1200},
            {"x":50, "y":300, "z":1200},




        ],
        "faces":[
            {"ind0":0, "ind1":2, "ind2":3, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},
            {"ind0":3, "ind1":1, "ind2":0, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},

            {"ind0":1, "ind1":3, "ind2":5, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":1, "ind1":4, "ind2":5, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},

            {"ind0":4, "ind1":6, "ind2":7, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":4, "ind1":5, "ind2":7, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},

            {"ind0":6, "ind1":8, "ind2":9, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},
            {"ind0":6, "ind1":7, "ind2":9, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},


            {"ind0":10, "ind1":12, "ind2":13, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":10, "ind1":11, "ind2":13, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},


            {"ind0":11, "ind1":14, "ind2":15, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":11, "ind1":13, "ind2":15, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},


            {"ind0":14, "ind1":15, "ind2":17, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":14, "ind1":16, "ind2":17, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},


            {"ind0":16, "ind1":18, "ind2":19, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":16, "ind1":17, "ind2":19, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},



            {"ind0":8, "ind1":9, "ind2":19, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},
            {"ind0":8, "ind1":18, "ind2":19, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},

            {"ind0":10, "ind1":12, "ind2":2, "color":(100, 100, 100), "face_angle_h":0, "face_angle_v":0},
            {"ind0":2, "ind1":0, "ind2":10, "color":(120, 120, 120), "face_angle_h":0, "face_angle_v":0},
        ]
    },

    "box": {
        "points":[
            {"x":0, "y":0, "z":0},
            {"x":0, "y":0, "z":300},
            {"x":300, "y":0, "z":0},
            {"x":300, "y":0, "z":300},

            {"x":0, "y":300, "z":0},
            {"x":0, "y":300, "z":300},
            {"x":300, "y":300, "z":0},
            {"x":300, "y":300, "z":300},
        ],
        "faces":[
            {"ind0":0, "ind1":4, "ind2":6, "color":(139, 69, 19), "face_angle_h":0, "face_angle_v":0},
            {"ind0":0, "ind1":2, "ind2":6, "color":(159, 89, 39), "face_angle_h":0, "face_angle_v":0},

            {"ind0":3, "ind1":6, "ind2":7, "color":(159, 89, 39), "face_angle_h":0, "face_angle_v":0},
            {"ind0":2, "ind1":3, "ind2":6, "color":(139, 69, 19), "face_angle_h":0, "face_angle_v":0},

            {"ind0":1, "ind1":0, "ind2":4, "color":(159, 89, 39), "face_angle_h":0, "face_angle_v":0},
            {"ind0":1, "ind1":5, "ind2":4, "color":(139, 69, 19), "face_angle_h":0, "face_angle_v":0},

            {"ind0":1, "ind1":5, "ind2":7, "color":(159, 89, 39), "face_angle_h":0, "face_angle_v":0},
            {"ind0":1, "ind1":3, "ind2":7, "color":(139, 69, 19), "face_angle_h":0, "face_angle_v":0},

            {"ind0":5, "ind1":4, "ind2":6, "color":(159, 89, 39), "face_angle_h":0, "face_angle_v":0},
            {"ind0":5, "ind1":7, "ind2":6, "color":(139, 69, 19), "face_angle_h":0, "face_angle_v":0},

        ]
    },

    "booster":{
        "points":[
            {"x":0, "y":0, "z":0},
            {"x":0, "y":0, "z":300},
            {"x":300, "y":0, "z":0},
            {"x":300, "y":0, "z":300},
        ],
        "faces":[
            {"ind0":1, "ind1":0, "ind2":2, "color":(0, 169, 0), "face_angle_h":0, "face_angle_v":0},
            {"ind0":1, "ind1":3, "ind2":2, "color":(0, 189, 0), "face_angle_h":0, "face_angle_v":0},
        ]
    },

    "player":{
        "points":[
            {"x":0, "y":0, "z":0},
            {"x":0, "y":0, "z":100},
            {"x":100, "y":0, "z":0},
            {"x":100, "y":0, "z":100},

            {"x":0, "y":250, "z":0},
            {"x":0, "y":250, "z":100},
            {"x":100, "y":250, "z":0},
            {"x":100, "y":250, "z":100},
        ],
        "faces":[
            {"ind0":0, "ind1":4, "ind2":6, "color":(139, 69, 19), "face_angle_h":0, "face_angle_v":0},
            {"ind0":0, "ind1":2, "ind2":6, "color":(159, 89, 39), "face_angle_h":0, "face_angle_v":0},

            {"ind0":3, "ind1":6, "ind2":7, "color":(159, 89, 39), "face_angle_h":0, "face_angle_v":0},
            {"ind0":2, "ind1":3, "ind2":6, "color":(139, 69, 19), "face_angle_h":0, "face_angle_v":0},

            {"ind0":1, "ind1":0, "ind2":4, "color":(159, 89, 39), "face_angle_h":0, "face_angle_v":0},
            {"ind0":1, "ind1":5, "ind2":4, "color":(139, 69, 19), "face_angle_h":0, "face_angle_v":0},

            {"ind0":1, "ind1":5, "ind2":7, "color":(159, 89, 39), "face_angle_h":0, "face_angle_v":0},
            {"ind0":1, "ind1":3, "ind2":7, "color":(139, 69, 19), "face_angle_h":0, "face_angle_v":0},

            {"ind0":5, "ind1":4, "ind2":6, "color":(159, 89, 39), "face_angle_h":0, "face_angle_v":0},
            {"ind0":5, "ind1":7, "ind2":6, "color":(139, 69, 19), "face_angle_h":0, "face_angle_v":0},

        ]
    }
    
}

PI = 3.141592

class Object:
    def __init__(
            self, 
            x, y, z, name,
            w, h, l,
            collider="box",
        ) -> None:
        self.points = deepcopy(objects[name]["points"])
        self.faces = deepcopy(objects[name]["faces"])
        
        self.name = name
        self.type = "object"
        self.collider = collider

        self.x = x
        self.y = y
        self.z = z


        self.w = w
        self.h = h
        self.l = l

        self.rotation_x = 0
        self.rotation_y = 0
        self.rotation_z = 0

        for point in self.points:
            point["x"] += x
            point["y"] += y
            point["z"] += z

    def rotate_y(self, angle):
        # self.rotation_y += 0.1

        for point in self.points:
            x = point["x"]
            z = point["z"]

            
            

            dist_x = self.x - x 
            dist_z = self.z - z

            distanse_to_camera_XZ = math.sqrt(
                ((self.x - x)**2) + ((self.z - z)**2)
            )
            
            angleRadians_XZ = math.atan2(dist_x, dist_z)
            angleDegrees_XZ = angleRadians_XZ * (180 / PI)

            
            point["x"] = math.sin(math.radians((angleDegrees_XZ - 180) + angle)) * distanse_to_camera_XZ + self.x
            point["z"] = math.cos(math.radians((angleDegrees_XZ + 180) + angle)) * distanse_to_camera_XZ + self.z