
class Cliente:
    def __init__(self, dni, nombre, domicilio,  mascota, especie, edad, telefono, turno):
        self._dni = dni
        self._nombre = nombre
        self._domicilio = domicilio        
        self._mascota = mascota
        self._especie = especie
        self._edad = edad
        self._telefono = telefono
        self._turno = turno


    # Getters >>>>>>>>>>>>>>

    def getDni(self):
        return self._dni

    def getNombre(self):
        return self._nombre
    
    def getDomicilio(self):
        return self._domicilio
    
    def getMascota(self):
        return self._mascota
    
    def getEspecie(self):
        return self._especie
    
    def getEdad(self):
        return self._edad    
    
    def getTelefono(self):
        return self._telefono
    
    def getTurno(self):
        return self._turno

    # Setters >>>>>>>>>>>>>>>

    def setDni(self, dni):
        self._dni = dni

    def setNombre(self, nombre):
        self._nombr = nombre

    def setDomicilio(self, domicilio):
        self._domicilio = domicilio

    def setMascota(self, mascota):
        self._mascota = mascota

    def setEspecie(self, especie):
        self._especie = especie

    def setEdad(self, edad):
        self._edad = edad

    def setTelefono(self, telefono):
        self._telefono = telefono
    
    def setTurno(self, turno):
        self._turno = turno
