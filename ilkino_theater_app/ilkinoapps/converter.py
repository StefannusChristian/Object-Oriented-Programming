class Converter:
    def convert_ticket_to_txt_file(self, guest_name: str, seat_number: str, ticket: str):
        with open(f'{guest_name}_seat_number_{seat_number}_.txt', 'w') as f:
            f.write(ticket)
