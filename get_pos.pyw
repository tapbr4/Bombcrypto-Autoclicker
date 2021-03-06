# Run after opening your Browser and logging into Metamask !!!

# If you are using Windows Power Toys + Multiple browsers just run the script
# Otherwise, run the following command in Windows Powershell (Without #):
# Start-Process -NoNewWindow python get_pos.py

from plyer import notification
from pynput import mouse
from pyautogui import alert, confirm

title = 'Bombcrypto Autoclicker'
browsers = 2 #Enter the number of accounts/browsers here
browser = 1 #Just a counter. Keep the value 1!

name_list = [
    'Browser Icon (Taskbar)', 'Address Bar', 
    '"Connect Wallet" Button', 'Login Metamask',
    'Metamask Icon (Taskbar)', 'Metamask Confirmation', 
    'Treasure Hunt', 'In-game Menu Arrow', 'Heroes Button', 'Character List (center)', 
    'Work Button (All)', 'Rest Button (All)', 'Close Button (Char List)', 
    'Back to Treasure Hunt', 'Back to Main Menu']
lines = []
count = 0

start = confirm(title=title, text='Start capturing positions?',
                buttons=['OK','Cancel'])
print(start)



def on_click(x, y, button, pressed):
    global browsers
    global browser
    global count

    if button == mouse.Button.left and pressed:
        lines.append('{}'.format((x, y)))
        
        #'[Browser {}] {} at {}'.format(browser, name_list[count], (x, y))
        
        count += 1
        
    if count == len(name_list):
        message = '[Browser {}] Finished'.format(browser)
        notification.notify(title=title,
                            message=message,
                            timeout=1)
        browser += 1
        count = 0

    if browser > browsers:
        with open('config.txt', 'w') as f:
            f.write('\n'.join(lines))
        return False

if(start=='OK'):
    listener = mouse.Listener(on_click=on_click)
    listener.start()
    listener.join()
else:
    quit()

alert(title=title, text='Finished!', button='OK')
