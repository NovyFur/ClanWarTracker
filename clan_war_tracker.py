#!/usr/bin/env python3
"""
Clan War Tracker - Nex Clan Themed Edition
Version 2.0 - Custom Theme with Gaming Features
Created by Nex Clan
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
from tkinter import font as tkFont
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Any
import calendar

class NexClanTheme:
    """Custom theme colors for Nex Clan"""
    # Main colors
    BLACK = "#0a0a0a"
    DARK_GRAY = "#1a1a1a"
    MEDIUM_GRAY = "#2a2a2a"
    LIGHT_GRAY = "#3a3a3a"
    
    # Flame colors
    FLAME_ORANGE = "#ff6600"
    FLAME_RED = "#cc3300"
    FLAME_YELLOW = "#ffaa00"
    
    # Accent colors
    WHITE = "#ffffff"
    LIGHT_ORANGE = "#ff8833"
    DARK_RED = "#990000"
    
    # Status colors
    SUCCESS = "#00cc66"
    WARNING = "#ffcc00"
    ERROR = "#ff3333"

class ClassIcons:
    """Gaming class icons and names"""
    CLASSES = {
        "sword_shield": {"icon": "🛡️⚔️", "name": "Sword & Shield"},
        "two_handed": {"icon": "⚔️", "name": "Two-Handed Sword"},
        "spear": {"icon": "🔱", "name": "Spear"},
        "dual_axe": {"icon": "🪓🪓", "name": "Dual Axe"},
        "dual_dagger": {"icon": "🗡️🗡️", "name": "Dual Dagger"},
        "war_hammer": {"icon": "🔨", "name": "War Hammer"},
        "bow": {"icon": "🏹", "name": "Bow"},
        "crossbow": {"icon": "🏹", "name": "Crossbow"},
        "staff": {"icon": "🔮", "name": "Staff"},
        "life_staff": {"icon": "✨", "name": "Life Staff"}
    }

class ClanWarTracker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Nex Clan War Tracker v2.0")
        self.root.geometry("1600x900")
        self.root.minsize(1400, 800)
        
        # Set custom theme
        self.setup_custom_theme()
        
        # Application data
        self.participants = []
        self.squads = []
        self.prize_pool = tk.DoubleVar(value=0.0)
        self.war_dates = self.generate_war_dates()
        
        # Prize system data
        self.prize_mode = tk.StringVar(value="equal")
        self.ranked_prizes = []
        
        # UI Variables
        self.participant_vars = {}
        self.date_vars = []
        
        # Auto-reload settings
        self.last_saved_file = None
        self.auto_reload_enabled = tk.BooleanVar(value=True)
        
        # Paned window variables
        self.main_paned = None
        self.prize_paned = None
        
        self.setup_ui()
        self.initialize_ranked_prizes()
        self.check_auto_reload()
        
    def setup_custom_theme(self):
        """Setup custom Nex Clan theme"""
        # Configure root window
        self.root.configure(bg=NexClanTheme.BLACK)
        
        # Create custom style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure custom fonts
        self.title_font = tkFont.Font(family="Arial", size=16, weight="bold")
        self.heading_font = tkFont.Font(family="Arial", size=12, weight="bold")
        self.body_font = tkFont.Font(family="Arial", size=10)
        self.small_font = tkFont.Font(family="Arial", size=9)
        
        # Configure styles
        self.configure_styles()
        
    def configure_styles(self):
        """Configure all custom styles"""
        # Main frame styles
        self.style.configure('Nex.TFrame', 
                           background=NexClanTheme.BLACK,
                           borderwidth=0)
        
        self.style.configure('NexCard.TFrame',
                           background=NexClanTheme.DARK_GRAY,
                           relief='raised',
                           borderwidth=2)
        
        # Label styles
        self.style.configure('NexTitle.TLabel',
                           background=NexClanTheme.BLACK,
                           foreground=NexClanTheme.FLAME_ORANGE,
                           font=self.title_font)
        
        self.style.configure('NexHeading.TLabel',
                           background=NexClanTheme.DARK_GRAY,
                           foreground=NexClanTheme.FLAME_YELLOW,
                           font=self.heading_font)
        
        self.style.configure('NexBody.TLabel',
                           background=NexClanTheme.DARK_GRAY,
                           foreground=NexClanTheme.WHITE,
                           font=self.body_font)
        
        self.style.configure('NexBrand.TLabel',
                           background=NexClanTheme.BLACK,
                           foreground=NexClanTheme.FLAME_RED,
                           font=self.small_font)
        
        # Button styles
        self.style.configure('Nex.TButton',
                           background=NexClanTheme.FLAME_ORANGE,
                           foreground=NexClanTheme.WHITE,
                           borderwidth=0,
                           focuscolor='none',
                           font=self.body_font,
                           padding=(10, 5))
        
        self.style.map('Nex.TButton',
                      background=[('active', NexClanTheme.LIGHT_ORANGE),
                                ('pressed', NexClanTheme.FLAME_RED)])
        
        self.style.configure('NexPrimary.TButton',
                           background=NexClanTheme.FLAME_RED,
                           foreground=NexClanTheme.WHITE,
                           font=self.heading_font,
                           padding=(15, 8))
        
        self.style.map('NexPrimary.TButton',
                      background=[('active', NexClanTheme.DARK_RED),
                                ('pressed', NexClanTheme.FLAME_ORANGE)])
        
        # Entry styles
        self.style.configure('Nex.TEntry',
                           fieldbackground=NexClanTheme.MEDIUM_GRAY,
                           foreground=NexClanTheme.WHITE,
                           borderwidth=1,
                           insertcolor=NexClanTheme.FLAME_ORANGE)
        
        # Notebook styles
        self.style.configure('Nex.TNotebook',
                           background=NexClanTheme.BLACK,
                           borderwidth=0)
        
        self.style.configure('Nex.TNotebook.Tab',
                           background=NexClanTheme.MEDIUM_GRAY,
                           foreground=NexClanTheme.WHITE,
                           padding=[20, 10],
                           font=self.heading_font)
        
        self.style.map('Nex.TNotebook.Tab',
                      background=[('selected', NexClanTheme.FLAME_ORANGE),
                                ('active', NexClanTheme.LIGHT_GRAY)])
        
        # LabelFrame styles
        self.style.configure('Nex.TLabelframe',
                           background=NexClanTheme.DARK_GRAY,
                           foreground=NexClanTheme.FLAME_YELLOW,
                           borderwidth=2,
                           relief='raised')
        
        self.style.configure('Nex.TLabelframe.Label',
                           background=NexClanTheme.DARK_GRAY,
                           foreground=NexClanTheme.FLAME_YELLOW,
                           font=self.heading_font)
        
        # Checkbutton styles
        self.style.configure('Nex.TCheckbutton',
                           background=NexClanTheme.DARK_GRAY,
                           foreground=NexClanTheme.WHITE,
                           focuscolor='none')
        
        # Radiobutton styles
        self.style.configure('Nex.TRadiobutton',
                           background=NexClanTheme.DARK_GRAY,
                           foreground=NexClanTheme.WHITE,
                           focuscolor='none')
        
        # Scrollbar styles
        self.style.configure('Nex.Vertical.TScrollbar',
                           background=NexClanTheme.MEDIUM_GRAY,
                           troughcolor=NexClanTheme.DARK_GRAY,
                           borderwidth=0,
                           arrowcolor=NexClanTheme.FLAME_ORANGE,
                           darkcolor=NexClanTheme.FLAME_ORANGE,
                           lightcolor=NexClanTheme.FLAME_ORANGE)
        
        self.style.configure('Nex.Horizontal.TScrollbar',
                           background=NexClanTheme.MEDIUM_GRAY,
                           troughcolor=NexClanTheme.DARK_GRAY,
                           borderwidth=0,
                           arrowcolor=NexClanTheme.FLAME_ORANGE,
                           darkcolor=NexClanTheme.FLAME_ORANGE,
                           lightcolor=NexClanTheme.FLAME_ORANGE)
        
        # PanedWindow styles
        self.style.configure('Nex.TPanedwindow',
                           background=NexClanTheme.BLACK)
        
    def generate_war_dates(self):
        """Generate 14 consecutive dates starting from today"""
        today = datetime.now()
        dates = []
        for i in range(14):
            date = today + timedelta(days=i)
            dates.append(date.strftime("%m/%d/%Y"))
        return dates
    
    def initialize_ranked_prizes(self):
        """Initialize default ranked prize structure"""
        self.ranked_prizes = [
            {"rank": 1, "amount": 400000, "label": "1st Place"},
            {"rank": 2, "amount": 200000, "label": "2nd Place"},
            {"rank": 3, "amount": 100000, "label": "3rd Place"},
            {"rank": 4, "amount": 50000, "label": "4th Place"},
            {"rank": 5, "amount": 25000, "label": "5th Place"}
        ]
    
    def setup_ui(self):
        """Setup the main user interface"""
        # Main container
        main_container = ttk.Frame(self.root, style='Nex.TFrame')
        main_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Header with title and branding
        self.setup_header(main_container)
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(main_container, style='Nex.TNotebook')
        self.notebook.pack(fill='both', expand=True, pady=(10, 0))
        
        # Create tabs
        self.war_frame = ttk.Frame(self.notebook, style='Nex.TFrame')
        self.roster_frame = ttk.Frame(self.notebook, style='Nex.TFrame')
        
        self.notebook.add(self.war_frame, text="🏆 Clan War Tracker")
        self.notebook.add(self.roster_frame, text="👥 Roster Manager")
        
        self.setup_war_tab()
        self.setup_roster_tab()
        
        # Footer with branding
        self.setup_footer(main_container)
        
    def setup_header(self, parent):
        """Setup header with title and auto-reload"""
        header_frame = ttk.Frame(parent, style='Nex.TFrame')
        header_frame.pack(fill='x', pady=(0, 10))
        
        # Title
        title_label = ttk.Label(header_frame, text="🔥 NEX CLAN WAR TRACKER 🔥", 
                               style='NexTitle.TLabel')
        title_label.pack(side='left')
        
        # Auto-reload controls
        reload_frame = ttk.Frame(header_frame, style='Nex.TFrame')
        reload_frame.pack(side='right')
        
        ttk.Checkbutton(reload_frame, text="Auto-reload last file", 
                       variable=self.auto_reload_enabled,
                       style='Nex.TCheckbutton').pack(side='left', padx=(0, 10))
        
        ttk.Button(reload_frame, text="🔄 Reload Last", 
                  command=self.reload_last_file, 
                  style='Nex.TButton').pack(side='left')
        
    def setup_footer(self, parent):
        """Setup footer with Nex Clan branding"""
        footer_frame = ttk.Frame(parent, style='Nex.TFrame')
        footer_frame.pack(fill='x', pady=(10, 0))
        
        # Separator line
        separator = ttk.Frame(footer_frame, style='Nex.TFrame', height=2)
        separator.configure(style='NexCard.TFrame')
        separator.pack(fill='x', pady=(0, 5))
        
        # Branding
        brand_label = ttk.Label(footer_frame, text="Created by Nex Clan", 
                               style='NexBrand.TLabel')
        brand_label.pack()
        
    def setup_war_tab(self):
        """Setup the clan war tracking tab with enhanced layout"""
        # Main paned window for resizable sections
        self.main_paned = ttk.PanedWindow(self.war_frame, orient='horizontal', style='Nex.TPanedwindow')
        self.main_paned.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Left panel container
        left_container = ttk.Frame(self.main_paned, style='Nex.TFrame')
        self.main_paned.add(left_container, weight=1)
        
        # Create vertical paned window for left side
        left_paned = ttk.PanedWindow(left_container, orient='vertical', style='Nex.TPanedwindow')
        left_paned.pack(fill='both', expand=True)
        
        # Participant management section
        participant_frame = ttk.LabelFrame(left_paned, text="👤 Participant Management", 
                                         padding=15, style='Nex.TLabelframe')
        left_paned.add(participant_frame, weight=1)
        
        self.setup_participant_section(participant_frame)
        
        # Prize management section
        prize_frame = ttk.LabelFrame(left_paned, text="💰 Prize Management", 
                                   padding=15, style='Nex.TLabelframe')
        left_paned.add(prize_frame, weight=1)
        
        self.setup_prize_section(prize_frame)
        
        # Right panel for attendance tracking
        right_container = ttk.Frame(self.main_paned, style='Nex.TFrame')
        self.main_paned.add(right_container, weight=2)
        
        self.setup_attendance_section(right_container)
        
        # Bottom panel for actions and results
        self.setup_bottom_section()
        
    def setup_participant_section(self, parent):
        """Setup participant management section"""
        # Participant entry
        ttk.Label(parent, text="Add Participant:", style='NexHeading.TLabel').pack(anchor='w', pady=(0, 8))
        
        entry_frame = ttk.Frame(parent, style='Nex.TFrame')
        entry_frame.pack(fill='x', pady=(0, 15))
        
        self.participant_entry = ttk.Entry(entry_frame, font=self.body_font, style='Nex.TEntry')
        self.participant_entry.pack(side='left', fill='x', expand=True)
        self.participant_entry.bind('<Return>', self.add_participant)
        
        add_btn = ttk.Button(entry_frame, text="➕ Add", command=self.add_participant, 
                           style='Nex.TButton')
        add_btn.pack(side='right', padx=(10, 0))
        
        # Participant list with enhanced styling
        ttk.Label(parent, text="Participants:", style='NexHeading.TLabel').pack(anchor='w', pady=(0, 8))
        
        list_container = ttk.Frame(parent, style='NexCard.TFrame')
        list_container.pack(fill='both', expand=True, pady=(0, 15))
        
        # Custom listbox with theme colors
        self.participant_listbox = tk.Listbox(list_container, 
                                            selectmode='single',
                                            font=self.body_font,
                                            bg=NexClanTheme.MEDIUM_GRAY,
                                            fg=NexClanTheme.WHITE,
                                            selectbackground=NexClanTheme.FLAME_ORANGE,
                                            selectforeground=NexClanTheme.WHITE,
                                            relief='flat',
                                            highlightthickness=0,
                                            borderwidth=0)
        
        # Enhanced scrollbar
        scrollbar = ttk.Scrollbar(list_container, orient='vertical', 
                                command=self.participant_listbox.yview,
                                style='Nex.Vertical.TScrollbar')
        self.participant_listbox.configure(yscrollcommand=scrollbar.set)
        
        self.participant_listbox.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        scrollbar.pack(side='right', fill='y', padx=(0, 5), pady=5)
        
        # Remove participant button
        remove_btn = ttk.Button(parent, text="🗑️ Remove Selected", 
                               command=self.remove_participant, style='Nex.TButton')
        remove_btn.pack()
        
    def setup_prize_section(self, parent):
        """Setup prize management section"""
        # Prize mode selection
        mode_frame = ttk.Frame(parent, style='Nex.TFrame')
        mode_frame.pack(fill='x', pady=(0, 15))
        
        ttk.Label(mode_frame, text="Prize Distribution Mode:", style='NexHeading.TLabel').pack(anchor='w', pady=(0, 8))
        
        mode_radio_frame = ttk.Frame(mode_frame, style='Nex.TFrame')
        mode_radio_frame.pack(fill='x')
        
        ttk.Radiobutton(mode_radio_frame, text="Equal Distribution", 
                       variable=self.prize_mode, value="equal",
                       command=self.on_prize_mode_change,
                       style='Nex.TRadiobutton').pack(anchor='w', pady=2)
        ttk.Radiobutton(mode_radio_frame, text="Ranked Prizes", 
                       variable=self.prize_mode, value="ranked",
                       command=self.on_prize_mode_change,
                       style='Nex.TRadiobutton').pack(anchor='w', pady=2)
        
        # Prize configuration container
        self.prize_config_frame = ttk.Frame(parent, style='Nex.TFrame')
        self.prize_config_frame.pack(fill='both', expand=True)
        
        self.setup_prize_config()
        
    def setup_prize_config(self):
        """Setup prize configuration based on current mode"""
        # Clear existing widgets
        for widget in self.prize_config_frame.winfo_children():
            widget.destroy()
        
        if self.prize_mode.get() == "equal":
            self.setup_equal_prize_config()
        else:
            self.setup_ranked_prize_config()
    
    def setup_equal_prize_config(self):
        """Setup equal distribution prize configuration"""
        ttk.Label(self.prize_config_frame, text="Total Prize Pool:", 
                 style='NexHeading.TLabel').pack(anchor='w', pady=(0, 8))
        
        prize_frame = ttk.Frame(self.prize_config_frame, style='Nex.TFrame')
        prize_frame.pack(fill='x')
        
        ttk.Label(prize_frame, text="$", style='NexBody.TLabel', 
                 font=self.heading_font).pack(side='left')
        self.prize_entry = ttk.Entry(prize_frame, textvariable=self.prize_pool, 
                                   font=self.body_font, style='Nex.TEntry')
        self.prize_entry.pack(side='left', fill='x', expand=True, padx=(5, 0))
        
    def setup_ranked_prize_config(self):
        """Setup ranked prizes configuration"""
        ttk.Label(self.prize_config_frame, text="Ranked Prize Structure:", 
                 style='NexHeading.TLabel').pack(anchor='w', pady=(0, 8))
        
        # Scrollable frame for ranked prizes
        canvas_container = ttk.Frame(self.prize_config_frame, style='NexCard.TFrame')
        canvas_container.pack(fill='both', expand=True, pady=(0, 10))
        
        canvas = tk.Canvas(canvas_container, height=200,
                          bg=NexClanTheme.MEDIUM_GRAY,
                          highlightthickness=0,
                          borderwidth=0)
        scrollbar = ttk.Scrollbar(canvas_container, orient="vertical", 
                                command=canvas.yview,
                                style='Nex.Vertical.TScrollbar')
        scrollable_frame = ttk.Frame(canvas, style='Nex.TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create prize entries
        self.ranked_prize_vars = []
        for i, prize in enumerate(self.ranked_prizes):
            prize_frame = ttk.Frame(scrollable_frame, style='Nex.TFrame')
            prize_frame.pack(fill='x', pady=3, padx=5)
            
            ttk.Label(prize_frame, text=f"{prize['label']}:", width=12,
                     style='NexBody.TLabel', font=self.body_font).pack(side='left')
            
            ttk.Label(prize_frame, text="$", style='NexBody.TLabel').pack(side='left', padx=(8, 0))
            
            var = tk.IntVar(value=prize['amount'])
            entry = ttk.Entry(prize_frame, textvariable=var, width=12, 
                            font=self.body_font, style='Nex.TEntry')
            entry.pack(side='left', padx=(0, 5))
            entry.bind('<KeyRelease>', lambda e, idx=i: self.update_ranked_prize(idx, var.get()))
            
            self.ranked_prize_vars.append(var)
        
        canvas.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        scrollbar.pack(side="right", fill="y", padx=(0, 5), pady=5)
        
        # Add/Remove rank buttons
        rank_btn_frame = ttk.Frame(self.prize_config_frame, style='Nex.TFrame')
        rank_btn_frame.pack(fill='x')
        
        ttk.Button(rank_btn_frame, text="➕ Add Rank", 
                  command=self.add_rank, style='Nex.TButton').pack(side='left', padx=(0, 10))
        ttk.Button(rank_btn_frame, text="➖ Remove Last", 
                  command=self.remove_rank, style='Nex.TButton').pack(side='left')
        
    def setup_attendance_section(self, parent):
        """Setup attendance tracking section"""
        attendance_frame = ttk.LabelFrame(parent, text="📅 Attendance Tracking (14 Days)", 
                                        padding=15, style='Nex.TLabelframe')
        attendance_frame.pack(fill='both', expand=True)
        
        # Date management section
        date_mgmt_frame = ttk.Frame(attendance_frame, style='Nex.TFrame')
        date_mgmt_frame.pack(fill='x', pady=(0, 15))
        
        ttk.Label(date_mgmt_frame, text="Date Management:", 
                 style='NexHeading.TLabel').pack(side='left')
        ttk.Button(date_mgmt_frame, text="📅 Calendar Picker", 
                  command=self.open_calendar_picker, style='Nex.TButton').pack(side='left', padx=(15, 10))
        ttk.Button(date_mgmt_frame, text="📝 Edit Dates", 
                  command=self.edit_dates, style='Nex.TButton').pack(side='left', padx=(0, 10))
        ttk.Button(date_mgmt_frame, text="🔄 Reset to Today", 
                  command=self.reset_dates, style='Nex.TButton').pack(side='left')
        
        # Attendance grid container
        self.attendance_container = ttk.Frame(attendance_frame, style='Nex.TFrame')
        self.attendance_container.pack(fill='both', expand=True)
        
    def setup_bottom_section(self):
        """Setup bottom section with actions and results"""
        bottom_frame = ttk.Frame(self.war_frame, style='Nex.TFrame')
        bottom_frame.pack(fill='x', padx=5, pady=5)
        
        # Action buttons
        button_frame = ttk.Frame(bottom_frame, style='Nex.TFrame')
        button_frame.pack(fill='x', pady=(0, 15))
        
        ttk.Button(button_frame, text="🧮 Calculate Payouts", 
                  command=self.open_calculate_window, style='NexPrimary.TButton').pack(side='left', padx=(0, 15))
        ttk.Button(button_frame, text="📤 Export Results", 
                  command=self.export_results, style='Nex.TButton').pack(side='left', padx=(0, 15))
        ttk.Button(button_frame, text="💾 Save Data", 
                  command=self.save_data, style='Nex.TButton').pack(side='left', padx=(0, 15))
        ttk.Button(button_frame, text="📁 Load Data", 
                  command=self.load_data, style='Nex.TButton').pack(side='left')
        
    def open_calculate_window(self):
        """Open resizable calculate window"""
        calc_window = CalculateWindow(self.root, self)
        
    def open_calendar_picker(self):
        """Open calendar picker for date selection"""
        calendar_dialog = CalendarDialog(self.root, self.war_dates)
        if calendar_dialog.result:
            self.war_dates = calendar_dialog.result
            self.refresh_attendance_grid()
    
    def check_auto_reload(self):
        """Check for auto-reload on startup"""
        if self.auto_reload_enabled.get() and os.path.exists('last_saved_file.txt'):
            try:
                with open('last_saved_file.txt', 'r') as f:
                    last_file = f.read().strip()
                if last_file and os.path.exists(last_file):
                    self.load_specific_file(last_file)
            except:
                pass  # Ignore errors in auto-reload
    
    def reload_last_file(self):
        """Reload the last saved file"""
        if os.path.exists('last_saved_file.txt'):
            try:
                with open('last_saved_file.txt', 'r') as f:
                    last_file = f.read().strip()
                if last_file and os.path.exists(last_file):
                    self.load_specific_file(last_file)
                else:
                    messagebox.showwarning("No File", "No previous file found to reload.")
            except Exception as e:
                messagebox.showerror("Reload Error", f"Failed to reload file: {str(e)}")
        else:
            messagebox.showwarning("No File", "No previous file found to reload.")
    
    def refresh_attendance_grid(self):
        """Refresh the attendance tracking grid with enhanced styling and sticky names"""
        # Clear existing grid
        for widget in self.attendance_container.winfo_children():
            widget.destroy()
        
        if not self.participants:
            ttk.Label(self.attendance_container, 
                     text="Add participants to start tracking attendance",
                     style='NexHeading.TLabel').pack(expand=True)
            return
        
        # Create main frame for the grid with enhanced styling
        main_frame = ttk.Frame(self.attendance_container, style='NexCard.TFrame')
        main_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Create canvas and enhanced scrollbars
        canvas = tk.Canvas(main_frame, 
                          bg=NexClanTheme.MEDIUM_GRAY,
                          highlightthickness=0, 
                          borderwidth=0)
        v_scrollbar = ttk.Scrollbar(main_frame, orient="vertical", 
                                  command=canvas.yview,
                                  style='Nex.Vertical.TScrollbar')
        h_scrollbar = ttk.Scrollbar(main_frame, orient="horizontal", 
                                  command=canvas.xview,
                                  style='Nex.Horizontal.TScrollbar')
        
        # Create scrollable frame
        scrollable_frame = ttk.Frame(canvas, style='Nex.TFrame')
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Configure grid weights for proper alignment and sticky names
        scrollable_frame.grid_columnconfigure(0, weight=0, minsize=180)  # Wider for sticky names
        for i in range(14):
            scrollable_frame.grid_columnconfigure(i+1, weight=0, minsize=85)
        scrollable_frame.grid_columnconfigure(15, weight=0, minsize=70)
        
        # Create header row with enhanced styling
        header_bg = NexClanTheme.FLAME_ORANGE
        
        # Sticky participant header
        participant_header = tk.Label(scrollable_frame, text="Participant", 
                                    bg=header_bg, fg=NexClanTheme.WHITE,
                                    font=self.heading_font, relief='raised', bd=1)
        participant_header.grid(row=0, column=0, padx=2, pady=2, sticky='ew', ipadx=5, ipady=5)
        
        # Date headers
        for i, date in enumerate(self.war_dates):
            short_date = date.split('/')[0] + '/' + date.split('/')[1]
            date_header = tk.Label(scrollable_frame, text=short_date,
                                 bg=header_bg, fg=NexClanTheme.WHITE,
                                 font=self.body_font, relief='raised', bd=1)
            date_header.grid(row=0, column=i+1, padx=1, pady=2, sticky='ew', ipadx=3, ipady=5)
        
        # Total header
        total_header = tk.Label(scrollable_frame, text="Total",
                              bg=header_bg, fg=NexClanTheme.WHITE,
                              font=self.heading_font, relief='raised', bd=1)
        total_header.grid(row=0, column=15, padx=2, pady=2, sticky='ew', ipadx=5, ipady=5)
        
        # Create rows for each participant with sticky names and alternating colors
        self.participant_vars = {}
        for row, participant in enumerate(self.participants, 1):
            # Alternating row colors
            row_bg = NexClanTheme.DARK_GRAY if row % 2 == 0 else NexClanTheme.MEDIUM_GRAY
            
            # Sticky participant name with enhanced styling
            name_label = tk.Label(scrollable_frame, text=participant['name'],
                                bg=NexClanTheme.LIGHT_GRAY, fg=NexClanTheme.WHITE,
                                font=self.body_font, relief='raised', bd=1,
                                anchor='w')
            name_label.grid(row=row, column=0, padx=2, pady=1, sticky='ew', ipadx=8, ipady=3)
            
            # Attendance checkboxes with enhanced styling
            self.participant_vars[participant['name']] = []
            for day in range(14):
                var = tk.BooleanVar(value=participant['attendance'][day])
                
                # Create frame for checkbox with background
                cb_frame = tk.Frame(scrollable_frame, bg=row_bg, relief='sunken', bd=1)
                cb_frame.grid(row=row, column=day+1, padx=1, pady=1, sticky='ew', ipadx=2, ipady=2)
                
                checkbox = tk.Checkbutton(cb_frame, variable=var,
                                        bg=row_bg, fg=NexClanTheme.WHITE,
                                        selectcolor=NexClanTheme.FLAME_ORANGE,
                                        activebackground=row_bg,
                                        relief='flat', bd=0,
                                        command=lambda p=participant['name'], d=day, v=var: self.update_attendance(p, d, v))
                checkbox.pack()
                self.participant_vars[participant['name']].append(var)
            
            # Total days label with enhanced styling
            total_label = tk.Label(scrollable_frame, text=str(participant['total_days']),
                                 bg=NexClanTheme.FLAME_RED, fg=NexClanTheme.WHITE,
                                 font=self.heading_font, relief='raised', bd=1)
            total_label.grid(row=row, column=15, padx=2, pady=1, sticky='ew', ipadx=5, ipady=3)
        
        # Pack scrollbars and canvas with enhanced positioning
        canvas.pack(side="left", fill="both", expand=True)
        v_scrollbar.pack(side="right", fill="y", padx=(2, 0))
        h_scrollbar.pack(side="bottom", fill="x", pady=(2, 0))
        
        # Enhanced mousewheel binding
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        def _on_shift_mousewheel(event):
            canvas.xview_scroll(int(-1*(event.delta/120)), "units")
        
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        canvas.bind_all("<Shift-MouseWheel>", _on_shift_mousewheel)
    
    def setup_roster_tab(self):
        """Setup the roster management tab with class icons"""
        # Main container with paned window
        roster_paned = ttk.PanedWindow(self.roster_frame, orient='horizontal', style='Nex.TPanedwindow')
        roster_paned.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Left panel for squad management
        left_panel = ttk.LabelFrame(roster_paned, text="👥 Squad Management", 
                                  padding=15, style='Nex.TLabelframe')
        roster_paned.add(left_panel, weight=1)
        
        # Squad creation
        ttk.Label(left_panel, text="Create Squad:", style='NexHeading.TLabel').pack(anchor='w', pady=(0, 8))
        
        squad_entry_frame = ttk.Frame(left_panel, style='Nex.TFrame')
        squad_entry_frame.pack(fill='x', pady=(0, 15))
        
        self.squad_entry = ttk.Entry(squad_entry_frame, font=self.body_font, style='Nex.TEntry')
        self.squad_entry.pack(side='left', fill='x', expand=True)
        self.squad_entry.bind('<Return>', self.add_squad)
        
        add_squad_btn = ttk.Button(squad_entry_frame, text="➕ Add", 
                                  command=self.add_squad, style='Nex.TButton')
        add_squad_btn.pack(side='right', padx=(10, 0))
        
        # Squad list with enhanced styling
        ttk.Label(left_panel, text="Squads:", style='NexHeading.TLabel').pack(anchor='w', pady=(0, 8))
        
        squad_list_container = ttk.Frame(left_panel, style='NexCard.TFrame')
        squad_list_container.pack(fill='both', expand=True, pady=(0, 15))
        
        self.squad_listbox = tk.Listbox(squad_list_container, selectmode='single',
                                       font=self.body_font,
                                       bg=NexClanTheme.MEDIUM_GRAY,
                                       fg=NexClanTheme.WHITE,
                                       selectbackground=NexClanTheme.FLAME_ORANGE,
                                       selectforeground=NexClanTheme.WHITE,
                                       relief='flat',
                                       highlightthickness=0,
                                       borderwidth=0)
        squad_scrollbar = ttk.Scrollbar(squad_list_container, orient='vertical', 
                                      command=self.squad_listbox.yview,
                                      style='Nex.Vertical.TScrollbar')
        self.squad_listbox.configure(yscrollcommand=squad_scrollbar.set)
        self.squad_listbox.bind('<<ListboxSelect>>', self.on_squad_select)
        
        self.squad_listbox.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        squad_scrollbar.pack(side='right', fill='y', padx=(0, 5), pady=5)
        
        # Squad management buttons
        squad_btn_frame = ttk.Frame(left_panel, style='Nex.TFrame')
        squad_btn_frame.pack(fill='x')
        
        ttk.Button(squad_btn_frame, text="✏️ Rename", 
                  command=self.rename_squad, style='Nex.TButton').pack(side='left', padx=(0, 10))
        ttk.Button(squad_btn_frame, text="🗑️ Delete", 
                  command=self.delete_squad, style='Nex.TButton').pack(side='left')
        
        # Right panel for squad details with class icons
        right_panel = ttk.LabelFrame(roster_paned, text="📋 Squad Details & Class Icons", 
                                   padding=15, style='Nex.TLabelframe')
        roster_paned.add(right_panel, weight=2)
        
        self.squad_details_frame = ttk.Frame(right_panel, style='Nex.TFrame')
        self.squad_details_frame.pack(fill='both', expand=True)
        
        # Initially show instructions
        ttk.Label(self.squad_details_frame, 
                 text="Select a squad from the left to view and manage members with class icons",
                 style='NexHeading.TLabel').pack(expand=True)
    
    # Continue with remaining methods...
    def on_prize_mode_change(self):
        """Handle prize mode change"""
        self.setup_prize_config()
    
    def update_ranked_prize(self, index, value):
        """Update ranked prize amount"""
        try:
            if 0 <= index < len(self.ranked_prizes):
                self.ranked_prizes[index]['amount'] = int(value)
        except (ValueError, TypeError):
            pass
    
    def add_rank(self):
        """Add a new rank to the prize structure"""
        next_rank = len(self.ranked_prizes) + 1
        new_prize = {
            "rank": next_rank,
            "amount": 10000,
            "label": f"{self.get_ordinal(next_rank)} Place"
        }
        self.ranked_prizes.append(new_prize)
        self.setup_ranked_prize_config()
    
    def remove_rank(self):
        """Remove the last rank from the prize structure"""
        if len(self.ranked_prizes) > 1:
            self.ranked_prizes.pop()
            self.setup_ranked_prize_config()
    
    def get_ordinal(self, n):
        """Get ordinal string for a number (1st, 2nd, 3rd, etc.)"""
        if 10 <= n % 100 <= 20:
            suffix = 'th'
        else:
            suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
        return f"{n}{suffix}"
    
    def add_participant(self, event=None):
        """Add a new participant"""
        name = self.participant_entry.get().strip()
        if not name:
            return
        
        # Check if participant already exists
        if any(p['name'] == name for p in self.participants):
            messagebox.showwarning("Duplicate Participant", f"'{name}' is already in the list.")
            return
        
        # Add new participant
        participant = {
            'name': name,
            'attendance': [False] * 14,
            'total_days': 0,
            'payout': 0.0,
            'rank': 0,
            'class_icon': None  # For roster management
        }
        
        self.participants.append(participant)
        self.participant_listbox.insert(tk.END, name)
        self.participant_entry.delete(0, tk.END)
        
        self.refresh_attendance_grid()
    
    def remove_participant(self):
        """Remove selected participant"""
        selection = self.participant_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a participant to remove.")
            return
        
        index = selection[0]
        participant_name = self.participants[index]['name']
        
        # Confirm removal
        if messagebox.askyesno("Confirm Removal", f"Remove '{participant_name}' from the list?"):
            self.participants.pop(index)
            self.participant_listbox.delete(index)
            self.refresh_attendance_grid()
    
    def update_attendance(self, participant_name, day, var):
        """Update attendance for a participant"""
        # Find participant and update attendance
        for participant in self.participants:
            if participant['name'] == participant_name:
                participant['attendance'][day] = var.get()
                participant['total_days'] = sum(participant['attendance'])
                break
        
        self.refresh_attendance_grid()
    
    def edit_dates(self):
        """Open dialog to edit the war dates"""
        dialog = DateEditDialog(self.root, self.war_dates)
        if dialog.result:
            self.war_dates = dialog.result
            self.refresh_attendance_grid()
    
    def reset_dates(self):
        """Reset dates to start from today"""
        if messagebox.askyesno("Reset Dates", "Reset all dates to start from today? This will clear all attendance data."):
            self.war_dates = self.generate_war_dates()
            # Reset all attendance data
            for participant in self.participants:
                participant['attendance'] = [False] * 14
                participant['total_days'] = 0
            self.refresh_attendance_grid()
    
    def export_results(self):
        """Export results to a text file"""
        if not self.participants:
            messagebox.showwarning("No Data", "No participants to export.")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Export Results"
        )
        
        if filename:
            try:
                # Get results from calculate window or generate them
                results = self.generate_export_results()
                with open(filename, 'w') as f:
                    f.write(results)
                messagebox.showinfo("Export Successful", f"Results exported to {filename}")
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export results: {str(e)}")
    
    def generate_export_results(self):
        """Generate results text for export"""
        results = []
        results.append("NEX CLAN WAR TRACKER - RESULTS")
        results.append("=" * 60)
        results.append(f"War Period: {self.war_dates[0]} to {self.war_dates[-1]}")
        results.append("")
        
        if self.prize_mode.get() == "equal":
            results.extend(self.generate_equal_results())
        else:
            results.extend(self.generate_ranked_results())
        
        results.append("")
        results.append("Created by Nex Clan")
        return "\n".join(results)
    
    def generate_equal_results(self):
        """Generate equal distribution results"""
        prize_total = self.prize_pool.get()
        total_attendance_days = sum(p['total_days'] for p in self.participants)
        
        if total_attendance_days == 0:
            return ["No attendance recorded."]
        
        per_day_value = prize_total / total_attendance_days
        
        results = []
        results.append("EQUAL DISTRIBUTION CALCULATION")
        results.append("-" * 40)
        results.append(f"Total Prize Pool: ${prize_total:,.2f}")
        results.append(f"Total Attendance Days: {total_attendance_days}")
        results.append(f"Value per Day: ${per_day_value:,.2f}")
        results.append("")
        results.append("INDIVIDUAL PAYOUTS:")
        results.append("-" * 40)
        
        for participant in self.participants:
            payout = participant['total_days'] * per_day_value
            results.append(f"{participant['name']:<25} {participant['total_days']:>2} days  ${payout:>12,.2f}")
        
        return results
    
    def generate_ranked_results(self):
        """Generate ranked distribution results"""
        sorted_participants = sorted(self.participants, key=lambda p: p['total_days'], reverse=True)
        
        results = []
        results.append("RANKED PRIZE DISTRIBUTION")
        results.append("-" * 40)
        results.append("PRIZE STRUCTURE:")
        
        for prize in self.ranked_prizes:
            results.append(f"{prize['label']:<15} ${prize['amount']:>12,}")
        
        results.append("")
        results.append("RANKINGS AND PAYOUTS:")
        results.append("-" * 40)
        
        current_rank = 1
        prev_attendance = None
        
        for i, participant in enumerate(sorted_participants):
            if prev_attendance is not None and participant['total_days'] != prev_attendance:
                current_rank = i + 1
            
            if current_rank <= len(self.ranked_prizes):
                payout = self.ranked_prizes[current_rank - 1]['amount']
                rank_label = self.ranked_prizes[current_rank - 1]['label']
            else:
                payout = 0
                rank_label = f"{self.get_ordinal(current_rank)} Place"
            
            results.append(f"{rank_label:<15} {participant['name']:<20} {participant['total_days']:>2} days  ${payout:>12,}")
            prev_attendance = participant['total_days']
        
        return results
    
    def save_data(self):
        """Save application data to JSON file"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            title="Save Clan War Data"
        )
        
        if filename:
            try:
                data = {
                    'participants': self.participants,
                    'squads': self.squads,
                    'prize_pool': self.prize_pool.get(),
                    'war_dates': self.war_dates,
                    'prize_mode': self.prize_mode.get(),
                    'ranked_prizes': self.ranked_prizes
                }
                
                with open(filename, 'w') as f:
                    json.dump(data, f, indent=2)
                
                # Save last file reference
                with open('last_saved_file.txt', 'w') as f:
                    f.write(filename)
                
                self.last_saved_file = filename
                messagebox.showinfo("Save Successful", f"Data saved to {filename}")
            except Exception as e:
                messagebox.showerror("Save Error", f"Failed to save data: {str(e)}")
    
    def load_data(self):
        """Load application data from JSON file"""
        filename = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            title="Load Clan War Data"
        )
        
        if filename:
            self.load_specific_file(filename)
    
    def load_specific_file(self, filename):
        """Load specific file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.participants = data.get('participants', [])
            self.squads = data.get('squads', [])
            self.prize_pool.set(data.get('prize_pool', 0.0))
            self.war_dates = data.get('war_dates', self.generate_war_dates())
            self.prize_mode.set(data.get('prize_mode', 'equal'))
            self.ranked_prizes = data.get('ranked_prizes', self.ranked_prizes)
            
            # Refresh UI
            self.participant_listbox.delete(0, tk.END)
            for participant in self.participants:
                self.participant_listbox.insert(tk.END, participant['name'])
            
            self.squad_listbox.delete(0, tk.END)
            for squad in self.squads:
                self.squad_listbox.insert(tk.END, squad['name'])
            
            self.setup_prize_config()
            self.refresh_attendance_grid()
            self.refresh_squad_details()
            
            # Save as last file
            with open('last_saved_file.txt', 'w') as f:
                f.write(filename)
            
            self.last_saved_file = filename
            messagebox.showinfo("Load Successful", f"Data loaded from {filename}")
        except Exception as e:
            messagebox.showerror("Load Error", f"Failed to load data: {str(e)}")
    
    def add_squad(self, event=None):
        """Add a new squad"""
        name = self.squad_entry.get().strip()
        if not name:
            return
        
        # Check if squad already exists
        if any(s['name'] == name for s in self.squads):
            messagebox.showwarning("Duplicate Squad", f"'{name}' already exists.")
            return
        
        # Add new squad
        squad = {
            'name': name,
            'members': []
        }
        
        self.squads.append(squad)
        self.squad_listbox.insert(tk.END, name)
        self.squad_entry.delete(0, tk.END)
    
    def rename_squad(self):
        """Rename selected squad"""
        selection = self.squad_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a squad to rename.")
            return
        
        index = selection[0]
        old_name = self.squads[index]['name']
        
        # Get new name
        new_name = simpledialog.askstring("Rename Squad", f"Enter new name for '{old_name}':")
        if new_name and new_name.strip():
            new_name = new_name.strip()
            
            # Check if name already exists
            if any(s['name'] == new_name for s in self.squads):
                messagebox.showwarning("Duplicate Name", f"'{new_name}' already exists.")
                return
            
            self.squads[index]['name'] = new_name
            self.squad_listbox.delete(index)
            self.squad_listbox.insert(index, new_name)
            self.squad_listbox.selection_set(index)
    
    def delete_squad(self):
        """Delete selected squad"""
        selection = self.squad_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a squad to delete.")
            return
        
        index = selection[0]
        squad_name = self.squads[index]['name']
        
        if messagebox.askyesno("Confirm Deletion", f"Delete squad '{squad_name}'?"):
            self.squads.pop(index)
            self.squad_listbox.delete(index)
            self.refresh_squad_details()
    
    def on_squad_select(self, event):
        """Handle squad selection"""
        self.refresh_squad_details()
    
    def refresh_squad_details(self):
        """Refresh the squad details panel with class icons"""
        # Clear existing content
        for widget in self.squad_details_frame.winfo_children():
            widget.destroy()
        
        selection = self.squad_listbox.curselection()
        if not selection:
            ttk.Label(self.squad_details_frame, 
                     text="Select a squad from the left to view and manage members with class icons",
                     style='NexHeading.TLabel').pack(expand=True)
            return
        
        squad_index = selection[0]
        squad = self.squads[squad_index]
        
        # Squad name header
        ttk.Label(self.squad_details_frame, text=f"🔥 Squad: {squad['name']} 🔥", 
                 style='NexTitle.TLabel').pack(pady=(0, 20))
        
        # Available participants section
        available_frame = ttk.LabelFrame(self.squad_details_frame, text="Available Participants", 
                                       padding=15, style='Nex.TLabelframe')
        available_frame.pack(fill='x', pady=(0, 15))
        
        available_participants = [p for p in self.participants if p['name'] not in squad['members']]
        
        if available_participants:
            for participant in available_participants:
                participant_frame = ttk.Frame(available_frame, style='Nex.TFrame')
                participant_frame.pack(fill='x', pady=5)
                
                # Participant info with class icon
                info_frame = ttk.Frame(participant_frame, style='Nex.TFrame')
                info_frame.pack(side='left', fill='x', expand=True)
                
                class_icon = participant.get('class_icon', 'none')
                if class_icon != 'none' and class_icon in ClassIcons.CLASSES:
                    icon_text = f"{ClassIcons.CLASSES[class_icon]['icon']} {participant['name']}"
                else:
                    icon_text = participant['name']
                
                ttk.Label(info_frame, text=icon_text, style='NexBody.TLabel').pack(side='left')
                
                # Buttons
                btn_frame = ttk.Frame(participant_frame, style='Nex.TFrame')
                btn_frame.pack(side='right')
                
                ttk.Button(btn_frame, text="🎮 Set Class", 
                          command=lambda p=participant: self.set_class_icon(p),
                          style='Nex.TButton').pack(side='left', padx=(0, 5))
                ttk.Button(btn_frame, text="➕ Add to Squad", 
                          command=lambda p=participant['name']: self.add_to_squad(squad_index, p),
                          style='Nex.TButton').pack(side='left')
        else:
            ttk.Label(available_frame, text="No available participants", 
                     style='NexBody.TLabel').pack()
        
        # Squad members section
        members_frame = ttk.LabelFrame(self.squad_details_frame, text="Squad Members", 
                                     padding=15, style='Nex.TLabelframe')
        members_frame.pack(fill='both', expand=True)
        
        if squad['members']:
            for member_name in squad['members']:
                # Find participant data
                participant = next((p for p in self.participants if p['name'] == member_name), None)
                if not participant:
                    continue
                
                member_frame = ttk.Frame(members_frame, style='NexCard.TFrame')
                member_frame.pack(fill='x', pady=5, padx=5)
                
                # Member info with class icon
                info_frame = ttk.Frame(member_frame, style='Nex.TFrame')
                info_frame.pack(side='left', fill='x', expand=True, padx=10, pady=5)
                
                class_icon = participant.get('class_icon', 'none')
                if class_icon != 'none' and class_icon in ClassIcons.CLASSES:
                    icon_text = f"{ClassIcons.CLASSES[class_icon]['icon']} {member_name}"
                    class_name = ClassIcons.CLASSES[class_icon]['name']
                    display_text = f"{icon_text}\n{class_name}"
                else:
                    display_text = f"{member_name}\nNo class assigned"
                
                ttk.Label(info_frame, text=display_text, style='NexBody.TLabel').pack(side='left')
                
                # Buttons
                btn_frame = ttk.Frame(member_frame, style='Nex.TFrame')
                btn_frame.pack(side='right', padx=10, pady=5)
                
                ttk.Button(btn_frame, text="🎮 Change Class", 
                          command=lambda p=participant: self.set_class_icon(p),
                          style='Nex.TButton').pack(pady=2)
                ttk.Button(btn_frame, text="➖ Remove", 
                          command=lambda m=member_name: self.remove_from_squad(squad_index, m),
                          style='Nex.TButton').pack(pady=2)
        else:
            ttk.Label(members_frame, text="No members assigned", 
                     style='NexBody.TLabel').pack()
    
    def set_class_icon(self, participant):
        """Set class icon for participant"""
        dialog = ClassIconDialog(self.root, participant.get('class_icon', 'none'))
        if dialog.result:
            participant['class_icon'] = dialog.result
            self.refresh_squad_details()
    
    def add_to_squad(self, squad_index, participant_name):
        """Add participant to squad"""
        self.squads[squad_index]['members'].append(participant_name)
        self.refresh_squad_details()
    
    def remove_from_squad(self, squad_index, participant_name):
        """Remove participant from squad"""
        self.squads[squad_index]['members'].remove(participant_name)
        self.refresh_squad_details()
    
    def run(self):
        """Start the application"""
        self.root.mainloop()


class CalculateWindow:
    """Resizable calculate window"""
    
    def __init__(self, parent, tracker):
        self.tracker = tracker
        
        # Create window
        self.window = tk.Toplevel(parent)
        self.window.title("Nex Clan - Prize Calculation")
        self.window.geometry("800x600")
        self.window.configure(bg=NexClanTheme.BLACK)
        
        # Make resizable
        self.window.resizable(True, True)
        
        # Center window
        self.window.transient(parent)
        self.window.grab_set()
        
        self.setup_calculate_ui()
        self.calculate_and_display()
        
    def setup_calculate_ui(self):
        """Setup calculate window UI"""
        # Header
        header_frame = ttk.Frame(self.window, style='Nex.TFrame')
        header_frame.pack(fill='x', padx=20, pady=20)
        
        ttk.Label(header_frame, text="🔥 PRIZE CALCULATION RESULTS 🔥", 
                 style='NexTitle.TLabel').pack()
        
        # Results area with scrolling
        results_frame = ttk.LabelFrame(self.window, text="Calculation Results", 
                                     padding=15, style='Nex.TLabelframe')
        results_frame.pack(fill='both', expand=True, padx=20, pady=(0, 20))
        
        # Text widget with custom styling
        text_container = ttk.Frame(results_frame, style='Nex.TFrame')
        text_container.pack(fill='both', expand=True)
        
        self.results_text = tk.Text(text_container, 
                                   font=('Consolas', 11),
                                   bg=NexClanTheme.MEDIUM_GRAY,
                                   fg=NexClanTheme.WHITE,
                                   insertbackground=NexClanTheme.FLAME_ORANGE,
                                   selectbackground=NexClanTheme.FLAME_ORANGE,
                                   selectforeground=NexClanTheme.WHITE,
                                   relief='flat',
                                   highlightthickness=0,
                                   borderwidth=0,
                                   wrap='word')
        
        scrollbar = ttk.Scrollbar(text_container, orient='vertical', 
                                command=self.results_text.yview,
                                style='Nex.Vertical.TScrollbar')
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        scrollbar.pack(side='right', fill='y', padx=(0, 5), pady=5)
        
        # Button frame
        button_frame = ttk.Frame(self.window, style='Nex.TFrame')
        button_frame.pack(fill='x', padx=20, pady=(0, 20))
        
        ttk.Button(button_frame, text="📤 Export Results", 
                  command=self.export_results, style='Nex.TButton').pack(side='left', padx=(0, 10))
        ttk.Button(button_frame, text="🔄 Recalculate", 
                  command=self.calculate_and_display, style='Nex.TButton').pack(side='left', padx=(0, 10))
        ttk.Button(button_frame, text="❌ Close", 
                  command=self.window.destroy, style='Nex.TButton').pack(side='right')
        
    def calculate_and_display(self):
        """Calculate and display results"""
        if not self.tracker.participants:
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(1.0, "No participants added yet.")
            return
        
        results = self.tracker.generate_export_results()
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(1.0, results)
        
        # Add some color highlighting
        self.highlight_results()
    
    def highlight_results(self):
        """Add color highlighting to results"""
        # Highlight headers
        content = self.results_text.get(1.0, tk.END)
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            line_start = f"{i+1}.0"
            line_end = f"{i+1}.end"
            
            if "NEX CLAN" in line or "RESULTS" in line:
                self.results_text.tag_add("title", line_start, line_end)
            elif line.startswith("=") or line.startswith("-"):
                self.results_text.tag_add("separator", line_start, line_end)
            elif "Place" in line and "$" in line:
                self.results_text.tag_add("prize", line_start, line_end)
        
        # Configure tags
        self.results_text.tag_configure("title", foreground=NexClanTheme.FLAME_ORANGE, font=('Consolas', 12, 'bold'))
        self.results_text.tag_configure("separator", foreground=NexClanTheme.FLAME_YELLOW)
        self.results_text.tag_configure("prize", foreground=NexClanTheme.SUCCESS, font=('Consolas', 11, 'bold'))
    
    def export_results(self):
        """Export results from calculate window"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Export Calculation Results"
        )
        
        if filename:
            try:
                with open(filename, 'w') as f:
                    f.write(self.results_text.get(1.0, tk.END))
                messagebox.showinfo("Export Successful", f"Results exported to {filename}")
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export results: {str(e)}")


