from sys import exit
from random import randint
from textwrap import dedent

a = 3
b = 'estoy nivel'
c = 75.8

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)
        


class Engine(object): #debería ser: class Engine(scene_map):

    def __init__(self, scene_map):# inheritance: scene_map.enter ; scene_map.next_scene; scene_map.opening_scene
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)# be sure to print out the last scene
            current_scene.enter()
