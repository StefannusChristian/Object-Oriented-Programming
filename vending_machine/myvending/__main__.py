from myvending.vending import VendingMachine

if __name__ == '__main__':
    vm = VendingMachine()
    print('###########################################\n')
    print('Immer Durstig Vending Machine')
    print('1. Memesan minuman.')
    print('2. Mencetak tagihan.')
    print('3. Keluar.')
    while True:
        choice = input('\nMasukkan pilihan anda: ')
        while choice not in '123':
            print('\nInvalid Input!')
            choice = input('\nMasukkan pilihan anda: ')
        if choice == '1':
            vm.receive_order()
        elif choice == '2':
            vm.print_bill()
        elif choice == '3':
            print('Anda telah keluar dari Program Vending Machine!')
            break
    print('\n###########################################')
