class Student:
    def __init__(self, name, age, pref_subject):
        self.name = name
        self.age = age
        self._preffered_subject = pref_subject

    def bodedInClass(self, current_subject):
        if self._preffered_subject == current_subject:
            return True
        return False

    def makeFunOfTeacher(self, teacher):
        print("making fun of {}".format(teacher))

        if self.bodedInClass():
            print("without him noticing")
        else:
            print("they know, they now, oh no, they now")

    def talk(self, other):
        print("I, {} am talking with {}".format(self.name, other))

class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return "{}:{}".format(self.hour, self.minute)

    def returnMaxPair(self):