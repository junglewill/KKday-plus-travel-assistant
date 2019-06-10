import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont
from date_selection import Calendar  # import class
from datetime import datetime
from tkinter import messagebox
from Web_scraping_currency import currency_function  # import function(country)
from Web_scraping_temperature import temperature  # import function(city_input, date1_input, date2_input)
from Web_scraping_pollution import Get_pollution  # import Class C = Class() data = C.choose_city(city) C.print_poll(data)
from Web_scraping_safety import safety  # import function
from Web_scraping_schedule import schedule # import function(kwlist, nolist, SelectCity)

class Window(tk.Frame):

	def __init__(self):
		tk.Frame.__init__(self)
		self.grid()
		self.create_widgets()
	
	def input_time_wrong_message_box(self):
			messagebox.showinfo( "錯誤!", "結束日期早於開始日期")

	def combine_func(self):
		self.end_date_str_gain()
		if self.end_date_str.get() == "" or self.date_str.get() == "":
			return
		elif self.check_time(self.date_str.get(),self.end_date_str.get()) == 0:
			self.input_time_wrong_message_box()
			self.combine_func()
			
		else:
			return 
		
	
	def create_widgets(self):
		f = tkFont.Font(size = 20, family = "Courier New")

		self.dict = {'泰國': ['芭達雅', '普吉島', '曼谷'],
                     '日本': ['東京', '沖繩', '大阪', '京都'],
                     '韓國': ['釜山', '首爾'],
					 '香港': ['香港'],
					 '新加坡': ['新加坡']}
		self.variable1 = tk.StringVar()
		self.variable2 = tk.StringVar()
		self.variable1.set('選擇國家')
		self.variable2.set('選擇城市')
		self.variable1.trace('w', self.updateoptions)
		self.droplist1 = tk.OptionMenu(self, self.variable1, *self.dict.keys(), command=self.getValue())
		self.droplist2 = tk.OptionMenu(self, self.variable2, '', command=self.getValue())

		default1 = "要的行程"
		self.txt1 = tk.Entry(self, bd=1)
		self.txt1.insert(0, default1)
		self.txt1.bind('<FocusIn>', lambda event:self.on_entry_click(self.txt1, default1))
		self.txt1.bind('<FocusOut>', lambda event:self.on_focusout(self.txt1, default1))
		self.txt1.config(fg='grey')
		default2 = "不要的行程"
		self.txt2 = tk.Entry(self, bd=1)
		self.txt2.insert(0, default2)
		self.txt2.bind('<FocusIn>', lambda event:self.on_entry_click(self.txt2, default2))
		self.txt2.bind('<FocusOut>', lambda event:self.on_focusout(self.txt2, default2))
		self.txt2.config(fg='grey')
		

		#開始日期
		self.date_str = tk.StringVar()
		self.date = ttk.Entry(self, textvariable = self.date_str)
		self.date.grid(row = 3, column = 0, columnspan = 5,sticky = 'ew')
		self.date_str_gain = lambda: [
			self.date_str.set(self.date)
			for self.date in [Calendar((500,500),'ur').selection()]
			if self.date]
		tk.Button(self, text = '開始日期', command = self.date_str_gain).grid(row = 3,column = 5, columnspan = 10, sticky = tk.W)
		

		#結束日期
		self.end_date_str = tk.StringVar()
		self.end_date = ttk.Entry(self, textvariable = self.end_date_str)
		self.end_date.grid(row = 3, column = 8, columnspan = 5,sticky = 'ew')
		self.end_date_str_gain = lambda: [
			self.end_date_str.set(self.end_date)
			for self.end_date in [Calendar((500,500),'ur').selection()]
			if self.end_date]
		tk.Button(self, text = '結束日期', command = self.combine_func).grid(row = 3,column = 13, columnspan = 10, sticky = 'W')
		
		

		self.btn1 = tk.Button(self, height=2, width=8, text="Search", command=self.clickBtn, font=f)
		self.cvsMain = tk.Canvas(self, width = 800, height = 600, bg = "white")
		
		
		self.droplist1.grid(row=0, column=0, columnspan=8,sticky=tk.E+tk.W)
		self.droplist2.grid(row=0, column=8, columnspan=8,sticky=tk.E+tk.W)
		self.txt1.grid(row=1, column=0, columnspan=16,sticky=tk.E+tk.W)
		self.txt2.grid(row=2, column=0, columnspan=16,sticky=tk.E+tk.W)
		self.btn1.grid(row=2, column=17, rowspan=2, sticky=tk.E+tk.W)
		self.cvsMain.grid(row=5, column=0, columnspan=18, sticky= tk.NE + tk.SW)

	def check_time(self,start,end):  #比較結束時間是否小於開始時間
		start_time = datetime.strptime(start,'%Y-%m-%d')
		end_time = datetime.strptime(end,'%Y-%m-%d')
		if start_time > end_time:
			return 0
		else:
			return 1


	def clickBtn(self): 
		country_to_use = self.variable1.get()
		city_to_use = self.variable2.get()
		start_time = self.date_str.get()
		end_time = self.end_date_str.get()
		self.List = [0,0,0,0]
		self.List[0] = country_to_use
		self.List[1] = city_to_use
		self.List[2] = start_time
		self.List[3] = end_time

		print(self.List)       #test print

		return self.List
		

	def getValue(self):
		pass		


	def on_entry_click(self, entry, text):  # function that gets called whenever entry is clicked
		if entry.cget('fg') == 'grey':
			entry.delete(0, "end") # delete all the text in the entry
			entry.insert(0, '') #Insert blank for user input
			entry.config(fg = 'black')

	def on_focusout(self, entry, text):
		if entry.get() == '':
			entry.insert(0, text)
			entry.config(fg = 'grey')	

	def updateoptions(self, *args):
		countries = self.dict[self.variable1.get()]
		self.variable2.set(countries[0])
		menu = self.droplist2['menu']
		menu.delete(0, 'end')
		for country in countries:
			menu.add_command(label=country, command=lambda country=country: self.variable2.set(country))
	
		
	
mywindow = Window()
mywindow.master.title("KKDay+")




mywindow.mainloop()