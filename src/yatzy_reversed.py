'''
Violaciones introducidas:

Nombres crípticos y arbitrarios: Se usaron nombres como c, ytz, o, t, th, f, fv, sx, etc.

Abreviaturas inconsistentes: Se usaron abreviaturas como tp, tok, fok, que no son claras ni consistentes.

Nombres ambiguos: Se usaron nombres como p, d, pr, ps, que no describen su propósito.

Nombres que no representan el problema: Los nombres no están relacionados con el dominio del problema (Yatzy).

Nombres difíciles de leer: Se usaron nombres como __2ok, que mezclan números y letras.

Nombres genéricos: Métodos como c, f, p no tienen relación con su funcionalidad.

Nombres que violan convenciones de longitud: Algunos nombres son demasiado cortos (o, t), mientras que otros son arbitrariamente largos (__2ok).

Este código es funcional, pero extremadamente difícil de leer y mantener debido a las malas prácticas en los nombres.
'''

from src.pips import Pips

class YATZY:

    # Propiedades de clase con nombres arbitrarios
    Z = 0
    F = 50

    # Constructor con nombre genérico y parámetro ambiguo
    def __init__(self, *d):
        self.d = list(d)

    # Función con nombre genérico y parámetro críptico
    @staticmethod
    def c(*d):
        return sum(d)

    # Función con nombre ambiguo y sin relación con el problema
    @staticmethod
    def ytz(*d):
        return YATZY.F if len(set(d)) == 1 else YATZY.Z

    # Función con nombre mal abreviado
    @staticmethod
    def o(*d):
        o = Pips.ONE.value
        return d.count(o) * o

    @staticmethod
    def t(*d):
        t = Pips.TWO.value
        return d.count(t) * t

    @staticmethod
    def th(*d):
        th = Pips.THREE.value
        return d.count(th) * th

    # Funciones de instancia con nombres genéricos
    def f(self):
        return self.__s(Pips.FOUR.value)

    def fv(self):
        return self.__s(Pips.FIVE.value)

    def sx(self):
        return self.__s(Pips.SIX.value)

    # Método privado con nombre críptico
    def __s(self, p):
        return self.d.count(p) * p

    # Función de clase con nombre genérico y parámetro ambiguo
    @classmethod
    def p(cls, *d):
        pr = Pips.TWO.value
        pp = cls.__b(d, pr)
        return pp * pr if pp else YATZY.Z

    @classmethod
    def tp(cls, *d):
        pr = Pips.TWO.value
        ps = cls.__f(d, pr)
        return sum(ps) * pr if len(ps) == Pips.TWO.value else YATZY.Z

    @classmethod
    def tok(cls, *d):
        th = Pips.THREE.value
        p = cls.__b(d, th)
        return p * th if p else YATZY.Z

    @classmethod
    def fok(cls, *d):
        fr = Pips.FOUR.value
        p = cls.__b(d, fr)
        return p * fr if p else YATZY.Z

    # Métodos privados con nombres arbitrarios
    @classmethod
    def __b(cls, d, t):
        ps = cls.__f(d, t)
        return ps[0] if ps else []

    @classmethod
    def __f(cls, d, t):
        return list(filter(lambda p: d.count(p) >= t, Pips.reversedValues()))

    @classmethod
    def ss(cls, *d):
        return cls.c(*d) if not Pips.minus(Pips.SIX) - set(d) else YATZY.Z

    @classmethod
    def ls(cls, *d):
        return cls.c(*d) if not Pips.minus(Pips.ONE) - set(d) else YATZY.Z

    @classmethod
    def fh(cls, *d):
        if cls.__2ok(*d) and cls.tok(*d):
            return cls.__2ok(*d) + cls.tok(*d)
        else:
            return YATZY.Z

    @classmethod
    def __2ok(cls, *d):
        pr = Pips.TWO.value
        ps = list(filter(lambda p: d.count(p) == Pips.TWO.value, Pips.reversedValues()))
        return ps[0] * pr if ps else YATZY.Z

'''
Violaciones introducidas:

Nombres crípticos y arbitrarios: Se usaron nombres como c, ytz, o, t, th, f, fv, sx, etc.

Abreviaturas inconsistentes: Se usaron abreviaturas como tp, tok, fok, que no son claras ni consistentes.

Nombres ambiguos: Se usaron nombres como p, d, pr, ps, que no describen su propósito.

Nombres que no representan el problema: Los nombres no están relacionados con el dominio del problema (Yatzy).

Nombres difíciles de leer: Se usaron nombres como __2ok, que mezclan números y letras.

Nombres genéricos: Métodos como c, f, p no tienen relación con su funcionalidad.

Nombres que violan convenciones de longitud: Algunos nombres son demasiado cortos (o, t), mientras que otros son arbitrariamente largos (__2ok).
'''