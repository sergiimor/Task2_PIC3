import sqlite3
import cgi
from datetime import datetime, date

#We will use two databases the BASEPATH is the secundary database and it is use for introduce the zones and the temperature.
BASEPATH = "/home/pi/Desktop/Programacio3/flask/"
BASEPATH_1 = "/home/pi/pic3/db/" #In this database we have the time, the zone, temperature and the date.

#####Note: The databa BASEPATH_1 is in the folder BaseDadesGran
def insert_zone(name):
	conn = sqlite3.connect(BASEPATH + 'mydatabase.db')
	if name not in get_zones(): #Here we insert the variable name that is a new area and then we compare with the secundary database.
		conn.execute("insert into zones values (?)" , (name,)) #If the area is no in the database we will put it.
		conn.commit()
		conn.close()

def get_zones (): #This function is for show the different ares of the secundary database.
	conn = sqlite3.connect(BASEPATH + 'mydatabase.db')
	curs = conn.cursor()
	q = curs.execute ("SELECT * FROM zones")
	aux_list = [elem[0] for elem in q.fetchall()] #We create an aux_list because when we call the database it passes like a tuple.
	#We have to convert it to a type list.
	return aux_list
def insert_temp_zone(zone, temp):
	conn = sqlite3.connect(BASEPATH_1 + 'mydatabase.db')
    conn.execute("insert into temps (tdate,ttime,zone,temperature) values (?, ?, ?, ?)", ( #This is use for insert a zone and the temperature that the user had introduce
        date.today(),
        datetime.now().strftime("%H:%M:%S"),
        zone,
        str(temp)))
    conn.commit()
    conn.close()
	print zone, temp

def show_zone(zona):

	conn = sqlite3.connect(BASEPATH_1 + 'mydatabase.db')
	curs = conn.cursor()
	q = curs.execute ("SELECT * FROM temps WHERE zone=?", (zona,)) #Here is for select an specific area that we had to introduce previously
	aux_list = [(elem[0],elem[1],elem[2],elem[3]) for elem in q.fetchall()] #We convert a tuple to a list.
	return aux_list


if __name__ == '__main__':

	print get_zones()
