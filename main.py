import requests
import haversine as hs
from haversine import Unit
from sys import exit


def main() -> None:
    distance_units: list[str] = ['km', 'mi', 'mi.', 'M', 'NM', 'nmi']
    print('Welcome to The Distance-Between-Two-Cities Calculator! 🌎🌍🌏')
    exit_message: str = 'Exiting program...'
    while True:
        try:
            # distance_unit: str = input('Enter a unit of distance: ')
            user_input: str = input('Enter a unit of distance: ')

            if user_input == 'exit':
                print(exit_message)
                exit()

            distance_unit: str = user_input

            if distance_unit not in distance_units:
                print('Please enter valid units...')
                continue

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

            dest_url: str = f'https://nominatim.openstreetmap.org/search?city={second_city}&country={second_country}&format=json'
            dest_response: requests.models.Response = requests.get(
                dest_url, headers={'User-Agent': 'distance-between-two-cities'})

            dest_data: list[str] = dest_response.json()

            dest_coords: tuple[float, float] = (
                float(dest_data[0]["lat"]), float(dest_data[0]["lon"]))

            if distance_unit == distance_units[0]:
                distance: float = hs.haversine(
                    src_coords, dest_coords, unit=Unit.KILOMETERS)
            elif distance_unit == distance_units[1] or distance_unit == distance_units[2]:
                distance: float = hs.haversine(
                    src_coords, dest_coords, unit=Unit.MILES)
            else:
                distance: float = hs.haversine(
                    src_coords, dest_coords, unit=Unit.NAUTICAL_MILES)

            print(
                f'The distance between {first_city_country} and {second_city_country} is {distance:.2f} {distance_unit}.')

        except (IndexError, ValueError):
            print('Please enter some valid input...')
            continue

        except KeyboardInterrupt:
            print(exit_message)
            exit()


if __name__ == '__main__':
    main()
