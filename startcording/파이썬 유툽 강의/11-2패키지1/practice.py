# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# a = vietnam.VietnamPackage()
# a.detail()

from travel import *
# a = thailand.ThailandPackage()
# a.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))