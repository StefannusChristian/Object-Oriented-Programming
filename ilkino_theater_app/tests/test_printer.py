from ilkinoapps.printer import RealPrinter
from tests.mocks import MockPrinter, MockGenerator
from ilkinoapps.seats import Seat, SpecialSeat, Thexx
from ilkinoapps.ilkino import Ilkino
from ilkinoapps.printer import RealPrinter


def test_print_booking():
    mp = MockPrinter()
    name = 'Victor'
    seat_num = [1, 2, 3]
    expected = name, seat_num
    result = mp.print_booking(name, seat_num)
    assert expected == result


def test_print_normal_ticket():
    mp = MockPrinter()
    name = 'Noel'
    seat_num = [5, 25]
    expected = name, seat_num
    result = mp.print_normal_ticket(name, seat_num)
    assert expected == result


def test_print_special_ticket():
    mp = MockPrinter()
    name = 'Jastin'
    seat_num = [7, 31]
    expected = name, seat_num
    result = mp.print_normal_ticket(name, seat_num)
    assert expected == result


def test_print_ticket_1():
    mp = MockPrinter()
    name = 'pak bambang'
    seat_num = [3, 29, 15]
    is_special = True
    expected = name, seat_num, is_special
    result = mp.print_ticket(name, seat_num, is_special)
    assert expected == result


def test_print_ticket_2():
    mp = MockPrinter()
    name = 'pak bambang'
    seat_num = [3, 29, 15]
    is_special = False
    expected = name, seat_num, is_special
    result = mp.print_ticket(name, seat_num, is_special)
    assert expected == result


def test_print_header():
    mp = MockPrinter()
    result = mp.print_header()
    expected = True
    assert result == expected


def test_print_choice():
    mp = MockPrinter()
    result = mp.print_choice()
    expected = True
    assert result == expected


def test_print_guest_info():
    mp = MockPrinter()
    his_seat = [10, 11, 12, 13, 14, 15]
    his_time = '18:00'
    expected = his_seat, his_time
    result = mp.print_guest_info(his_seat, his_time)
    assert expected == result


def test_print_report():
    mp = MockPrinter()
    report = [['3:00', 5], ['4:00', 7]]
    result = mp.print_report(report)
    expected = report
    assert result == expected


def test_print_all_distributed_gift():
    mp = MockPrinter()
    s1 = Seat('1')
    s2 = Seat('2')
    s3 = SpecialSeat('3', 'chocolate')
    left_seats = [s1, s3]
    right_seats = [s2]
    expected = left_seats, right_seats, s3
    result = mp.print_all_distributed_gift(left_seats, right_seats, s3)
    assert expected == result


def test_print_exit_msg():
    mp = MockPrinter()
    result = mp.print_exit_msg()
    expected = True
    assert result == expected


def test_print_seats():
    mp = MockPrinter()
    xxi = Ilkino(MockGenerator(), RealPrinter())
    thex = Thexx('10')
    ss = SpecialSeat('5', 'Doll')
    s1 = Seat('23')
    s2 = Seat('20')
    left = [s1, ss]
    right = [s2]
    full = xxi.get_Ilkino_max_capacity()
    expected = thex, ss, full, left, right
    result = mp.print_seats(thex, ss, full, left, right)
    assert expected == result
