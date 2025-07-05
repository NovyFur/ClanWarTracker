# Clan War Tracker - Version 1.2 Changelog

## Major New Features

### 🏆 Prize Picker System
- **Ranked Prize Distribution**: New prize mode with customizable ranked payouts
- **Flexible Prize Structure**: Set specific amounts for 1st, 2nd, 3rd place, etc.
- **Editable Prize Amounts**: Modify any prize amount with real-time updates
- **Add/Remove Ranks**: Dynamically add or remove prize ranks as needed
- **Automatic Ranking**: Participants automatically ranked by attendance days
- **Tie Handling**: Proper handling of tied attendance scores

### 🎨 Enhanced GUI Design
- **Modern Visual Style**: Updated with contemporary colors and typography
- **Enhanced Scrollbars**: More visible and easier-to-use scrollbars throughout
- **Improved Icons**: Added emoji icons for better visual navigation
- **Better Typography**: Improved fonts and sizing for readability
- **Card-style Frames**: Modern card-based layout design

### 📏 Expandable/Resizable Sections
- **PanedWindow Layout**: All major sections now resizable
- **Horizontal Panes**: Left/right sections can be resized
- **Vertical Panes**: Top/bottom sections within panels are resizable
- **Flexible Layout**: Customize the interface to your preferences
- **Persistent Sizing**: Pane sizes maintain during session

## Detailed Improvements

### Prize Management
- **Dual Mode System**: Choose between "Equal Distribution" or "Ranked Prizes"
- **Real-time Updates**: Prize changes update immediately
- **Default Prize Structure**: Starts with 5 ranks (400k, 200k, 100k, 50k, 25k)
- **Ordinal Display**: Proper 1st, 2nd, 3rd, 4th formatting
- **Unranked Handling**: Shows participants who don't place in top ranks

### User Interface
- **Enhanced Scrolling**: Both vertical and horizontal scrolling support
- **Better Visual Hierarchy**: Clear section separation and labeling
- **Improved Spacing**: Better padding and margins throughout
- **Color Coding**: Consistent color scheme for better usability
- **Responsive Design**: Better handling of different window sizes

### Functionality
- **Enhanced Calculations**: More detailed calculation displays
- **Better Error Handling**: Improved validation and error messages
- **Save/Load Support**: Prize picker settings saved with data files
- **Export Enhancements**: Better formatted export results

## Technical Improvements

### Code Structure
- **Modular Design**: Better separation of concerns
- **Enhanced Styling**: Comprehensive ttk.Style configuration
- **Improved Layout**: PanedWindow for flexible layouts
- **Better Event Handling**: More responsive user interactions

### Performance
- **Optimized Rendering**: Faster grid updates and redraws
- **Memory Efficiency**: Better resource management
- **Smooth Scrolling**: Enhanced scrolling performance

## Usage Guide

### Using Ranked Prizes
1. Select "Ranked Prizes" in Prize Management
2. Modify prize amounts for each rank as needed
3. Use "Add Rank" or "Remove Last" to adjust structure
4. Calculate payouts to see rankings based on attendance

### Resizing Sections
- **Drag Pane Dividers**: Click and drag the dividers between sections
- **Horizontal Resize**: Adjust left panel vs. attendance grid width
- **Vertical Resize**: Adjust participant vs. prize management height
- **Custom Layout**: Create your preferred workspace layout

### Enhanced Scrolling
- **Mouse Wheel**: Scroll vertically in attendance grid
- **Shift + Mouse Wheel**: Scroll horizontally in attendance grid
- **Scrollbar Dragging**: Use enhanced scrollbars for precise navigation
- **Keyboard Navigation**: Arrow keys work in list boxes

## Compatibility
- **Backward Compatible**: Loads data files from previous versions
- **Forward Compatible**: New features gracefully degrade if not supported
- **Cross-Platform**: Works on Windows, Mac, and Linux with Python/tkinter

## Version History
- **v1.0**: Initial release with basic functionality
- **v1.1**: Fixed date alignment and added date modification
- **v1.2**: Added prize picker system and enhanced GUI

