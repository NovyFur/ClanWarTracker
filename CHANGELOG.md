# Clan War Tracker - Changelog

## Version 1.1 - Date Alignment and Modification Update

### Fixed Issues
- **Date Alignment**: Fixed checkbox alignment with date headers in the attendance grid
- **Grid Layout**: Improved grid layout using consistent column configuration
- **Scrolling**: Added both horizontal and vertical scrolling for better navigation
- **Column Sizing**: Set proper minimum column widths for better readability

### New Features
- **Edit Dates**: Added "Edit Dates" button to modify war period dates
- **Date Dialog**: New dialog window for editing all 14 dates individually
- **Reset Dates**: "Reset to Today" button to quickly set dates starting from current date
- **Date Validation**: Proper date format validation (MM/DD/YYYY)
- **Full Date Display**: War dates now show full year (MM/DD/YYYY format)

### Improvements
- **Better Layout**: Improved grid alignment and spacing
- **Enhanced UI**: Added date management section in the main interface
- **Responsive Design**: Better handling of different screen sizes
- **Mouse Wheel Support**: Added mouse wheel scrolling for the attendance grid

### Technical Changes
- Upgraded to version 1.1
- Improved grid layout using proper tkinter grid configuration
- Added DateEditDialog class for date modification
- Enhanced date generation and validation functions
- Better column weight distribution for alignment

### Usage Notes
- Use "Edit Dates" to customize your war period dates
- "Reset to Today" will clear all attendance data and start fresh
- Dates are validated to ensure proper MM/DD/YYYY format
- The grid now properly aligns checkboxes with their corresponding dates

