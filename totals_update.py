from datetime import datetime as dt

class TotalUpdate:
    
    def updater(app, database):
        with app.app_context():            
            cur = database.connection.cursor()
            
            total_list = []
            year_list = []


            date_format = dt.now()
            date_year = date_format.year + 1
            for x in range(0,3):
                date_year -= 1
                year_list.append(date_year)

            incomefirst = []
            outflowfirst = []

            incomesecond = []
            outflowsecond = []

            for i in range(1,13):
                # FIRST YEAR
                sql_1 = """select sum(total) from bj7l3xtoftrlpschwtah.egresos where year(fecha) = {} and month(fecha) = {};""".format(year_list[0], i)

                sql_2 = """select sum(total) + (
                    select sum(total) from bj7l3xtoftrlpschwtah.ingresos_damaris 
                    where year(fecha) = {} and month(fecha) = {}
                ) 
                from bj7l3xtoftrlpschwtah.ingresos_ivan
                where year(fecha) = {} and month(fecha) = {};""".format(year_list[0], i, year_list[0], i)

                cur.execute(sql_1)
                outflow_1 = cur.fetchone()

                cur.execute(sql_2)
                income_1 = cur.fetchone()

                if income_1[0] == None:
                    incomefirst.append(0.00)
                else:
                    incomefirst.append(income_1[0])
                    

                if outflow_1[0] == None:
                    outflowfirst.append(0.00)
                else:
                    outflowfirst.append(outflow_1[0])


            for i in range(1,13):
                # SECOND YEAR
                sql_3 = """select sum(total) from bj7l3xtoftrlpschwtah.egresos where year(fecha) = {} and month(fecha) = {};""".format(year_list[1], i)

                sql_4 = """select sum(total) + (
                    select sum(total) from bj7l3xtoftrlpschwtah.ingresos_damaris 
                    where year(fecha) = {} and month(fecha) = {}
                ) 
                from bj7l3xtoftrlpschwtah.ingresos_ivan
                where year(fecha) = {} and month(fecha) = {};""".format(year_list[1], i, year_list[1], i)

                cur.execute(sql_3)
                outflow_2 = cur.fetchone()
                
                cur.execute(sql_4)
                income_2 = cur.fetchone()

                if income_2[0] == None:
                    incomesecond.append(0.00)
                else:
                    incomesecond.append(income_2[0])

                if outflow_2[0] == None:
                    outflowsecond.append(0.00)
                else:
                    outflowsecond.append(outflow_2[0])

            total_list.append(incomefirst)
            total_list.append(outflowfirst)
            total_list.append(incomesecond)
            total_list.append(outflowsecond)
        
            jan = """update bj7l3xtoftrlpschwtah.totales 
                set ingreso_actual={},
                    egreso_actual={},
                    ingreso_pasado={},
                    egreso_pasado={} where id='enero' """.format(total_list[0][0],total_list[1][0],total_list[2][0],total_list[3][0]) #january
            
            feb = """update bj7l3xtoftrlpschwtah.totales 
                set ingreso_actual={},
                    egreso_actual={},
                    ingreso_pasado={},
                    egreso_pasado={} where id='febrero' """.format(total_list[0][1],total_list[1][1],total_list[2][1],total_list[3][1]) #february

            mar = """update bj7l3xtoftrlpschwtah.totales 
                set ingreso_actual={},
                    egreso_actual={},
                    ingreso_pasado={},
                    egreso_pasado={} where id='marzo' """.format(total_list[0][2],total_list[1][2],total_list[2][2],total_list[3][2]) #march

            apr = """update bj7l3xtoftrlpschwtah.totales 
                set ingreso_actual={},
                    egreso_actual={},
                    ingreso_pasado={},
                    egreso_pasado={} where id='abril' """.format(total_list[0][3],total_list[1][3],total_list[2][3],total_list[3][3]) #april

            may = """update bj7l3xtoftrlpschwtah.totales 
                set ingreso_actual={},
                    egreso_actual={},
                    ingreso_pasado={},
                    egreso_pasado={} where id='mayo' """.format(total_list[0][4],total_list[1][4],total_list[2][4],total_list[3][4]) #may

            jun = """update bj7l3xtoftrlpschwtah.totales 
                set ingreso_actual={},
                    egreso_actual={},
                    ingreso_pasado={},
                    egreso_pasado={} where id='junio' """.format(total_list[0][5],total_list[1][5],total_list[2][5],total_list[3][5]) #june

            jul = """update bj7l3xtoftrlpschwtah.totales 
                set ingreso_actual={},
                    egreso_actual={},
                    ingreso_pasado={},
                    egreso_pasado={} where id='julio' """.format(total_list[0][6],total_list[1][6],total_list[2][6],total_list[3][6]) #july

            aug = """update bj7l3xtoftrlpschwtah.totales 
                set ingreso_actual={},
                    egreso_actual={},
                    ingreso_pasado={},
                    egreso_pasado={} where id='agosto' """.format(total_list[0][7],total_list[1][7],total_list[2][7],total_list[3][7]) #august

            sep = """update bj7l3xtoftrlpschwtah.totales 
                set ingreso_actual={},
                    egreso_actual={},
                    ingreso_pasado={},
                    egreso_pasado={} where id='septiembre' """.format(total_list[0][8],total_list[1][8],total_list[2][8],total_list[3][8]) #september

            oct = """update bj7l3xtoftrlpschwtah.totales 
                set ingreso_actual={},
                    egreso_actual={},
                    ingreso_pasado={},
                    egreso_pasado={} where id='octubre' """.format(total_list[0][9],total_list[1][9],total_list[2][9],total_list[3][9]) #october

            nov = """update bj7l3xtoftrlpschwtah.totales 
                set ingreso_actual={},
                    egreso_actual={},
                    ingreso_pasado={},
                    egreso_pasado={} where id='noviembre' """.format(total_list[0][10],total_list[1][10],total_list[2][10],total_list[3][10]) #november

            dec = """update bj7l3xtoftrlpschwtah.totales 
                set ingreso_actual={},
                    egreso_actual={},
                    ingreso_pasado={},
                    egreso_pasado={} where id='diciembre' """.format(total_list[0][11],total_list[1][11],total_list[2][11],total_list[3][11]) #december


            months = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]


            for month in months:
                cur.execute(month)
                database.connection.commit()