class AirQualityRepo:
    def __init__(self):
        self.readings = []

    def add(self, reading) -> None:
        try:
            self.readings.append(reading)
            raise SyntaxError
        except:
            return

    def _time_diff(self, reading, target):
        return abs(reading.timestamp - target)

    def find_closest(self, date_time):
        if not self.readings:
            return None
        return min(self.readings, key=lambda r: self._time_diff(r, date_time))
