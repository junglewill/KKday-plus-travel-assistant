import tkinter as tk
from tkinter import ttk

class Window(tk.Frame):

	def __init__(self):
		tk.Frame.__init__(self)
		self.grid()
		self.create_widgets()
		
	def create_widgets(self):
		
		self.dropdown1 = ttk.Combobox(self , values=["泰國", "日本", "香港", "韓國", "新加坡"])
		self.dropdown2 = ttk.Combobox(self , values=["北海道", "東京", "沖繩", "大阪", "京都", "首爾", "釜山", "芭達雅", "普吉島" , "曼谷", "新加坡", "香港"])
		self.txt1 = tk.Text(self, height=1, width=5)
		self.txt2 = tk.Text(self, height=1, width=5)
		self.lb1 = tk.Label(self, height=1, width=10, text="要的關鍵字")
		self.lb2 = tk.Label(self, height=1, width=10, text="不要的關鍵字")
		self.btn1 = tk.Button(self, height=1, width=5, text="Search", command=self.clickBtn)
		
		
		self.dropdown1.grid(row=0, column=0, columnspan=1,sticky=tk.E+tk.W)
		self.dropdown2.grid(row=0, column=2, columnspan=1,sticky=tk.E+tk.W)
		self.txt1.grid(row=2, column=0, columnspan=1,sticky=tk.E+tk.W)
		self.txt2.grid(row=2, column=2, columnspan=1,sticky=tk.E+tk.W)
		self.lb1.grid(row=1, column=0, columnspan=3,sticky=tk.W) 
		self.lb2.grid(row=1, column=2, columnspan=3,sticky=tk.W)
		self.btn1.grid(row=2, column=4, sticky=tk.E+tk.W)
		
	def clickBtn(self): 
		
		pass		
		
	
	
mywindow = Window()
mywindow.master.title("KKDay+")
mywindow.mainloop()