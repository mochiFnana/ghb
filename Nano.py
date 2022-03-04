import os
try :
	import mysql.connector
except :
	os.system("apt install python3-pip")
	os.system("pip install python3-mysql.connector")
	import mysql.connector
fn = os.path.basename(__file__)		
si = []
nm = ""
for io in fn :
	si.append(io)
for ii in range((len(fn))-3) :
	nm = nm + si[ii]
def C() :
	os.system("clear")
C()
pas = 'Sn5lLE7xUSiS3284cP9t'
num = 0
def main(h="") :
	C()
	arr = []	
	global pas,num,fn,nm
	myd = mysql.connector.connect(
		host="botvk2osfpfc5tldr8yu-mysql.services.clever-cloud.com",
		user="uvjtbfzla0bqoo3x",
		password=pas,
		database="botvk2osfpfc5tldr8yu"
	)
	cc = myd.cursor()
	if h == "DELETE ALL ROWS !" :
		cc.execute("TRUNCATE TABLE nano")
		sq = "INSERT INTO nano (id, password, chat)"
		l  = "VALUE (null, 'hinako_note', 'Hello World')"
		sql = sq+l
		cc.execute(sql)
		myd.commit()
		os.system("python3 " + fn)
	elif h != "" :
		sq = "INSERT INTO nano (id, password, chat)"
		l  = "VALUE (null, '', '"+nm+" : "+h+"')"
		sql = sq+l
		cc.execute(sql)
		myd.commit()
	cc.execute("SELECT * FROM nano")
	for io in cc.fetchall() :
		arr.append(io)
	print("CHAT user [ "+nm+" ]")
	print(("_"*20)+"\n\n")
	for u in arr :
		print(num,u[2])
		num += 1
	num = 0
def check(a) :
	global pas
	arr = []
	mydb = mysql.connector.connect(
		host="botvk2osfpfc5tldr8yu-mysql.services.clever-cloud.com",
		user="uvjtbfzla0bqoo3x",
		password=pas,
		database="botvk2osfpfc5tldr8yu"
	)
	ci = mydb.cursor()
	ci.execute("SELECT * FROM nano")
	for xx in ci.fetchall() :
		arr.append(xx)
	if arr[0][1] != a :
		C()
		print("password yang anda masukkan salah! ")
		quit()
	else :
		pass
aa = ""
if __name__ == "__main__" :
	check(input("masukkan password : "))
	main(aa)
	while True :
		print("\n"+("_"*20))
		print("\n\nclick enter untuk merefrefreash")
		aa = input("\nmasukkan pesan : ")
		if aa != "" :
			main(aa)		
			aa = ""
		else :
			main(aa)
