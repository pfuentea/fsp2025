class SistemaError(Exception):
    pass


class EmailInvalidoError(SistemaError):
    pass

class ClienteExisteError(SistemaError):
    pass

