#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DICOM to PNG Converter
Ứng dụng để chuyển đổi file DICOM (.dcm) thành ảnh PNG

Copyright (c) 2025 @Tins
All rights reserved.
"""

import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import pydicom
import numpy as np
from pathlib import Path


class DICOMToPNGConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DICOM Viewer Pro - @Tins")
        
        # Thiết lập kích thước cửa sổ phù hợp với màn hình
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Tính toán kích thước cửa sổ (45% màn hình, tối thiểu 800x600)
        window_width = max(800, int(screen_width * 0.45))
        window_height = max(600, int(screen_height * 0.75))
        
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.minsize(800, 600)  # Kích thước tối thiểu
        
        # Center window on screen
        self.center_window()
        
        # Cấu hình màu sắc hiện đại
        self.colors = {
            'primary': '#2E86AB',      # Xanh dương chính
            'secondary': '#A23B72',   # Tím hồng
            'accent': '#F18F01',      # Cam vàng
            'success': '#06D6A0',     # Xanh lá
            'danger': '#F72585',      # Đỏ hồng
            'light': '#F8F9FA',       # Xám nhạt
            'dark': '#212529',        # Đen
            'white': '#FFFFFF'        # Trắng
        }
        
        # Cấu hình style
        self.root.configure(bg=self.colors['light'])
        
        # Biến để lưu đường dẫn file
        self.input_files = []  # Danh sách file DICOM
        self.output_dir = tk.StringVar()
        
        self.setup_styles()
        self.setup_ui()
    
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def setup_styles(self):
        """Thiết lập style cho các widget"""
        style = ttk.Style()
        
        # Cấu hình style cho các widget
        style.configure('Title.TLabel', 
                       font=('Segoe UI', 24, 'bold'),
                       foreground=self.colors['primary'],
                       background=self.colors['light'])
        
        style.configure('Subtitle.TLabel',
                       font=('Segoe UI', 12),
                       foreground=self.colors['dark'],
                       background=self.colors['light'])
        
        style.configure('Modern.TButton',
                       font=('Segoe UI', 10, 'bold'),
                       padding=(15, 8))
        
        style.configure('Primary.TButton',
                       font=('Segoe UI', 12, 'bold'),
                       padding=(20, 10))
        
        style.configure('Success.TButton',
                       font=('Segoe UI', 11, 'bold'),
                       padding=(15, 8))
        
        style.configure('Modern.TFrame',
                       background=self.colors['light'])
        
        style.configure('Card.TFrame',
                       background=self.colors['white'],
                       relief='solid',
                       borderwidth=1)
        
        style.configure('Modern.TLabelFrame',
                       font=('Segoe UI', 11, 'bold'),
                       foreground=self.colors['primary'],
                       background=self.colors['light'])
        
        # Map styles để áp dụng
        style.map('Modern.TLabelFrame',
                 background=[('active', self.colors['light'])])
        
        style.configure('Modern.TCheckbutton',
                       font=('Segoe UI', 10),
                       background=self.colors['light'])
        
        style.configure('Modern.TLabel',
                       font=('Segoe UI', 10),
                       background=self.colors['light'])
        
        style.configure('Modern.TEntry',
                       font=('Segoe UI', 10),
                       padding=(8, 5))
        
    def setup_ui(self):
        """Thiết lập giao diện người dùng"""
        # Frame chính với scrollbar
        main_canvas = tk.Canvas(self.root, bg=self.colors['light'])
        main_scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=main_canvas.yview)
        scrollable_frame = ttk.Frame(main_canvas, style='Modern.TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"))
        )
        
        main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        main_canvas.configure(yscrollcommand=main_scrollbar.set)
        
        # Layout chính
        main_canvas.pack(side="left", fill="both", expand=True)
        main_scrollbar.pack(side="right", fill="y")
        
        # Frame chính với padding nhỏ hơn
        main_frame = ttk.Frame(scrollable_frame, style='Modern.TFrame', padding="8")
        main_frame.pack(fill="both", expand=True, padx=3, pady=3)
        
        # Cấu hình grid cho layout 2 cột
        main_frame.columnconfigure(0, weight=1)  # Cột trái
        main_frame.columnconfigure(1, weight=1)  # Cột phải
        main_frame.rowconfigure(1, weight=1)     # Cho phép listbox mở rộng
        
        # Header gọn gàng - span cả 2 cột
        header_frame = ttk.Frame(main_frame, style='Card.TFrame', padding="8")
        header_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 8))
        header_frame.columnconfigure(1, weight=1)
        
        # Title và subtitle gọn hơn
        title_label = ttk.Label(header_frame, text="DICOM Viewer Pro", 
                               style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 2))
        
        subtitle_label = ttk.Label(header_frame, text="Professional DICOM to PNG Converter", 
                                  style='Subtitle.TLabel')
        subtitle_label.grid(row=1, column=0, columnspan=2, pady=(0, 3))
        
        # Copyright gọn hơn
        copyright_label = ttk.Label(header_frame, text="© 2025 @Tins - All Rights Reserved", 
                                   font=('Segoe UI', 8, 'italic'),
                                   foreground=self.colors['secondary'],
                                   background=self.colors['white'])
        copyright_label.grid(row=2, column=0, columnspan=2)
        
        # File input selection - Cột trái
        input_card = ttk.LabelFrame(main_frame, text="📁 Select DICOM Files", padding="6")
        input_card.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=(0, 4), pady=(0, 6))
        input_card.columnconfigure(1, weight=1)
        
        ttk.Label(input_card, text="DICOM Files (.dcm):", style='Modern.TLabel').grid(row=0, column=0, sticky=tk.W, pady=2)
        ttk.Button(input_card, text="📂 Select Files", command=self.browse_multiple_files, 
                  style='Modern.TButton').grid(row=0, column=2, padx=(6, 0), pady=2)
        
        # Output directory - Cột phải
        output_card = ttk.LabelFrame(main_frame, text="📁 Output Directory", padding="6")
        output_card.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(4, 0), pady=(0, 6))
        output_card.columnconfigure(1, weight=1)
        
        ttk.Label(output_card, text="Save PNG files to:", style='Modern.TLabel').grid(row=0, column=0, sticky=tk.W, pady=2)
        ttk.Entry(output_card, textvariable=self.output_dir, style='Modern.TEntry').grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(6, 6), pady=2)
        ttk.Button(output_card, text="📂 Browse", command=self.browse_output_dir, 
                  style='Modern.TButton').grid(row=0, column=2, pady=2)
        
        # Listbox to display selected files - Span cả 2 cột
        listbox_card = ttk.LabelFrame(main_frame, text="📋 Selected Files", padding="6")
        listbox_card.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 6))
        listbox_card.columnconfigure(0, weight=1)
        listbox_card.rowconfigure(1, weight=1)
        
        self.file_count_label = ttk.Label(listbox_card, text="📊 Selected Files (0 files):", 
                                         font=('Segoe UI', 10, 'bold'),
                                         foreground=self.colors['primary'],
                                         background=self.colors['white'])
        self.file_count_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 4))
        
        # Create Listbox with Scrollbar - nhỏ hơn
        listbox_container = ttk.Frame(listbox_card)
        listbox_container.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 4))
        listbox_container.columnconfigure(0, weight=1)
        listbox_container.rowconfigure(0, weight=1)
        
        self.file_listbox = tk.Listbox(listbox_container, height=5, font=('Segoe UI', 9),
                                      bg=self.colors['white'], fg=self.colors['dark'],
                                      selectbackground=self.colors['primary'],
                                      selectforeground=self.colors['white'])
        scrollbar = ttk.Scrollbar(listbox_container, orient=tk.VERTICAL, command=self.file_listbox.yview)
        self.file_listbox.configure(yscrollcommand=scrollbar.set)
        
        self.file_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 3))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Remove file buttons - gọn hơn
        button_frame = ttk.Frame(listbox_card)
        button_frame.grid(row=2, column=0, columnspan=2, pady=(4, 0))
        
        ttk.Button(button_frame, text="🗑️ Remove Selected", command=self.remove_selected_file,
                  style='Modern.TButton').grid(row=0, column=0, padx=(0, 4))
        ttk.Button(button_frame, text="🧹 Clear All", command=self.clear_all_files,
                  style='Modern.TButton').grid(row=0, column=1, padx=(4, 0))
        
        # Bind keyboard shortcuts
        self.file_listbox.bind('<Delete>', lambda e: self.remove_selected_file())
        self.file_listbox.bind('<BackSpace>', lambda e: self.remove_selected_file())
        
        # Context menu for right-click
        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Remove Selected", command=self.remove_selected_file)
        self.context_menu.add_command(label="Clear All", command=self.clear_all_files)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Refresh List", command=self.refresh_file_list)
        
        self.file_listbox.bind('<Button-3>', self.show_context_menu)  # Right-click
        
        # Options - Cột trái
        options_card = ttk.LabelFrame(main_frame, text="⚙️ Conversion Options", padding="6")
        options_card.grid(row=3, column=0, sticky=(tk.W, tk.E), padx=(0, 4), pady=(0, 6))
        options_card.columnconfigure(1, weight=1)
        
        # Normalize checkbox
        self.normalize_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_card, text="✨ Normalize pixel values (0-255)", 
                       variable=self.normalize_var, style='Modern.TCheckbutton').grid(row=0, column=0, sticky=tk.W, pady=2)
        
        # Invert checkbox
        self.invert_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(options_card, text="🔄 Invert colors", 
                       variable=self.invert_var, style='Modern.TCheckbutton').grid(row=1, column=0, sticky=tk.W, pady=2)
        
        # Quality slider - gọn hơn
        ttk.Label(options_card, text="🎨 PNG Quality:", style='Modern.TLabel').grid(row=2, column=0, sticky=tk.W, pady=(6, 0))
        self.quality_var = tk.IntVar(value=95)
        quality_scale = ttk.Scale(options_card, from_=50, to=100, variable=self.quality_var, 
                                 orient=tk.HORIZONTAL)
        quality_scale.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(6, 0), pady=(6, 0))
        
        # Progress bar - Cột phải
        progress_card = ttk.LabelFrame(main_frame, text="📊 Progress", padding="6")
        progress_card.grid(row=3, column=1, sticky=(tk.W, tk.E), padx=(4, 0), pady=(0, 6))
        progress_card.columnconfigure(0, weight=1)
        
        self.progress = ttk.Progressbar(progress_card, mode='determinate')
        self.progress.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 4))
        
        # Status label - gọn hơn
        self.status_label = ttk.Label(progress_card, text="✅ Ready to convert", 
                                    font=('Segoe UI', 10, 'bold'),
                                    foreground=self.colors['success'],
                                    background=self.colors['white'])
        self.status_label.grid(row=1, column=0, pady=(0, 2))
        
        # Additional info - gọn hơn
        info_label = ttk.Label(progress_card, text="💡 Tip: Select multiple DICOM files for batch processing", 
                              font=('Segoe UI', 8),
                              foreground=self.colors['secondary'],
                              background=self.colors['white'])
        info_label.grid(row=2, column=0, pady=(2, 0))
        
        # Convert button - Span cả 2 cột
        convert_button = ttk.Button(main_frame, text="🚀 Convert DICOM to PNG", 
                                   command=self.convert_dicom_to_png, style='Primary.TButton')
        convert_button.grid(row=4, column=0, columnspan=2, pady=12)
        
    def browse_multiple_files(self):
        """Select DICOM files (single or multiple)"""
        filenames = filedialog.askopenfilenames(
            title="Select DICOM Files",
            filetypes=[("DICOM files", "*.dcm"), ("All files", "*.*")]
        )
        for filename in filenames:
            self.add_file_to_list(filename)
    
    def add_file_to_list(self, filename):
        """Add file to the list"""
        if filename not in self.input_files:
            self.input_files.append(filename)
            self.file_listbox.insert(tk.END, os.path.basename(filename))
            self.update_file_count()
            # Auto-set output directory
            if not self.output_dir.get():
                self.output_dir.set(os.path.dirname(filename))
    
    def remove_selected_file(self):
        """Remove selected file from the list"""
        selection = self.file_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a file to remove.")
            return
        
        index = selection[0]
        filename = self.file_listbox.get(index)
        
        # Confirm removal
        if messagebox.askyesno("Confirm Removal", f"Remove '{filename}' from the list?"):
            self.file_listbox.delete(index)
            del self.input_files[index]
            self.update_file_count()
    
    def clear_all_files(self):
        """Clear all files from the list"""
        if not self.input_files:
            messagebox.showinfo("Info", "No files to clear.")
            return
        
        count = len(self.input_files)
        if messagebox.askyesno("Confirm Clear All", f"Remove all {count} files from the list?"):
            self.file_listbox.delete(0, tk.END)
            self.input_files.clear()
            self.update_file_count()
    
    def update_file_count(self):
        """Update the file count display"""
        count = len(self.input_files)
        self.file_count_label.config(text=f"📊 Selected Files ({count} files):")
    
    def show_context_menu(self, event):
        """Show context menu on right-click"""
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()
    
    def refresh_file_list(self):
        """Refresh the file list to check if files still exist"""
        files_to_remove = []
        
        for i, file_path in enumerate(self.input_files):
            if not os.path.exists(file_path):
                files_to_remove.append(i)
        
        if files_to_remove:
            # Remove non-existent files (in reverse order to maintain indices)
            for i in reversed(files_to_remove):
                self.file_listbox.delete(i)
                del self.input_files[i]
            
            self.update_file_count()
            messagebox.showinfo("Refresh Complete", 
                              f"Removed {len(files_to_remove)} non-existent files from the list.")
        else:
            messagebox.showinfo("Refresh Complete", "All files are still valid.")
    
    def browse_output_dir(self):
        """Select output directory for PNG files"""
        dirname = filedialog.askdirectory(title="Select Output Directory")
        if dirname:
            self.output_dir.set(dirname)
    
    def normalize_pixel_array(self, pixel_array):
        """Normalize pixel array to 0-255 range"""
        # Remove negative values and normalize
        pixel_array = np.maximum(pixel_array, 0)
        
        # Normalize to 0-255 range
        if pixel_array.max() > pixel_array.min():
            pixel_array = ((pixel_array - pixel_array.min()) / 
                          (pixel_array.max() - pixel_array.min()) * 255)
        
        return pixel_array.astype(np.uint8)
    
    def convert_dicom_to_png(self):
        """Convert DICOM files to PNG (Batch processing)"""
        try:
            # Check input
            if not self.input_files:
                messagebox.showerror("Error", "Please select at least one DICOM file!")
                return
            
            if not self.output_dir.get():
                messagebox.showerror("Error", "Please select an output directory!")
                return
            
            # Check if output directory exists
            if not os.path.exists(self.output_dir.get()):
                messagebox.showerror("Error", "Output directory does not exist!")
                return
            
            # Setup progress bar
            self.progress['maximum'] = len(self.input_files)
            self.progress['value'] = 0
            
            # Start conversion
            self.status_label.config(text="🔄 Converting...", foreground=self.colors['primary'])
            self.root.update()
            
            success_count = 0
            error_count = 0
            
            for i, input_file in enumerate(self.input_files):
                try:
                    # Update status
                    filename = os.path.basename(input_file)
                    self.status_label.config(text=f"⚙️ Processing: {filename} ({i+1}/{len(self.input_files)})", 
                                           foreground=self.colors['primary'])
                    self.root.update()
                    
                    # Check if file exists
                    if not os.path.exists(input_file):
                        print(f"File does not exist: {input_file}")
                        error_count += 1
                        continue
                    
                    # Read DICOM file
                    dicom_file = pydicom.dcmread(input_file, force=True)
                    
                    # Get pixel data
                    pixel_array = dicom_file.pixel_array
                    
                    # Normalize pixel values if selected
                    if self.normalize_var.get():
                        pixel_array = self.normalize_pixel_array(pixel_array)
                    else:
                        # Convert to uint8 if needed
                        if pixel_array.dtype != np.uint8:
                            pixel_array = pixel_array.astype(np.uint8)
                    
                    # Invert colors if selected
                    if self.invert_var.get():
                        pixel_array = 255 - pixel_array
                    
                    # Create output filename
                    input_path = Path(input_file)
                    output_filename = input_path.stem + ".png"
                    output_path = os.path.join(self.output_dir.get(), output_filename)
                    
                    # Convert to PIL Image
                    if len(pixel_array.shape) == 2:  # Grayscale
                        image = Image.fromarray(pixel_array, mode='L')
                    elif len(pixel_array.shape) == 3:  # Color
                        image = Image.fromarray(pixel_array, mode='RGB')
                    else:
                        raise ValueError("Unsupported image format")
                    
                    # Save PNG file
                    image.save(output_path, "PNG", optimize=True, 
                              compress_level=int(100 - self.quality_var.get()))
                    
                    success_count += 1
                    print(f"✓ Converted: {output_filename}")
                    
                except Exception as e:
                    error_count += 1
                    print(f"✗ Error converting {filename}: {str(e)}")
                
                # Update progress bar
                self.progress['value'] = i + 1
                self.root.update()
            
            # Complete
            if error_count == 0:
                self.status_label.config(text=f"✅ Complete! Successfully converted {success_count} files", 
                                       foreground=self.colors['success'])
            else:
                self.status_label.config(text=f"⚠️ Complete! Success: {success_count}, Errors: {error_count}", 
                                       foreground=self.colors['danger'])
            
            if success_count > 0:
                messagebox.showinfo("Complete", 
                                  f"Successfully converted {success_count}/{len(self.input_files)} files!\n"
                                  f"Output directory: {self.output_dir.get()}")
            
            if error_count > 0:
                messagebox.showwarning("Errors", 
                                     f"{error_count} files encountered errors during conversion.\n"
                                     f"Please check console for details.")
            
        except Exception as e:
            self.status_label.config(text="❌ Error during conversion", 
                                   foreground=self.colors['danger'])
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def run(self):
        """Run the application"""
        self.root.mainloop()


def main():
    """Main function"""
    print("=" * 50)
    print("    DICOM Viewer Pro - Professional Converter")
    print("    Copyright (c) 2025 @Tins")
    print("    All Rights Reserved")
    print("=" * 50)
    
    # Check required libraries
    try:
        import pydicom
        import PIL
        import numpy as np
    except ImportError as e:
        print(f"Error: Missing required library - {e}")
        print("Please install: pip install -r requirements.txt")
        return
    
    # Run GUI
    app = DICOMToPNGConverter()
    app.run()


if __name__ == "__main__":
    main()