class CalendarDialog:
    """Calendar dialog for date selection"""
    
    def __init__(self, parent, current_dates):
        self.result = None
        self.current_dates = current_dates
        
        # Create dialog window
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Nex Clan - Calendar Date Picker")
        self.dialog.geometry("600x500")
        self.dialog.configure(bg=NexClanTheme.BLACK)
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Center the dialog
        self.dialog.geometry("+%d+%d" % (parent.winfo_rootx() + 100, parent.winfo_rooty() + 100))
        
        self.setup_calendar_ui()
        
        # Wait for dialog to close
        self.dialog.wait_window()
    
    def setup_calendar_ui(self):
        """Setup calendar UI"""
        # Header
        header_frame = ttk.Frame(self.dialog, style='Nex.TFrame')
        header_frame.pack(fill='x', padx=20, pady=20)
        
        ttk.Label(header_frame, text="🔥 SELECT WAR START DATE 🔥", 
                 style='NexTitle.TLabel').pack()
        
        # Instructions
        ttk.Label(header_frame, text="Select the first day of your 14-day war period", 
                 style='NexBody.TLabel').pack(pady=(10, 0))
        
        # Calendar frame
        cal_frame = ttk.LabelFrame(self.dialog, text="Calendar", 
                                 padding=20, style='Nex.TLabelframe')
        cal_frame.pack(fill='both', expand=True, padx=20, pady=(0, 20))
        
        # Simple calendar implementation
        self.setup_simple_calendar(cal_frame)
        
        # Button frame
        button_frame = ttk.Frame(self.dialog, style='Nex.TFrame')
        button_frame.pack(fill='x', padx=20, pady=(0, 20))
        
        ttk.Button(button_frame, text="✅ Use Selected Date", 
                  command=self.use_selected_date, style='NexPrimary.TButton').pack(side='left', padx=(0, 10))
        ttk.Button(button_frame, text="📅 Use Today", 
                  command=self.use_today, style='Nex.TButton').pack(side='left', padx=(0, 10))
        ttk.Button(button_frame, text="❌ Cancel", 
                  command=self.dialog.destroy, style='Nex.TButton').pack(side='right')
    
    def setup_simple_calendar(self, parent):
        """Setup simple calendar widget"""
        # Current date
        today = datetime.now()
        self.selected_date = today
        
        # Month/Year navigation
        nav_frame = ttk.Frame(parent, style='Nex.TFrame')
        nav_frame.pack(fill='x', pady=(0, 20))
        
        ttk.Button(nav_frame, text="◀", command=self.prev_month, 
                  style='Nex.TButton').pack(side='left')
        
        self.month_label = ttk.Label(nav_frame, text="", style='NexHeading.TLabel')
        self.month_label.pack(side='left', expand=True)
        
        ttk.Button(nav_frame, text="▶", command=self.next_month, 
                  style='Nex.TButton').pack(side='right')
        
        # Calendar grid
        self.cal_frame = ttk.Frame(parent, style='Nex.TFrame')
        self.cal_frame.pack(fill='both', expand=True)
        
        self.update_calendar()
    
    def update_calendar(self):
        """Update calendar display"""
        # Clear existing calendar
        for widget in self.cal_frame.winfo_children():
            widget.destroy()
        
        # Update month label
        self.month_label.config(text=self.selected_date.strftime("%B %Y"))
        
        # Get calendar data
        cal = calendar.monthcalendar(self.selected_date.year, self.selected_date.month)
        
        # Day headers
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for i, day in enumerate(days):
            label = tk.Label(self.cal_frame, text=day, 
                           bg=NexClanTheme.FLAME_ORANGE, fg=NexClanTheme.WHITE,
                           font=('Arial', 10, 'bold'), relief='raised', bd=1)
            label.grid(row=0, column=i, sticky='ew', padx=1, pady=1, ipadx=5, ipady=5)
        
        # Calendar days
        today = datetime.now()
        for week_num, week in enumerate(cal, 1):
            for day_num, day in enumerate(week):
                if day == 0:
                    # Empty cell
                    label = tk.Label(self.cal_frame, text="", 
                                   bg=NexClanTheme.DARK_GRAY, relief='flat')
                else:
                    # Day cell
                    date_obj = datetime(self.selected_date.year, self.selected_date.month, day)
                    
                    # Determine colors
                    if date_obj.date() == today.date():
                        bg_color = NexClanTheme.FLAME_RED
                        fg_color = NexClanTheme.WHITE
                    elif date_obj.date() == self.selected_date.date():
                        bg_color = NexClanTheme.FLAME_YELLOW
                        fg_color = NexClanTheme.BLACK
                    else:
                        bg_color = NexClanTheme.MEDIUM_GRAY
                        fg_color = NexClanTheme.WHITE
                    
                    label = tk.Label(self.cal_frame, text=str(day),
                                   bg=bg_color, fg=fg_color,
                                   font=('Arial', 10), relief='raised', bd=1,
                                   cursor='hand2')
                    label.bind('<Button-1>', lambda e, d=date_obj: self.select_date(d))
                
                label.grid(row=week_num, column=day_num, sticky='ew', padx=1, pady=1, ipadx=8, ipady=8)
        
        # Configure grid weights
        for i in range(7):
            self.cal_frame.grid_columnconfigure(i, weight=1)
    
    def prev_month(self):
        """Go to previous month"""
        if self.selected_date.month == 1:
            self.selected_date = self.selected_date.replace(year=self.selected_date.year - 1, month=12)
        else:
            self.selected_date = self.selected_date.replace(month=self.selected_date.month - 1)
        self.update_calendar()
    
    def next_month(self):
        """Go to next month"""
        if self.selected_date.month == 12:
            self.selected_date = self.selected_date.replace(year=self.selected_date.year + 1, month=1)
        else:
            self.selected_date = self.selected_date.replace(month=self.selected_date.month + 1)
        self.update_calendar()
    
    def select_date(self, date_obj):
        """Select a date"""
        self.selected_date = date_obj
        self.update_calendar()
    
    def use_selected_date(self):
        """Use the selected date as start date"""
        start_date = self.selected_date
        dates = []
        for i in range(14):
            date = start_date + timedelta(days=i)
            dates.append(date.strftime("%m/%d/%Y"))
        
        self.result = dates
        self.dialog.destroy()
    
    def use_today(self):
        """Use today as start date"""
        start_date = datetime.now()
        dates = []
        for i in range(14):
            date = start_date + timedelta(days=i)
            dates.append(date.strftime("%m/%d/%Y"))
        
        self.result = dates
        self.dialog.destroy()


