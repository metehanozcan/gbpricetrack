from flask import Flask, render_template,jsonify,request
from backend import job




app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

#* Flask uses routes to navigate pages.
#* You have to use templates for flask.

  


@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html')
    
    # return render_template('index.html',table=[0],table1=[1],table2=[2],table3=[3],table4=[4])
@app.route('/update', methods=['GET'])
def update():   

    data=job() 
    # return jsonify(data[0],data[1],data[2],data[3],data[4])
    return jsonify(table=data[0],table1=data[1],table2=data[2],table3=data[3],table4=data[4])

if __name__=='__main__':
    app.run()