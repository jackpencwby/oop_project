class Opinion:
    def __init__(self, comment, rating):
        self.__comment = comment
        self.__rating = rating

    def get_comment(self):
        return self.__comment
    
    def get_rating(self):
        return self.__rating