class ClassIconDialog:
    """Dialog for selecting class icons"""
    
    def __init__(self, parent, current_class):
        self.result = None
        self.current_class = current_class
        
        # Create dialog window
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Nex Clan - Select Class Icon")
        self.dialog.geometry("500x600")
        self.dialog.configure(bg=NexClanTheme.BLACK)
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Center the dialog
        self.dialog.geometry("+%d+%d" % (parent.winfo_rootx() + 150, parent.winfo_rooty() + 100))
        
        self.setup_class_ui()
        
        # Wait for dialog to close
        self.dialog.wait_window()
    
    def setup_class_ui(self):
        """Setup class selection UI"""
        # Header
        header_frame = ttk.Frame(self.dialog, style='Nex.TFrame')
        header_frame.pack(fill='x', padx=20, pady=20)
        
        ttk.Label(header_frame, text="🎮 SELECT CLASS ICON 🎮", 
                 style='NexTitle.TLabel').pack()
        
        # Class selection frame
        class_frame = ttk.LabelFrame(self.dialog, text="Available Classes", 
                                   padding=20, style='Nex.TLabelframe')
        class_frame.pack(fill='both', expand=True, padx=20, pady=(0, 20))
        
        # Scrollable class list
        canvas = tk.Canvas(class_frame, bg=NexClanTheme.MEDIUM_GRAY,
                          highlightthickness=0, borderwidth=0)
        scrollbar = ttk.Scrollbar(class_frame, orient="vertical", 
                                command=canvas.yview,
                                style='Nex.Vertical.TScrollbar')
        scrollable_frame = ttk.Frame(canvas, style='Nex.TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Add "No Class" option
        self.add_class_option(scrollable_frame, "none", "❌", "No Class Assigned")
        
        # Add all class options
        for class_key, class_data in ClassIcons.CLASSES.items():
            self.add_class_option(scrollable_frame, class_key, 
                                class_data['icon'], class_data['name'])
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Button frame
        button_frame = ttk.Frame(self.dialog, style='Nex.TFrame')
        button_frame.pack(fill='x', padx=20, pady=(0, 20))
        
        ttk.Button(button_frame, text="❌ Cancel", 
                  command=self.dialog.destroy, style='Nex.TButton').pack(side='right')
    
    def add_class_option(self, parent, class_key, icon, name):
        """Add a class option to the selection"""
        # Determine if this is the current selection
        is_selected = (class_key == self.current_class)
        
        # Create frame for this class
        if is_selected:
            class_frame = ttk.Frame(parent, style='NexCard.TFrame')
        else:
            class_frame = ttk.Frame(parent, style='Nex.TFrame')
        
        class_frame.pack(fill='x', pady=5, padx=5)
        
        # Create button for selection
        btn_frame = tk.Frame(class_frame, 
                           bg=NexClanTheme.FLAME_ORANGE if is_selected else NexClanTheme.MEDIUM_GRAY,
                           relief='raised' if is_selected else 'flat',
                           bd=2 if is_selected else 1,
                           cursor='hand2')
        btn_frame.pack(fill='x', padx=5, pady=5)
        btn_frame.bind('<Button-1>', lambda e: self.select_class(class_key))
        
        # Icon and name
        content_frame = tk.Frame(btn_frame, 
                               bg=NexClanTheme.FLAME_ORANGE if is_selected else NexClanTheme.MEDIUM_GRAY)
        content_frame.pack(fill='x', padx=10, pady=10)
        content_frame.bind('<Button-1>', lambda e: self.select_class(class_key))
        
        # Icon label
        icon_label = tk.Label(content_frame, text=icon, 
                            bg=NexClanTheme.FLAME_ORANGE if is_selected else NexClanTheme.MEDIUM_GRAY,
                            fg=NexClanTheme.WHITE,
                            font=('Arial', 16))
        icon_label.pack(side='left', padx=(0, 15))
        icon_label.bind('<Button-1>', lambda e: self.select_class(class_key))
        
        # Name label
        name_label = tk.Label(content_frame, text=name,
                            bg=NexClanTheme.FLAME_ORANGE if is_selected else NexClanTheme.MEDIUM_GRAY,
                            fg=NexClanTheme.WHITE,
                            font=('Arial', 12, 'bold' if is_selected else 'normal'))
        name_label.pack(side='left')
        name_label.bind('<Button-1>', lambda e: self.select_class(class_key))
        
        if is_selected:
            selected_label = tk.Label(content_frame, text="✓ SELECTED",
                                    bg=NexClanTheme.FLAME_ORANGE,
                                    fg=NexClanTheme.WHITE,
                                    font=('Arial', 10, 'bold'))
            selected_label.pack(side='right')
            selected_label.bind('<Button-1>', lambda e: self.select_class(class_key))
    
    def select_class(self, class_key):
        """Select a class and close dialog"""
        self.result = class_key
        self.dialog.destroy()


class DateEditDialog:
    """Dialog for editing war dates"""
    
    def __init__(self, parent, current_dates):
        self.result = None
        
        # Create dialog window
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Nex Clan - Edit War Dates")
        self.dialog.geometry("500x600")
        self.dialog.configure(bg=NexClanTheme.BLACK)
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Center the dialog
        self.dialog.geometry("+%d+%d" % (parent.winfo_rootx() + 100, parent.winfo_rooty() + 50))
        
        # Main frame
        main_frame = ttk.Frame(self.dialog, style='Nex.TFrame')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header
        ttk.Label(main_frame, text="🔥 EDIT WAR DATES 🔥", 
                 style='NexTitle.TLabel').pack(pady=(0, 15))
        ttk.Label(main_frame, text="Edit the dates for the 14-day war period:", 
                 style='NexHeading.TLabel').pack(pady=(0, 10))
        ttk.Label(main_frame, text="Format: MM/DD/YYYY", 
                 style='NexBody.TLabel').pack(pady=(0, 20))
        
        # Scrollable frame for date entries
        canvas_container = ttk.LabelFrame(main_frame, text="War Dates", 
                                        padding=15, style='Nex.TLabelframe')
        canvas_container.pack(fill='both', expand=True, pady=(0, 20))
        
        canvas = tk.Canvas(canvas_container, bg=NexClanTheme.MEDIUM_GRAY,
                          highlightthickness=0, borderwidth=0)
        scrollbar = ttk.Scrollbar(canvas_container, orient="vertical", 
                                command=canvas.yview,
                                style='Nex.Vertical.TScrollbar')
        scrollable_frame = ttk.Frame(canvas, style='Nex.TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create date entry fields
        self.date_vars = []
        for i, date in enumerate(current_dates):
            frame = ttk.Frame(scrollable_frame, style='Nex.TFrame')
            frame.pack(fill='x', pady=5, padx=10)
            
            ttk.Label(frame, text=f"Day {i+1}:", width=8,
                     style='NexBody.TLabel').pack(side='left')
            
            var = tk.StringVar(value=date)
            entry = ttk.Entry(frame, textvariable=var, width=15, 
                            style='Nex.TEntry')
            entry.pack(side='left', padx=(15, 0))
            
            self.date_vars.append(var)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Button frame
        button_frame = ttk.Frame(main_frame, style='Nex.TFrame')
        button_frame.pack(fill='x')
        
        ttk.Button(button_frame, text="✅ Save Changes", 
                  command=self.ok_clicked, style='NexPrimary.TButton').pack(side='left', padx=(0, 10))
        ttk.Button(button_frame, text="❌ Cancel", 
                  command=self.cancel_clicked, style='Nex.TButton').pack(side='left')
        
        # Bind Enter and Escape keys
        self.dialog.bind('<Return>', lambda e: self.ok_clicked())
        self.dialog.bind('<Escape>', lambda e: self.cancel_clicked())
        
        # Wait for dialog to close
        self.dialog.wait_window()
    
    def ok_clicked(self):
        """Handle OK button click"""
        try:
            # Validate and collect dates
            new_dates = []
            for i, var in enumerate(self.date_vars):
                date_str = var.get().strip()
                if not date_str:
                    raise ValueError(f"Day {i+1} date is empty")
                
                # Try to parse the date to validate format
                try:
                    datetime.strptime(date_str, "%m/%d/%Y")
                except ValueError:
                    raise ValueError(f"Day {i+1} has invalid date format. Use MM/DD/YYYY")
                
                new_dates.append(date_str)
            
            self.result = new_dates
            self.dialog.destroy()
            
        except ValueError as e:
            messagebox.showerror("Invalid Date", str(e))
    
    def cancel_clicked(self):
        """Handle Cancel button click"""
        self.dialog.destroy()


if __name__ == "__main__":
    app = ClanWarTracker()
    app.run()

