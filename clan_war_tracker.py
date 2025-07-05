#!/usr/bin/env python3
"""
Clan War Tracker - Enhanced version with prize picker and improved GUI
Version 1.2 - Prize Picker System and GUI Improvements
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Any

class ClanWarTracker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Clan War Tracker v1.2")
        self.root.geometry("1400x800")
        self.root.minsize(1200, 700)
        
        # Application data
        self.participants = []
        self.squads = []
        self.prize_pool = tk.DoubleVar(value=0.0)
        self.war_dates = self.generate_war_dates()
        
        # Prize system data
        self.prize_mode = tk.StringVar(value="equal")  # "equal" or "ranked"
        self.ranked_prizes = []  # List of prize amounts for ranks
        
        # UI Variables
        self.participant_vars = {}
        self.date_vars = []
        
        # Paned window variables for resizable sections
        self.main_paned = None
        self.prize_paned = None
        
        self.setup_ui()
        self.setup_styles()
        self.initialize_ranked_prizes()
        
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
    
    def setup_styles(self):
        """Configure modern styling for the application"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors for modern look
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), foreground='#2c3e50')
        style.configure('Heading.TLabel', font=('Arial', 12, 'bold'), foreground='#34495e')
        style.configure('Modern.TButton', padding=8, font=('Arial', 10))
        style.configure('Small.TButton', padding=4, font=('Arial', 9))
        style.configure('Prize.TButton', padding=6, font=('Arial', 10, 'bold'))
        
        # Configure notebook styling
        style.configure('TNotebook.Tab', padding=[20, 8])
        
        # Configure frame styling
        style.configure('Card.TFrame', relief='raised', borderwidth=1)
        style.configure('Prize.TLabelframe', font=('Arial', 11, 'bold'))
        
    def setup_ui(self):
        """Setup the main user interface"""
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create tabs
        self.war_frame = ttk.Frame(self.notebook)
        self.roster_frame = ttk.Frame(self.notebook)
        
        self.notebook.add(self.war_frame, text="🏆 Clan War Tracker")
        self.notebook.add(self.roster_frame, text="👥 Roster Manager")
        
        self.setup_war_tab()
        self.setup_roster_tab()
        
    def setup_war_tab(self):
        """Setup the clan war tracking tab with resizable panes"""
        # Main paned window for resizable sections
        self.main_paned = ttk.PanedWindow(self.war_frame, orient='horizontal')
        self.main_paned.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Left panel for participant and prize management
        left_container = ttk.Frame(self.main_paned)
        self.main_paned.add(left_container, weight=1)
        
        # Create vertical paned window for left side
        left_paned = ttk.PanedWindow(left_container, orient='vertical')
        left_paned.pack(fill='both', expand=True)
        
        # Participant management section
        participant_frame = ttk.LabelFrame(left_paned, text="👤 Participant Management", padding=10, style='Prize.TLabelframe')
        left_paned.add(participant_frame, weight=1)
        
        self.setup_participant_section(participant_frame)
        
        # Prize management section
        prize_frame = ttk.LabelFrame(left_paned, text="💰 Prize Management", padding=10, style='Prize.TLabelframe')
        left_paned.add(prize_frame, weight=1)
        
        self.setup_prize_section(prize_frame)
        
        # Right panel for attendance tracking
        right_container = ttk.Frame(self.main_paned)
        self.main_paned.add(right_container, weight=2)
        
        self.setup_attendance_section(right_container)
        
        # Bottom panel for actions and results
        self.setup_bottom_section()
        
    def setup_participant_section(self, parent):
        """Setup participant management section"""
        # Participant entry
        ttk.Label(parent, text="Add Participant:", style='Heading.TLabel').pack(anchor='w', pady=(0, 5))
        
        entry_frame = ttk.Frame(parent)
        entry_frame.pack(fill='x', pady=(0, 10))
        
        self.participant_entry = ttk.Entry(entry_frame, font=('Arial', 10))
        self.participant_entry.pack(side='left', fill='x', expand=True)
        self.participant_entry.bind('<Return>', self.add_participant)
        
        add_btn = ttk.Button(entry_frame, text="➕ Add", command=self.add_participant, style='Modern.TButton')
        add_btn.pack(side='right', padx=(5, 0))
        
        # Participant list with improved scrollbar
        ttk.Label(parent, text="Participants:", style='Heading.TLabel').pack(anchor='w', pady=(0, 5))
        
        list_container = ttk.Frame(parent)
        list_container.pack(fill='both', expand=True)
        
        # Create custom scrollbar frame
        list_frame = ttk.Frame(list_container, style='Card.TFrame')
        list_frame.pack(fill='both', expand=True)
        
        self.participant_listbox = tk.Listbox(list_frame, selectmode='single', 
                                            font=('Arial', 10), relief='flat',
                                            highlightthickness=0, borderwidth=0)
        
        # Enhanced scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=self.participant_listbox.yview)
        self.participant_listbox.configure(yscrollcommand=scrollbar.set)
        
        self.participant_listbox.pack(side='left', fill='both', expand=True, padx=2, pady=2)
        scrollbar.pack(side='right', fill='y', padx=(0, 2), pady=2)
        
        # Remove participant button
        remove_btn = ttk.Button(parent, text="🗑️ Remove Selected", 
                               command=self.remove_participant, style='Modern.TButton')
        remove_btn.pack(pady=(10, 0))
        
    def setup_prize_section(self, parent):
        """Setup prize management section"""
        # Prize mode selection
        mode_frame = ttk.Frame(parent)
        mode_frame.pack(fill='x', pady=(0, 10))
        
        ttk.Label(mode_frame, text="Prize Distribution Mode:", style='Heading.TLabel').pack(anchor='w')
        
        mode_radio_frame = ttk.Frame(mode_frame)
        mode_radio_frame.pack(fill='x', pady=5)
        
        ttk.Radiobutton(mode_radio_frame, text="Equal Distribution", variable=self.prize_mode, 
                       value="equal", command=self.on_prize_mode_change).pack(anchor='w')
        ttk.Radiobutton(mode_radio_frame, text="Ranked Prizes", variable=self.prize_mode, 
                       value="ranked", command=self.on_prize_mode_change).pack(anchor='w')
        
        # Prize configuration container
        self.prize_config_frame = ttk.Frame(parent)
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
        ttk.Label(self.prize_config_frame, text="Total Prize Pool:", style='Heading.TLabel').pack(anchor='w', pady=(0, 5))
        
        prize_frame = ttk.Frame(self.prize_config_frame)
        prize_frame.pack(fill='x')
        
        ttk.Label(prize_frame, text="$", font=('Arial', 12, 'bold')).pack(side='left')
        self.prize_entry = ttk.Entry(prize_frame, textvariable=self.prize_pool, font=('Arial', 11))
        self.prize_entry.pack(side='left', fill='x', expand=True)
        
    def setup_ranked_prize_config(self):
        """Setup ranked prizes configuration"""
        ttk.Label(self.prize_config_frame, text="Ranked Prize Structure:", style='Heading.TLabel').pack(anchor='w', pady=(0, 5))
        
        # Scrollable frame for ranked prizes
        canvas = tk.Canvas(self.prize_config_frame, height=200)
        scrollbar = ttk.Scrollbar(self.prize_config_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create prize entries
        self.ranked_prize_vars = []
        for i, prize in enumerate(self.ranked_prizes):
            prize_frame = ttk.Frame(scrollable_frame)
            prize_frame.pack(fill='x', pady=2)
            
            ttk.Label(prize_frame, text=f"{prize['label']}:", width=12, 
                     font=('Arial', 10, 'bold')).pack(side='left')
            
            ttk.Label(prize_frame, text="$").pack(side='left', padx=(5, 0))
            
            var = tk.IntVar(value=prize['amount'])
            entry = ttk.Entry(prize_frame, textvariable=var, width=12, font=('Arial', 10))
            entry.pack(side='left', padx=(0, 5))
            entry.bind('<KeyRelease>', lambda e, idx=i: self.update_ranked_prize(idx, var.get()))
            
            self.ranked_prize_vars.append(var)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Add/Remove rank buttons
        rank_btn_frame = ttk.Frame(self.prize_config_frame)
        rank_btn_frame.pack(fill='x', pady=(5, 0))
        
        ttk.Button(rank_btn_frame, text="➕ Add Rank", 
                  command=self.add_rank, style='Small.TButton').pack(side='left', padx=(0, 5))
        ttk.Button(rank_btn_frame, text="➖ Remove Last", 
                  command=self.remove_rank, style='Small.TButton').pack(side='left')
        
    def setup_attendance_section(self, parent):
        """Setup attendance tracking section"""
        attendance_frame = ttk.LabelFrame(parent, text="📅 Attendance Tracking (14 Days)", 
                                        padding=10, style='Prize.TLabelframe')
        attendance_frame.pack(fill='both', expand=True)
        
        # Date management section
        date_mgmt_frame = ttk.Frame(attendance_frame)
        date_mgmt_frame.pack(fill='x', pady=(0, 10))
        
        ttk.Label(date_mgmt_frame, text="Date Management:", style='Heading.TLabel').pack(side='left')
        ttk.Button(date_mgmt_frame, text="📝 Edit Dates", 
                  command=self.edit_dates, style='Small.TButton').pack(side='left', padx=(10, 5))
        ttk.Button(date_mgmt_frame, text="🔄 Reset to Today", 
                  command=self.reset_dates, style='Small.TButton').pack(side='left')
        
        # Attendance grid container
        self.attendance_container = ttk.Frame(attendance_frame)
        self.attendance_container.pack(fill='both', expand=True)
        
    def setup_bottom_section(self):
        """Setup bottom section with actions and results"""
        bottom_frame = ttk.Frame(self.war_frame)
        bottom_frame.pack(fill='x', padx=5, pady=5)
        
        # Action buttons
        button_frame = ttk.Frame(bottom_frame)
        button_frame.pack(fill='x', pady=(0, 10))
        
        ttk.Button(button_frame, text="🧮 Calculate Payouts", 
                  command=self.calculate_payouts, style='Prize.TButton').pack(side='left', padx=(0, 10))
        ttk.Button(button_frame, text="📤 Export Results", 
                  command=self.export_results, style='Modern.TButton').pack(side='left', padx=(0, 10))
        ttk.Button(button_frame, text="💾 Save Data", 
                  command=self.save_data, style='Modern.TButton').pack(side='left', padx=(0, 10))
        ttk.Button(button_frame, text="📁 Load Data", 
                  command=self.load_data, style='Modern.TButton').pack(side='left')
        
        # Results display with enhanced scrollbar
        results_frame = ttk.LabelFrame(bottom_frame, text="📊 Calculation Results", 
                                     padding=5, style='Prize.TLabelframe')
        results_frame.pack(fill='both', expand=True)
        
        text_container = ttk.Frame(results_frame)
        text_container.pack(fill='both', expand=True)
        
        self.results_text = tk.Text(text_container, height=8, wrap='word', 
                                   font=('Consolas', 10), relief='flat',
                                   highlightthickness=0, borderwidth=0)
        
        results_scrollbar = ttk.Scrollbar(text_container, orient='vertical', command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=results_scrollbar.set)
        
        self.results_text.pack(side='left', fill='both', expand=True, padx=2, pady=2)
        results_scrollbar.pack(side='right', fill='y', padx=(0, 2), pady=2)
        
    def on_prize_mode_change(self):
        """Handle prize mode change"""
        self.setup_prize_config()
        
    def update_ranked_prize(self, index, value):
        """Update ranked prize amount"""
        try:
            if 0 <= index < len(self.ranked_prizes):
                self.ranked_prizes[index]['amount'] = int(value)
        except (ValueError, TypeError):
            pass  # Ignore invalid input
    
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
    
    def setup_roster_tab(self):
        """Setup the roster management tab"""
        # Main container with paned window
        roster_paned = ttk.PanedWindow(self.roster_frame, orient='horizontal')
        roster_paned.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Left panel for squad management
        left_panel = ttk.LabelFrame(roster_paned, text="👥 Squad Management", 
                                  padding=10, style='Prize.TLabelframe')
        roster_paned.add(left_panel, weight=1)
        
        # Squad creation
        ttk.Label(left_panel, text="Create Squad:", style='Heading.TLabel').pack(anchor='w')
        
        squad_entry_frame = ttk.Frame(left_panel)
        squad_entry_frame.pack(fill='x', pady=5)
        
        self.squad_entry = ttk.Entry(squad_entry_frame, font=('Arial', 10))
        self.squad_entry.pack(side='left', fill='x', expand=True)
        self.squad_entry.bind('<Return>', self.add_squad)
        
        add_squad_btn = ttk.Button(squad_entry_frame, text="➕ Add", 
                                  command=self.add_squad, style='Modern.TButton')
        add_squad_btn.pack(side='right', padx=(5, 0))
        
        # Squad list with enhanced scrollbar
        ttk.Label(left_panel, text="Squads:", style='Heading.TLabel').pack(anchor='w', pady=(15, 5))
        
        squad_list_container = ttk.Frame(left_panel, style='Card.TFrame')
        squad_list_container.pack(fill='both', expand=True)
        
        self.squad_listbox = tk.Listbox(squad_list_container, selectmode='single',
                                       font=('Arial', 10), relief='flat',
                                       highlightthickness=0, borderwidth=0)
        squad_scrollbar = ttk.Scrollbar(squad_list_container, orient='vertical', command=self.squad_listbox.yview)
        self.squad_listbox.configure(yscrollcommand=squad_scrollbar.set)
        self.squad_listbox.bind('<<ListboxSelect>>', self.on_squad_select)
        
        self.squad_listbox.pack(side='left', fill='both', expand=True, padx=2, pady=2)
        squad_scrollbar.pack(side='right', fill='y', padx=(0, 2), pady=2)
        
        # Squad management buttons
        squad_btn_frame = ttk.Frame(left_panel)
        squad_btn_frame.pack(fill='x', pady=5)
        
        ttk.Button(squad_btn_frame, text="✏️ Rename", 
                  command=self.rename_squad, style='Modern.TButton').pack(side='left', padx=(0, 5))
        ttk.Button(squad_btn_frame, text="🗑️ Delete", 
                  command=self.delete_squad, style='Modern.TButton').pack(side='left')
        
        # Right panel for squad details
        right_panel = ttk.LabelFrame(roster_paned, text="📋 Squad Details", 
                                   padding=10, style='Prize.TLabelframe')
        roster_paned.add(right_panel, weight=2)
        
        self.squad_details_frame = ttk.Frame(right_panel)
        self.squad_details_frame.pack(fill='both', expand=True)
        
        # Initially show instructions
        ttk.Label(self.squad_details_frame, 
                 text="Select a squad from the left to view and manage members",
                 style='Heading.TLabel').pack(expand=True)
    
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
    
    def refresh_attendance_grid(self):
        """Refresh the attendance tracking grid with enhanced styling"""
        # Clear existing grid
        for widget in self.attendance_container.winfo_children():
            widget.destroy()
        
        if not self.participants:
            ttk.Label(self.attendance_container, 
                     text="Add participants to start tracking attendance",
                     style='Heading.TLabel').pack(expand=True)
            return
        
        # Create main frame for the grid with enhanced styling
        main_frame = ttk.Frame(self.attendance_container, style='Card.TFrame')
        main_frame.pack(fill='both', expand=True, padx=2, pady=2)
        
        # Create canvas and enhanced scrollbars
        canvas = tk.Canvas(main_frame, relief='flat', highlightthickness=0, borderwidth=0)
        v_scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        h_scrollbar = ttk.Scrollbar(main_frame, orient="horizontal", command=canvas.xview)
        
        # Create scrollable frame
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Configure grid weights for proper alignment
        scrollable_frame.grid_columnconfigure(0, weight=0, minsize=150)
        for i in range(14):
            scrollable_frame.grid_columnconfigure(i+1, weight=0, minsize=80)
        scrollable_frame.grid_columnconfigure(15, weight=0, minsize=60)
        
        # Create header row with enhanced styling
        header_style = {'font': ('Arial', 11, 'bold'), 'foreground': '#2c3e50'}
        
        ttk.Label(scrollable_frame, text="Participant", style='Heading.TLabel', 
                 anchor='w').grid(row=0, column=0, padx=5, pady=8, sticky='ew')
        
        for i, date in enumerate(self.war_dates):
            short_date = date.split('/')[0] + '/' + date.split('/')[1]
            ttk.Label(scrollable_frame, text=short_date, style='Heading.TLabel', 
                     anchor='center').grid(row=0, column=i+1, padx=2, pady=8, sticky='ew')
        
        ttk.Label(scrollable_frame, text="Total", style='Heading.TLabel', 
                 anchor='center').grid(row=0, column=15, padx=5, pady=8, sticky='ew')
        
        # Create rows for each participant with alternating colors
        self.participant_vars = {}
        for row, participant in enumerate(self.participants, 1):
            # Participant name with enhanced styling
            name_label = ttk.Label(scrollable_frame, text=participant['name'], 
                                 anchor='w', font=('Arial', 10))
            name_label.grid(row=row, column=0, padx=5, pady=4, sticky='ew')
            
            # Attendance checkboxes
            self.participant_vars[participant['name']] = []
            for day in range(14):
                var = tk.BooleanVar(value=participant['attendance'][day])
                checkbox = ttk.Checkbutton(scrollable_frame, variable=var, 
                                         command=lambda p=participant['name'], d=day, v=var: self.update_attendance(p, d, v))
                checkbox.grid(row=row, column=day+1, padx=2, pady=4)
                self.participant_vars[participant['name']].append(var)
            
            # Total days label
            total_label = ttk.Label(scrollable_frame, text=str(participant['total_days']), 
                                   anchor='center', font=('Arial', 10, 'bold'))
            total_label.grid(row=row, column=15, padx=5, pady=4, sticky='ew')
        
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
            'rank': 0
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
    
    def calculate_payouts(self):
        """Calculate and display prize distribution based on selected mode"""
        if not self.participants:
            messagebox.showwarning("No Participants", "Add participants before calculating payouts.")
            return
        
        if self.prize_mode.get() == "equal":
            self.calculate_equal_payouts()
        else:
            self.calculate_ranked_payouts()
    
    def calculate_equal_payouts(self):
        """Calculate equal distribution payouts"""
        prize_total = self.prize_pool.get()
        if prize_total <= 0:
            messagebox.showwarning("Invalid Prize Pool", "Enter a valid prize pool amount.")
            return
        
        # Calculate total attendance days
        total_attendance_days = sum(p['total_days'] for p in self.participants)
        
        if total_attendance_days == 0:
            messagebox.showwarning("No Attendance", "No attendance recorded for any participant.")
            return
        
        # Calculate per-day value
        per_day_value = prize_total / total_attendance_days
        
        # Calculate individual payouts
        results = []
        results.append("EQUAL DISTRIBUTION CALCULATION")
        results.append("=" * 60)
        results.append(f"War Period: {self.war_dates[0]} to {self.war_dates[-1]}")
        results.append(f"Total Prize Pool: ${prize_total:,.2f}")
        results.append(f"Total Attendance Days: {total_attendance_days}")
        results.append(f"Value per Day: ${per_day_value:,.2f}")
        results.append("")
        results.append("INDIVIDUAL PAYOUTS:")
        results.append("-" * 60)
        
        for participant in self.participants:
            payout = participant['total_days'] * per_day_value
            participant['payout'] = payout
            results.append(f"{participant['name']:<25} {participant['total_days']:>2} days  ${payout:>12,.2f}")
        
        results.append("-" * 60)
        total_paid = sum(p['payout'] for p in self.participants)
        results.append(f"{'TOTAL PAID:':<25} {total_attendance_days:>2} days  ${total_paid:>12,.2f}")
        
        # Display results
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(1.0, "\n".join(results))
    
    def calculate_ranked_payouts(self):
        """Calculate ranked prize distribution"""
        # Sort participants by attendance (descending)
        sorted_participants = sorted(self.participants, key=lambda p: p['total_days'], reverse=True)
        
        # Assign ranks and prizes
        results = []
        results.append("RANKED PRIZE DISTRIBUTION")
        results.append("=" * 60)
        results.append(f"War Period: {self.war_dates[0]} to {self.war_dates[-1]}")
        results.append("")
        results.append("PRIZE STRUCTURE:")
        results.append("-" * 30)
        
        total_prizes = 0
        for prize in self.ranked_prizes:
            results.append(f"{prize['label']:<15} ${prize['amount']:>12,}")
            total_prizes += prize['amount']
        
        results.append(f"{'Total Prizes:':<15} ${total_prizes:>12,}")
        results.append("")
        results.append("RANKINGS AND PAYOUTS:")
        results.append("-" * 60)
        
        # Assign payouts based on ranking
        current_rank = 1
        prev_attendance = None
        
        for i, participant in enumerate(sorted_participants):
            # Handle ties - participants with same attendance get same rank
            if prev_attendance is not None and participant['total_days'] != prev_attendance:
                current_rank = i + 1
            
            participant['rank'] = current_rank
            
            # Assign prize based on rank
            if current_rank <= len(self.ranked_prizes):
                participant['payout'] = self.ranked_prizes[current_rank - 1]['amount']
                rank_label = self.ranked_prizes[current_rank - 1]['label']
            else:
                participant['payout'] = 0
                rank_label = f"{self.get_ordinal(current_rank)} Place"
            
            results.append(f"{rank_label:<15} {participant['name']:<20} {participant['total_days']:>2} days  ${participant['payout']:>12,}")
            prev_attendance = participant['total_days']
        
        # Show participants who didn't place
        unranked = [p for p in sorted_participants if p['rank'] > len(self.ranked_prizes)]
        if unranked:
            results.append("")
            results.append("UNRANKED PARTICIPANTS:")
            results.append("-" * 40)
            for participant in unranked:
                results.append(f"{participant['name']:<25} {participant['total_days']:>2} days  $0")
        
        results.append("")
        results.append("-" * 60)
        total_paid = sum(p['payout'] for p in self.participants)
        results.append(f"{'TOTAL PAID:':<25} ${total_paid:>12,}")
        
        # Display results
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(1.0, "\n".join(results))
    
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
                with open(filename, 'w') as f:
                    f.write(self.results_text.get(1.0, tk.END))
                messagebox.showinfo("Export Successful", f"Results exported to {filename}")
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export results: {str(e)}")
    
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
        """Refresh the squad details panel"""
        # Clear existing content
        for widget in self.squad_details_frame.winfo_children():
            widget.destroy()
        
        selection = self.squad_listbox.curselection()
        if not selection:
            ttk.Label(self.squad_details_frame, 
                     text="Select a squad from the left to view and manage members",
                     style='Heading.TLabel').pack(expand=True)
            return
        
        squad_index = selection[0]
        squad = self.squads[squad_index]
        
        # Squad name header
        ttk.Label(self.squad_details_frame, text=f"Squad: {squad['name']}", 
                 style='Title.TLabel').pack(pady=(0, 15))
        
        # Available participants section
        available_frame = ttk.LabelFrame(self.squad_details_frame, text="Available Participants", 
                                       padding=10, style='Prize.TLabelframe')
        available_frame.pack(fill='x', pady=(0, 10))
        
        available_participants = [p['name'] for p in self.participants if p['name'] not in squad['members']]
        
        if available_participants:
            for participant in available_participants:
                participant_frame = ttk.Frame(available_frame)
                participant_frame.pack(fill='x', pady=3)
                
                ttk.Label(participant_frame, text=participant, font=('Arial', 10)).pack(side='left')
                ttk.Button(participant_frame, text="➕ Add to Squad", 
                          command=lambda p=participant: self.add_to_squad(squad_index, p),
                          style='Small.TButton').pack(side='right')
        else:
            ttk.Label(available_frame, text="No available participants", 
                     font=('Arial', 10, 'italic')).pack()
        
        # Squad members section
        members_frame = ttk.LabelFrame(self.squad_details_frame, text="Squad Members", 
                                     padding=10, style='Prize.TLabelframe')
        members_frame.pack(fill='both', expand=True)
        
        if squad['members']:
            for member in squad['members']:
                member_frame = ttk.Frame(members_frame)
                member_frame.pack(fill='x', pady=3)
                
                ttk.Label(member_frame, text=member, font=('Arial', 10)).pack(side='left')
                ttk.Button(member_frame, text="➖ Remove", 
                          command=lambda m=member: self.remove_from_squad(squad_index, m),
                          style='Small.TButton').pack(side='right')
        else:
            ttk.Label(members_frame, text="No members assigned", 
                     font=('Arial', 10, 'italic')).pack()
    
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


class DateEditDialog:
    """Dialog for editing war dates"""
    
    def __init__(self, parent, current_dates):
        self.result = None
        
        # Create dialog window
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Edit War Dates")
        self.dialog.geometry("450x550")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Center the dialog
        self.dialog.geometry("+%d+%d" % (parent.winfo_rootx() + 50, parent.winfo_rooty() + 50))
        
        # Main frame
        main_frame = ttk.Frame(self.dialog, padding=15)
        main_frame.pack(fill='both', expand=True)
        
        # Instructions
        ttk.Label(main_frame, text="Edit the dates for the 14-day war period:", 
                 font=('Arial', 12, 'bold')).pack(pady=(0, 10))
        ttk.Label(main_frame, text="Format: MM/DD/YYYY", 
                 font=('Arial', 10, 'italic')).pack(pady=(0, 15))
        
        # Scrollable frame for date entries
        canvas = tk.Canvas(main_frame, relief='flat', highlightthickness=0)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create date entry fields
        self.date_vars = []
        for i, date in enumerate(current_dates):
            frame = ttk.Frame(scrollable_frame)
            frame.pack(fill='x', pady=3)
            
            ttk.Label(frame, text=f"Day {i+1}:", width=8, 
                     font=('Arial', 10, 'bold')).pack(side='left')
            
            var = tk.StringVar(value=date)
            entry = ttk.Entry(frame, textvariable=var, width=15, font=('Arial', 10))
            entry.pack(side='left', padx=(10, 0))
            
            self.date_vars.append(var)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill='x', pady=(15, 0))
        
        ttk.Button(button_frame, text="✅ OK", command=self.ok_clicked,
                  style='Modern.TButton').pack(side='right', padx=(10, 0))
        ttk.Button(button_frame, text="❌ Cancel", command=self.cancel_clicked,
                  style='Modern.TButton').pack(side='right')
        
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

