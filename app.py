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
x.append(True) #* Is initiate
x.append('') #* Response
@app.route('/')
async def index():    
    
    if x[1] == True: #* Initiate 
        data= await job()
        x[1]=False
        x[2] = data
        data_ = x[2]
        return render_template('index.html',table=data_[0],table1=data_[1],table2=data_[2],table3=data_[4],table4=data_[3])
                
    elif x[1] == False: #* Update
        data_ = x[2]        
        return render_template('index.html',table=data_[0],table1=data_[1],table2=data_[2],table3=data_[4],table4=data_[3])
    else:
        return 'Eğer bu yazıyı görüyorsan site gitmiş, geçmiş olsun.'
   



    

@app.route('/update', methods=['GET'])
async def update():
    dt_started = datetime.datetime.utcnow()   
    remaining_sec=(dt_started-x[0]).total_seconds()
    if remaining_sec > 300:         
        data = await job()
        x[0]  = datetime.datetime.utcnow()
        x[2] = data
        data_ = x[2]   
        return jsonify(table=data_[0],table1=data_[1],table2=data_[2],table3=data_[3],table4=data_[4])
    else:
        return F'{remaining_sec} ,seconds passed.'
    

    
                
if __name__=='__main__':  
    app.run()
