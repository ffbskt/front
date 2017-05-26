import pygame.camera
import Image
import numpy as np
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start() #
img = cam.get_image()#
strimg = pygame.image.tostring(img, "RGB")
cam.stop()
pygame.camera.quit()
pil_i = Image.fromstring("RGB",(640,480),strimg)
k=np.reshape(np.array(pil_i.convert('1')), (307200, 1))
"""
def work_camera(n, delay, mass):
    #mass = np.array()
    cam.start()
    for i in range(n):
        img = cam.get_image()
        k = pygame.image.tostring(img, "RGB")
        #k=np.reshape(np.array(img.convert('1')), (307200, 1))
    cam.stop()
    mass.append([k, -1])

#mass = []
#work_camera(1, mass)
"""
print k[:10]

pygame.display.init()
w = 640
h = 480
size=(w,h)
screen = pygame.display.set_mode(size)

img2 = pygame.image.fromstring(strimg, size, "RGB")
#while True:
   # screen.blit(img2,(0,0))
   # pygame.display.flip()