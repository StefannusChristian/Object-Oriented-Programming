class Sorter:
    '''Buat nge-sort seat nya biar rapih aja
    Kalo input user nya 10,9,8 kita jadiin dia 8,9,10 biar
    pas print txt sama ticket nya dia ascending order'''

    def sort_seat(self, seat: list):
        seat = list(map(int, seat))
        seat.sort()
        seat = list(map(str, seat))
        return seat
