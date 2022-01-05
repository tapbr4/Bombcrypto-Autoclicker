# Run after opening your Browser and logging into Metamask !!!

# If you are using Windows Power Toys + Multiple browsers just run the script
# Otherwise, run the following command in Windows Powershell (Without #):
# Start-Process -NoNewWindow python get_pos.py

from pynput import mouse


accounts = 2 #Enter the number of accounts/browsers here
browser = 1 #Just a counter. Keep the value 1!

name_list = [
    'Browser Icon (Taskbar)', 'Address Bar', '"Play Now!" Button', 
    '"Connect Wallet" Button', 'Metamask Icon (Taskbar)', 'Metamask Confirmation', 
    'Treasure Hunt', 'In-game Menu Arrow', 'Heroes Button', 'Character List (center)', 
    'Work Button (All)', 'Rest Button (All)', 'Close Button (Char List)', 
    'Back to Treasure Hunt', 'Back to Main Menu']
lines = []
count = 0

print('Running...')

def on_click(x, y, button, pressed):
    global accounts
    global browser
    global count

    if button == mouse.Button.left and pressed:
        lines.append('{}'.format((x, y)))
        print('[Browser {}] {} at {}'.format(browser, name_list[count], (x, y)))
        count += 1
        
    if count == len(name_list):
        browser += 1
        count = 0

    if browser > accounts:
        with open('config.txt', 'w') as f:
            f.write('\n'.join(lines))

        print('Finished!')
        return False

listener = mouse.Listener(on_click=on_click)
listener.start()
listener.join()