class Seat:
    # CONSTRUCTOR
    def __init__(self, seat_num: str):
        self._seat_num = seat_num
        self._name = None
        self._booked_time = None

    # GETTER
    def get_seat_num(self):
        return self._seat_num

    def get_guest_name(self):
        return self._name

    def get_booked_time(self):
        return self._booked_time


class SpecialSeat(Seat):
    # CONSTRUTOR
    def __init__(self, seat_num: str, gift: str):
        super().__init__(seat_num)
        self._gift = gift

    # GETTER
    def get_ss_gift(self):
        return self._gift


class Thexx(Seat):
    def __init__(self, seat_num):
        super().__init__(seat_num)
        self._seat_num = seat_num
