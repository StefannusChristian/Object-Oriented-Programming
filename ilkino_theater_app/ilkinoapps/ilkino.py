from datetime import datetime
from ilkinoapps.seats import Seat, SpecialSeat, Thexx
from ilkinoapps.printer import RealPrinter
from ilkinoapps.validator import Validator
from ilkinoapps.remover import TxtRemover
from ilkinoapps.sorter import Sorter


class Ilkino:
    # CONSTRUCTOR

    def __init__(self, generator_type, printer, Ilkino_max_capacity=36):
        self._Ilkino_max_capacity = Ilkino_max_capacity

        '''List yang isinya objek kursi yang seat number nya ganjil'''
        self._left_seats = []

        '''List yang isinya objek kursi yang seat number nya genap'''
        self._right_seats = []

        '''List yang isinya nomor - nomor kursi ganjil mana aja yang special'''
        self._left_gift = []

        '''List yang isinya nomor - nomor kursi genap mana aja yang special'''
        self._right_gift = []

        '''List yang isinya list yang isinya [[seat_number,guest_name],[seat_number,guest_name]]'''
        self._booked_seat = []

        '''List yang isinya list yang isinya [['2:00',4],['3:00',5]]'''
        self._report = []

        '''List yang isinya gift apa saja yang diinput (misal: teddy_bear, coklat, dll)'''
        self._gift_list = []

        '''Ada Random Generator sama Mock Generator Buat Test Buat Nanti di Masukin ke Parameter Setup'''
        self._generator_type = generator_type

        '''Printer nya Ilkino'''
        self._printer = printer

    # GETTER

    def get_Ilkino_max_capacity(self):
        return self._Ilkino_max_capacity

    def get_report(self):
        return self._report

    def get_booked_seat(self):
        return self._booked_seat

    def get_right_seats(self):
        return self._right_seats

    def get_left_seats(self):
        return self._left_seats

    def get_left_gift(self):
        return self._left_gift

    def get_right_gift(self):
        return self._right_gift

    def get_gift_list(self):
        return self._gift_list

    def get_generator_type(self):
        return self._generator_type

    def get_printer(self):
        return self._printer

    # SETTER

    def make_report(self, thetime: list):
        self._report.append(thetime)

    def make_booked_seat(self, booked_seat: list):
        self._booked_seat.append(booked_seat)

    def make_left_seats(self, left_seat):
        self._left_seats.append(left_seat)

    def make_right_seats(self, right_seat):
        self._right_seats.append(right_seat)

    def make_gift_list(self, gift_list: list):
        self._gift_list = gift_list

    # METHODS

    def setup(self):
        self._left_gift, self._right_gift = self.get_generator_type().generate()
        left_gift = self.get_left_gift()
        right_gift = self.get_right_gift()
        left_gift_list = self.get_gift_list()
        right_gift_list = self.get_gift_list()
        cout = 0
        for left_seat in range(1, self.get_Ilkino_max_capacity() + 1, 2):
            if left_seat in left_gift:
                gift = left_gift_list[cout]
                special_seat = SpecialSeat(left_seat, gift)
                self.make_left_seats(special_seat)
                cout += 1
            else:
                seat = Seat(left_seat)
                self.make_left_seats(seat)
        ctr = 0
        for right_seat in range(2, self.get_Ilkino_max_capacity() + 1, 2):
            if right_seat in right_gift:
                gift = right_gift_list[ctr]
                special_seat = SpecialSeat(right_seat, gift)
                self.make_right_seats(special_seat)
                ctr += 1
            else:
                seat = Seat(right_seat)
                self.make_right_seats(seat)

    def booking(self, seat_number: list, guest_name: str, is_special=False, rp=RealPrinter(), s=Sorter()):
        right_seats = self.get_right_seats()
        left_seats = self.get_left_seats()
        timereport = self.get_report()

        '''Catet real time sekarang (Hour nya Aja)'''
        curr_time = datetime.now().time().strftime('%H')
        curr_time = str(curr_time) + ':00'

        '''Iterasi sepanjang panjang dari time_report yang isinya waktu sekarang
        dan jumlah yang ada pada jam segitu, kalau dia sama berarti tambahin aja 
        orderan si yang lagi pesen yaitu len(seat_number) kalau ga sama berarti udah 
        beda jam lagi jadinya dia masuk ke else habis itu dia buat lagi report baru
        yang isinya jam segitu dan len(seat_number)'''

        for alltime in range(len(timereport)):
            if curr_time == timereport[alltime][0]:
                timereport[alltime][1] += len(seat_number)
                break
        else:
            self.make_report([curr_time, len(seat_number)])

        for seat in seat_number:
            self.make_booked_seat([seat, guest_name])

        '''Di sort biar mengantisipasi kalau input dia ga ascending'''

        seat_number = s.sort_seat(seat_number)

        '''Masukin seat_number yang udah dipesen ke list left_seats (kalau dia ganjil)
        dan right_seats (kalau dia genap) terus sebelom dimasukin kita check dulu
        apakah dia special_seat atau bukan. kalau iya kita bikin parameter 
        is_special dan di set ke True agar bisa di-test. Set juga nama di kursi itu
        biar bisa di find_by_name'''

        for seat in seat_number:
            if int(seat) % 2 == 0:
                right_seats[int(seat) // 2 - 1]._name = guest_name
                right_seats[int(seat) // 2 - 1]._booked_time = curr_time
                if isinstance(right_seats[int(seat) // 2 - 1], SpecialSeat):
                    is_special = True
            else:
                left_seats[(int(seat) // 2)]._name = guest_name
                left_seats[(int(seat) // 2)]._booked_time = curr_time
                if isinstance(left_seats[(int(seat) // 2)], SpecialSeat):
                    is_special = True

        '''Panggil objek printer buat nge_print si guest_name udh nge book
        kursi yang mana aja terus kita convert ticket ke txt terus di print'''

        rp.print_booking(guest_name, seat_number)
        rp.print_ticket(guest_name, seat_number, is_special)

    def find_by_name(self, find_name, rp=RealPrinter(), s=Sorter()):
        '''Buat variabel is_found yang pertama di set ke False dulu, kemudian kalo
        nama yang ingin dicari ketemu, tinggal set si is_found ke True biar bisa di test.
        Kemudian if len(booked_seats) == 0 itu buat mengantisipasi kalau pas pertama banget
        dia langsung booking kan theater nya masi kosong jadi pasti gabakalan ketemu nama yang dia pengen cari'''

        is_found = False
        booked_seats = self.get_booked_seat()
        left_seats = self.get_left_seats()
        right_seats = self.get_right_seats()
        if len(booked_seats) == 0:
            print('Theater is Empty! No Booking has Been Made Yet!\n')
            return is_found
        else:
            '''pas kita cari nama kita juga pengen tau dia pesen kursi yang mana aja jadi pertama
            kita buat list buat nampung kursi dia yang mana aja. Terus kita iterasi list booked_seats
            yang isinya nomor" kursi yang dibook orang tertentu, kalau misalnya ketemu namanya, kita append 
            ke his_seat kemudian di_sort biar rapih aja'''

            his_seat = []
            for seat_order, guest_name in booked_seats:
                if guest_name == find_name:
                    his_seat.append(seat_order)
            his_seat = s.sort_seat(his_seat)

            '''Kalau his_seat ga kosong artinya nama yang ingin dicari pernah nge_book
            ,kemudian di join agar pas di print dia bentuk nya 1,2,3. Kemudian kita panggil
            objek printer buat nge_print informasi tentang si nama yang ingin kita cari
            bersama dengan kursi mana saja yang dia sudah book. Kemudian kita set is_found = True biar
            bisa di test'''
            if len(his_seat) > 0:
                one_of_his_seat = int(his_seat[0])
                if one_of_his_seat % 2 == 0:
                    his_time = right_seats[one_of_his_seat //
                                           2-1].get_booked_time()
                else:
                    his_time = left_seats[one_of_his_seat//2].get_booked_time()
                rp.print_guest_info(his_seat, his_time)
                is_found = True
                return is_found
            else:
                '''Kalau list his_seat nya itu kosong berarti pas kita iterasi list booked_seats dia ga nemu
                nama yang ingin dicari artinya ga ada yang di append ke list his_seat artinya ga ada nama yang
                ketemu'''
                print(f'There is no guest named {find_name}!\n')
                return is_found

    def get_booked_by_hour(self):
        timereport = self.get_report()
        return timereport

    def get_all_distributed_gifts(self, rp=RealPrinter()):
        left_seats = self.get_left_seats()
        right_seats = self.get_right_seats()
        print('\nAll distributed Seat Number-Gift:')
        rp.print_all_distributed_gift(left_seats, right_seats, SpecialSeat)

    def gui(self, rp=RealPrinter()):
        rp.print_header()
        rp.print_seats(Thexx, SpecialSeat, self.get_Ilkino_max_capacity(),
                       self.get_left_seats(), self.get_right_seats())
        rp.print_choice()

    def run(self, rp=RealPrinter(), v=Validator(), s=Sorter(), d=TxtRemover()):
        while True:
            self.gui()
            user_choice = input('Enter your choice 1-4: ')
            '''Kalau input user nya bukan 1,2,3,4, program bakal minta user input ulang'''
            if v.is_invalid_choice(user_choice):
                print('Invalid Input! Please enter a number between 1-4!\n')
                continue
            else:
                if user_choice == '1':
                    booked_seat = self.get_booked_seat()
                    print('\n1. Seat Boooking')
                    if len(booked_seat) == 36:
                        print('THEATER IS FULL! Cannot Book Anymore!\n')
                        continue
                    while len(booked_seat) < 36:
                        seat_number = list(
                            map(str, (input('Enter Seat Number: ').split(','))))
                        '''Kalau input user bukan seat_number yang valid yaitu dari 1 - 36 maka program
                        bakal auto validate input user dan kalau semua input dari user salah maka program
                        bakal minta user input ulang'''
                        if v.is_invalid_input(seat_number):
                            seat_number = v.auto_correct_for_unknown_seat(
                                seat_number)
                            s.sort_seat(seat_number)
                            if len(seat_number) == 0:
                                print(
                                    'All of your inputs are wrong! Please enter a valid input :)\n')
                                continue
                        '''Kalau dari semua kursi yang user pesen, ada satu aja kursi yang not_available atau udah kepesen
                        maka program bakal minta user input ulang'''
                        if v.seat_is_not_available(seat_number, booked_seat):
                            print(
                                'One of your seat order is already booked! Please order another seat!\n')
                            continue
                        '''Kalau user misalnya lalai dalam menginput program dan ada duplikasi dalam inputnya
                        maka program bakal auto validate input user dan membuang semua duplicate 
                        misalnya input dia [1,2,2,3,3] maka program bakal auto validate input dia menjadi
                        [1,2,3]'''
                        if v.seat_order_is_duplicate(seat_number):
                            seat_number = v.auto_correct_for_duplicate_input(
                                seat_number)
                            s.sort_seat(seat_number)
                        break

                    guest_name = input('Enter name: ').lower()
                    self.booking(seat_number, guest_name)

                elif user_choice == '2':
                    print('\n2. Find by Name')
                    find_name = input(
                        'Enter the name you want to find: ').lower()
                    self.find_by_name(find_name)

                elif user_choice == '3':
                    print('\n3. Report')
                    report = self.get_booked_by_hour()
                    rp.print_report(report)
                    self.get_all_distributed_gifts()

                elif user_choice == '4':
                    d.delete_txt_files()
                    rp.print_exit_msg()
                    break
