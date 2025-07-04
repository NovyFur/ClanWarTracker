# Clan War Tracker v1.1

A desktop application for tracking 2-week clan wars with participant management, attendance tracking, prize pool distribution, and roster management features.

## New in Version 1.1
- ✅ **Fixed Date Alignment**: Checkboxes now properly align with date headers
- ✅ **Edit Dates Feature**: Modify war period dates with custom date picker
- ✅ **Reset Dates**: Quick reset to start from today's date
- ✅ **Improved Grid Layout**: Better spacing and alignment throughout
- ✅ **Enhanced Scrolling**: Both horizontal and vertical scrolling support

## Features

### Clan War Tracking
- **Participant Management**: Add and remove participants easily
- **14-Day Attendance Grid**: Visual tracking with checkboxes for each day
- **Prize Pool Management**: Enter total prize amount for distribution
- **Automatic Calculations**: Calculate payouts based on attendance
- **Data Persistence**: Save and load war data to/from JSON files
- **Export Results**: Export calculation results to text files

### Roster Management
- **Squad Creation**: Create multiple squads with custom names
- **Member Assignment**: Assign participants to different squads
- **Squad Management**: Rename and delete squads as needed
- **Visual Organization**: Clear display of squad compositions

## Installation and Setup

### Option 1: Run from Source (Recommended)

1. **Install Python 3.7 or higher**
   - Download from [python.org](https://www.python.org/downloads/)
   - Make sure to check "Add Python to PATH" during installation

2. **Download the application files**
   - Download `clan_war_tracker.py` to your desired folder

3. **Install required packages**
   ```bash
   pip install tkinter
   ```
   Note: tkinter usually comes with Python, but if not available, install it.

4. **Run the application**
   ```bash
   python clan_war_tracker.py
   ```

### Option 2: Create Windows Executable

1. **Install PyInstaller**
   ```bash
   pip install pyinstaller
   ```

2. **Create executable**
   ```bash
   pyinstaller --onefile --windowed --name "ClanWarTracker" clan_war_tracker.py
   ```

3. **Find your executable**
   - The executable will be created in the `dist` folder
   - Copy `ClanWarTracker.exe` to your desired location

## How to Use

### Getting Started

1. **Launch the Application**
   - Run the executable or Python script
   - The application opens with two tabs: "Clan War Tracker" and "Roster Manager"

2. **Add Participants**
   - In the "Clan War Tracker" tab, enter participant names in the left panel
   - Click "Add" or press Enter to add each participant
   - Participants will appear in the list below

### Tracking Attendance

1. **View the Attendance Grid**
   - The right panel shows a 14-day grid with your custom dates
   - Each row represents a participant
   - Each column represents a day (showing month/day format)

2. **Manage Dates**
   - Click "Edit Dates" to customize the war period dates
   - Use "Reset to Today" to start fresh from today's date
   - Dates must be in MM/DD/YYYY format

3. **Mark Attendance**
   - Check the boxes for days when participants attend
   - The "Total" column automatically updates with attendance count
   - Changes are saved automatically

### Prize Distribution

1. **Enter Prize Pool**
   - In the left panel, enter the total prize amount in the "Prize Pool Total" field
   - Use numbers only (e.g., 1000 for $1000)

2. **Calculate Payouts**
   - Click "Calculate Payouts" button at the bottom
   - The calculation appears in the results area showing:
     - Total prize pool and attendance days
     - Value per day attended
     - Individual payouts for each participant

3. **Export Results**
   - Click "Export Results" to save calculations to a text file
   - Choose location and filename when prompted

### Managing Rosters

1. **Switch to Roster Manager Tab**
   - Click the "Roster Manager" tab at the top

2. **Create Squads**
   - Enter squad name in the left panel (e.g., "Squad 1", "Alpha Team")
   - Click "Add" to create the squad

3. **Assign Members**
   - Select a squad from the list on the left
   - In the right panel, click "Add to Squad" next to available participants
   - Use "Remove" to take members out of squads

4. **Manage Squads**
   - Select a squad and click "Rename" to change its name
   - Click "Delete" to remove a squad entirely

### Saving and Loading Data

1. **Save Your Work**
   - Click "Save Data" to save all participants, attendance, and squads
   - Choose a location and filename (saves as .json file)

2. **Load Previous Data**
   - Click "Load Data" to restore saved information
   - Select the .json file you previously saved
   - All data will be restored including attendance and squads

## Tips and Best Practices

### Attendance Tracking
- Mark attendance daily for best accuracy
- Double-check attendance before calculating payouts
- Use the export feature to keep records of each war period

### Prize Distribution
- Verify the prize pool amount before calculating
- The system divides the total pool by total attendance days across all participants
- Each participant receives: (their attendance days) × (prize per day)

### Data Management
- Save your data regularly to avoid losing information
- Use descriptive filenames like "ClanWar_Week1_Jan2025.json"
- Keep backup copies of important war data

### Roster Organization
- Create squads based on your clan's structure
- Use clear, descriptive names for squads
- Reassign members as needed for different war strategies

## Troubleshooting

### Application Won't Start
- Ensure Python is installed correctly
- Check that tkinter is available: `python -c "import tkinter"`
- Try running from command line to see error messages

### Display Issues
- The application requires a minimum screen resolution of 800x600
- If text appears cut off, try maximizing the window
- Ensure your system display scaling is set to 100% for best results

### Data Problems
- If attendance checkboxes don't respond, try removing and re-adding the participant
- For calculation errors, verify the prize pool is a valid number
- If save/load fails, check file permissions in the target directory

### Performance
- The application handles up to 50 participants efficiently
- For larger groups, consider splitting into multiple war periods
- Close other applications if the interface becomes slow

## Technical Details

- **Built with**: Python 3.x and tkinter
- **Data Format**: JSON for save files
- **Platform**: Windows (primary), Linux/Mac (with Python installed)
- **Dependencies**: tkinter (usually included with Python)

## Support

For issues or questions:
1. Check this README for common solutions
2. Verify your Python installation is working correctly
3. Ensure all participants are added before marking attendance
4. Try restarting the application if problems persist

## Version History

- **v1.0**: Initial release with core functionality
  - Participant management
  - 14-day attendance tracking
  - Prize pool calculation and distribution
  - Roster management with squads
  - Save/load functionality
  - Export capabilities

