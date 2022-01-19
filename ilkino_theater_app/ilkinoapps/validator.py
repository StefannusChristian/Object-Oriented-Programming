class Validator:
    '''Method untuk menentukan apakah ketika user diminta choice nya 1-4, dia input
    selain itu. Pertama caranya buat list valid_choice yang isinya 1-4 kemudian tinggal
    check aja kalau input user ga ada di dalem list itu berarti input dia invalid'''

    def is_invalid_choice(self, user_choice: str):
        valid_choice = [str(x) for x in range(1, 5)]
        if user_choice not in valid_choice:
            return True
        return False

    '''Kalau ada satu aja order dari user yang udah ada di booked_seat artinya
    dia order seat yang udah dibooked jadinya seat_is_not_available bakal return True'''

    def seat_is_not_available(self, seat_order: list, booked_seat: list):
        return any(seat in seat_order for seat, name in booked_seat)

    '''Kalau user nya lalai dalam input nya terus diinput nya ada duplicate
    maka seat_order_is_duplicate bakal return True'''

    def seat_order_is_duplicate(self, seat_order: list):
        return any(seat_order.count(seat) > 1 for seat in seat_order)

    '''Method buat cek kalau input user nya itu unknown seat atau misalnya pas
    dia diminta input seat_number dia masukin ayam goreng misalnya atau dimasukkin
    99,-4, dll'''

    def is_invalid_input(self, seat_order: list):
        valid_input = [seat_num for seat_num in range(1, 37)]
        valid_input = list(map(str, valid_input))
        check = all(seat in valid_input for seat in seat_order)
        return not check

    '''Method buat membetulkan input user yang duplicate. Jadi kalau usernya input duplicate
    program langsung auto ilangin semua yang duplicate'''

    def auto_correct_for_duplicate_input(self, seat_number: list):
        print('There are multiple seat orders in your order! ')
        print(
            'Our program will automatically validate your input!')
        print(f'Your wrong input = {seat_number}')
        seat_number = list(set(seat_number))
        seat_number = sorted(list(map(int, seat_number)))
        seat_number = list(map(str, seat_number))
        print(
            f'Your Order After Validation = {seat_number}\n')
        return seat_number

    '''Method buat membetulkan input user yang salah. Jadi kalau usernya inputnya salah
    program bakal benerin inputnya misalnya input dia [es_krim_durian,1,2,-5] maka
    program bakal validate inputnya menjadi [1,2]. Tapi kalau misalnya input dia salah semua maka
    program bakal nyuruh user input ulang  '''

    def auto_correct_for_unknown_seat(self, seat_number: list):
        print(
            'Your input is invalid! Ilkino Seat Numbers is in the range of 1-36!')
        print(
            'Our program will automatically validate your input!')
        print(f'Your wrong input = {seat_number}')
        valid_input = [seat_num for seat_num in range(1, 37)]
        valid_input = list(map(str, valid_input))
        valid_seat_number = []
        for seat in seat_number:
            if seat in valid_input:
                valid_seat_number.append(seat)
        seat_number = valid_seat_number
        seat_number = sorted(list(map(int, seat_number)))
        seat_number = list(map(str, seat_number))
        print(
            f'Your Order After Validation = {seat_number}\n')
        return seat_number
