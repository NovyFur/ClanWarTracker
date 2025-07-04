# Installation Guide - Clan War Tracker

## What's Included

- `clan_war_tracker.py` - Main application file
- `create_executable.bat` - Windows batch file to create .exe
- `requirements.txt` - Python dependencies
- `README.md` - Complete documentation
- `QUICK_START.md` - Quick setup guide
- `INSTALLATION.md` - This file

## Installation Options

### Option A: Create Windows Executable (Recommended)

**Requirements:**
- Windows 10/11
- Python 3.7+ installed with "Add to PATH" checked

**Steps:**
1. Extract all files to a folder
2. Double-click `create_executable.bat`
3. Wait for completion
4. Find `ClanWarTracker.exe` in the `dist` folder
5. Copy the .exe anywhere you want to use it

### Option B: Run with Python

**Requirements:**
- Python 3.7+ installed
- tkinter (usually included with Python)

**Steps:**
1. Extract all files to a folder
2. Open Command Prompt in that folder
3. Run: `python clan_war_tracker.py`

## Verification

After installation, test the application:
1. Add a few test participants
2. Mark some attendance
3. Enter a test prize pool amount
4. Click "Calculate Payouts"
5. Try saving and loading data

## Troubleshooting

**"Python not found" error:**
- Reinstall Python with "Add to PATH" checked
- Restart your computer after installation

**"tkinter not found" error:**
- Reinstall Python with all optional components
- Or run: `pip install tk`

**Application won't start:**
- Right-click the .exe and "Run as administrator"
- Check Windows Defender hasn't quarantined the file

## Support

- Read `README.md` for detailed usage instructions
- Check `QUICK_START.md` for basic setup
- Ensure Python is properly installed if using Option B

## System Requirements

- **OS**: Windows 10/11 (primary), Linux/Mac (with Python)
- **RAM**: 512MB minimum
- **Storage**: 50MB for application files
- **Display**: 800x600 minimum resolution

