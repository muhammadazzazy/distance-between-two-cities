import requests
import haversine as hs
from haversine import Unit
from sys import exit


def main() -> None:
    distance_units = ['km', 'mi', 'mi.', 'M', 'NM', 'nmi']
    while True:
        try:
            distance_unit = input('Enter a unit of distance: ')

            if distance_unit not in distance_units:
                print('Invalid units...')

            first_city_country: str = input(
                'Enter the first city and its country: ')

            first_city, first_country = first_city_country.split(', ')

            second_city_country: str = input(
                'Enter the second city and its country: ')

            second_city, second_country = second_city_country.split(', ')

            if first_city == second_city and first_country == second_country:
                print('Same city...')
                continue

            src_url: str = f'https://nominatim.openstreetmap.org/search?city={first_city}&country={first_country}&format=json'

            src_response = requests.get(
                src_url, headers={'User-Agent': 'distance-between-two-cities'})
            src_data = src_response.json()

            src_coords: tuple[float, float] = (
                float(src_data[0]["lat"]), float(src_data[0]["lon"]))

            dest_url = f'https://nominatim.openstreetmap.org/search?city={second_city}&country={second_country}&format=json'
            dest_response = requests.get(
                dest_url, headers={'User-Agent': 'distance-between-two-cities'})

            dest_data = dest_response.json()
            dest_coords = (
                float(dest_data[0]["lat"]), float(dest_data[0]["lon"]))
            if distance_unit == distance_units[0]:
                distance = hs.haversine(
                    src_coords, dest_coords, unit=Unit.KILOMETERS)
            elif distance_unit == distance_units[1] or distance_unit == distance_units[2]:
                distance = hs.haversine(
                    src_coords, dest_coords, unit=Unit.MILES)
            else:
                distance = hs.haversine(
                    src_coords, dest_coords, unit=Unit.NAUTICAL_MILES)

            print(
                f'The distance between {first_city_country} and {second_city_country} is {distance:.2f} {distance_unit}.')
        except (IndexError, ValueError):
            print('Invalid input...')
            continue

        except KeyboardInterrupt:
            print('Exiting...')
            exit()


if __name__ == '__main__':
    main()
