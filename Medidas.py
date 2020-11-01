pit = lambda *x: (sum([el**2 for el in x]))**0.5

class Medida:
    def __init__(self, val, inc):
        self.val = val
        self.inc = inc
    def __add__(self, m2):
        val = self.val + m2.val
        inc = pit(self.inc, m2.inc)
        return Medida(val, inc)
    def __sub__(self, m2):
        val = self.val - m2.val
        inc = pit(self.inc, m2.inc)
        return Medida(val, inc)
    def __mul__(self, m2):
        if isinstance(m2, Medida):
            val = self.val*m2.val
            inc = val*pit(self.inc/self.val, m2.inc/m2.val)
            return Medida(val, inc)
        #senão, é escalar
        else:
            return Medida(self.val*m2, self.inc*m2)
    def __truediv__(self, m2):
        if isinstance(m2, Medida):
            val = self.val/m2.val
            inc = val*pit(self.inc/self.val, m2.inc/m2.val)
            return Medida(val, inc)
        else:
            return Medida(self.val/m2, self.inc/m2)
    def __pow__(self, exp):
        return Medida(self.val**exp, exp*(self.val)**(exp-1)*self.inc)
    def __str__(self):
        return f"{self.val:.3f} \pm {self.inc:.3f}".replace(".", ",")

def read(filename, headerline = False, col = 0, totalcol = 1):
    """Lê os dados do arquivo. O arquivo deve ter APENAS os dados em questão."""
    with open(filename, 'r') as f:
        s = f.read()
        if headerline:
            s = s.split('\n', 1)[1]
        s = s.replace(",", ".")
        data = [float(val) for i, val in enumerate(s.split()) if i%totalcol == col]
    return data

def sigma_m(data):
    l = len(data)
    av = sum(data)/l
    return ( sum([(x-av)**2 for x in data])/((l-1)*l) ) ** 0.5
def create(filename):
    data = read(filename)
    return Medida( sum(data)/len(data), sigma_m(data) )
