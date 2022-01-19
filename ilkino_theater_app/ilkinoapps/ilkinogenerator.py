from abc import abstractmethod
from random import sample


class Generator:
    @abstractmethod
    def generate(self):
        pass


class RandomGenerator(Generator):
    '''Mengenerate 10 random number untuk diisi ke list left_gift dan right_gift'''

    def generate(self):
        super().generate()
        left_gift_num = sample(range(1, 37, 2), 5)
        right_gift_num = sample(range(2, 37, 2), 5)
        return left_gift_num, right_gift_num
