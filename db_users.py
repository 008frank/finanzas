from datetime import datetime as dt
from totals_update import TotalUpdate

class GetData:
    def set_balance(self, app, db):
        with app.app_context():
            cursor = db.connection.cursor()
            sql_update = """UPDATE bj7l3xtoftrlpschwtah.balance
                        SET diezmo=(select(select sum(diezmo)+(select sum(diezmo) from bj7l3xtoftrlpschwtah.ingresos_damaris) from bj7l3xtoftrlpschwtah.ingresos_ivan) - (select sum(diezmo) from bj7l3xtoftrlpschwtah.egresos)),
                            despensa=(select sum(despensa)-(select sum(despensa)from bj7l3xtoftrlpschwtah.egresos) from bj7l3xtoftrlpschwtah.ingresos_ivan),
                            salud=(select sum(salud)-(select sum(salud)from bj7l3xtoftrlpschwtah.egresos) from bj7l3xtoftrlpschwtah.ingresos_ivan),
                            transporte=(select sum(transporte)-(select sum(transporte)from bj7l3xtoftrlpschwtah.egresos) from bj7l3xtoftrlpschwtah.ingresos_ivan),
                            internet=(select sum(internet)-(select sum(internet)from bj7l3xtoftrlpschwtah.egresos) from bj7l3xtoftrlpschwtah.ingresos_ivan),
                            luz=(select sum(luz)-(select sum(luz)from bj7l3xtoftrlpschwtah.egresos) from bj7l3xtoftrlpschwtah.ingresos_ivan),
                            agua=(select sum(agua)-(select sum(agua)from bj7l3xtoftrlpschwtah.egresos) from bj7l3xtoftrlpschwtah.ingresos_ivan),
                            gas=(select sum(gas)-(select sum(gas)from bj7l3xtoftrlpschwtah.egresos) from bj7l3xtoftrlpschwtah.ingresos_ivan),
                            dentista=(select sum(dentista)-(select sum(dentista)from bj7l3xtoftrlpschwtah.egresos) from bj7l3xtoftrlpschwtah.ingresos_damaris),
                            saldo=(select sum(saldo)-(select sum(saldo)from bj7l3xtoftrlpschwtah.egresos) from bj7l3xtoftrlpschwtah.ingresos_damaris),
                            gasolina=(select sum(gasolina)-(select sum(gasolina)from bj7l3xtoftrlpschwtah.egresos) from bj7l3xtoftrlpschwtah.ingresos_damaris),
                            renta=(select sum(renta)-(select sum(renta)from bj7l3xtoftrlpschwtah.egresos) from bj7l3xtoftrlpschwtah.ingresos_damaris);"""
            cursor.execute(sql_update)
            db.connection.commit()
            try:
                with app.app_context():
                    cursor = db.connection.cursor()
                    sql = "SELECT * FROM bj7l3xtoftrlpschwtah.balance"
                    cursor.execute(sql)
                    elements = cursor.fetchall()
                    row = elements[0]
                    if row != None:
                        element_list = [
                            row[2], row[3], row[4],
                            row[5], row[6], row[7],
                            row[8], row[9], row[10],
                            row[11], row[12], row[13]
                        ]
                        return element_list
                    else:
                        return None
                
            except Exception as ex:
                raise Exception(ex)
    
    
    def db_history(app, database):
        with app.app_context():            
            cur = database.connection.cursor()
            myData = []
            cur_outflow_year = []
            past_outflow_year = []

            date_format = dt.now()
            cur_year = date_format.year
            past_year = cur_year - 1
            
            sql = """select * from bj7l3xtoftrlpschwtah.totales"""
            cur.execute(sql)
            data = cur.fetchall()

            for x in data:
                myData.append(list(x))
                
             # CURRENT YEAR
            for x in range(1, 13):
                sql2 = """select sum(total) from bj7l3xtoftrlpschwtah.egresos where year(fecha) = {} and month(fecha) = {};""".format(cur_year, x)
                cur.execute(sql2)
                outflow_data = cur.fetchall()
                result1 = outflow_data[0][0]

                if result1 == None:
                    cur_outflow_year.append(0)
                else:
                    cur_outflow_year.append(float(result1))

            # LAST YEAR
            for x in range(1, 13):
                sql3 = """select sum(total) from bj7l3xtoftrlpschwtah.egresos where year(fecha) = {} and month(fecha) = {};""".format(past_year, x)
                cur.execute(sql3)
                outflow_data = cur.fetchall()
                result2 = outflow_data[0][0]

                if result2 == None:
                    past_outflow_year.append(0)
                else:
                    past_outflow_year.append(float(result2))

            outflows_list = [cur_outflow_year, past_outflow_year]

            return [myData, outflows_list]
        
     
    def get_data_charts(self, app, database):
        ivan_li = []
        damaris_li = []
        date_li = []

        year = dt.now().year
        month = dt.now().month
        
        # IVAN DATA
        with app.app_context():            
            cursor = database.connection.cursor()
            sql = """select diezmo+despensa+salud+transporte+internet+luz+agua+gas
            from bj7l3xtoftrlpschwtah.ingresos_ivan
            where year(fecha)={} and month(fecha)={}""".format(year, month)
            
            cursor.execute(sql)
            data = cursor.fetchall()
            for x in data:
                ivan_li.append(x[0])
                
            # DAMARIS DATA
            sql2 = """select diezmo+dentista+gasolina+saldo+renta
            from bj7l3xtoftrlpschwtah.ingresos_damaris
            where year(fecha)={} and month(fecha)={}""".format(year, month)
            
            cursor.execute(sql2)
            data2 = cursor.fetchall()
            for x in data2:
                damaris_li.append(x[0])
                
            sql3 = """select a.fecha, b.fecha 
            from bj7l3xtoftrlpschwtah.ingresos_ivan a, bj7l3xtoftrlpschwtah.ingresos_damaris b """
            
            cursor.execute(sql3)
            data3 = cursor.fetchall()
            for x in data3:
                date_li.append(x[0])
                
            max_date = max(date_li)
                
            result_list1 = sum(ivan_li)
            result_list2 = sum(damaris_li)

            total_sum = result_list1 + result_list2
            goal = 16320
            
            current_value = goal - (total_sum)
                
            return [total_sum, current_value, max_date]
        
        
    def save_income(app, database, income_list, name):
        if name == 'ivan':
            try:
                cur_date = dt.now()
                with app.app_context():            
                    cursor = database.connection.cursor()
                    
                    current_date = dt.strftime(cur_date, "%Y-%m-%d")
                    cur_total = sum(income_list)
                    
                    # CONNETION TO SAVE DATA
                    sql = """INSERT INTO bj7l3xtoftrlpschwtah.ingresos_ivan(fecha, diezmo, despensa, salud, transporte, internet, luz, agua, gas, total)
                    VALUES ('{}',{},{},{},{},{},{},{},{},{})""".format(current_date, income_list[0],income_list[1],income_list[2],
                                                                income_list[3],income_list[4],income_list[5],income_list[6],
                                                                income_list[7], cur_total)
                    cursor.execute(sql)
                    database.connection.commit()
                    
                    tup = TotalUpdate
                    tup.updater(app, database)
                    
                    return True
                
            except:
                return False
        
        if name == 'damaris':
            try:
                cur_date = dt.now()
                with app.app_context():            
                    cursor = database.connection.cursor()
                
                    current_date = dt.strftime(cur_date, "%Y-%m-%d")
                    cur_total = sum(income_list)
                    
                    # CONNETION TO SAVE DATA
                    sql = """INSERT INTO bj7l3xtoftrlpschwtah.ingresos_damaris(fecha, diezmo, dentista, saldo, gasolina, renta, total)
                    VALUES ('{}',{},{},{},{},{},{})""".format(current_date, income_list[0],income_list[1],income_list[2],
                                                                income_list[3],income_list[4], cur_total)
                    cursor.execute(sql)
                    database.connection.commit()
                    
                    tup = TotalUpdate
                    tup.updater(app, database)
                    
                    return True
            
            except:
                return False
    
    
    def save_bills(app, database, bills_list):
        try:
            cur_date = dt.now()
            with app.app_context():            
                cursor = database.connection.cursor()
            
                current_date = dt.strftime(cur_date, "%Y-%m-%d")
                cur_total = sum(bills_list)
                
                # CONNETION TO SAVE DATA
                sql = """INSERT INTO bj7l3xtoftrlpschwtah.egresos(fecha, diezmo, despensa, salud, transporte, internet, luz, agua, gas, dentista, gasolina, saldo, renta, total)
                VALUES ('{}',{},{},{},{},{},{},{},{},{},{},{},{},{})""".format(current_date, bills_list[0],bills_list[1],bills_list[2],
                                                            bills_list[3],bills_list[4],bills_list[5],bills_list[6],
                                                            bills_list[7],bills_list[8],bills_list[9],bills_list[10],bills_list[11], cur_total)
                cursor.execute(sql)
                database.connection.commit()
                
                tup = TotalUpdate
                tup.updater(app, database)
                
                return True
        
        except:
            return False