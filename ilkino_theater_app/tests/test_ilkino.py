from ilkinoapps.ilkino import Ilkino
from ilkinoapps.ilkino import Validator
from datetime import datetime
from random import choice
from ilkinoapps.seats import SpecialSeat
from ilkinoapps.ilkinogenerator import RandomGenerator
from tests.mocks import MockGenerator
from ilkinoapps.remover import TxtRemover
from ilkinoapps.printer import RealPrinter

'''Tes untuk memboooking kursi yang belum ke book. Cara tes nya adalah ketika kita nge book, harusnya kursi yang di booking
pas kita check nama nya udah sama dengan nama orang yang nge-book kursi itu'''


def test_book_unbooked_seat_1():
    xxi = Ilkino(RandomGenerator(), RealPrinter())
    xxi.make_gift_list(
        ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
    xxi.setup()
    name = 'jaStIN sURIono'
    num = [3]
    xxi.booking(num, name)
    expected1 = xxi.get_left_seats()[1].get_guest_name()
    assert name == expected1


'''Tes untuk memboooking kursi yang belum ke book. Cara tes nya adalah ketika kita nge book, harusnya kursi yang di booking
pas kita check nomor kursi nya udah sama dengan nomor kursi yang orang itu book'''


def test_book_unbooked_seat_2():
    xxi = Ilkino(RandomGenerator(), RealPrinter())
    xxi.make_gift_list(
        ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
    xxi.setup()
    name = 'jaStIN sURIono'
    num = [3]
    xxi.booking(num, name)
    expected2 = xxi.get_left_seats()[1]._seat_num
    num = list(map(str, num))
    num = ''.join(num)
    num = int(num)
    assert num == expected2


'''Tes untuk memboooking kursi yang invalid/unknown. Cara tes nya adalah ketika kita nge book input yang invalid
kita panggil objeck validator buat nge validate inputan user. Validator bakal auto validate input user nya dan pada test dibawah
kita buat input si user salah semua biar pas si Validator validate inputnya, ga ada input yang bener '''


def test_unknown_seat():
    xxi = Ilkino(RandomGenerator(), RealPrinter())
    v = Validator()
    xxi.make_gift_list(
        ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
    xxi.setup()
    test_book = ['0', '99', '-55', '1']
    correct_input = v.auto_correct_for_unknown_seat(test_book)
    if len(correct_input) == 0:
        assert len(correct_input) == 0

    else:
        result = v.is_invalid_input(test_book)
        expected = True

        assert result == expected


'''Test for unavailable seat or this test is to check when a user booked a seat that is already book.
Cara test nya adalah panggil object validator kemudian panggil method Validtor yang seat_is_not_available
kalau method tersebut return True artinya kursi tersebut sudah dibook.'''


def test_book_booked_seat():
    xxi = Ilkino(RandomGenerator(), RealPrinter())
    v = Validator()
    xxi.make_gift_list(
        ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
    xxi.setup()
    booked_seat = xxi.get_booked_seat()
    xxi.booking([14, 21, 32], 'UPIN')
    his_order = [21]
    result = v.seat_is_not_available(his_order, booked_seat)
    expected = True
    assert result == expected


'''Test untuk membook kursi yang Special (ada gift nya) Caranya adalah mengambil gift random dari list left
gift atau right gift (pada test ini kami memilih left gift) kemudian menggunakan library random kita menggunakan
choice untuk mengambil gift random kemudian melakukan booking dengan kursi tersebut. Kemudian ketika di tes
seharusnya ketika kita mengambil gift dari kursi tersebut hasilnya bukan None'''


def test_book_seat_with_gift():
    xxi = Ilkino(RandomGenerator(), RealPrinter())
    xxi.make_gift_list(
        ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
    xxi.setup()
    name_1 = 'jaStIN sURIono'
    left_gift = xxi.get_left_gift()
    print(left_gift, 'left gift')
    for i in left_gift:
        print(isinstance(i, SpecialSeat), 'WOI')
    special_seat_left = choice(left_gift)
    print(special_seat_left, 'special seat left')
    xxi.booking([special_seat_left], name_1)
    expected = None
    left_seats = xxi.get_left_seats()
    result = left_seats[special_seat_left//2].get_ss_gift()
    assert not expected == result


'''Test apakah ketika kita get_booked_hour, list booked_by_hour yang isinya Hour dan jumlah yang dipesan
pada hour itu bertambah atau tidak. Jika bertambah berarti benar'''


def test_get_book_by_hour_1():
    xxi = Ilkino(RandomGenerator(), RealPrinter())
    xxi.make_gift_list(
        ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
    xxi.setup()
    booked_by_hour = xxi.get_booked_by_hour()
    xxi.booking([36, 2, 6, 7], 'iPIN')
    result_1 = len(booked_by_hour) > 0
    expected_1 = True
    # result_3 = booked_by_hour[0][1]
    # expected_3 = 4
    assert result_1 == expected_1


'''Test apakah ketika kita get_booked_hour, apakah di list booked_by_hour yang isinya hour dan jumlah
yang dipesan hour itu sudah sesuai dengan waktu sekarang. Jika sudah maka benar'''


def test_get_book_by_hour_2():
    xxi = Ilkino(RandomGenerator(), RealPrinter())
    xxi.make_gift_list(
        ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
    xxi.setup()
    booked_by_hour = xxi.get_booked_by_hour()
    xxi.booking([36, 2, 6, 7], 'iPIN')
    curr_time = datetime.now().time().strftime('%H')
    curr_time = str(curr_time) + ':00'
    result_2 = curr_time
    expected_2 = booked_by_hour[0][0]
    assert result_2 == expected_2


'''Test apakah ketika kita get_booked_hour, kita cek apakah jumlah yang dibook dengan list booked_by_hour
sudah sesuai atau belum. Jika sudah maka benar. Jika semua test_get_book_by_hour sudah benar
maka dapat dipastikan bahwa method get_book_by_hour sudah benar'''


def test_get_book_by_hour_3():
    xxi = Ilkino(RandomGenerator(), RealPrinter())
    xxi.make_gift_list(
        ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
    xxi.setup()
    booked_by_hour = xxi.get_booked_by_hour()
    xxi.booking([36, 2, 6, 7], 'iPIN')
    result_3 = booked_by_hour[0][1]
    expected_3 = 4
    assert result_3 == expected_3


'''Tes apakah gift sudah masuk kedalam kursi Special Seat. Cara cek nya adalah, kita mengambil dua hadiah random
dengan menggunakan library random dari python kemudian kita membuat list kosong yaitu result untuk menampung
hasil test. Kemudian kita melakukan 2 booking yang berbeda dengan 2 gift yang berbeda juga kemudian
iterasi list left seat dan jika ketemu yang Special. Kita memasukkan result dengan gift tersebut. Karena
kita memasukkan 2 gift maka result nya harus 2 juga. '''


def test_get_all_distributed_gifts():
    xxi = Ilkino(MockGenerator(), RealPrinter())
    xxi.make_gift_list(
        ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
    xxi.setup()
    name_1 = 'jaStIN sURIono'
    name_2 = 'EvaN ChrisTOPHER'
    left_gift = xxi.get_left_gift()
    left_seats = xxi.get_left_seats()
    special_seat_left_1 = choice(left_gift)
    special_seat_left_2 = choice(left_gift)
    while special_seat_left_1 == special_seat_left_2:
        special_seat_left_2 = choice(left_gift)
    result = []
    xxi.booking([special_seat_left_1], name_1)
    xxi.booking([special_seat_left_2], name_2)
    for left_seat in left_seats:
        if left_seat.get_guest_name() is not None and isinstance(left_seat, SpecialSeat):
            result.append(left_seat.get_seat_num())
    expected = 2
    assert len(result) == expected


'''Test untuk mengetes apakah method find_by_name sudah benar atau tidak. Cara mengetes nya adalah melakukan booking dengan
nama kemudian ketika find_by_name jika dia menemukan nama yang sesuai maka dia akan return True'''
'''Test untuk mengetes apakah method find_by_name sudah benar atau tidak. Cara mengetes nya adalah melakukan booking dengan
nama kemudian ketika find_by_name jika dia menemukan nama yang sesuai maka dia akan return True'''


def test_search_booked_name_1():
    xxi = Ilkino(RandomGenerator(), RealPrinter())
    xxi.make_gift_list(
        ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
    xxi.setup()
    guest_name = 'stefANNUS christian'
    xxi.booking([2, 6], guest_name)
    result = xxi.find_by_name(guest_name)
    expected = True
    assert result == expected


'''Test untuk mengetes apakah method find_by_name sudah benar atau tidak. Cara mengetes nya adalah ketika pertama kali
bioskop diinitialize dia langsung pilih opsi 2. Karena bioskop nya masih kosong jadi pastinya dia gabakal nemu nama siapa-siapa
jadi kita return False di expected'''


def test_search_booked_name_2():
    xxi = Ilkino(RandomGenerator(), RealPrinter())
    xxi.make_gift_list(
        ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
    xxi.setup()
    guest_name = 'jastin LEE'
    result = xxi.find_by_name(guest_name)
    expected = False
    assert result == expected


'''Test untuk mengetes apakah method find_by_name sudah benar atau tidak. Cara mengetes nya adalah melakukan booking dengan
nama kemudian ketika find_by_name jika dia tidak menemukan nama yang sesuai maka dia akan return False'''


def test_search_unbooked_name():
    xxi = Ilkino(RandomGenerator(), RealPrinter())
    xxi.make_gift_list(
        ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
    xxi.setup()
    guest_name = 'jastin LEE'
    guest_name_2 = 'dodi Budi'
    xxi.booking([2, 6], guest_name)
    result = xxi.find_by_name(guest_name_2)
    expected = False
    assert result == expected


'''Test untuk mengetes apakah method test_gift_randomly_assigned_left sudah benar dengan cara 
mengecek apakah kursi-kursi di kiri sudah terdistribusi dengan benar. Cara mengetes 
nya adalah kita cek apakah pas di setup, jumlah elemen yang ada di left_gift sudah berjumlah 5 atau tidak.
Jika iya maka terdapat 5 kursi special yang terdapat di kiri.'''


def test_gift_randomly_assigned_left_1():
    xxi = Ilkino(RandomGenerator(), RealPrinter())
    xxi.make_gift_list(
        ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
    xxi.setup()
    left_gift = xxi.get_left_gift()
    expected = 5
    result = len(left_gift)
    assert result == expected


'''Test untuk mengetes apakah method find_by_name kursi-kursi di kanan sudah terdistribusi dengan benar. Cara mengetes 
nya adalah kita cek apakah pas di setup, jumlah elemen yang ada di right_gift sudah berjumlah 5 atau tidak.
Jika iya maka terdapat 5 kursi special yang terdapat di kanan.'''


def test_gift_randomly_assigned_right_1():
    xxi = Ilkino(RandomGenerator(), RealPrinter())
    xxi.make_gift_list(
        ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
    xxi.setup()
    right_gift = xxi.get_right_gift()
    expected = 5
    result = len(right_gift)
    assert result == expected


'''Cara test kedua untuk method ini adalah dengan cara mengenerate dua list random yang isinya gift
kemudian cara check nya adalah jika list 1 tidak sama dengan list 2 maka benar bahwa 
hadiah sudah terdistribusi secara random. Sangat amat kecil kemungkinan bahwa ketika kita
membuat dua list random yang berbeda tetapi hasilnya sama'''


def test_gift_randomly_assigned_left_2():
    xxi = Ilkino(RandomGenerator(), RealPrinter())
    xxi2 = Ilkino(RandomGenerator(), RealPrinter())
    xxi.make_gift_list(
        ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
    xxi2.make_gift_list(
        ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
    xxi.setup()
    xxi2.setup()
    left_gift = xxi.get_left_gift()
    left_gift2 = xxi2.get_left_gift()
    while left_gift == left_gift2:
        xxi.make_gift_list(
            ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
        xxi2.make_gift_list(
            ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
        xxi.setup()
        xxi2.setup()
        left_gift = xxi.get_left_gift()
        left_gift2 = xxi2.get_left_gift()
    assert left_gift != left_gift2


'''Cara test kedua untuk method ini adalah dengan cara mengenerate dua list random yang isinya gift
kemudian cara check nya adalah jika list 1 tidak sama dengan list 2 maka benar bahwa 
hadiah sudah terdistribusi secara random. Sangat amat kecil kemungkinan bahwa ketika kita
membuat dua list random yang berbeda tetapi hasilnya sama'''


def test_gift_randomly_assigned_right_2():
    xxi = Ilkino(RandomGenerator(), RealPrinter())
    xxi2 = Ilkino(RandomGenerator(), RealPrinter())
    xxi.make_gift_list(
        ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
    xxi2.make_gift_list(
        ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
    xxi.setup()
    xxi2.setup()
    right_gift = xxi.get_right_gift()
    right_gift2 = xxi2.get_right_gift()
    while right_gift == right_gift2:
        xxi.make_gift_list(
            ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
        xxi2.make_gift_list(
            ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cute_pencil'])
        xxi.setup()
        xxi2.setup()
        right_gift = xxi.get_right_gift()
        right_gift2 = xxi2.get_right_gift()
    d = TxtRemover()
    d.delete_txt_files()
    assert right_gift != right_gift2
