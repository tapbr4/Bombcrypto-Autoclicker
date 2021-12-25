# Command to run in background (Windows Powershell):
# Start-Process -NoNewWindow python get_pos.py
from pynput import mouse


print('Running...')
# After opening your Browser and logging into Metamask
name_list = [
    'Browser Icon (Taskbar)', 'Address Bar', '"Play Now!" Button', 
    '"Connect Wallet" Button', 'Metamask Icon (Taskbar)', 'Metamask Confirmation', 
    'Treasure Hunt', 'In-game Menu Arrow', 'Heroes Button', 'Character List (center)', 
    'Last Work Button', 'First Rest Button', 'Close Button (Char List)', 
    'Back to Treasure Hunt', 'Next Map', 'Back to Main Menu']
lines = []
count = 0

def on_click(x, y, button, pressed):
    global count
    if button == mouse.Button.left and pressed:
        lines.append('{}'.format((x, y)))
        print('{} at {}'.format(name_list[count], (x, y)))
        count += 1
        
    if count == len(name_list):
        with open('config.txt', 'w') as f:
            f.write('\n'.join(lines))
        
        print('Finished!')
        return False

listener = mouse.Listener(on_click=on_click)
listener.start()
listener.join()