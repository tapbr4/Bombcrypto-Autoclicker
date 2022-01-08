# Bombcrypto Autoclicker

!!! Before running any script, make sure your browser is open and Metamask is already logged in. !!!

First time running:

Change the variable called "browsers" to indicate the number of accounts you want to activate the autoclicker on.
Variable "browsers" at (Line 8 - main.py) and (Line 10 - get_pos.py).

Run the script named "get_pos.py" using the following command (Windows):

" Start-Process -NoNewWindow python get_pos.py "

Then, start the click routine in the following order:

1.Browser Icon (Taskbar)

2.Address Bar

3.Write the url "https://bombcrypto.io/" using the keyboard only (No additional clicks)

4."Play Now!" button

5."Connect Wallet" Button

6.Metamask Icon (Taskbar) - !!! Use alt+tab to return the window if clicking it minimized it !!!

7.Metamask Confirmation

8.Treasure Hunt

9.In-game Menu (Arrow)

10.Heroes Button

11.Center of character list (only to select frame and then scroll)

12.Work Button (All)

13.Rest Button (All)

14.Close Button (Char List)

15.Back to Treasure Hunt (Click once in the middle of the map)

16.Back to Main Menu (Green arrow in the upper left corner)


After finishing this process, a file called "config.txt" will be generated with the coordinates in this order.

Run the script called "main.py" and avoid using the computer while it is running. The autoclicker will be farming for you on a frequency of 2 hours (1h farming and 1h resting).

!!! The coordinate capture process does not need to be done in the next runs. Just start "main.py" !!!
