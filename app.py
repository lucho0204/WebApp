#Import libraries from Flask
from flask import Flask, render_template, request

#Declare the app
app = Flask(__name__)

#Start an app route which is '/'
@app.route('/')

#Declare main function
def main():
    return render_template('app.html')


#Form submission route
@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        #Start Pulling data from form input
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']
        # Calculation
        if operation == 'Suma':
            sum = float(num1) + float(num2)
            return render_template('app.html', sum=sum)
        elif operation == 'Resta':
            sum = float(num1) - float(num2)
            return render_template('app.html', sum=sum)
        elif operation == 'Multiplicacion':
            sum = float(num1) * float(num2)
            return render_template('app.html', sum=sum)
        elif operation == 'Division':
            sum = float(num1) / float(num2)
            return render_template('app.html', sum=sum)
        else:
            return render_template('app.html')