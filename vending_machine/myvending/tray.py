from myvending.glass import Glass
from myvending.electric_glass import ElectricGlass


class Tray:
    # CONSTRUCTOR

    def __init__(self, max_cap):
        self.__max_cap = max_cap
        self.__tray_min_capacity = 0
        self.__glass_list = []  # list to hold glass objects

    # METHODS

    def add_glass(self, glass_object):
        if isinstance(glass_object, Glass) or isinstance(glass_object, ElectricGlass):
            if self.get_glass_list_length() < self.get_tray_max_cap():
                self.__glass_list.append(glass_object)
            else:
                print("Tray is Full. Cannot Add Anymore Glass! ")
        else:
            print("Tray can only hold Glass and Electric Glass")

    def remove_glass_from_tray(self, glass_object):
        if self.get_glass_list_length() == self.get_tray_min_capacity():
            print("ERROR! Tray is Empty!")

        self.__glass_list.remove(glass_object)

    def remove_all_glass_from_tray(self):
        self.__glass_list = []
        return self.get_glass_list()

    # 1 ml = 1 Gram
    def get_weight(self):
        weight = 0
        for glass_objects in self.get_glass_list():
            weight += glass_objects.get_glass_water_volume()
        return weight

    def count_glass_objects_in_tray(self):
        return len(self.get_glass_list())

    def count_glass(self, glass_count=0):
        for glass_obj in self.get_glass_list():
            if isinstance(glass_obj, Glass):
                glass_count += 1
        return glass_count

    def count_eglass(self, eglass_count=0):
        for glass_obj in self.get_glass_list():
            if isinstance(glass_obj, ElectricGlass):
                eglass_count += 1
        return eglass_count

    # GETTER

    def get_glass_list(self):
        return self.__glass_list[:]

    def get_tray_min_capacity(self):
        return self.__tray_min_capacity

    def get_tray_max_cap(self):
        return self.__max_cap

    def get_glass_list_length(self):
        return len(self.__glass_list)

    # PRINT TRAY OBJECT

    def __str__(self):
        return f"Tray: [Max Capacity: {self.get_tray_max_cap()}] - {list(map(str,self.get_glass_list()))} - [Amount of Glass in Tray: {self.count_glass_objects_in_tray()}] - [Tray Weight: {self.get_weight()}]"
