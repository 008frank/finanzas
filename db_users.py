from datetime import datetime as dt
from totals_update import TotalUpdate

class GetData:
    def update_balance(app, db):
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
            goal = 16600
            
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

                    tiup = TotalUpdate
                    tiup.total_income_update(app, database)
                    
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
        

    def incomes_barchart(app, database):
        with app.app_context():            
                cur = database.connection.cursor()

                current_list =[]
                past_list = []

                sql_query = """SELECT * FROM bj7l3xtoftrlpschwtah.ingresos_mensuales;"""
                cur.execute(sql_query)
                data = cur.fetchall()

                cur_list = [
                    data[0][1],data[0][3],data[0][5],data[0][7],data[0][9],data[0][11],data[0][13],data[0][15],data[0][17],data[0][19],data[0][21],data[0][23], #enero
                    data[1][1],data[1][3],data[1][5],data[1][7],data[1][9],data[1][11],data[1][13],data[1][15],data[1][17],data[1][19],data[1][21],data[1][23], #febrero
                    data[2][1],data[2][3],data[2][5],data[2][7],data[2][9],data[2][11],data[2][13],data[2][15],data[2][17],data[2][19],data[2][21],data[2][23], #marzo
                    data[3][1],data[3][3],data[3][5],data[3][7],data[3][9],data[3][11],data[3][13],data[3][15],data[3][17],data[3][19],data[3][21],data[3][23], #abril
                    data[4][1],data[4][3],data[4][5],data[4][7],data[4][9],data[4][11],data[4][13],data[4][15],data[4][17],data[4][19],data[4][21],data[4][23], #mayo
                    data[5][1],data[5][3],data[5][5],data[5][7],data[5][9],data[5][11],data[5][13],data[5][15],data[5][17],data[5][19],data[5][21],data[5][23], #junio
                    data[6][1],data[6][3],data[6][5],data[6][7],data[6][9],data[6][11],data[6][13],data[6][15],data[6][17],data[6][19],data[6][21],data[6][23], #julio
                    data[7][1],data[7][3],data[7][5],data[7][7],data[7][9],data[7][11],data[7][13],data[7][15],data[7][17],data[7][19],data[7][21],data[7][23], #agosto
                    data[8][1],data[8][3],data[8][5],data[8][7],data[8][9],data[8][11],data[8][13],data[8][15],data[8][17],data[8][19],data[8][21],data[8][23], #septiembre
                    data[9][1],data[9][3],data[9][5],data[9][7],data[9][9],data[9][11],data[9][13],data[9][15],data[9][17],data[9][19],data[9][21],data[9][23], #octubre
                    data[10][1],data[10][3],data[10][5],data[10][7],data[10][9],data[10][11],data[10][13],data[10][15],data[10][17],data[10][19],data[10][21],data[10][23], #noviembre
                    data[11][1],data[11][3],data[11][5],data[11][7],data[11][9],data[11][11],data[11][13],data[11][15],data[11][17],data[11][19],data[11][21],data[11][23], #diciembre
                ]
                for x in cur_list:
                    if x == None:
                        current_list.append(0.00)
                    else:
                        current_list.append(x)


                pas_list = [
                    data[0][2],data[0][4],data[0][6],data[0][8],data[0][10],data[0][12],data[0][14],data[0][16],data[0][18],data[0][20],data[0][22],data[0][24],
                    data[1][2],data[1][4],data[1][6],data[1][8],data[1][10],data[1][12],data[1][14],data[1][16],data[1][18],data[1][20],data[1][22],data[1][24],
                    data[2][2],data[2][4],data[2][6],data[2][8],data[2][10],data[2][12],data[2][14],data[2][16],data[2][18],data[2][20],data[2][22],data[2][24],
                    data[3][2],data[3][4],data[3][6],data[3][8],data[3][10],data[3][12],data[3][14],data[3][16],data[3][18],data[3][20],data[3][22],data[3][24],
                    data[4][2],data[4][4],data[4][6],data[4][8],data[4][10],data[4][12],data[4][14],data[4][16],data[4][18],data[4][20],data[4][22],data[4][24],
                    data[5][2],data[5][4],data[5][6],data[5][8],data[5][10],data[5][12],data[5][14],data[5][16],data[5][18],data[5][20],data[5][22],data[5][24],
                    data[6][2],data[6][4],data[6][6],data[6][8],data[6][10],data[6][12],data[6][14],data[6][16],data[6][18],data[6][20],data[6][22],data[6][24],
                    data[7][2],data[7][4],data[7][6],data[7][8],data[7][10],data[7][12],data[7][14],data[7][16],data[7][18],data[7][20],data[7][22],data[7][24],
                    data[8][2],data[8][4],data[8][6],data[8][8],data[8][10],data[8][12],data[8][14],data[8][16],data[8][18],data[8][20],data[8][22],data[8][24],
                    data[9][2],data[9][4],data[9][6],data[9][8],data[9][10],data[9][12],data[9][14],data[9][16],data[9][18],data[9][20],data[9][22],data[9][24],
                    data[10][2],data[10][4],data[10][6],data[10][8],data[10][10],data[10][12],data[10][14],data[10][16],data[10][18],data[10][20],data[10][22],data[10][24],
                    data[11][2],data[11][4],data[11][6],data[11][8],data[11][10],data[11][12],data[11][14],data[11][16],data[11][18],data[11][20],data[11][22],data[11][24]
                ]
                for y in pas_list:
                    if y == None:
                        past_list.append(0.00)
                    else:
                        past_list.append(y)

                return [current_list, past_list]