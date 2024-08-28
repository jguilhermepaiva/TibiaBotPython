import pyautogui as pg
import keyboard

REGION_BATTLE = (1745, 457, 174, 62)

def check_battle():
    return pg.locateOnScreen('./imgs/region_battle.png', region=REGION_BATTLE)

def kill_monsters():
    while True:
        keyboard.wait('h')
        is_battle = check_battle()
        if is_battle == None:
            pg.press('space')
            while pg.locateOnScreen('./imgs/red_target.png', confidence=0.8, region=REGION_BATTLE) != None:
                print('Esperando monstro morrer')
            print('Procurando outro monstro')
        print(is_battle)

kill_monsters()