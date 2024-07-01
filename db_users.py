from datetime import datetime as dt

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
    
    
    def db_history(app, database, name):
        if name == 'ivan':
            cur_time = dt.now()
            cur_year = cur_time.year
            year_list = []

            list_1 = []
            list_2 = []
            list_3 = []
            response = []
            
            year_list.append(cur_year)
            
            for yl in range(2):
                cur_year -= 1
                year_list.append(cur_year)
            
            
            # CONNETION TO GET FROM CURRENT DATE TO OLDEST
            # CURRENT
            sql = """SELECT * FROM bj7l3xtoftrlpschwtah.ingresos_ivan
            WHERE YEAR(fecha) = {}""".format(year_list[0])
            with app.app_context():            
                cursor = database.connection.cursor()
                cursor.execute(sql)
                elements = cursor.fetchall()
                
                for a in elements:
                    list_1.append(a)
                
                
                # LAST
                sql = """SELECT * FROM bj7l3xtoftrlpschwtah.ingresos_ivan
                WHERE YEAR(fecha) = {}""".format(year_list[1])
                cursor.execute(sql)
                elements = cursor.fetchall()
                
                for b in elements:
                    list_2.append(b)
                    
                    
                # OLDEST
                sql = """SELECT * FROM bj7l3xtoftrlpschwtah.ingresos_ivan
                WHERE YEAR(fecha) = {}""".format(year_list[2])
                cursor.execute(sql)
                elements = cursor.fetchall()
                
                for c in elements:
                    list_3.append(c)
                    
                
                response.append(year_list)
                response.append(list_1)
                response.append(list_2)
                response.append(list_3)
                
                return response
        
        
        if name == 'damaris':
            cur_time = dt.now()
            cur_year = cur_time.year
            year_list = []

            list_1 = []
            list_2 = []
            list_3 = []
            response = []
            
            year_list.append(cur_year)
            
            for yl in range(2):
                cur_year -= 1
                year_list.append(cur_year)
            
            
            # CONNETION TO GET FROM CURRENT DATE TO OLDEST
            # CURRENT
            sql = """SELECT * FROM bj7l3xtoftrlpschwtah.ingresos_damaris
            WHERE YEAR(fecha) = {}""".format(year_list[0])
            with app.app_context():            
                cursor = database.connection.cursor()
                cursor.execute(sql)
                elements = cursor.fetchall()
                
                for a in elements:
                    list_1.append(a)
                    
                    
                # LAST
                sql = """SELECT * FROM bj7l3xtoftrlpschwtah.ingresos_damaris
                WHERE YEAR(fecha) = {}""".format(year_list[1])
                cursor.execute(sql)
                elements = cursor.fetchall()
                
                for b in elements:
                    list_2.append(b)
                    
                    
                # OLDEST
                sql = """SELECT * FROM bj7l3xtoftrlpschwtah.ingresos_damaris
                WHERE YEAR(fecha) = {}""".format(year_list[2])
                cursor.execute(sql)
                elements = cursor.fetchall()
                
                for c in elements:
                    list_3.append(c)
                    
                
                response.append(year_list)
                response.append(list_1)
                response.append(list_2)
                response.append(list_3)
                
                return response
        
        
        
        if name == 'egresos':
            cur_time = dt.now()
            cur_year = cur_time.year
            year_list = []

            list_1 = []
            list_2 = []
            list_3 = []
            response = []
            
            year_list.append(cur_year)
            
            for yl in range(2):
                cur_year -= 1
                year_list.append(cur_year)
            
            
            # CONNETION TO GET FROM CURRENT DATE TO OLDEST
            # CURRENT
            sql = """SELECT * FROM bj7l3xtoftrlpschwtah.egresos
            WHERE YEAR(fecha) = {}""".format(year_list[0])
            with app.app_context():            
                cursor = database.connection.cursor()
                cursor.execute(sql)
                elements = cursor.fetchall()
                
                for a in elements:
                    list_1.append(a)
                    
                    
                # LAST
                sql = """SELECT * FROM bj7l3xtoftrlpschwtah.egresos
                WHERE YEAR(fecha) = {}""".format(year_list[1])
                cursor.execute(sql)
                elements = cursor.fetchall()
                
                for b in elements:
                    list_2.append(b)
                    
                    
                # OLDEST
                sql = """SELECT * FROM bj7l3xtoftrlpschwtah.egresos
                WHERE YEAR(fecha) = {}""".format(year_list[2])
                cursor.execute(sql)
                elements = cursor.fetchall()
                
                for c in elements:
                    list_3.append(c)
                    
                
                response.append(year_list)
                response.append(list_1)
                response.append(list_2)
                response.append(list_3)
                
                return response
        
     
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
                    
                    # CONNETION TO SAVE DATA
                    sql = """INSERT INTO bj7l3xtoftrlpschwtah.ingresos_ivan(fecha, diezmo, despensa, salud, transporte, internet, luz, agua, gas)
                    VALUES ('{}',{},{},{},{},{},{},{},{})""".format(current_date, income_list[0],income_list[1],income_list[2],
                                                                income_list[3],income_list[4],income_list[5],income_list[6],
                                                                income_list[7])
                    cursor.execute(sql)
                    database.connection.commit()
                    
                    return True
                
            except:
                return False
        
        if name == 'damaris':
            try:
                cur_date = dt.now()
                with app.app_context():            
                    cursor = database.connection.cursor()
                
                    current_date = dt.strftime(cur_date, "%Y-%m-%d")
                    
                    # CONNETION TO SAVE DATA
                    sql = """INSERT INTO bj7l3xtoftrlpschwtah.ingresos_damaris(fecha, diezmo, dentista, saldo, gasolina, renta)
                    VALUES ('{}',{},{},{},{},{})""".format(current_date, income_list[0],income_list[1],income_list[2],
                                                                income_list[3],income_list[4])
                    cursor.execute(sql)
                    database.connection.commit()
                    
                    return True
            
            except:
                return False
    
    
    def save_bills(app, database, bills_list):
        try:
            cur_date = dt.now()
            with app.app_context():            
                cursor = database.connection.cursor()
            
                current_date = dt.strftime(cur_date, "%Y-%m-%d")
                
                # CONNETION TO SAVE DATA
                sql = """INSERT INTO bj7l3xtoftrlpschwtah.egresos(fecha, diezmo, despensa, salud, transporte, internet, luz, agua, gas, dentista, gasolina, saldo, renta)
                VALUES ('{}',{},{},{},{},{},{},{},{},{},{},{},{})""".format(current_date, bills_list[0],bills_list[1],bills_list[2],
                                                            bills_list[3],bills_list[4],bills_list[5],bills_list[6],
                                                            bills_list[7],bills_list[8],bills_list[9],bills_list[10],bills_list[11])
                cursor.execute(sql)
                database.connection.commit()
                
                return True
        
        except:
            return False