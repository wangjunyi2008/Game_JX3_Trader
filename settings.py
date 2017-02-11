# -*- coding:gbk -*-  
import win32api


DEBUGNAME = "debug.txt" #调试文件输出名
INT_GLOBAL_WAITING = 0.5 #每次操作后等待时间


#反侦测模式设置
INT_ANTI_SCAN = 1 #反侦测总开关 1 = 开
FLOAT_WAITING_RANDOM_LOWER = 0.1 #随机等待时间下限
FLOAT_WAITING_RANDOM_UPPER = 0.3 #随机等待时间上限

#登录模块相对位置设置
TUPLE_LOGIN_USERNAME = (951/1920,484/1080)
TUPLE_LOGIN_PWD = (957/1920,526/1080)
TUPLE_LOGIN_OK = (1051/1920,595/1080)
TUPLE_LOGIN_CONFIRM_LOCATION = (66/1920,1007/1080) #左下角西山居白色标志。如果消失(非(255,255,255))意味着进入“角色选择页面”
TUPLE_LOGIN_CONFRIM_PIXEL = (255,255,255)
TUPLE_LOGIN_SUCCESS_LOCATION = (29/1920,1033/1080) #左下角登陆成功后的修饰花纹
TUPLE_LOGIN_SUCCESS_PIXEL = (9,59,57) #左下角登陆成功后的修饰花纹

TUPLE_LOGIN_HOTSPAM_LOCATION = (1395/1920,276/1080)
TUPLE_LOGIN_HOTSPAM_PIXEL = (64,90,86)

TUPLE_MAIL_NEW_LOCATION = (1702/1920,148/1080)
TUPLE_MAIL_NEW_PIXEL = (219,212,192)

#交易行模块
TUPLE_TRADER_DIALOG = (272/1920,254/1080) #交易行对话——交易行
TUPLE_TRADER_ITEMINPUT = (88/1920,273/1080) #交易行物品输入框
TUPLE_TRADER_QUERYBUTTON = (62/1920,215/1080) #"买卖"分页按钮
TUPLE_TRADER_SELLBUTTON = (285/1920,214/1080) #"寄卖"分页按钮
TUPLE_TRADER_SEARCHBUTTON = (714/1920,274/1080) #搜索按钮
TUPLE_TRADER_ITEMICON_LEFTTOP (25/1920,271/1080) #物品图标左上角
TUPLE_TRADER_ITEMICON_RIGHTDOWN (58/1920,304/1080) #物品图标右下角
TUPLE_TRADER_ITEM_ZHUAN (40/1920,429/1080) #物品寄售砖数窗口
TUPLE_TRADER_ITEM_JIN (94/1920,427/1080) #物品寄售金数窗口
TUPLE_TRADER_ITEM_YIN (146/1920,429/1080) #物品寄售银数窗口

#背包
TUPLE_BAG1_START = (1164/1920,236/1080)  ###第一次需初始化【手动修改】
TUPLE_BAG_NEXT = (38/1920,38/1080) #和相邻格子的位置



#将相对位置转化为绝对位置
class util():
	Screen_X = 0
	Screen_Y = 0
	def __init__(self):
		self.Screen_X =  win32api.GetSystemMetrics(0)
		self.Screen_Y = win32api.GetSystemMetrics(1)
	def GetIntTuple(self,value):
		return tuple((int(value[0]* self.Screen_X),int(value[1] * self.Screen_Y)))
	def CompareTuple(self,x,y,sensitive = 20):
		#比较两个像素点的相似性，如果非常相似（合之差<20）返回1
		xsum = 0
		ysum = 0
		for i in x:
			xsum += i
		for j in y:
			ysum += j
		if abs(xsum-ysum)<sensitive:
			return True
		else:
			return False

