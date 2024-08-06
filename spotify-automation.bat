@echo off
echo %DATE% %TIME% > C:\Users\grazi\projects\spotify-automation\logs\log.txt
echo Running script... >> C:\Users\grazi\projects\spotify-automation\logs\log.txt
"C:\Users\grazi\projects\spotify-automation\venv\Scripts\python.exe" "C:\Users\grazi\projects\spotify-automation\main.py" >> C:\Users\grazi\projects\spotify-automation\logs\log.txt 2>&1
echo Script finished with exit code %ERRORLEVEL% >> C:\Users\grazi\projects\spotify-automation\logs\log.txt