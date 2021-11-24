from flask import Flask,render_template,request,url_for
import sqlite3
app=Flask(__name__)

con = sqlite3.connect("dineshst.db")

con.close()

@app.route("/")
@app.route("/index")
def index():
	return render_template("mentor1.html")

@app.route("/batch")

def batch():
	return render_template("batchselect.html")


@app.route("/sub",methods=['POST'])
def sub():
	
	cname=request.form["coursename"]
	dur=request.form["dur"]
	print(dur)
	con=sqlite3.connect("dineshst.db")
	con.row_factory=sqlite3.Row
	cur=con.cursor()
	if dur=="cat1":
		cur.execute('SELECT reg_no,present FROM Attendance_fat_cat1 ')
		data=cur.fetchall()
	if dur=="cat2":
		cur.execute('SELECT reg_no,present  FROM Attendance_fat_cat2')
		data=cur.fetchall()
	if dur=="cat2":
		cur.execute('SELECT reg_no,present  FROM Attendance_fat_cat2')
		data=cur.fetchall()
	
	
	
	con.close()
	return render_template("coursewise.html",data=data,dur=dur,cname=cname)

@app.route("/catwise")

def catwise():
	return render_template("catselect.html")

@app.route("/view",methods=['POST'])
def view():

	
	catname=request.form["period"]
	sem=request.form["semester"]
	print(sem)
	con=sqlite3.connect("dineshst.db")
	con.row_factory=sqlite3.Row
	cur=con.cursor()
	print(catname)
	if catname=="cat1":
		cur.execute('SELECT * FROM Attendance_fat_cat1')
		data=cur.fetchall()
	if catname=="cat2":
		cur.execute('SELECT * FROM Attendance_fat_cat2')
		data=cur.fetchall()
	if catname=="cat2":
		cur.execute('SELECT * FROM Attendance_fat_cat2')
		data=cur.fetchall()
	
	
	
	con.close()
	return render_template("catwise.html",data=data,sem=sem,catname=catname)




@app.route("/hod")
def hod():
	return render_template("hod.html")

@app.route("/batch_hod")

def batch_hod():
	return render_template("batchselect_hod.html")

@app.route("/ins",methods=['POST'])
def ins():
	curname=request.form["coursename"]
	duration=request.form["dur"]
	print(duration)
	con=sqlite3.connect("dineshst.db")
	con.row_factory=sqlite3.Row
	cur=con.cursor()
	
	if duration=="cat1":
		cur.execute('SELECT * FROM Attendance_fat_cat1')
		data=cur.fetchall()
	if duration=="cat2":
		cur.execute('SELECT * FROM Attendance_fat_cat2')
		data=cur.fetchall()
	if duration=="cat2":
		cur.execute('SELECT * FROM Attendance_fat_cat2')
		data=cur.fetchall()
	
	
	
	con.close()
	return render_template("coursewise_hod.html",data=data,duration=duration,curname=curname)



@app.route("/catwise_hod")

def catwise_hod():
	return render_template("catselect_hod.html")

@app.route("/view_hod",methods=['POST'])
def view_hod():

	catname=request.form["period"]
	sem=request.form["semester"]
	print(sem)
	con=sqlite3.connect("dineshst.db")
	con.row_factory=sqlite3.Row
	cur=con.cursor()
	print(catname)
	if catname=="cat1":
		cur.execute('SELECT * FROM Attendance_fat_cat1')
		data=cur.fetchall()
	if catname=="cat2":
		cur.execute('SELECT * FROM Attendance_fat_cat2')
		data=cur.fetchall()
	if catname=="cat3":
		cur.execute('SELECT * FROM Attendance_fat_cat3')
		data=cur.fetchall()
	
	
	
	con.close()
	return render_template("catwise_hod.html",data=data,sem=sem,catname=catname)


if __name__=="__main__":
	app.run(debug=True)