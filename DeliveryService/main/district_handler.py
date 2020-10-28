from geopy.geocoders import Nominatim

coord_list = {
    1: (0, 100, 100, 0),
    2: (0, 0, 100, -100),
    3: (-100, 100, 0, 0),
    4: (-100, -100, 0, 0)
}


def set_coords(district: int, coords: tuple) -> None:
    coord_list[district] = coords


def check_coords(x, y):
    for key, val in coord_list.items():
        if val[2] >= x >= val[0] and val[3] <= y <= val[1]:
            return key
    else:
        return 0


def check_location(location: str) -> int:
    """function for determine the district"""
    geolocator = Nominatim(user_agent="test")
    place = geolocator.geocode(location)
    # print(place.latitude, place.longitude)
    for key, val in coord_list.items():
        if val[2] >= place.latitude >= val[0] and val[3] <= place.longitude <= val[1]:
            return key
    else:
        return 0


if __name__ == '__main__':
    print(check_coords("maputu"))
    print(check_coords("Moscow"))
