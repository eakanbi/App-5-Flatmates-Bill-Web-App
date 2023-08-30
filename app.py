from flask import Flask, redirect, url_for, render_template, request, flash
from forms import BillForm
from wtforms.validators import DataRequired
from flatmates_bill import flat

app = Flask(__name__)
app.secret_key = b'l\xa4\xa1\xa1qo\x99\x10\xc2;\x08\x8a\xb6o\xba\xbcz5\xb9L&\xf2\xcf%O75\xd2\xcao\xdd\x9b'


@app.route('/')
@app.route('/index')  
def index():
    return render_template('index2.html')

@app.route('/billspage', methods=['GET', 'POST'])
def billspage():
    bill_form = BillForm()

    if request.method == 'POST':
        return redirect(url_for('results'))
        
    return render_template('bill_form_page2.html', title = 'Bills', 
                           billform = bill_form)


@app.route('/results', methods=['GET', 'POST'])
def results():

    billform = BillForm(request.form)
    
    the_bill = flat.Bill(float(billform.amount.data), billform.period.data)
    flatmate1 = flat.Flatmate(billform.name1.data, float(billform.days_in_house1.data))
    flatmate2 = flat.Flatmate(billform.name2.data, float(billform.days_in_house2.data))

    return render_template('results2.html',
                           billform = billform,
                           name1 = flatmate1.name,
                                amount1 = flatmate1.pays(the_bill, flatmate2),
                                name2 = flatmate2.name,
                                amount2 = flatmate2.pays(the_bill, flatmate1))


if __name__ == '__main__':
    app.run(debug=True)