#建立時間資料型態，必須有小時/分鐘/秒三種屬性
class Time() :

	def __init__(self , h , m , s) :
		
		self.hour = h
		self.minute = m
		self.second = s
	
	#建立把時間全部換成秒數的函數	
	def change_to_second(self) :
		
		return self.hour * 3600 + self.minute * 60 + self.second

#建立event資料型態，必須有名稱/開始時間/結束時間/價值四種屬性		
class Event() :

	def __init__(self , n , t1 , t2 , v) :
		
		self.name = n
		self.start = t1
		self.end = t2
		self.value = v	
#建立schedule資料型態，是一個list儲存所有在行程表上的event		
class Schedule() :

	def __init__(self) :
		
		self.events = []
	
	#建立加入event的函數
	def add_event(self , e) :
	
		self.events.append(e)
	
	#建立刪除event的函數	
	def remove_event(self , e) :
	
		self.events.remove(e)
	
	#建立一個確認行程e和原本行事曆中的行程是否衝突，確認之後決定是否插入e，以及是否刪除行事曆裡面已經有的行程的函數	
	def check_add_schedule(self , e) :
		
		#建立變數add，no代表不加入行程/yes代表加入行程
		add = 'no'
		#建立一個list儲存所有已經在行事曆上會跟e時間衝突的行程
		sametime = []
		#建立變數計算所有已經在行事曆然後和e重疊的行程總價值
		value = 0
		#用來計算和e不衝突的行程個數
		n = 0
		#把e的開始和結束時間都換成秒
		e_start_in_second = e.start.change_to_second()
		e_end_in_second = e.end.change_to_second()
		
		
		for i in range(len(self.events)) :
			
			#把每一個已經在行事曆中的event的開始以及結束時間換成秒
			self_start_in_second = self.events[i].start.change_to_second()
			self_end_in_second = self.events[i].end.change_to_second()

			#如果e的開始和結束時間都在一個行程的開始時間之前，或是都在結束時間之後，代表兩個行程時間不衝突
			#如果不衝突的話，就把不衝突行程個數加一
			if e_start_in_second <= self_start_in_second and e_end_in_second <= self_start_in_second :
				n += 1
			elif e_start_in_second >= self_end_in_second and e_end_in_second >= self_end_in_second :
				n += 1
			#時間衝突的話，就把原形程加入時間衝突的list	
			else:
				sametime.append(self.events[i])
				
		#計算所有和e衝突的行程的價值總和	
		for x in sametime :
			value += x.value 
		
		#n等於行程總數代表和所有行程和e都不衝突，可以直接加入e
		if n == len(self.events) :
			add = 'yes'
		#行程衝突的話，只有在e的價值大於所有重疊行程的總價值的情況下才加入
		elif len(sametime) > 0 and e.value > value:
			add = 'yes'		
		
		#把有衝突的行程刪除
		#加入e
		if add == 'yes' :
			
			#建立一個存有現有行程(未加入e之前)的list
			eventslist = []
			for i in self.events :
				eventslist.append(i)
			
			
			for x in eventslist :
				self_start_in_second = x.start.change_to_second()
				self_end_in_second = x.end.change_to_second()
				#如果跟e重疊的話就要刪除(扣除上面沒重疊的兩種情況)
				if not ((e_start_in_second <= self_start_in_second and e_end_in_second <= self_start_in_second) or (e_start_in_second >= self_end_in_second and e_end_in_second >= self_end_in_second)) : 
					s.remove_event(x)
			
			#加入e
			s.add_event(e)
			
	def search_event(self,s) :
			
		in_event = "no"
		for x in self.events :
			if s in x.name.lower() :
				in_event = "yes"
							
		
		print('Nothing found.')
		



#建立行事曆s		
s = Schedule()		
eventstr = []
printlist = []

#共有n個行程資訊		
n = int(input())
for i in range(n) :
	eventinfo = input()
	eventstr.append(eventinfo)
	eventinfo = eventinfo.split(',')
	name = eventinfo[0]
	t1str = eventinfo[1].split(':')
	t1 = Time(int(t1str[0]) , int(t1str[1]) , int(t1str[2]))
	t2str = eventinfo[2].split(':')
	t2 = Time(int(t2str[0]) , int(t2str[1]) , int(t2str[2]))
	value = int(eventinfo[3])
	
	event = Event(name , t1 , t2 , value)
	#呼叫函數檢查是否可將此行程加入，並刪除多於行程
	s.check_add_schedule(event)
	
search = input().lower()
s.search_event(search)

second = []
for i in printlist :
	info = i.split(',')
	timestr = info[1].split(':')
	time = Time(int(timestr[0]) , int(timestr[1]) , int(timestr[2]))
	t = int(time.change_to_second())
	second.append(t)


for i in range(1,len(second)) :
	for j in range(i) :
		if second[i] < second[j] :
			second.insert(j , second[i])
			second.pop(i+1)
			printlist.insert(j , printlist[i])
			printlist.pop(i+1)
		
		
