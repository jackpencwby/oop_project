class Opinion:
    def __init__(self, rating, comment):
        self.__rating = rating
        self.__comment = comment

    def get_rating(self):
        return self.__rating

    def get_comment(self):
        return self.__comment
    