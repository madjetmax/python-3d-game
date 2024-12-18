import math
from object import Object
import pygame as pg
from numba import njit

PI = 3.141592


class World:
    def __init__(self) -> None:
        self.objects = []
        self.points = []
        self.faces = []

        self.font = pg.font.Font(None, 32)

    def generate_word(self):
        


        # walls
        obj = Object(
            900, 0, 900, 
            "wall",
            1200, 300, 50
        )
        obj.rotate_y(90)
        self.objects.append(obj)
        obj = Object(
            0, 0, 1250, 
            "wall",
            1200, 300, 50
        )
        obj.rotate_y(90)
        self.objects.append(obj)



        obj = Object(
            900, 0, 3300, 
            "wall",
            1200, 300, 50
        )
        obj.rotate_y(90)
        self.objects.append(obj)
        obj = Object(
            0, 0, 3650, 
            "wall",
            1200, 300, 50
        )
        obj.rotate_y(90)
        self.objects.append(obj)



        # floor
        for x in range(1):
            for z in range(5):
                obj = Object(
                    x*2100, 0, z*900, 
                    "floor",
                    2100, 1, 1000
                )
                self.objects.append(obj)


        # boxes
        obj = Object(
            1500, 0, 1500, 
            "box",
            300, 300, 400
        )
        self.objects.append(obj)

        obj = Object(
            900, 0, 2100, 
            "box",
            300, 300, 400
        )
        self.objects.append(obj)


        obj = Object(
            300, 0, 2700, 
            "box",
            300, 300, 400
        )
        self.objects.append(obj)


        obj = Object(
            0, 10, 2100, 
            "booster",
            300, 0, 400,
            "booster"
        )
        self.objects.append(obj)

        obj = Object(
            1800, 10, 2100, 
            "booster",
            300, 0, 400,
            "booster"
        )
        self.objects.append(obj)


    def draw(self, screen, camera, sc_w, sc_h):
        # distanse_to_camera_YZ = math.sqrt(
        #             ((0 - (x["c_point0"]["y"] + x["c_point1"]["y"] + x["c_point2"]["y"]) / 3)**2) + ((0 - (x["c_point0"]["z"] + x["c_point1"]["z"] + x["c_point2"]["z"]) / 3)**2)
        #         )
        
        self.faces = sorted(self.faces, key=lambda x: -math.sqrt(
                    (((x["c_point0"]["x"] + x["c_point1"]["x"] + x["c_point2"]["x"]) / 3)**2) + (((x["c_point0"]["y"] + x["c_point1"]["y"] + x["c_point2"]["y"]) / 3)**2) + (((x["c_point0"]["z"] + x["c_point1"]["z"] + x["c_point2"]["z"]) / 3)**2)
                ))

        for i, face in enumerate(self.faces):
            # print(face[0])
            d_point0 = face["d_point0"]
            d_point1 = face["d_point1"]
            d_point2 = face["d_point2"]

            point0 = face['point0']
            point1 = face['point1']
            point2 = face['point2']


            c_point0 = face['c_point0']
            c_point1 = face['c_point1']
            c_point2 = face['c_point2']

            # dist_x = point0["x"] - point1["x"]
            # if point0['x'] < point1['x']:
            #     dist_x = point1["x"] - point0["x"]

            # dist_z = point0["z"] - point1["z"]
            # if point0['z'] < point1['z']:
            #     dist_z = point1["z"] - point0["z"]

            

            # centerx = (point0["x"] + point1["x"] + point2['x']) / 3
            # centerz = (point0["z"] + point1["z"] + point2['z']) / 3

            
            # # angleRadians_XZ = math.atan2(dist_x, dist_z)
            # # angleDegrees_XZ = angleRadians_XZ * (180 / PI)

            # start_angle = int(180 - 90)
            # end_angle = int(180 + 90)

            # camera_dist_x = -(camera.x + centerx)
            # camera_dist_z = -(camera.z + centerz)
            
            # camera_angleRadians_XZ = math.atan2(camera_dist_x, camera_dist_z)
            # camera_angleDegrees_XZ = camera_angleRadians_XZ * (180 / PI) - 180

            
            # face_centerX = (point0["x"] + point1["x"] + point2["x"]) / 3
            # face_centerZ = (point0["z"] + point1["z"] + point2["z"]) / 3
            # # print(face_centerX)
			
            # distX = 0 - (camera.x + face_centerX)
            # distZ = 0 - (camera.z + face_centerZ)
			




            # angleRadians = math.atan2(distX, distZ)
            # angleDegrees = angleRadians * (180 / PI) + 180

			
            # start_angle = face['face_angle_h'] - 90
            # end_angle = face['face_angle_h'] + 90

            

            # if int(angleDegrees) >= start_angle and int(angleDegrees) <= end_angle:
            #     face_visible_h = True

            # if start_angle < 0:
            #     if int(angleDegrees) >= 360 + start_angle and int(angleDegrees) <= 360:
            #         face_visible_h = True


            # if end_angle > 360:
            #     if int(angleDegrees) >= 0 and int(angleDegrees) <= end_angle - 360:
            #         face_visible_h = True



            # face_centerY = (point0["y"] + point1["y"] + point2["y"]) / 3

            # distY = 0 - (camera.y + face_centerY)


            # angleRadians = math.atan2(distY, distZ)
            # angleDegrees = angleRadians * (180 / PI) + 180

			
            # start_angle = face['face_angle_v'] - 90
            # end_angle = face['face_angle_v'] + 90



            # if int(angleDegrees) >= start_angle and int(angleDegrees) <= end_angle:
            #     face_visible_v = True

            # if start_angle < 0:
            #     if int(angleDegrees) >= 360 + start_angle and int(angleDegrees) <= 360:
            #         face_visible_v = True


            # if end_angle > 360:
            #     if int(angleDegrees) >= 0 and int(angleDegrees) <= end_angle - 360:
            #         face_visible_v = True

            # print(angleDegrees)
            
            face_visible = True

            # behind = False
            # in_area = False

            # if c_point0["z"] < 10 and c_point1["z"] < 10 and c_point2["z"] < 10:
            #     behind = True
            

            # if (d_point0[0] < 1000 or d_point1[0] < 1000 or d_point2[0] < 1000) and (d_point0[0] > 0 or d_point1[0] > 0 or d_point2[0] > 0):
            #     if (d_point0[1] < 600 or d_point1[1] < 600 or d_point2[1] <  600) and (d_point0[1] > 0 or d_point1[1] > 0 or d_point2[1] > 0):
            #         in_area = True
            

            # if in_area and behind ==False:
            #     face_visible = True




            if face_visible:
                    if (d_point0[0] < sc_w or d_point1[0] < sc_w or d_point2[0] < sc_w) and (d_point0[0] > 0 or d_point1[0] > 0 or d_point2[0] > 0):
                        if (d_point0[1] < sc_h or d_point1[1] < sc_h or d_point2[1]< sc_h)  and (d_point0[1] > 0 or d_point1[1] > 0 or d_point2[1] > 0):
                            try:
                            
                                pg.draw.polygon(screen, face['color'], (
                                    d_point0, d_point1, d_point2
                                ))
                            except Exception:
                                pass
                    #     print(d_point0, d_point1, d_point2)

        # for point in self.points:

        #     pg.draw.rect(screen, "red", (point["d_x"], point['d_y'], 5, 5))

        #     text = self.font.render(str(point["ind"]), True, "green")
        #     screen.blit(text, (point['d_x']+10, point['d_y'], 5, 5))

