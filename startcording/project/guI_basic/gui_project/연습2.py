import time
from PIL import ImageGrab

time.sleep(5)

for i in range(0, 10):
    img = ImageGrab.grab()
    img.save()