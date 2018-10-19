class Hoja:

    def __init__(self, valor, enlace):
        self.valor = valor
        self.valor_enlace = enlace

    def g_valor(self):
        """valor
        Retorna el valor de hoja
        """

        return self.valor

    def g_enlace(self):
        """ enlace
        Retorna el valor de enlace de la hoja
        """

        return self.valor_enlace
