

class Classwork:
    def __init__(self, classwork_name, random_day, random_hour):
        self._classwork_name = classwork_name
        self._day = random_day
        self._hour = random_hour
        self._id = id

    @property
    def classwork_name(self):
        return self._classwork_name

    @property
    def day(self):
        return self._day

    @property
    def hour(self):
        return self._hour

    @property 
    def id(self):
        return self._id
