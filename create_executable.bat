@echo off
echo Clan War Tracker - Creating Windows Executable
echo ===============================================
echo.

echo Installing PyInstaller...
pip install pyinstaller

echo.
echo Creating executable...
pyinstaller --onefile --windowed --name "ClanWarTracker" clan_war_tracker.py

echo.
echo Executable created successfully!
echo You can find ClanWarTracker.exe in the 'dist' folder.
echo.
pause

