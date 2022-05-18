MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
          'november', 'december']


class Date:
    def __init__(self, d, m, y):
        self._d = d
        self._m = m
        self._y = y

    def day(self):
        return self._d

    def month(self):
        return self._m

    def year(self):
        return self._y

    def month_name(self):
        return MONTHS[self._m - 1]

    def leap_year(self):
        if (self._y % 4 == 0 and (self._y % 100 != 0)) or self._y % 400 == 0:
            return True
        else:
            return False

    def to_string(self):
        a = (str(self._d) + "/" + str(self._m) + "/" + str(self._y))
        return a

    def __str__(self):
        return str(self._d) + '-' + str(self._m) + '-' + str(self._y)

    def __eq__(self, other):
        return self._d == other._d and self._m == other._m and self._y == other._y

    def __lt__(self, other):
        if self._y < other.y:
            return -1
        elif self._y > other.y:
            return 1
        elif self._m < other.m:
            return -1
        elif self._m > other.m:
            return 1
        elif self._d < other.d:
            return -1
        else:
            return 1
