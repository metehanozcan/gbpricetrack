from flask import Flask, render_template,jsonify,request
from backend import job
import cchardet
import time
import datetime

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True



old_t = datetime.datetime.utcnow()
x=[]
x.append(old_t) #*Server Start Time
x.append(True) #* IsIniate
x.append('') #* Response
@app.route('/')
async def index():
    
    dt_started = datetime.datetime.utcnow()
    if x[1] == True:
        data= await job()
        x[1]=False
        x[2] = data
        return render_template('index.html',table=data[0],table1=data[1],table2=data[2],table3=data[4],table4=data[3])
        

        
    elif (dt_started-x[0]).total_seconds() > 300:         
        data = await job()
        x[0]  = datetime.datetime.utcnow()
        x[2] = data
        return render_template('index.html',table=data[0],table1=data[1],table2=data[2],table3=data[4],table4=data[3])   
    
    elif x[1] == False or (dt_started-x[0]).total_seconds()<300:
        data_ = x[2]
        return render_template('index.html',table=data_[0],table1=data_[1],table2=data_[2],table3=data_[4],table4=data_[3])
    else:
        return '404 bro. Yamulduk'
      
# def update():   

#     data=job() 
#     # return jsonify(data[0],data[1],data[2],data[3],data[4])
#     return jsonify(table=data[0],table1=data[1],table2=data[2],table3=data[3],table4=data[4])

if __name__=='__main__':
    app.run()
