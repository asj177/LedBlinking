from flask import Flask,render_template
import RPi.GPIO as GPIO
app = Flask(__name__)
LEDPIN1=13
LEDPIN2=5
LEDPIN3=17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPIN1,GPIO.OUT)
GPIO.setup(LEDPIN2,GPIO.OUT)
GPIO.setup(LEDPIN3,GPIO.OUT)
keyMap={1:13,2:5,3:17}

@app.route('/welcome')
def test():
    return render_template('login.html')

@app.route('/operate/<status>/<lightNumber>',methods=['POST'])
def operate(status,lightNumber):
    gpPin=keyMap.get(int(lightNumber))
    if status =='off':
        GPIO.output(gpPin,True)
    else :
        GPIO.output(gpPin,False)
    
    return "success"
        
        
        
    

if __name__=='__main__':
    app.run(debug=True,port=80,host='0.0.0.0')