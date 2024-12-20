from object import Object
import math
import pygame as pg
from numba import njit
from functools import lru_cache
from bullet import Bullet
from client import client

PI = 3.141592
from threading import Thread


class Camera:
    def __init__(self, sc_w, sc_h) -> None:
        self.x = 0
        self.y = -2000
        self.z = 0

        self.screen_w, self.screen_h = sc_w, sc_h

        self.camera_angle_y = 0
        self.camera_angle_x = 0

        self.move_speed = 14
        self.updown_speed = 13

        self.mx = 0
        self.my = 0
        self.mz = 0

        self.gravity = 0
        self.grounded = False

        self.sprint = False

        self.fov = 100
        self.fov_horizontal = (40 + self.fov) * (PI / 180)
        self.f_h = (self.screen_w / 2) / math.tan(self.fov_horizontal / 2)
        self.f_v = (self.screen_w / 2) / math.tan(self.fov_horizontal / 2)
        self.draw_points = []
        self.draw_faces = []
        self.objects = []
        self.players = []

        self.sc_w, self.sc_h = 0, 0

    def projection(self):
        self.fov_horizontal = (40 + self.fov) * (PI / 180)
        self.f_h = (self.screen_w / 2) / math.tan(self.fov_horizontal / 2)
        self.f_v = (self.screen_w / 2) / math.tan(self.fov_horizontal / 2)


        for obj in self.objects:

            # if obj.type == "bullet":
            #     obj.update()
            obj_points = []
            for i, point in enumerate(obj.points):

                world_x = point["x"]
                world_y = point["y"]
                world_z = point["z"]


                x = point["x"] + self.x
                y = point["y"] + self.y
                z = point["z"] + self.z

                
                

                dist_x = 0 - x
                dist_y = 0 - y
                dist_z = 0 - z

                distanse_to_camera_XZ = math.sqrt(
                    ((0 - x)**2) + ((0 - z)**2)
                )
                
                angleRadians_XZ = math.atan2(dist_x, dist_z)
                angleDegrees_XZ = angleRadians_XZ * (180 / PI)
                
                x = math.cos(math.radians(angleDegrees_XZ + self.camera_angle_y - 90)) * distanse_to_camera_XZ + 0
                z = math.sin(math.radians(angleDegrees_XZ + self.camera_angle_y - 90)) * distanse_to_camera_XZ + 0


                dist_x = 0 - x
                dist_y = 0 - y
                dist_z = 0 - z

                distanse_to_camera_YZ = math.sqrt(
                    ((0 - y)**2) + ((0 - z)**2)
                )

                angleRadians_YZ = math.atan2(dist_y, dist_z)
                angleDegrees_YZ = angleRadians_YZ * (180 / PI)

                y = math.cos(math.radians(angleDegrees_YZ + self.camera_angle_x - 90)) * distanse_to_camera_YZ + 0
                z = math.sin(math.radians(angleDegrees_YZ + self.camera_angle_x - 90)) * distanse_to_camera_YZ + 0
                
                c_x = x
                c_y = y
                c_z = z
            

                draw_x0: int
                draw_y0: int
                draw_x0 = int(self.sc_w / 2 + (x * self.f_h) / (z + 2))
                draw_y0 = int(self.sc_h / 2 + (y * self.f_v) / (z + 2))
                # draw_x0 = int(sc_w/2 + (x *  self.f_h) / (z))
                # draw_y0 = int(sc_h/2 + (y *  self.f_v) / (z))
    
                if z == 0:
                    draw_x0 = int(self.sc_w/2 + (x *  self.f_h) / 5)
                    draw_y0 = int(self.sc_h/2 + (y *  self.f_v) / 5)
                # WindowSizeX / 2 + (vertex.x * FOV) / (FOV + vertex.z) * 100, WindowSizeY / 2 + (vertex.y * FOV) / (FOV + vertex.z) * 100
                
                if z < 0:
                    draw_x0 = int(self.sc_w / 2 + ((x * self.f_h) * (-z)) / math.sqrt(-z * 1000))
                    draw_y0 = int(self.sc_h / 2 + ((y * self.f_v) * (-z)) / math.sqrt(-z * 1000))


                    # draw_x0 = int(sc_w / 2 + ((x * self.f_h) * (-z + 1))/ math.sqrt(-z * 2000))
                    # draw_y0 = int(sc_h / 2 + ((y * self.f_v) * (-z + 1))/ math.sqrt(-z * 2000))

                    # draw_x0 = int(sc_w/2 + (((x *  self.f_h) * (-z / math.sqrt(-z * 500)))))
                    # draw_y0 = int(sc_h/2 + (((y *  self.f_v) * (-z / math.sqrt(-z * 500)))))
                    

                self.draw_points.append(
                    {
                        "d_x":draw_x0, "d_y":draw_y0, 
                        "ind": i
                    }
                )

                obj_points.append(
                    {
                        "d_x":draw_x0, "d_y":draw_y0, 
                        "x":world_x, "y":world_y, "z":world_z, 
                        "c_x":c_x, "c_y":c_y, "c_z":c_z, 

                        "ind":i
                    }
                )
            
            for face in obj.faces:
                point0 = obj_points[face["ind0"]]
                point1 = obj_points[face["ind1"]]
                point2 = obj_points[face["ind2"]]

                if point0["c_z"] > 10 or point1["c_z"] > 10 or point2["c_z"] > 10:
                    self.draw_faces.append({
                        "d_point0":(point0["d_x"], point0["d_y"]), 
                        "d_point1":(point1["d_x"], point1["d_y"]), 
                        "d_point2":(point2["d_x"], point2["d_y"]), 

                        "point0":{
                            "x":point0['x'], "y":point0['y'], "z":point0['z']
                        },
                        "point1":{
                            "x":point1['x'], "y":point1['y'], "z":point1['z']
                        },
                        "point2":{
                            "x":point2['x'], "y":point2['y'], "z":point2['z']
                        },




                        "c_point0":{
                            "x":point0['c_x'], "y":point0['c_y'], "z":point0['c_z']
                        },
                        "c_point1":{
                            "x":point1['c_x'], "y":point1['c_y'], "z":point1['c_z']
                        },
                        "c_point2":{
                            "x":point2['c_x'], "y":point2['c_y'], "z":point2['c_z']
                        },
                        "color":face["color"],
                        "face_angle_h":face['face_angle_h'],
                        "face_angle_v":face['face_angle_v']
                    })

        
        self.players = []
        
        # print(client.players)
        for plr in client.players:
            new_plr = Object(
                -int(plr["x"]), -int(plr["y"]) - 150, -int(plr["z"]), 
                "player",
                100, 250, 200
            )
            self.players.append(new_plr)


        for obj in self.players:

            # if obj.type == "bullet":
            #     obj.update()
            obj_points = []
            for i, point in enumerate(obj.points):

                world_x = point["x"]
                world_y = point["y"]
                world_z = point["z"]


                x = point["x"] + self.x
                y = point["y"] + self.y
                z = point["z"] + self.z

                
                

                dist_x = 0 - x
                dist_y = 0 - y
                dist_z = 0 - z

                distanse_to_camera_XZ = math.sqrt(
                    ((0 - x)**2) + ((0 - z)**2)
                )
                
                angleRadians_XZ = math.atan2(dist_x, dist_z)
                angleDegrees_XZ = angleRadians_XZ * (180 / PI)
                
                x = math.cos(math.radians(angleDegrees_XZ + self.camera_angle_y - 90)) * distanse_to_camera_XZ + 0
                z = math.sin(math.radians(angleDegrees_XZ + self.camera_angle_y - 90)) * distanse_to_camera_XZ + 0


                dist_x = 0 - x
                dist_y = 0 - y
                dist_z = 0 - z

                distanse_to_camera_YZ = math.sqrt(
                    ((0 - y)**2) + ((0 - z)**2)
                )

                angleRadians_YZ = math.atan2(dist_y, dist_z)
                angleDegrees_YZ = angleRadians_YZ * (180 / PI)

                y = math.cos(math.radians(angleDegrees_YZ + self.camera_angle_x - 90)) * distanse_to_camera_YZ + 0
                z = math.sin(math.radians(angleDegrees_YZ + self.camera_angle_x - 90)) * distanse_to_camera_YZ + 0
                
                c_x = x
                c_y = y
                c_z = z
            

                draw_x0: int
                draw_y0: int
                draw_x0 = int(self.sc_w / 2 + (x * self.f_h) / (z + 2))
                draw_y0 = int(self.sc_h / 2 + (y * self.f_v) / (z + 2))
                # draw_x0 = int(sc_w/2 + (x *  self.f_h) / (z))
                # draw_y0 = int(sc_h/2 + (y *  self.f_v) / (z))
    
                if z == 0:
                    draw_x0 = int(self.sc_w/2 + (x *  self.f_h) / 5)
                    draw_y0 = int(self.sc_h/2 + (y *  self.f_v) / 5)
                # WindowSizeX / 2 + (vertex.x * FOV) / (FOV + vertex.z) * 100, WindowSizeY / 2 + (vertex.y * FOV) / (FOV + vertex.z) * 100
                
                if z < 0:
                    draw_x0 = int(self.sc_w / 2 + ((x * self.f_h) * (-z)) / math.sqrt(-z * 1000))
                    draw_y0 = int(self.sc_h / 2 + ((y * self.f_v) * (-z)) / math.sqrt(-z * 1000))


                    # draw_x0 = int(sc_w / 2 + ((x * self.f_h) * (-z + 1))/ math.sqrt(-z * 2000))
                    # draw_y0 = int(sc_h / 2 + ((y * self.f_v) * (-z + 1))/ math.sqrt(-z * 2000))

                    # draw_x0 = int(sc_w/2 + (((x *  self.f_h) * (-z / math.sqrt(-z * 500)))))
                    # draw_y0 = int(sc_h/2 + (((y *  self.f_v) * (-z / math.sqrt(-z * 500)))))
                    

                self.draw_points.append(
                    {
                        "d_x":draw_x0, "d_y":draw_y0, 
                        "ind": i
                    }
                )

                obj_points.append(
                    {
                        "d_x":draw_x0, "d_y":draw_y0, 
                        "x":world_x, "y":world_y, "z":world_z, 
                        "c_x":c_x, "c_y":c_y, "c_z":c_z, 

                        "ind":i
                    }
                )
            
            for face in obj.faces:
                point0 = obj_points[face["ind0"]]
                point1 = obj_points[face["ind1"]]
                point2 = obj_points[face["ind2"]]

                if point0["c_z"] > 10 or point1["c_z"] > 10 or point2["c_z"] > 10:
                    self.draw_faces.append({
                        "d_point0":(point0["d_x"], point0["d_y"]), 
                        "d_point1":(point1["d_x"], point1["d_y"]), 
                        "d_point2":(point2["d_x"], point2["d_y"]), 

                        "point0":{
                            "x":point0['x'], "y":point0['y'], "z":point0['z']
                        },
                        "point1":{
                            "x":point1['x'], "y":point1['y'], "z":point1['z']
                        },
                        "point2":{
                            "x":point2['x'], "y":point2['y'], "z":point2['z']
                        },




                        "c_point0":{
                            "x":point0['c_x'], "y":point0['c_y'], "z":point0['c_z']
                        },
                        "c_point1":{
                            "x":point1['c_x'], "y":point1['c_y'], "z":point1['c_z']
                        },
                        "c_point2":{
                            "x":point2['c_x'], "y":point2['c_y'], "z":point2['c_z']
                        },
                        "color":face["color"],
                        "face_angle_h":face['face_angle_h'],
                        "face_angle_v":face['face_angle_v']
                    })
    def camera_view(self, objects, sc_w, sc_h):
        self.draw_points = []
        self.draw_faces = []
        self.objects = objects

        self.sc_w = sc_w
        self.sc_h = sc_h
        self.projection()
        return (self.draw_faces, self.draw_points)


    def controls(self, sc_w, sc_h, objects, dt):
        key = pg.key.get_pressed()
        mrel = pg.mouse.get_rel()
        mpos = pg.mouse.get_pos()
        mb = pg.mouse.get_pressed()

        if dt == 0:
            dt = 1
        self.mx = 0
        self.my = 0
        self.mz = 0

        self.camera_angle_y += mrel[0]
        self.camera_angle_x += mrel[1]

        if self.camera_angle_x < -90:
            self.camera_angle_x = -90

        if self.camera_angle_x > 90:
            self.camera_angle_x = 90

        if mpos[0] < 10:
            pg.mouse.set_pos(sc_w/2, sc_h/2)

        if mpos[0] > sc_w - 10:
            pg.mouse.set_pos(sc_w/2, sc_h/2)

        if mpos[1] < 10:
            pg.mouse.set_pos(sc_w/2, sc_h/2)

        if mpos[1] > sc_h - 10:
            pg.mouse.set_pos(sc_w/2, sc_h/2)
        
        if key[pg.K_SPACE]:
            if self.grounded:
                self.gravity = 30
                self.grounded = False
        
        if key[pg.K_c]:
            try:
                client.send_data("close_server")
            except Exception:
                pass
            
        # if mb[0]:
            # new_bullet = Bullet(
            #     self.x, self.y + 50, self.z,
            #     self.camera_angle_y,
            #     self.camera_angle_x,
            #     "bullet",
            #     1
            # )

            # new_bullet.rotate_y(self.camera_angle_y)
            # new_bullet.rotate_x(self.camera_angle_x)

            # objects.append(new_bullet)

        if key[pg.K_LSHIFT]:
            self.sprint = True

        if key[pg.K_ESCAPE]:
            quit()

        # if mb[0]:
        #     if mpos[1] < 300:
        #         self.z += 2 * math.sin(math.radians(self.camera_angle_y - 90))/dt
        #         self.x += 2 * math.cos(math.radians(self.camera_angle_y - 90))/dt
        #     else:
        #         self.z -= 2 * math.sin(math.radians(self.camera_angle_y - 90))/dt
        #         self.x -= 2 * math.cos(math.radians(self.camera_angle_y - 90))/dt

        if self.sprint and key[pg.K_w]:
            self.move_speed = 25
            if self.fov < 110:
                self.fov += 4 / dt
                if self.fov > 110:
                    self.fov = 110
        else:
            self.move_speed = 14
            if self.fov > 90:
                self.fov -= 4 / dt
                if self.fov < 90:
                    self.fov = 90

        if key[pg.K_w]:
            # th = Thread(target=client.send_pos, args=(self.x, self.y, self.z))
            # th.start()
            # client.send_pos(self.x, self.y, self.z)
            self.mz += self.move_speed * math.sin(math.radians(self.camera_angle_y - 90))/dt
            self.mx += self.move_speed * math.cos(math.radians(self.camera_angle_y - 90))/dt
        else:
            self.sprint = False
            

        if key[pg.K_s]:
            self.mz -= self.move_speed * math.sin(math.radians(self.camera_angle_y - 90))/dt
            self.mx -= self.move_speed * math.cos(math.radians(self.camera_angle_y - 90))/dt

        if key[pg.K_a]:
            self.mz -= self.move_speed * math.sin(math.radians(self.camera_angle_y))/dt
            self.mx -= self.move_speed* math.cos(math.radians(self.camera_angle_y))/dt

        if key[pg.K_d]:
            self.mz += self.move_speed * math.sin(math.radians(self.camera_angle_y))/dt
            self.mx += self.move_speed * math.cos(math.radians(self.camera_angle_y))/dt



    def collide(self, obj: Object):
        if obj.collider == "box":
            x_collide = False
            y_collide = False
            z_collide = False

            x_offset = self.mx - 1
            if self.mx > 0:
                x_offset = self.mx + 1
            
            if -self.x + 100 - x_offset > obj.x and -self.x - 100 - x_offset < obj.x + obj.w:
                x_collide = True

            if -self.y + 120 > obj.y and -self.y - 140 < obj.y + obj.h:
                y_collide = True

            if -self.z + 100 > obj.z and -self.z - 0 < obj.z + obj.l:
                z_collide = True

            if x_collide and y_collide and z_collide:
                self.mx = 0


            x_collide = False
            y_collide = False
            z_collide = False

            z_offset = self.mz - 1
            if self.mz > 0:
                z_offset = self.mz + 1
            
            if -self.x + 100 > obj.x and -self.x - 100 < obj.x + obj.w:
                x_collide = True

            if -self.y + 120 > obj.y and -self.y - 140 < obj.y + obj.h:
                y_collide = True

            if -self.z + 100 - z_offset > obj.z and -self.z - 0 - z_offset < obj.z + obj.l:
                z_collide = True

            if x_collide and y_collide and z_collide:
                self.mz = 0


            x_collide = False
            y_collide = False
            z_collide = False

            y_offset = self.my - 1
            if self.my > 0:
                y_offset = self.my + 1
            
            if -self.x + 100 > obj.x and -self.x - 100 < obj.x + obj.w:
                x_collide = True

            if -self.y + 120 + y_offset > obj.y and -self.y - 140 + y_offset < obj.y + obj.h:
                y_collide = True

            if -self.z + 100 > obj.z and -self.z - 0 < obj.z + obj.l:
                z_collide = True

            if x_collide and y_collide and z_collide:
                self.my = 0
                self.gravity = 0
                self.grounded = True


        if obj.collider == "booster":
            x_collide = False
            y_collide = False
            z_collide = False

            y_offset = self.my - 1
            if self.my > 0:
                y_offset = self.my + 1
            
            if -self.x + 100 > obj.x and -self.x - 100 < obj.x + obj.w:
                x_collide = True

            if -self.y + 120 + y_offset > obj.y and -self.y - 140 + y_offset < obj.y + obj.h:
                y_collide = True

            if -self.z + 100 > obj.z and -self.z - 0 < obj.z + obj.l:
                z_collide = True

            if x_collide and y_collide and z_collide:
                self.gravity = 150
                self.grounded = False




    def collisions(self, objects, dt):

        if self.gravity > -60:
            if dt != 0:
                self.gravity -= 1.5 / dt 

        self.my = self.gravity


        for obj in objects:
            # if obj.y <= self.y + 200:
            #     self.gravity = 0
            #     self.my = 0
            # if obj.collider == "box":
            self.collide(obj)
                # self.mz = 0
            # else:
            #     print(2)


        self.x += self.mx
        self.y -= self.my / dt
        self.z += self.mz