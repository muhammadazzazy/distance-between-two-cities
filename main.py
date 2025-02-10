import requests
import haversine as hs
from haversine import Unit
from sys import exit


def main() -> None:
    while True:
        try:
            first_city_country: str = input(
                'Enter the first city and its country: ')

            first_city, first_country = first_city_country.split(', ')

            second_city_country: str = input(
                'Enter the second city and its country: ')

            second_city, second_country = second_city_country.split(', ')

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

            distance = hs.haversine(
                src_coords, dest_coords, unit=Unit.KILOMETERS)
            print(
                f'The distance between {first_city} and {second_city} is {distance:.2f} km.')

        except (IndexError, ValueError):
            print('Invalid input...')
            continue

        except KeyboardInterrupt:
            print('Exiting...')
            exit()


if __name__ == '__main__':
    main()
