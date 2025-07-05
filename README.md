# Clan War Tracker v1.2 - Enhanced Edition

A powerful desktop application for tracking 2-week clan wars with advanced prize distribution, participant management, and roster organization.

## 🆕 What's New in Version 1.2

### 🏆 Prize Picker System
- **Ranked Prize Distribution**: Set specific amounts for 1st, 2nd, 3rd place, etc.
- **Customizable Prize Structure**: Modify any prize amount (e.g., 1st place: $400,000)
- **Dynamic Ranking**: Add or remove prize ranks as needed
- **Automatic Participant Ranking**: Based on attendance days with tie handling

### 🎨 Enhanced User Interface
- **Modern Design**: Contemporary styling with improved colors and typography
- **Better Scrollbars**: More visible and easier-to-use scrollbars throughout
- **Resizable Sections**: Drag dividers to customize your workspace layout
- **Visual Icons**: Emoji icons for better navigation and visual appeal

### 📏 Flexible Layout
- **Expandable Panels**: Resize participant, prize, and attendance sections
- **Customizable Workspace**: Adjust panel sizes to your preferences
- **Responsive Design**: Better handling of different screen sizes

## Core Features

### Clan War Tracking
- **Participant Management**: Add/remove participants with enhanced interface
- **14-Day Attendance Grid**: Visual tracking with properly aligned checkboxes
- **Dual Prize Modes**: Choose between equal distribution or ranked prizes
- **Advanced Calculations**: Detailed payout calculations with rankings
- **Data Persistence**: Save/load with support for new prize features

### Prize Distribution Modes

#### Equal Distribution Mode
- Enter total prize pool amount
- Automatic division based on attendance days
- Fair distribution: (Total Pool ÷ Total Attendance Days) × Individual Days

#### Ranked Prize Mode
- Set specific amounts for each rank (1st, 2nd, 3rd, etc.)
- Participants automatically ranked by attendance
- Customizable prize structure with add/remove ranks
- Handles ties appropriately

### Roster Management
- **Squad Creation**: Create multiple squads with custom names
- **Member Assignment**: Drag-and-drop style assignment interface
- **Squad Organization**: Visual management of team compositions
- **Enhanced UI**: Improved styling and layout

## Installation

### Quick Setup (Windows)
1. Download and extract the application files
2. Install Python 3.7+ (if not already installed)
3. Double-click `create_executable.bat` to create ClanWarTracker.exe
4. Run the executable - no Python needed after this step!

### Run with Python
```bash
python clan_war_tracker.py
```

## How to Use

### Setting Up Prize Distribution

#### For Equal Distribution:
1. Select "Equal Distribution" in Prize Management
2. Enter total prize pool amount
3. Calculate payouts for fair distribution

#### For Ranked Prizes:
1. Select "Ranked Prizes" in Prize Management
2. Modify prize amounts for each rank:
   - 1st Place: $400,000 (default)
   - 2nd Place: $200,000 (default)
   - 3rd Place: $100,000 (default)
   - etc.
3. Use "Add Rank" or "Remove Last" to adjust structure
4. Calculate payouts to see rankings

### Managing Participants
1. **Add Participants**: Enter names in the left panel
2. **Track Attendance**: Check boxes for each day attended
3. **View Rankings**: Participants automatically ranked by attendance
4. **Remove Participants**: Select and remove as needed

### Customizing Layout
- **Resize Panels**: Drag the dividers between sections
- **Horizontal Adjustment**: Change left panel vs. attendance grid width
- **Vertical Adjustment**: Modify participant vs. prize management height
- **Save Layout**: Panel sizes persist during your session

### Enhanced Navigation
- **Mouse Wheel Scrolling**: Scroll vertically in attendance grid
- **Shift + Mouse Wheel**: Scroll horizontally in attendance grid
- **Enhanced Scrollbars**: Click and drag for precise navigation
- **Keyboard Support**: Arrow keys work in all list boxes

## Prize Distribution Examples

### Ranked Prize Example
```
1st Place: John Smith    14 days  $400,000
2nd Place: Jane Doe      13 days  $200,000
3rd Place: Bob Wilson    12 days  $100,000
4th Place: Alice Brown   11 days   $50,000
5th Place: Mike Davis    10 days   $25,000
```

### Equal Distribution Example
```
Total Pool: $1,000,000
Total Attendance: 50 days
Value per Day: $20,000

John Smith:    14 days  $280,000
Jane Doe:      13 days  $260,000
Bob Wilson:    12 days  $240,000
Alice Brown:   11 days  $220,000
```

## Advanced Features

### Data Management
- **Enhanced Save/Load**: Includes prize picker settings
- **Export Results**: Detailed formatting with rankings
- **Backup Support**: JSON format for easy backup and sharing

### Date Management
- **Custom Date Ranges**: Edit any of the 14 war dates
- **Date Validation**: Ensures proper MM/DD/YYYY format
- **Quick Reset**: Reset to start from today's date

### Error Handling
- **Input Validation**: Prevents invalid data entry
- **Tie Handling**: Proper ranking for participants with same attendance
- **Graceful Degradation**: Handles missing or corrupted data

## System Requirements

- **Operating System**: Windows 10/11 (primary), Linux/Mac (with Python)
- **Memory**: 512MB RAM minimum
- **Storage**: 100MB for application and data files
- **Display**: 1200x700 minimum resolution (resizable interface)
- **Python**: 3.7+ (if running from source)

## Tips for Best Results

### Prize Management
- **Plan Your Structure**: Decide on prize distribution before the war
- **Test Calculations**: Use sample data to verify prize amounts
- **Save Regularly**: Keep backups of your prize configurations

### Layout Optimization
- **Adjust for Screen Size**: Resize panels to fit your monitor
- **Participant Focus**: Make participant panel larger for many members
- **Attendance Focus**: Expand attendance grid for detailed tracking

### Data Organization
- **Descriptive Filenames**: Use clear names like "ClanWar_Jan2025_Week1.json"
- **Regular Exports**: Export results after each calculation
- **Backup Strategy**: Keep multiple saves of important war data

## Troubleshooting

### Common Issues
- **Prize Amounts**: Ensure all prize amounts are positive numbers
- **Ranking Ties**: Participants with same attendance get same rank
- **Layout Issues**: Reset panel sizes by restarting the application
- **Scrolling Problems**: Use enhanced scrollbars if mouse wheel doesn't work

### Performance Tips
- **Large Participant Lists**: Use scrolling for 20+ participants
- **Complex Prize Structures**: Limit to reasonable number of ranks
- **Data Files**: Keep individual war files under 10MB for best performance

## Support and Updates

This enhanced version includes all previous features plus the new prize picker system and improved interface. For questions or issues, refer to the CHANGELOG.md for detailed feature descriptions.

## Version History
- **v1.0**: Initial release with basic functionality
- **v1.1**: Fixed date alignment and added date modification
- **v1.2**: Added prize picker system, enhanced GUI, and resizable layout

