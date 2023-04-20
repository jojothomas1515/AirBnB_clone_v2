#!/usr/bin/python3

from models.place import Place
from models.amenity import Amenity

if __name__ == '__main__':
    the_house = Place(name="the_hosues")
    the_house.save()
    print(the_house)
    light = Amenity(name="light")
    light.save()
    water = Amenity(name="water")
    water.save()
    gas = Amenity(name="gas")
    gas.save()

    print("\n\n")
    print(light, water, gas)
    print("\n\n")
    the_house.amenity_ids.extend([light.id, water.id, gas.id])
    print(the_house.amenities)
