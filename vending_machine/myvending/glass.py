class Glass:
    # CONSTRUCTOR

    def __init__(self, max_capacity):
        # assume the glass is empty when it is first made
        self.__current_capacity = max_capacity
        self.__max_capacity = max_capacity
        self.__min_capacity = 0
        self.__glass_price = 3

    # METHODS

    def add_water(self, vol):
        # if we add water than the current capacity of the glass decreases
        cap = self.get_current_capacity() - vol

        # if we add water the glass capacity can be lower than zero
        if cap < self.get_min_capacity():
            # set the glass current capacity to zero
            self.set_capacity(self.get_min_capacity())
            #print(f"Add {vol} ml of water\nCannot add anymore water! Capacity is full!\nGlass Capacity is now {self.get_current_capacity()} ml\n")

        else:
            self.set_capacity(cap)
            # print(
            # f"{vol} ml of water is added into the glass \nGlass Capacity is now {self.get_current_capacity()} ml\n")

    def pour_water(self, vol):
        # if we pour/spill water than the current capacity of the glass increases
        cap = self.get_current_capacity() + vol

        # when we pour out water the current empty glass capacity can exceed 500
        if cap > self.get_max_capacity():
            self.set_capacity(self.get_max_capacity())
            print(f"Pour {vol} ml of water.\nCannot pour anymore water! Capacity is minus!\nGlass Capacity is now {self.get_current_capacity()} ml\n")

        else:
            # set the empty glass capacity to the max_capacity (500)
            self.set_capacity(cap)
            print(
                f"{vol} ml of water is pour out of the glass \nGlass Capacity is now {self.get_current_capacity()} ml\n")

    def pour_all_water(self):   # empty the glass
        self.set_capacity(self.get_max_capacity())

    def fill_glass_until_full(self):  # fill the glass until full
        self.set_capacity(self.get_min_capacity())

    def get_glass_water_volume(self):
        volume = self.get_max_capacity() - self.get_current_capacity()
        return volume

    # SETTER

    def set_capacity(self, capacity):
        self.__current_capacity = capacity

    # GETTER

    def get_min_capacity(self):
        return self.__min_capacity

    def get_current_capacity(self):
        return self.__current_capacity

    def get_max_capacity(self):
        return self.__max_capacity

    def get_glass_price(self):
        return self.__glass_price

    # PRINT GLASS OBJECT

    def __str__(self):
        return f"Glass: [Curr Capacity: {self.get_current_capacity()}] - [Max Capacity: {self.get_max_capacity()}] - [Price: {self.get_glass_price()}$]"
