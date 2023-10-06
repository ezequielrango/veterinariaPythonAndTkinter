import mysql.connector
from ..modelos.clientes import Cliente  # Asegúrate de importar la clase Cliente

class ClienteRepository:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def guardar_cliente(self, cliente):
        # Insertar un nuevo cliente en la base de datos
        query = """
            INSERT INTO clientes (dni, nombre, domicilio, mascota, especie, edad, telefono, turno)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            cliente.getDni(),
            cliente.getNombre(),
            cliente.getDomicilio(),
            cliente.getMascota(),
            cliente.getEspecie(),
            cliente.getEdad(),
            cliente.getTelefono(),
            cliente.getTurno()
        )

        try:
            cursor = self.db_connector.connection.cursor()
            cursor.execute(query, values)
            self.db_connector.connection.commit()
            cursor.close()
            print("Cliente guardado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al guardar el cliente: {err}")

    def listar_clientes(self):
        # Obtener todos los clientes de la base de datos
        query = "SELECT * FROM clientes"
        try:
            cursor = self.db_connector.connection.cursor(dictionary=True)
            cursor.execute(query)
            clientes = []
            for row in cursor.fetchall():
                cliente = Cliente(
                    row["dni"],
                    row["nombre"],
                    row["domicilio"],
                    row["mascota"],
                    row["especie"],
                    row["edad"],
                    row["telefono"],
                    row["turno"]
                )
                clientes.append(cliente)
            cursor.close()
            return clientes
        except mysql.connector.Error as err:
            print(f"Error al listar los clientes: {err}")
            return []

    def eliminar_cliente(self, dni):
        # Eliminar un cliente de la base de datos por su DNI
        query = "DELETE FROM clientes WHERE dni = %s"
        values = (dni,)
        try:
            cursor = self.db_connector.connection.cursor()
            cursor.execute(query, values)
            self.db_connector.connection.commit()
            cursor.close()
            print("Cliente eliminado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al eliminar el cliente: {err}")
