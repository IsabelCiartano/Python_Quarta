class Nodo:
    """Nodo autoreferenziale per albero binario."""

    def __init__(self, valore, sx=None, dx=None):
        self.valore = valore
        self.sx = sx
        self.dx = dx

    def inserisci(self, valore):
        if valore < self.valore :
            if self.sx is None:
                self.sx = Nodo(valore)
            else:
                self.sx.inserisci(valore)
        else:
            if self.dx  is None:
                self.dx=Nodo(valore)
            else:
                self.dx.inserisci(valore)
     
    def cerca(self, valore):
        if valore == self.valore:
            return True
        if valore < self.valore:
            if self.sx is None:
                return False
            else:
               return self.sx.cerca(valore)
        if valore > self.valore:
            if self.dx is None:
                return False
            else:
               return self.dx.cerca(valore)     
    def __str__(self):
        return f"Nodo({self.valore}, sx={self.sx}, dx={self.dx})"


# Esempio d'uso
radice = Nodo(5)
for v in [3, 7, 1, 4, 6, 8]:
    radice.inserisci(v)

print(radice.cerca(4))            # True
print(radice.cerca(9))            # False