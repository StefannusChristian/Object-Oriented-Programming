from myvending.tray import Tray
from myvending.glass import Glass
from myvending.electric_glass import ElectricGlass


class VendingMachine:
    # CONSTRUCTOR

    def __init__(self):
        self.__vending_tray = None

    # METHODS

    def receive_order(self):
        while True:
            try:
                amount = int(input('Masukan jumlah pesanan anda: '))
                break
            except ValueError:
                print('\nInvalid Input! Please enter an Integer!\n')
                amount = int(input('Masukan jumlah pesanan anda: '))
                break

        print()
        self.__vending_tray = Tray(amount)
        for i in range(amount):
            order = input('Masukan jenis minuman [hot/cold]: ').lower()
            valid_order = ['cold', 'hot']

            while order not in valid_order:
                print(f'\nInvalid Input! Valid Input is {valid_order}\n')
                order = input('Masukan jenis minuman [hot/cold]: ').lower()

            if order == 'cold':
                glass = Glass(500)
                glass.add_water(200)
                self.__vending_tray.add_glass(glass)

            elif order == 'hot':
                e_glass = ElectricGlass(500)
                e_glass.add_water(200)
                e_glass.boil()
                self.__vending_tray.add_glass(e_glass)
        print(
            f'\nSilahkan terima tray dengan {self.__vending_tray.count_glass_objects_in_tray()} gelas.')
        print()
        print(self.__vending_tray)

    def print_bill(self):
        total_price = 0
        print('\nMencetak tagihan:')
        if self.__vending_tray is None:
            print('Tray is Empty! No Orders Has Been Made!')

        elif self.__vending_tray.get_glass_list_length() == 0:
            print('1. 0x Hot = 0$')
            print('2. 0x Cold = 0$')
            print(f'Total = {total_price}$')

        else:
            for glass_obj in (self.__vending_tray.get_glass_list()):
                if type(glass_obj) == type(ElectricGlass(500)):
                    print(
                        f'1x Hot = {glass_obj.get_e_glass_price()}$')
                    total_price += glass_obj.get_e_glass_price()
                elif type(glass_obj) == type(Glass(500)):
                    print(
                        f'1x Cold = {glass_obj.get_glass_price()}$')
                    total_price += glass_obj.get_glass_price()
            print(f'Total = {total_price}$')
