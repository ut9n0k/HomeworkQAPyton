class TrainCar:
    def __init__(self, num: int, places: int):
        self.__traincar_num = num
        self.__places = places
        self.__list_of_passengers = list()

    def add_passenger(self, place: int):
        if len(self.__list_of_passengers) < self.__places:
            self.__list_of_passengers.append(place)
        else:
            raise Exception(
                f"Sorry, but we haven't place for you here. Go to the next car!"
            )

    @property
    def __len__(self):
        return len(self.__list_of_passengers)

    @property
    def traincar_num(self):
        return f"Num of the traincar is {self.traincar_num}"

    @property
    def places(self):
        return self.__places

    @property
    def list_of_passengers(self):
        return self.__list_of_passengers

    def __str__(self):
        return f'[{self.__traincar_num}]'
