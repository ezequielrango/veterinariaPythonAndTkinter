import mysql.connector

class DBConnector:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="nombre_de_tu_base_de_datos"
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, values=None):
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)

        return self.cursor.fetchall()

    def execute_insert(self, query, values):
        self.cursor.execute(query, values)
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
