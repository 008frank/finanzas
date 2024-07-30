from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from User import User
from db_users import GetData
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'bj7l3xtoftrlpschwtah-mysql.services.clever-cloud.com'
app.config['MYSQL_USER'] = 'u28owjanx91fbbgg'
app.config['MYSQL_PASSWORD'] = 'Hib9YhOmKLh3xa3MMPMZ'
app.config['MYSQL_DATABASE'] = 'bj7l3xtoftrlpschwtah'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        user = User(app, mysql, request.form['input_1'], request.form['input_2'])
        if user.identication() == True:
            return redirect(url_for('home'))
        else:
            msg = "Contraseña incorrecta..."
            return render_template('index.html', message=msg)
    else:
        return render_template('index.html')


@app.route('/home')
def home():
    get_list = GetData.set_balance(None, app, mysql)
    get_totals = []
    for t in get_list:
        if t > 0:
            get_totals.append(f'{t:,.2f}')
        else:
            get_totals.append('-')
    
    total_value = sum(s for s in get_list if s > 0)
    
    current_amount = GetData.get_data_charts(None, app, mysql)
    income_amount = f'{current_amount[0]:,.2f}'
    remaining_amount = f'{current_amount[1]:,.2f}'
    
    return render_template('home.html', element=get_totals, total=f'{total_value:,.2f}', ca=current_amount, stat=[income_amount, remaining_amount])


@app.route('/income', methods=['GET','POST'])
def income():
    
    get_history_data = GetData.db_history(app, mysql)
    get_income_history = GetData.incomes_barchart(app, mysql)
    
    if request.method=='POST':
        selection = request.form['select_income_form']
        
        if selection == "incomes":
            # try:
                user = request.form['radio']
                if user == 'ivan':
                    try:
                        diezmo = int(request.form['diezmo_ivan'])
                        despensa = int(request.form['despensa'])
                        salud = int(request.form['salud'])
                        transporte = int(request.form['transporte'])
                        internet = int(request.form['internet'])
                        luz = int(request.form['luz'])
                        agua = int(request.form['agua'])
                        gas = int(request.form['gas'])
                        
                        elements_list = [diezmo, despensa, salud, transporte, internet, luz, agua, gas]
                        
                        save_information = GetData.save_income(app, mysql, elements_list, user)
                        
                        if save_information == True:
                            update_balance = GetData
                            update_balance.update_balance(app, mysql)
                            
                            end_tittle = "¡El proceso ha sido exitoso!"
                            end_text = "Se ha guardado tu informacion correctamente..."
                            return render_template('processed.html', et=end_tittle, etxt=end_text)
                        else:
                            end_tittle = "¡Óops! Algo salió mal..."
                            end_text = "No ha sido posible guardar su información..."
                            return render_template('processed.html', et=end_tittle, etxt=end_text)
                    except:
                        end_tittle = "¡Óops! Algo salió mal..."
                        end_text = "No ha sido posible guardar su información..."
                        return render_template('processed.html', et=end_tittle, etxt=end_text)
                
                if user == 'damaris':
                    try:
                        diezmo = int(request.form['diezmo_damaris'])
                        dentista = int(request.form['dentista'])
                        saldo = int(request.form['saldo'])
                        gasolina = int(request.form['gasolina'])
                        renta = int(request.form['renta'])
                        
                        elements_list = [diezmo, dentista, saldo, gasolina, renta]
                        
                        save_information = GetData.save_income(app, mysql, elements_list, user)
                        
                        if save_information == True:
                            update_balance = GetData
                            update_balance.update_balance(app, mysql)
                            
                            end_tittle = "¡El proceso ha sido exitoso!"
                            end_text = "Se ha guardado tu informacion correctamente..."
                            return render_template('processed.html', et=end_tittle, etxt=end_text)
                        else:
                            end_tittle = "¡Óops! Algo salió mal..."
                            end_text = "No ha sido posible guardar su información..."
                            return render_template('processed.html', et=end_tittle, etxt=end_text)
                    except:
                        end_tittle = "¡Óops! Algo salió mal..."
                        end_text = "No ha sido posible guardar su información..."
                        return render_template('processed.html', et=end_tittle, etxt=end_text)
                    
                return render_template('income.html', dt=get_history_data[0], of=get_history_data[1], 
                                       current=get_income_history[0], past=get_income_history[1])
            # except:
        return render_template('income.html', dt=get_history_data[0], of=get_history_data[1],
                               current=get_income_history[0], past=get_income_history[1])
        
    else:
        return render_template('income.html', dt=get_history_data[0], of=get_history_data[1],
                               current=get_income_history[0], past=get_income_history[1])


@app.route('/bills', methods=['GET','POST'])
def bills():
    if request.method == 'POST':
        try:
            diezmo = int(request.form['diezmo'])
            despensa = int(request.form['despensa'])
            salud = int(request.form['salud'])
            transporte = int(request.form['transporte'])
            internet = int(request.form['internet'])
            luz = int(request.form['luz'])
            agua = int(request.form['agua'])
            gas = int(request.form['gas'])
            dentista = int(request.form['dentista'])
            gasolina = int(request.form['gasolina'])
            saldo = int(request.form['saldo'])
            renta = int(request.form['renta'])
            
            elements_list = [diezmo, despensa, salud, transporte, internet, luz, agua, gas, dentista, gasolina, saldo, renta]
            
            save_information = GetData.save_bills(app, mysql, elements_list)
            
            if save_information == True:
                update_balance = GetData
                update_balance.update_balance(app, mysql)
                            
                end_tittle = "¡El proceso ha sido exitoso!"
                end_text = "Se ha guardado tu informacion correctamente..."
                return render_template('processed.html', et=end_tittle, etxt=end_text)
            else:
                end_tittle = "¡Óops! Algo salió mal..."
                end_text = "No ha sido posible guardar su información..."
                return render_template('processed.html', et=end_tittle, etxt=end_text)
            
        except:
            pass
    return render_template('bills.html')


@app.route('/history', methods=['GET','POST'])
def history():
    
    get_history_data = GetData.db_history(app, mysql)
    get_income_history = GetData.incomes_barchart(app, mysql)
    
    return render_template('history_resp.html', dt=get_history_data[0], of=get_history_data[1],
                           current=get_income_history[0], past=get_income_history[1])


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


if __name__=='__main__':
    app.run(debug=True, port=os.getenv("PORT",default=5000), host="0.0.0.0")