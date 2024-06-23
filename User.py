from werkzeug.security import check_password_hash, generate_password_hash

class User():
    def __init__(self, db, username, myPassword):
        self.db = db
        self.username = username
        self.myPassword = myPassword
        
    def identication(self):
        sql = """SELECT password FROM users WHERE user='{}'""".format(self.username)
                    
        cur = self.db.cursor()
        cur.execute(sql)
        password = cur.fetchone()

        response = check_password_hash(password[0], self.myPassword)
        
        return response