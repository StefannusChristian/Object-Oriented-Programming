from ilkinoapps.ilkinogenerator import Generator
from ilkinoapps.printer import Printer


class MockGenerator(Generator):
    def generate(self):
        left_gift = [1, 3, 5, 7, 9]
        right_gift = [2, 4, 6, 8, 10]
        return left_gift, right_gift


class MockPrinter(Printer):
    def print_booking(self, guest_name, seat_number):
        return guest_name, seat_number

    def print_normal_ticket(self, guest_name, seat_number):
        return guest_name, seat_number

    def print_special_ticket(self, guest_name, seat_number):
        return guest_name, seat_number

    def print_ticket(self, guest_name, seat_number, is_special):
        return guest_name, seat_number, is_special

    def print_header(self, is_header_print=False):
        is_header_print = True
        return is_header_print

    def print_choice(self, is_choice_print=False):
        is_choice_print = True
        return is_choice_print

    def print_guest_info(self, his_seat, his_time):
        return his_seat, his_time

    def print_report(self, report):
        return report

    def print_all_distributed_gift(self, left_seats, right_seats, SpecialSeat):
        return left_seats, right_seats, SpecialSeat

    def print_exit_msg(self, is_exit_msg_print=False):
        is_exit_msg_print = True
        return is_exit_msg_print

    def print_seats(self, Thexx, SpecialSeat, full, left, right):
        return Thexx, SpecialSeat, full, left, right
