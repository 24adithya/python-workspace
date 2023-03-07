import pandas as pd
import tkinter as tk
from tkinter import ttk

# Create a sample dataset
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
        'City': ['New York', 'London', 'London', 'New York', 'Paris'],
        'Country': ['USA', 'UK', 'UK', 'USA', 'France'],
        'Sales': [100, 200, 150, 300, 250]}

# df = pd.DataFrame(data)
df = pd.read_excel('python-pivot.xlsx', sheet_name='Sheet1')

# Create a pivot table using the `pivot_table()` function
pivot_table = pd.pivot_table(df, values='Sales', index=['Country', 'City'], columns=['Name'], aggfunc='sum')

# Create a Tkinter GUI window
root = tk.Tk()
root.title('Pivot Table')

# Create a Treeview widget to display the pivot table
tree = ttk.Treeview(root)

# Add columns to the Treeview widget
tree['columns'] = pivot_table.columns.tolist()

# Add headers to the Treeview columns
for col in pivot_table.columns.tolist():
    tree.heading(col, text=col)

# Add rows and data to the Treeview
for i, (index, row) in enumerate(pivot_table.iterrows()):
    tree.insert('', i, values=row.tolist(), text=str(index))

# Pack the Treeview widget
tree.pack()

# Start the GUI main loop
root.mainloop()
