from enum import Enum
import math
from decimal import Decimal, ROUND_HALF_UP

class COLOR_NAMES(Enum):
    R = 'Red'
    RO = 'Red Orange'
    O = 'Orange'
    YO = 'Yellow Orange'
    Y = 'Yellow'
    YG = 'Yellow Green'
    G = 'Green'
    BG = 'Blue Green'
    B = 'Blue'
    DB = 'Dark Blue'
    DeB = 'Deep Blue'
    BV = 'Blue Violet'
    V = 'Violet'
    RV = 'Red Violet'
    GREY = 'Grey'

def get_hue_from_RGB(rgb):
    hue = 0
    mx = max(rgb)
    mn = min(rgb)
    [r, g, b] = rgb

    if (r == mx):
      hue = 60 * ((g - b) / (mx - mn))

    elif (g == mx):
      hue = 60 * ((b - r) / (mx - mn)) + 120
    elif(b == mx):
      hue = 60 * ((r - g) / (mx - mn)) + 240

    if (hue > 360):
      hue %= 360

    if (hue < 0):
      hue += 360

    return int(Decimal(str(hue)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

def get_RGB_from_hex(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

def get_RGB_from_color_code(color_code):
    hex = color_code.lstrip('#')
    return get_RGB_from_hex(hex)


def get_color_name_from_RGB(rgb):
    [r, g, b] = rgb

    if(r + g + b == r*3):
        return COLOR_NAMES.GREY

    hue = get_hue_from_RGB(rgb)

    return get_name_from_hue(hue)

def get_name_from_hue(hue):
    if 0 <= hue <= 30:
        return COLOR_NAMES.R
    elif 30 < hue <= 60:
        return COLOR_NAMES.O
    elif 60 < hue <= 90:
        return COLOR_NAMES.Y
    elif 90 < hue <= 120:
        return COLOR_NAMES.YG
    elif 120 < hue <= 150:
        return COLOR_NAMES.G
    elif 150 < hue <= 180:
        return COLOR_NAMES.BG
    elif 180 <= hue <= 210:
        return COLOR_NAMES.B
    elif 210 < hue <= 240:
        return COLOR_NAMES.DB
    elif 240 < hue <= 270:
        return COLOR_NAMES.DeB
    elif 270 < hue <= 300:
        return COLOR_NAMES.BV
    elif 300 < hue <= 330:
        return COLOR_NAMES.V
    elif 330 < hue <= 360:
        return COLOR_NAMES.RV

def is_similer_RGB(rgb1, rgb2, rng=10):
    [r1, g1, b1] = rgb1
    [r2, g2, b2] = rgb2

    return in_range(r1, r2, rng) and in_range(g1, g2, rng) and in_range(b1, b2, rng)

def is_grey_RGB(self, rgb, rng=10):
    [r, g, b] = rgb
    avarage = sum(rgb) / len(rgb)

    return in_range(avarage, r, rng) and in_range(avarage, g, rng) and in_range(avarage, b, rng)

def in_range(num1, num2, rng):
    num1Exist = not num1 and not (num1 == 0)
    num2Exist = not num2 and not (num2 == 0)

    if (not num1Exist and num2Exist):
        return False
    if (num1Exist and not num2Exist):
        return False
    if (num1 == num2):
        return True

    diff = num1 - num2

    abst = abs(diff)
    return abst <= rng

def get_RGB_from_hue(hue):
    """
    get RGB params(ex. [255,255,255]) from hue degree.
    """
    mx = 255
    r, g, b = 0, 0, 0

    if hue is None or hue < 0:
      raise TypeError('invalid value')

    if 0 <= hue <= 60:
      r = mx
      g = math.floor(hue / 60 * mx)
    elif 60 < hue <= 120:
      r = math.floor((120 - hue) / 60 * mx)
      g = mx
    elif 120 < hue <= 180:
      g = mx
      b = math.floor((hue - 120) / 60 * mx)
    elif 180 < hue <= 240:
      g = math.floor((240 - hue) / 60 * mx)
      b = mx
    elif 240 < hue <= 300:
      r = math.floor((hue - 240) / 60 * mx)
      b = mx
    elif 300 < hue <= 360:
      r = mx
      b = math.floor((360 - hue) / 60 * mx)

    [r, g, b] = map(lambda n: n if 0 <= n <= 255 else 0, [r, g, b])

    return [r, g, b]

def get_RGB_from_hue(hue):
    """
    get RGB params(ex. [255,255,255]) from hue degree.
    """
    mx = 255
    r, g, b = 0, 0, 0

    if hue is None or hue < 0:
      raise TypeError('invalid value')

    if 0 <= hue <= 60:
      r = mx
      g = math.floor(hue / 60 * mx)
    elif 60 < hue <= 120:
      r = math.floor((120 - hue) / 60 * mx)
      g = mx
    elif 120 < hue <= 180:
      g = mx
      b = math.floor((hue - 120) / 60 * mx)
    elif 180 < hue <= 240:
      g = math.floor((240 - hue) / 60 * mx)
      b = mx
    elif 240 < hue <= 300:
      r = math.floor((hue - 240) / 60 * mx)
      b = mx
    elif 300 < hue <= 360:
      r = mx
      b = math.floor((360 - hue) / 60 * mx)

    [r, g, b] = map(lambda n: n if 0 <= n <= 255 else 0, [r, g, b])

    return [r, g, b]