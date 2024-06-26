from werkzeug.security import check_password_hash, generate_password_hash

class User():
    def __init__(self, app, db, username, myPassword):
        self.app = app
        self.db = db
        self.username = username
        self.myPassword = myPassword
        
    def identication(self):
        sql = """SELECT password FROM bj7l3xtoftrlpschwtah.users WHERE user='{}'""".format(self.username)
        with self.app.app_context():            
            cur = self.db.connection.cursor()
            cur.execute(sql)
            password = cur.fetchone()

            response = check_password_hash(password[0], self.myPassword)
            
            return response