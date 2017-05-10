#Fracesc Borda i Sergi Mor



from __future__ import print_function
from flask import Flask
from flask import render_template
from flask import request
from flask import Flask, redirect
from databases import insert_zone #This is use for import the function insert_zone from the file databases.
from databases import get_zones
from databases import insert_temp_zone
from databases import show_zone
#from databases import delete_zone
import sys

app = Flask(__name__)

#When we want to see the Flask app we have to put the ip of the Raspberry and then the port.
#e.g. 172.16.0.xxx/5000
@app.route('/')  #This route is the main route. If we only put 172.16.0.xxx/5000 the program will redirect to the landing_page function.
def landing_page():
   return render_template('landing_page.html')#When the program execute landing_page this function will return landing_page.html.
   #We can find it into the file template. And this is what we will see on internet.

@app.route('/crear_zona', methods=["get","post"])
def crear_zona():
    if request.method == "GET": #When the request method is "get" the function will return us the file crear_zona.html.
        return render_template('crear_zona.html')
    elif request.method == "POST": #After return the file crear_zona.html the page will show us a box for insert a zone. This is a Post method.
        data = request.form.get('zona') #We get from the form request the variable zona.
        print(data, file=sys.stderr) #This is use for print the variable data
        insert_zone("".join(data)) #We pass the variable data to the function insert_zone.
        return redirect ("/") #After introduce the zone the program will redirect to the main program

@app.route('/select_zone', methods=["get","post"])
def select_zone():
    if request.method == 'GET': #When the route is select_zone and the request method is "get".
	    historical_data = get_zones() #Here we call the function get_zone that is on the basesdades.py file.
        return render_template('select_zone.html',historical_data=historical_data) #Here we call the file select_zone.html and we pass the variable historical_data
    elif request.method == 'POST':
        print("POST", file=sys.stderr)
        zone = request.form.get('zones') #We obtain from the form the variable zones
        temp = request.form.get('temperature') #We obtain from the form the variable temperature
        print(zone, file=sys.stderr)
	    print(temp, file=sys.stderr)
        insert_temp_zone(zone,temp) #We insert this two variables into the function insert_temp_zone
        return redirect ("/")

@app.route ('/zones', methods=["get","post"])
def zones():
	if request.method == 'GET': #When we call the method 'GET' the variable historical_data get the return from te function get_zones.
		historical_data = get_zones()
        print("GET", file=sys.stderr)
        return render_template('zone.html',historical_data=historical_data)#Here we pass the variable historical_data to historical_data on the file zone.html


@app.route ('/zones/<zona>', methods=["get","post"]) #This route depends on the variable zona that it will be selected when we click on a specific zone.
def show_info(zona):
	if request.method == 'GET':
		historical_data = show_zone(zona)#When we select a zone the program send this variable to the function show_zone.
		return render_template('show_zone.html',historical_data=historical_data)



if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')
