import argparse
from ilkinoapps.ilkino import Ilkino
from ilkinoapps.ilkinogenerator import RandomGenerator
from ilkinoapps.printer import RealPrinter
if __name__ == '__main__':
    bioskop = Ilkino(RandomGenerator(), RealPrinter())
    parser = argparse.ArgumentParser()
    parser.add_argument('-gift')
    args = parser.parse_args()
    gift_list = args.gift.split(',')
    bioskop.make_gift_list(gift_list)
    bioskop.setup()
    bioskop.run()
