from src.pips import Pips

class Yatzy:

    # propiedades de clase
    ZERO = 0
    FIFTY = 50

    # No es necesario.
    # Lo mantengo para no romper la interfaz
    # publica de la clase segun los
    # casos test originales.
    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(*dice):
        return sum(dice)

    @staticmethod
    def yatzy(*dice):
        return Yatzy.FIFTY if len(set(dice)) == 1 else Yatzy.ZERO

    @staticmethod
    def ones(*dice):
        ONE = Pips.ONE.value
        return dice.count(ONE) * ONE

    @staticmethod
    def twos(*dice):
        TWO = Pips.TWO.value
        return dice.count(TWO) * TWO

    @staticmethod
    def threes(*dice):
        THREE = Pips.THREE.value
        return dice.count(THREE) * THREE

    def fours(self):
        return self.__sum_dice_equals(Pips.FOUR.value)

    def fives(self):
        return self.__sum_dice_equals(Pips.FIVE.value)

    def sixes(self):
        return self.__sum_dice_equals(Pips.SIX.value)

    def __sum_dice_equals(self, pip):
        return self.dice.count(pip) * pip

    @classmethod
    def pair(cls, *dice):
        PAIR = Pips.TWO.value
        pip= cls.__biggest_pip_repeated(dice, PAIR)
        return pip * PAIR if pip else Yatzy.ZERO

    @classmethod
    def two_pairs(cls, *dice):
        PAIR = Pips.TWO.value
        pips_pairs = cls.__filter_pips_repeated(dice, PAIR)
        return sum(pips_pairs) * PAIR if len(pips_pairs) == Pips.TWO.value else Yatzy.ZERO

    @classmethod
    def three_of_a_kind(cls, *dice):
        THREE = Pips.THREE.value
        pip = cls.__biggest_pip_repeated(dice, THREE)
        return pip * THREE if pip else Yatzy.ZERO

    @classmethod
    def four_of_a_kind(cls, *dice):
        FOUR = Pips.FOUR.value
        pip = cls.__biggest_pip_repeated(dice, FOUR)
        return pip * FOUR if pip else Yatzy.ZERO

    @classmethod
    def __biggest_pip_repeated(cls, dice, times):
        pips = cls.__filter_pips_repeated(dice, times)
        return pips[0] if pips else []

    @classmethod
    def __filter_pips_repeated(cls, dice, times):
        return list(filter(lambda pip: dice.count(pip) >= times, Pips.reversedValues()))

    @classmethod
    def small_straight(cls, *dice):
        return cls.chance(*dice) if not Pips.minus(Pips.SIX) - set(dice) else Yatzy.ZERO

    @classmethod
    def large_straight(cls, *dice):
        return cls.chance(*dice) if not Pips.minus(Pips.ONE) - set(dice) else Yatzy.ZERO

    @classmethod
    def full_house(cls, *dice):
        if cls.__two_of_a_kind(*dice) and cls.three_of_a_kind(*dice):
            return cls.__two_of_a_kind(*dice) + cls.three_of_a_kind(*dice)
        else:
            return Yatzy.ZERO

    @classmethod
    def __two_of_a_kind(cls, *dice):
        PAIR = Pips.TWO.value
        pips = list(filter(lambda pip: dice.count(pip) == Pips.TWO.value, Pips.reversedValues()))
        return pips[0] * PAIR if pips else Yatzy.ZERO
