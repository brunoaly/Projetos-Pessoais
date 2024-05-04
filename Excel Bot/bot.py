import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

def add_justification_and_filter(input_file, output_file):
    df = pd.read_excel(input_file)
    
    # Check if "ARQ" column exists in DataFrame
    if "ARQ" in df.columns:
        # Select rows where the "ARQ" field is empty
        condition_mask = df['ARQ'].isnull()
        new_df = df[condition_mask].copy()
        new_df['Justification'] = 'Denied, does not have ARQ data'
    else:
        # If "ARQ" column doesn't exist, select all rows and add justification
        new_df = df.copy()
        new_df['Justification'] = 'Denied, does not have ARQ data'
    
    new_df.to_excel(output_file, index=False)

def get_user_input():
    def submit():
        file_path = file_path_entry.get()
        output_file = output_file_entry.get()
        
        if file_path and output_file:
            get_user_input.result = file_path, output_file
            window.destroy()
        else:
            messagebox.showwarning('Incomplete Input', 'Please provide all inputs.')

    def browse_file():
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, file_path)
    
    def browse_output_file():
        output_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        output_file_entry.delete(0, tk.END)
        output_file_entry.insert(0, output_file)

    window = tk.Tk()
    window.title('Select Files')

    file_path_label = tk.Label(window, text='Select Excel File:')
    file_path_entry = tk.Entry(window)
    file_path_button = tk.Button(window, text='Browse', command=browse_file)
    
    output_file_label = tk.Label(window, text='Select Output File:')
    output_file_entry = tk.Entry(window)
    output_file_button = tk.Button(window, text='Browse', command=browse_output_file)

    submit_button = tk.Button(window, text='Submit', command=submit)
    cancel_button = tk.Button(window, text='Cancel', command=window.destroy)

    file_path_label.grid(row=0, column=0, sticky='e')
    file_path_entry.grid(row=0, column=1)
    file_path_button.grid(row=0, column=2)
    
    output_file_label.grid(row=1, column=0, sticky='e')
    output_file_entry.grid(row=1, column=1)
    output_file_button.grid(row=1, column=2)

    submit_button.grid(row=2, column=0, columnspan=2)
    cancel_button.grid(row=2, column=2)

    window.mainloop()

    return get_user_input.result

input_file, output_file = get_user_input()

if input_file is not None and output_file is not None:
    add_justification_and_filter(input_file, output_file)
    messagebox.showinfo('Success', 'Filtered rows copied to output.xlsx')
else:
    messagebox.showinfo('Canceled', 'Operation canceled')
