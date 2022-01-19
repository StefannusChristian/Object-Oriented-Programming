import argparse


class UI:
    def __init__(self, service):
        self.service = service

    def show_table(self, drop):
        self.print_header()
        if drop:
            l = self.service.get_table_from_db(True)
        else:
            l = self.service.get_table_from_db(False)

        print('+'+'-'*50+'+')
        print('|'+'Kandidat'.center(24)+'|' +
              'Suara'.center(25)+'|'.rjust(1))
        print('+'+'-'*50+'+')
        for candidate in l:
            print('|'+(candidate.name.capitalize()).center(24) +
                  '|'+str(candidate.count).center(24)+'|'.rjust(2))
        print('+'+'-'*50+'+')

    def show_option(self):
        print('\nPilihan')
        print('1: Voting')
        print('2: Keluar')

    def print_header(self):
        print('+'+'-'*50+'+')
        print('|'+'KELURAHAN MAJU MUNDUR'.center(50)+'|'.rjust(1))
        print('+'+'-'*50+'+\n')

    def print_exit_msg(self):
        print('\n2. Keluar')
        print('+'+'-' * 50 + '+')
        print(
            '|'+'TERIMA KASIH UNTUK MENGGUNAKAN PROGRAM KAMI!'.center(50)+'|')
        print('|'+'SEMOGA KANDIDAT ANDA DAPAT MENANG!'.center(50)+'|')
        print('|'+'SELAMAT TINGGAL!'.center(50)+'|')
        print('+'+'-' * 50 + '+')

    def parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-dbinit')
        args = parser.parse_args()
        init = args.dbinit
        init = init.lower()
        return init

    def run(self):
        init = self.parser()
        if init == 'true':
            self.service.get_table_from_db(True)
            while True:
                self.show_table(False)
                self.show_option()
                user_input = input('Masukkan Pilihan: ')
                if user_input == '1':
                    print('\n1. Voting')
                    check = input('Masukkan kandidat,suara: ').split(',')
                    while True:
                        if len(check) == 2:
                            kandidat, jmlh_suara = check
                            break
                        else:
                            print('Invalid Input!\n')
                            user_input = input(
                                'Masukkan kandidat,suara: ').split(',')

                    kandidat = check[0].lower()
                    jmlh_suara = int(check[1])
                    print()
                    self.service.vote(kandidat, jmlh_suara)

                elif user_input == '2':
                    self.print_exit_msg()
                    break
                else:
                    print('Invalid Input!\n')
                    continue

        elif init == 'false':
            self.service.get_table_from_db(False)
            while True:
                self.show_table(False)
                self.show_option()
                user_input = input('Masukkan Pilihan: ')
                if user_input == '1':
                    check = input('Masukkan kandidat,suara: ').split(',')
                    while True:
                        if len(check) == 2:
                            kandidat, jmlh_suara = check
                            break
                        else:
                            print('Invalid Input!\n')
                            check = input(
                                'Masukkan kandidat,suara: ').split(',')

                    kandidat = check[0].lower()
                    jmlh_suara = int(check[1])

                    print()
                    self.service.vote(kandidat, jmlh_suara)

                elif user_input == '2':
                    self.print_exit_msg()
                    break
                else:
                    print('Invalid Input!\n')
                    continue
        else:
            print('ERROR! Please Enter Only True / False!')
