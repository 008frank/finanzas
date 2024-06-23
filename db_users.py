from datetime import datetime as dt

class GetData:
    def set_balance(self, db):
        cursor = db.cursor()
        sql_uodate = """UPDATE balance
                    SET diezmo=(select(select sum(diezmo)+(select sum(diezmo) from ingresos_damaris) from ingresos_ivan) - (select sum(diezmo) from egresos)),
                        despensa=(select sum(despensa)-(select sum(despensa)from egresos) from ingresos_ivan),
                        salud=(select sum(salud)-(select sum(salud)from egresos) from ingresos_ivan),
                        transporte=(select sum(transporte)-(select sum(transporte)from egresos) from ingresos_ivan),
                        internet=(select sum(internet)-(select sum(internet)from egresos) from ingresos_ivan),
                        luz=(select sum(luz)-(select sum(luz)from egresos) from ingresos_ivan),
                        agua=(select sum(agua)-(select sum(agua)from egresos) from ingresos_ivan),
                        gas=(select sum(gas)-(select sum(gas)from egresos) from ingresos_ivan),
                        dentista=(select sum(dentista)-(select sum(dentista)from egresos) from ingresos_damaris),
                        saldo=(select sum(saldo)-(select sum(saldo)from egresos) from ingresos_damaris),
                        gasolina=(select sum(gasolina)-(select sum(gasolina)from egresos) from ingresos_damaris),
                        renta=(select sum(renta)-(select sum(renta)from egresos) from ingresos_damaris);"""
        cursor.execute(sql_uodate)
        db.commit()
        try:
            cursor = db.cursor()
            sql = "SELECT * FROM balance"
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
    
    
    def db_history(database, name):
        if name == 'ivan':
            cur_time = dt.now()
            cur_year = cur_time.year
            year_list = []

            list_1 = []
            list_2 = []
            list_3 = []
            response = []
            
            cursor = database.cursor()
            year_list.append(cur_year)
            
            for yl in range(2):
                cur_year -= 1
                year_list.append(cur_year)
            
            
            # CONNETION TO GET FROM CURRENT DATE TO OLDEST
            # CURRENT
            sql = """SELECT * FROM ingresos_ivan
            WHERE YEAR(fecha) = {}""".format(year_list[0])
            cursor.execute(sql)
            elements = cursor.fetchall()
            
            for a in elements:
                list_1.append(a)
                
                
            # LAST
            sql = """SELECT * FROM ingresos_ivan
            WHERE YEAR(fecha) = {}""".format(year_list[1])
            cursor.execute(sql)
            elements = cursor.fetchall()
            
            for b in elements:
                list_2.append(b)
                
                
            # OLDEST
            sql = """SELECT * FROM ingresos_ivan
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
            
            cursor = database.cursor()
            year_list.append(cur_year)
            
            for yl in range(2):
                cur_year -= 1
                year_list.append(cur_year)
            
            
            # CONNETION TO GET FROM CURRENT DATE TO OLDEST
            # CURRENT
            sql = """SELECT * FROM ingresos_damaris
            WHERE YEAR(fecha) = {}""".format(year_list[0])
            cursor.execute(sql)
            elements = cursor.fetchall()
            
            for a in elements:
                list_1.append(a)
                
                
            # LAST
            sql = """SELECT * FROM ingresos_damaris
            WHERE YEAR(fecha) = {}""".format(year_list[1])
            cursor.execute(sql)
            elements = cursor.fetchall()
            
            for b in elements:
                list_2.append(b)
                
                
            # OLDEST
            sql = """SELECT * FROM ingresos_damaris
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
            
            cursor = database.cursor()
            year_list.append(cur_year)
            
            for yl in range(2):
                cur_year -= 1
                year_list.append(cur_year)
            
            
            # CONNETION TO GET FROM CURRENT DATE TO OLDEST
            # CURRENT
            sql = """SELECT * FROM egresos
            WHERE YEAR(fecha) = {}""".format(year_list[0])
            cursor.execute(sql)
            elements = cursor.fetchall()
            
            for a in elements:
                list_1.append(a)
                
                
            # LAST
            sql = """SELECT * FROM egresos
            WHERE YEAR(fecha) = {}""".format(year_list[1])
            cursor.execute(sql)
            elements = cursor.fetchall()
            
            for b in elements:
                list_2.append(b)
                
                
            # OLDEST
            sql = """SELECT * FROM egresos
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
        
     
    def get_data_charts(self, database):
        ivan_li = []
        damaris_li = []

        year = dt.now().year
        month = dt.now().month
        cursor = database.cursor()
        
        # IVAN DATA
        sql = """select diezmo+despensa+salud+transporte+internet+luz+agua+gas
        from ingresos_ivan
        where year(fecha)={} and month(fecha)={}""".format(year, month)
        
        cursor.execute(sql)
        data = cursor.fetchall()
        for x in data:
            ivan_li.append(x[0])
        # DAMARIS DATA
        sql2 = """select diezmo+dentista+gasolina+saldo+renta
        from ingresos_damaris
        where year(fecha)={} and month(fecha)={}""".format(year, month)
        
        cursor.execute(sql2)
        data2 = cursor.fetchall()
        for x in data2:
            damaris_li.append(x[0])
            
        result_list1 = []
        result_list2 = []


        # RESULT FOR IVAN LIST
        if len(ivan_li) == 1:
            result_list1.append(ivan_li[0])

        elif len(ivan_li) == 2:
            result_list1.append(ivan_li[0])
            result_list1.append(ivan_li[0] + ivan_li[1])

        elif len(ivan_li) == 3:
            result_list1.append(ivan_li[0])
            result_list1.append(ivan_li[0] + ivan_li[1])
            result_list1.append(ivan_li[0] + ivan_li[1] + ivan_li[2])

        elif len(ivan_li) == 4:
            result_list1.append(ivan_li[0])
            result_list1.append(ivan_li[0] + ivan_li[1])
            result_list1.append(ivan_li[0] + ivan_li[1] + ivan_li[2])
            result_list1.append(ivan_li[0] + ivan_li[1] + ivan_li[2] + ivan_li[3])
        else:
            result_list1[0]
            
        # RESULT FOR DAMARIS LIST
        if len(damaris_li) == 1:
            result_list2.append(damaris_li[0])

        elif len(damaris_li) == 2:
            result_list2.append(damaris_li[0])
            result_list2.append(damaris_li[0] + damaris_li[1])
        else:
            result_list2[0]
            
        return [result_list1, result_list2]
        
        
    def save_income(database, income_list, name):
        if name == 'ivan':
            try:
                cursor = database.cursor()
                cur_date = dt.now()
                
                current_date = dt.strftime(cur_date, "%Y-%m-%d")
                
                # CONNETION TO SAVE DATA
                sql = """INSERT INTO ingresos_ivan(fecha, diezmo, despensa, salud, transporte, internet, luz, agua, gas)
                VALUES ('{}',{},{},{},{},{},{},{},{})""".format(current_date, income_list[0],income_list[1],income_list[2],
                                                            income_list[3],income_list[4],income_list[5],income_list[6],
                                                            income_list[7])
                cursor.execute(sql)
                database.commit()
                
                return True
            
            except:
                return False
        
        if name == 'damaris':
            try:
                cursor = database.cursor()
                cur_date = dt.now()
                
                current_date = dt.strftime(cur_date, "%Y-%m-%d")
                
                # CONNETION TO SAVE DATA
                sql = """INSERT INTO ingresos_damaris(fecha, diezmo, dentista, saldo, gasolina, renta)
                VALUES ('{}',{},{},{},{},{})""".format(current_date, income_list[0],income_list[1],income_list[2],
                                                            income_list[3],income_list[4])
                cursor.execute(sql)
                database.commit()
                
                return True
            
            except:
                return False
    
    
    def save_bills(database, bills_list):
        try:
            cursor = database.cursor()
            cur_date = dt.now()
            
            current_date = dt.strftime(cur_date, "%Y-%m-%d")
            
            # CONNETION TO SAVE DATA
            sql = """INSERT INTO egresos(fecha, diezmo, despensa, salud, transporte, internet, luz, agua, gas, dentista, gasolina, saldo, renta)
            VALUES ('{}',{},{},{},{},{},{},{},{},{},{},{},{})""".format(current_date, bills_list[0],bills_list[1],bills_list[2],
                                                        bills_list[3],bills_list[4],bills_list[5],bills_list[6],
                                                        bills_list[7],bills_list[8],bills_list[9],bills_list[10],bills_list[11])
            cursor.execute(sql)
            database.commit()
            
            return True
        
        except:
            return False