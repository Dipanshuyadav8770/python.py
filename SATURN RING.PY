import math 
import time
import os
WIDTH = 100
HEIGHT = 35
def draw_saturn(angle):
    output = []

    for y in range(-HEIGHT, HEIGHT):
        line = "" 

        for x in range(-WIDTH, WIDTH):
            a = x / 65
            b = y / 35


            d = a*a + b*b
            z =  math.sqrt(max(0, 0.55 - d))

      
            rx = a * math.cos(angle) + b * math.sin(angle)
            ry = (a * math.sin(angle)) + b * math.cos(angle) / 0.28

            r = math.sqrt(rx*rx + ry*ry)

            ring = 1.05 < r < 2.0

            char = " "
            color = (0, 0 , 0)

        if ring and b < 0:
            shade = int(130 +40*math.sin(r*12 + angle))
            char = "=-~*"[int(r*3) %  4]
            color = (shade, shade*0.8, shade*0.5)

        if d < 0.55:
            light = max(0, (0.8*a - 0.5*b + z))
            shade = min(255, int(70 + light*120))
            chars = " .:-=+*#%@"
            index = min(9, int(shade / 26))
            char = chars[index]
            color = (shade, int(shade*0.75), int(shade*0.5))

            line += (f"\033[38;2;{color[0]};"
                     f"{color[1]};{color[2]} m{char}"  
                     )
            output.append(line)
        return "\n". join(output)
try:
    angle = 0

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\033[1;36m   SATURN - MATHEMATICAL ANIMATION\033[0m")
        print(draw_saturn(angle))
        angle += 0.08
        time.sleep(0.08)

except KeyboardInterrupt:
    print("\nAnimation stopped!")


            