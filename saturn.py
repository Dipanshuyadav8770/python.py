import math
import time
import os

WIDTH = 36
HEIGHT = 12

def draw_saturn(angle):
    output = []

    for y in range(-HEIGHT, HEIGHT + 1):
        line = ""

        for x in range(-WIDTH, WIDTH + 1):
            a = x / 22
            b = y / 11

            d = a*a + b*b

            rx = a * math.cos(angle) - b * math.sin(angle)
            ry = (a * math.sin(angle) + b * math.cos(angle)) / 0.32

            r = math.sqrt(rx*rx + ry*ry)

            ring = 1.15 < r < 2.0

            char = " "
            color = (0, 0, 0)

            # Planet
            if d <= 1:
                z = math.sqrt(max(0, 1-d))
                light = max(0, 0.5 + 0.4*z - 0.25*a)
                shade = int(100 + light*130)

                chars = " .:-=+*#%@"
                index = min(9, shade // 26)

                char = chars[index]
                color = (shade, int(shade*0.78),
                         int(shade*0.48))

            # Rings
            if ring and (d > 1 or b > 0.15):
                shade = int(170 + 35*math.sin(r*12 + angle))
                char = "=-~*"[int(r*5) % 4]
                color = (shade, int(shade*0.8),
                         int(shade*0.55))

            line += (
                f"\033[38;2;{color[0]};"
                f"{color[1]};{color[2]}m{char}"
            )

        output.append(line)

    return "\n".join(output)


try:
    angle = 0

    os.system("cls")

    while True:
        print("\033[H", end="")
        print("\033[1;36m   SATURN - PYTHON ANIMATION\033[0m")
        print(draw_saturn(angle))
        print("\033[0m", end="", flush=True)

        angle += 0.08
        time.sleep(0.12)

except KeyboardInterrupt:
    print("\033[0m\nAnimation stopped!")