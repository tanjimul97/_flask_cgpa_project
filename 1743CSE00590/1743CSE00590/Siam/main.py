from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("app.html")


@app.route("/calculate", methods=['POST'])
def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    num3 = request.form['num3']
    num4 = request.form['num4']
    num5 = request.form['num5']
    num6 = request.form['num6']
    num7 = request.form['num7']
    num8 = request.form['num8']
    num9 = request.form['num9']
    num10 = request.form['num10']
    num11 = request.form['num11']
    num12 = request.form['num12']
    
    
    result = (float(num1) + float(num2) + float(num3) + float(num4) + float(num5)+float(num6)+float(num7)+float(num8)+float(num9)+float(num10)+float(num11)+float(num12))/12 
        
    myResult = "{:.2f}".format(result)
    origiResult = str(myResult)
        
     
    return render_template('app.html', result= "You obtained " +origiResult+ " out of 4")
    
    
        
if __name__ == '__main__':
	app.run(debug=True)
