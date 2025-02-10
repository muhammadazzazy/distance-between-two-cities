# Distance Between Two Cities
This is a Python implementation for a program that makes use of the names of a pair of cities and the countries in which they are located to find the distance in kilometers (km) between them via the Haversine formula. The Nominatim Application Programming Interface (API) is used to acquire the latitude and longitude coordinates of the two cities.

This program requires Python 3 which can be installed from [here](https://www.python.org/downloads/).

First, a virtual environment can be created and activated using the following commands:

```bash
python3 -m venv env
source env/bin/activate
```

Then, the required Python packages need to be installed which are listed in the `requirements.txt` file using the command below:
```bash
pip install -r requirements.txt
```

To start the program, run the following command:
```bash
python3 main.py
```
The project idea was obtained from [karan/Projects](https://github.com/karan/Projects#numbers).
