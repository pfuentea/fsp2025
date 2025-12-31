from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre: str, rut: str):
        self._nombre = nombre
        self._rut = rut
    
    @abstractmethod
    def calcular_sueldo(self) -> float:
        pass

    def __str__(self):
        return f"{self._nombre} ({self._rut})"
    
class EmpleadoHonorario(Empleado):

    def __init__(self, nombre: str, rut: str, horas_trabajadas: int, valor_hora: float):
        super().__init__(nombre, rut)
        self._horas_trabajadas = horas_trabajadas
        self._valor_hora = valor_hora

    def calcular_sueldo(self) -> float:
        return self._horas_trabajadas * self._valor_hora
    
class EmpleadoContratado(Empleado):

    def __init__(self, nombre: str, rut: str, sueldo_base: float, bono: float = 0):
        super().__init__(nombre, rut)
        self._sueldo_base = sueldo_base
        self._bono = bono

    def calcular_sueldo(self) -> float:
        return self._sueldo_base + self._bono
    
jorge=EmpleadoHonorario("Jorge","1-1",44,15000)

sueldo=jorge.calcular_sueldo()
print(jorge)
print(f"Sueldo:{sueldo}")