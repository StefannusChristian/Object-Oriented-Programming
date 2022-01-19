from myvending.glass import Glass


class ElectricGlass(Glass):  # Inherit Glass Object
    # CONSTRUCTOR

    def __init__(self, max_capacity):
        super().__init__(max_capacity)
        self.__is_boiled = False
        self.__eglass_price = 2

    # METHODS

    def boil(self):  # to boil the water inside the electric glass
        # if the current electric glass capacity is the max capacity that means the electric glass is empty so the E.glass cannot boil
        if self.get_current_capacity() == self.get_max_capacity():
            #print("Boil Water!\nCannot Boil. There is no water!")
            self.set_boil(False)
        else:  # there is water inside the E.glass and we boil the water
            self.set_boil(True)
            #print("Boil Water!\nWater is now boiled!")

    def pour_water(self, vol):
        super().pour_water(vol)
        print('Pour Hot Water\nsmoke: wushhhh.....wushhhhh.....\n')

    # SETTER

    def set_boil(self,  condition):  # to set the water state in the glass to boiled
        self.__is_boiled = condition

    # GETTER

    def get_boiled_status(self):
        return self.__is_boiled

    def get_e_glass_price(self):
        return self.__eglass_price

    # PRINT ELECTRIC GLASS OBJECT

    def __str__(self):
        return f"Electric Glass: [Curr Capacity: {self.get_current_capacity()}] - [Max Capacity: {self.get_max_capacity()}] - [Is_Boiled: {self.get_boiled_status()}] - [Price: {self.get_e_glass_price()}$] "
