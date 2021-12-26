from ast import literal_eval as make_tuple
from time import sleep
import pyautogui


# Setup #
name_list = [
    'browser_icon','address_bar',
    'play_now', 'connect_wallet',
    'metamask_icon','metamask_confirm',
    'treasure_hunt','menu_arrow',
    'heroes','character_list',
    'work','rest','close',
    'map','next_map','main_menu']
pos = {}

# Read config.txt #
with open('config.txt') as f:
    lines = f.read().splitlines()

# Dict #
count = 0
for item in lines:
    t_item = make_tuple(item)
    pos[name_list[count]] = t_item
    count += 1

# Auto #
## Opening Browser
pyautogui.click(x=pos['browser_icon'][0], y=pos['browser_icon'][1])
sleep(3)

## Loop
while True:
    print('\n[STARTING LOOP]')
    ## Entering the Website
    pyautogui.click(x=pos['address_bar'][0], y=pos['address_bar'][1])
    sleep(3)
    pyautogui.write('https://bombcrypto.io/')   
    pyautogui.press('enter')
    sleep(3)
    pyautogui.press('enter')
    sleep(6)

    ## Play / Metamask Confirmation
    print('PLAY NOW!')
    pyautogui.click(x=pos['play_now'][0], y=pos['play_now'][1])
    sleep(10)
    pyautogui.hotkey('alt', 'tab')
    sleep(3)
    pyautogui.hotkey('ctrl', 'w')
    sleep(5)
    pyautogui.click(x=pos['connect_wallet'][0], y=pos['connect_wallet'][1])
    sleep(20)
    pyautogui.click(x=pos['metamask_icon'][0], y=pos['metamask_icon'][1], clicks=2, interval=0.25)
    sleep(5)
    pyautogui.click(x=pos['metamask_confirm'][0], y=pos['metamask_confirm'][1])
    sleep(30)

    ## In-game / Work
    print('PUTTING TO WORK')
    pyautogui.click(x=pos['treasure_hunt'][0], y=pos['treasure_hunt'][1])
    sleep(5)
    pyautogui.click(x=pos['map'][0], y=pos['map'][1], clicks=2, interval=0.5)
    sleep(5)
    pyautogui.click(x=pos['menu_arrow'][0], y=pos['menu_arrow'][1])
    sleep(5)
    pyautogui.click(x=pos['heroes'][0], y=pos['heroes'][1])
    sleep(5)
    pyautogui.click(x=pos['character_list'][0], y=pos['character_list'][1])
    sleep(4)
    for i in range(45):
        pyautogui.scroll(-1)
    sleep(8)
    for i in range(16):
        pyautogui.click(x=pos['work'][0], y=pos['work'][1])
        sleep(3)
    sleep(2)
    pyautogui.click(x=pos['close'][0], y=pos['close'][1], clicks=2, interval=1.5)
    sleep(5)

    ## Working 1h (+1minute and 6 seconds)
    ## Click routine to go to the next map and avoid error messages.
    print('1 HOUR FARM')
    pyautogui.click(x=pos['map'][0], y=pos['map'][1], clicks=2, interval=0.5)
    for i in range(60): 
        sleep(15)
        pyautogui.click(x=pos['next_map'][0], y=pos['next_map'][1])
        sleep(10)
        pyautogui.click(x=pos['connect_wallet'][0], y=pos['connect_wallet'][1])
        sleep(15)
        pyautogui.click(x=pos['metamask_icon'][0], y=pos['metamask_icon'][1], clicks=2, interval=0.25)
        sleep(5)
        pyautogui.click(x=pos['metamask_confirm'][0], y=pos['metamask_confirm'][1])
        sleep(15)
        pyautogui.click(x=pos['treasure_hunt'][0], y=pos['treasure_hunt'][1])
        ### Prevents bombers from walking around without placing bombs.
        if(i%5==0 and i!=0): # Runs 11 times. (+1 minute and 6 seconds)
            sleep(3)
            pyautogui.click(x=pos['main_menu'][0], y=pos['main_menu'][1])
            sleep(3)
            pyautogui.click(x=pos['treasure_hunt'][0], y=pos['treasure_hunt'][1])
    sleep(5)

    ## Rest
    print('PUTTING TO REST')
    pyautogui.click(x=pos['menu_arrow'][0], y=pos['menu_arrow'][1])
    sleep(5)
    pyautogui.click(x=pos['heroes'][0], y=pos['heroes'][1])
    sleep(5)
    pyautogui.click(x=pos['character_list'][0], y=pos['character_list'][1])
    sleep(4)
    for i in range(45):
        pyautogui.scroll(1)
    sleep(8)
    for i in range(16):
        pyautogui.click(x=pos['rest'][0], y=pos['rest'][1])
        sleep(3)
    sleep(2)
    pyautogui.click(x=pos['close'][0], y=pos['close'][1], clicks=2, interval=1.5)
    sleep(5)
    pyautogui.click(x=pos['map'][0], y=pos['map'][1], clicks=2, interval=0.5)
    sleep(5)
    
    ## Rest Confirmation
    pyautogui.click(x=pos['main_menu'][0], y=pos['main_menu'][1])
    sleep(5)
    pyautogui.click(x=pos['treasure_hunt'][0], y=pos['treasure_hunt'][1])
    sleep(5)

    ## Close Tab
    pyautogui.hotkey('ctrl', 't')
    sleep(3)
    pyautogui.hotkey('alt', 'tab')
    sleep(2)
    pyautogui.hotkey('ctrl', 'w')

    ## Resting 1h (+1h farm = 2h frequency)
    print('REST 1H')
    sleep(3600) # 1h = 3600s