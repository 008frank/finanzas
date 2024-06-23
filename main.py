from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from User import User
from db_users import GetData

app = Flask(__name__)

db = mysql.connector.connect(
    host = "192.168.1.172",
    user ="caja",
    password = "hd_tu_08",
    database = "finanzas",
    port = "3306"
)


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        user = User(db, request.form['input_1'], request.form['input_2'])
        if user.identication() == True:
            return redirect(url_for('home'))
        else:
            msg = "Contraseña incorrecta..."
            return render_template('index.html', message=msg)
    else:
        return render_template('index.html')


@app.route('/home')
def home():
    get_list = GetData.set_balance(None, db)
    total_value = sum(get_list)
    list_values1 = [0]
    list_values2 = [0]
    
    charts_info = GetData.get_data_charts(None, db)
    
    for x in charts_info[0]:
        list_values1.append(float(x))
    for x in charts_info[1]:
        list_values2.append(float(x))
    
    return render_template('home.html', element=get_list, total=total_value, ch1=list_values1, ch2=list_values2)


@app.route('/income', methods=['GET','POST'])
def income():
    if request.method=='POST':
        try:
            selection = request.form['select_form']
        except:
            selection = request.form['select_income_form']
        
        if selection == "history":
            try:
                history = request.form['get_my_history']
                getting_history = GetData.db_history(db, history)
                
                years = getting_history[0]
                data1 = getting_history[1]
                data2 = getting_history[2]
                data3 = getting_history[3]
                
                return render_template('income.html', user=history, yr=years, 
                                       d1=data1, d2=data2, d3=data3)
            except:
                return redirect(url_for('income'))
        
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
                        
                        save_information = GetData.save_income(db, elements_list, user)
                        
                        if save_information == True:
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
                        
                        save_information = GetData.save_income(db, elements_list, user)
                        
                        if save_information == True:
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
                    
                return render_template('income.html')
            # except:
        return redirect(url_for('income'))
        
    else:
        return render_template('income.html')


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
            
            save_information = GetData.save_bills(db, elements_list)
            
            if save_information == True:
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
    if request.method=='POST':
        try:
            history = request.form['get_my_history']
            getting_history = GetData.db_history(db, history)
            
            years = getting_history[0]
            data1 = getting_history[1]
            data2 = getting_history[2]
            data3 = getting_history[3]
            
            return render_template('history_resp.html', user=history, yr=years, 
                                    d1=data1, d2=data2, d3=data3)
        except:
            return redirect(url_for('history'))
    return render_template('history_resp.html')


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


if __name__=='__main__':
    app.run(debug=True)