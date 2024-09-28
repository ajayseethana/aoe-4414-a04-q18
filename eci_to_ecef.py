# eci_to_ecef.py
#
# Usage: python3 eci_to_ecef.py year month day hour minute second eci_x_km eci_y_km eci_z_km
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Ajay Seethana
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math
# "constants"
# e.g., R_E_KM = 6378.137

w = 7.292115 * 10 ** -5

# helper functions

## function description
# def calc_something(param1, param2):
#   pass


def jd(year, month, day, hour, minute, second):
    JD1 = day - 32075
    JD2 = 1461 * (year + 4800 + ((month - 14)//12 + 1))//4
    JD3 = 367 * int(month - 2 - ((month-14)//12 + 1) * 12)//12
    JD4 = -3 * ((year + 4900 + ((month - 14)//12 + 1))//100)//4

    JD = JD1 + JD2 + JD3 + JD4
    JD_mid = JD - 0.5
    D_frac = (second + 60 * (minute + 60 * hour))/86400

    return (JD_mid + D_frac)

# initialize script arguments
# arg1 = '' # description of argument 1
# arg2 = '' # description of argument 2
# parse script arguments
if len(sys.argv)==10:
  year = int(sys.argv[1])
  month = int(sys.argv[2])
  day = int(sys.argv[3])
  hour = int(sys.argv[4])
  minute = int(sys.argv[5])
  second = float(sys.argv[6])
  eci_x_km = float(sys.argv[7])
  eci_y_km = float(sys.argv[8])
  eci_z_km = float(sys.argv[9])
  ...
else:
  print(\
   'Usage: '\
   'python3 eci_to_ecef.py year month day hour minute second eci_x_km eci_y_km eci_z_km'\
  )
  exit()

# write script below this line

JD_UT1 = jd(year, month, day, hour, minute, second)
T_UT1 = (JD_UT1 - 2451545.0)/36525
GMST_angle_sec = math.fmod(67310.54841 + (876600 * 60 * 60 + 8640184.812866) * T_UT1 + 0.093104 * T_UT1**2 -6.2 * 10 ** -6 * T_UT1**3, 86400)
if GMST_angle_sec < 0:
    GMST_angle_sec += 86400
GMST_angle_rad = GMST_angle_sec * w
angle = -1 * GMST_angle_rad

c = math.cos(angle)
s = math.sin(angle)

ecef_x_km = c*eci_x_km - s*eci_y_km
ecef_y_km = s*eci_x_km + c*eci_y_km
ecef_z_km = eci_z_km

print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)
