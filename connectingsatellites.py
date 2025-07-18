import pgzrun,random,pyautogui
WIDTH,HEIGHT = pyautogui.size()
satellite = []
r = random.randint(5,8)
for i in range(r):
    s = Actor("sat.png")
    s.pos = random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
    satellite.append(s)
    




pgzrun.go()