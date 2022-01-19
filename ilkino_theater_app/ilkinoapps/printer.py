from abc import abstractmethod
from ilkinoapps.converter import Converter


@abstractmethod
class Printer:
    def print_booking(self, guest_name, seat_number):
        pass

    def print_normal_ticket(self, guest_name: str, seat_number: list):
        pass

    def print_special_ticket(self, guest_name: str, seat_number: list):
        pass

    def print_ticket(self, guest_name: str, seat_number: list, is_special):
        pass

    def print_header(self, is_header_print=False):
        pass

    def print_choice(self, is_choice_print=False):
        pass

    def print_guest_info(self, his_seat, his_time):
        pass

    def print_report(self, report):
        pass

    def print_all_distributed_gift(self, left_seats, right_seats, SpecialSeat):
        pass

    def print_exit_msg(self, is_exit_msg_print=False):
        pass

    def print_seats(self, Thexx, SpecialSeat, full, left, right):
        pass


class RealPrinter(Printer):
    def print_booking(self, guest_name: str, seat_number: list):
        super().print_booking(guest_name, seat_number)
        guest_name = guest_name.lower()
        guest_name = guest_name.split(' ')
        g_name = []
        for name in guest_name:
            name = name.capitalize()
            g_name.append(name)
        g_name = '_'.join(g_name)
        guest_name = g_name
        seat_number = '_'.join(seat_number)
        print(f'Seat {seat_number} is booked by {guest_name}.')
        print(
            f'Receipt {guest_name}_{seat_number}_.txt is printed. Don"t lose your ticket.\n'
        )

    def print_normal_ticket(self, guest_name: str, seat_number: list, c=Converter()):
        super().print_normal_ticket(guest_name, seat_number)
        seat_number = ','.join(seat_number)
        ticket = ''
        ticket += '+' + '-' * 60 + '+\n'
        ticket += '|' + 'IL Kino Receipt'.center(60) + '|\n'
        ticket += '+' + '-' * 60 + '+\n'
        ticket += '|' + ' Name                    :   ' + \
            f'{guest_name}'.ljust(31)+'|\n'
        ticket += '|' + ' Seat Number             :   ' + \
            f'{seat_number}'.ljust(31)+'|\n'
        ticket += '+' + '-' * 60 + '+\n'
        ticket += '|' + \
            'Please arrive 15 minutes before.'.center(60) + '|\n'
        ticket += '+' + '-' * 60 + '+\n'
        c.convert_ticket_to_txt_file(guest_name, seat_number, ticket)

    def print_special_ticket(self, guest_name: str, seat_number: list, c=Converter()):
        super().print_special_ticket(guest_name, seat_number)
        seat_number = ','.join(seat_number)
        ticket = ''
        ticket += '+' + '-' * 60 + '+\n'
        ticket += '|' + 'IL Kino Receipt'.center(60) + '|\n'
        ticket += '+' + '-' * 60 + '+\n'
        ticket += '|' + ' Name                    :   ' + \
            f'{guest_name}'.ljust(31)+'|\n'
        ticket += '|' + ' Seat Number             :   ' + \
            f'{seat_number}'.ljust(31)+'|\n'
        ticket += '+' + '-' * 60 + '+\n'
        ticket += '|' + \
            'Please check below your seat to get your gift.'.center(
                60) + '|\n'
        ticket += '|' + \
            'Please arrive 15 minutes before.'.center(60) + '|\n'
        ticket += '+' + '-' * 60 + '+\n'
        c.convert_ticket_to_txt_file(guest_name, seat_number, ticket)

    def print_ticket(self, guest_name: str, seat_number: list, is_special):
        super().print_ticket(guest_name, seat_number, is_special)
        guest_name = guest_name.lower()
        guest_name = guest_name.split(' ')
        g_name = []
        for name in guest_name:
            name = name.capitalize()
            g_name.append(name)
        g_name = '_'.join(g_name)
        guest_name = g_name
        if not is_special:
            self.print_normal_ticket(guest_name, seat_number)
        else:
            self.print_special_ticket(guest_name, seat_number)

    def print_header(self, is_header_print=False):
        super().print_header(is_header_print)
        print('+'+'-' * 62 + '+')
        print('|'+'IL Kino'.center(62)+'|')
        print('|'+'Nansenstrasse 22,'.center(62)+'|')
        print('|'+'12047 Berlin'.center(62)+'|')
        print('+'+'-' * 62 + '+\n')
        print('+'+'-' * 62 + '+')
        print('|'+'SCREEN'.center(62)+'|')
        print('+'+'-' * 62 + '+')
        is_header_print = True

    def print_choice(self, is_choice_print=False):
        super().print_choice(is_choice_print)
        print('\n+'+'-' * 3+'+'+'-'*17+'+')
        print('| '+'1 '+'|'+'Seat Booking'.rjust(15)+'|'.rjust(3))
        print('+'+'-' * 3+'+'+'-'*17+'+')
        print('| '+'2 '+'|'+'Find by Name'.rjust(15)+'|'.rjust(3))
        print('+'+'-' * 3+'+'+'-'*17+'+')
        print('| '+'3 '+'|'+'Report'.rjust(11)+'|'.rjust(7))
        print('+'+'-' * 3+'+'+'-'*17+'+')
        print('| '+'4 '+'|'+'Exit'.rjust(10)+'|'.rjust(8))
        print('+'+'-' * 3+'+'+'-'*17+'+\n')
        is_choice_print = True

    def print_seats(self, Thexx, SpecialSeat, full, left, right):
        super().print_seats(Thexx, SpecialSeat, full, left, right)
        left_right = 0
        tracker = 0
        posisi_kursi = 'kiri'
        print('+------+  +------+  +------+        +------+  +------+  +------+')
        while left_right != full:
            if posisi_kursi == 'kiri':
                for i in range(tracker, tracker+3):
                    if left[i].get_guest_name() == None:
                        print(
                            '|  '+'{:0>2}'.format(left[i]._seat_num)+'  |  ', end='')
                    else:
                        if isinstance(left[i], SpecialSeat):
                            thex = Thexx('G')
                            print(
                                '|  '+'{:2}'.format(thex._seat_num)+'  |  ', end='')
                        else:
                            thex = Thexx('X')
                            print(
                                '|  '+'{:2}'.format(thex._seat_num)+'  |  ', end='')
                print('\t    ', end='')
                posisi_kursi = 'kanan'
            else:
                for i in range(tracker, tracker+3):
                    if right[i].get_guest_name() == None:
                        print(
                            '|  '+'{:0>2}'.format(right[i]._seat_num)+'  |  ', end='')
                    else:
                        if isinstance(right[i], SpecialSeat):
                            thex = Thexx('G')
                            print(
                                '|  '+'{:2}'.format(thex._seat_num)+'  |  ', end='')
                        else:
                            thex = Thexx('X')
                            print(
                                '|  '+'{:2}'.format(thex._seat_num)+'  |  ', end='')
                print('')
                print('+------+  +------+  +------+        +------+  +------+  +------+')
                posisi_kursi = 'kiri'
                left_right += 6
                tracker += 3

    def print_exit_msg(self, is_exit_msg_print=False):
        super().print_exit_msg(is_exit_msg_print)
        print('\n4. Exit')
        print('+'+'-' * 62 + '+')
        print('|'+'Thanks for using our program!'.center(62)+'|')
        print('|'+'Have a great experience!'.center(62)+'|')
        print('|'+'ENJOY YOUR MOVIE!'.center(62)+'|')
        print('+'+'-' * 62 + '+')
        is_exit_msg_print = True

    def print_all_distributed_gift(self, left_seats, right_seats, SpecialSeat):
        super().print_all_distributed_gift(left_seats, right_seats, SpecialSeat)
        all_distributed_gift = []
        for left_seat in left_seats:
            if left_seat.get_guest_name() is not None and isinstance(left_seat, SpecialSeat):
                all_distributed_gift.append(
                    (left_seat.get_seat_num(), '-', left_seat.get_ss_gift()))

        for right_seat in right_seats:
            if right_seat.get_guest_name() is not None and isinstance(right_seat, SpecialSeat):
                all_distributed_gift.append(
                    (right_seat.get_seat_num(), '-', right_seat.get_ss_gift()))

        all_distributed_gift.sort()
        for gift in all_distributed_gift:
            print(gift[0], gift[1], gift[2])
        print()

    def print_report(self, report):
        super().print_report(report)
        if len(report) > 0:
            print('+'+'-'*50+'+')
            print('|'+'Hour'.center(24)+'|' +
                  'Number of Booking'.center(25)+'|'.rjust(1))
            print('+'+'-'*50+'+')
            for ilkino_time, amount in report:
                print('|'+ilkino_time.center(24) +
                      '|'+str(amount).center(24)+'|'.rjust(2))
            print('+'+'-'*50+'+')
        else:
            print('+'+'-'*50+'+')
            print('|'+'Hour'.center(24)+'|' +
                  'Number of Booking'.center(25)+'|'.rjust(1))
            print('+'+'-'*50+'+')
            print('|'+' '*24+'|'+' '*24+'|'.rjust(2))
            print('|'+'EMPTY!'.center(24)+'|'+'0'.center(24)+'|'.rjust(2))
            print('|'+' '*24+'|'+' '*24+'|'.rjust(2))
            print('+'+'-'*50+'+')
            print('|'+'NO BOOKING HAS BEEN MADE!'.center(50)+'|')
            print('+'+'-'*50+'+\n')

    def print_guest_info(self, his_seat, his_time):
        super().print_guest_info(his_seat, his_time)
        his_seat = ','.join(his_seat)
        print('+'+'-'*50+'+')
        print('|'+'Seat'.center(24)+'|' +
              'Booking Information'.center(25)+'|'.rjust(1))
        print('+'+'-'*50+'+')
        print('|'+f'Seat: {his_seat}'.center(24) +
              '|'+f'Time: {his_time}'.center(25)+'|')
        print('+'+'-'*50+'+\n')
