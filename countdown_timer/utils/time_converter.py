

class TimeConverter(object):

    def get_seconds(self, time_str):
        """ Get seconds from HH:MM:SS """
        h, m, s = time_str.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)

    def validate_input_time(self, input):
        if len(input) == 8 and self.__validateHours(input) and self.__validateMinutes(input) and self.__validateSeconds(input):
            return True

        return False

    # Private section.
    def __validateHours(self, input):
        if input[:2].isnumeric() and input[2] == ':':
            return True

        return False

    def __validateMinutes(self, input):
        if input[3:5].isnumeric() and input[5] == ':':
            return True

        return False

    def __validateSeconds(self, input):
        if input[6:].isnumeric():
            return True

        return False