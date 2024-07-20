"""
This program is a menu that asks for user's menu selections.

It will generate a personalized selection based on user's input.
Until the user presses quit, the program will keep asking for user's input.
"""

import pgeocode
import math


def main():
    """Asks for user's name."""
    name = input("Please enter your name: ")
    print(f"Hi, {name}, welcome to the menu")
    menu()


class HistoricalTemps:
    """Class of attributes."""

    @staticmethod
    def zip_to_loc_info(zipcode):
        """Get location information based on the zipcode."""
        geocoder = pgeocode.Nominatim('us')
        result = geocoder.query_postal_code(zipcode)
        lat = result.latitude
        lon = result.longitude
        loc_name = result.place_name

        return lat, lon, loc_name

    def __init__(self, zip_code: str, start: str = "1950-08-13",
                 end: str = "2023-08-25"):
        """Initialize the HistoricalTemps instance."""
        self._zip_code = zip_code
        self._start = start
        self._end = end
        self._temp_list = None

        lat, lon, loc_name = self.zip_to_loc_info(zip_code)

        if math.isnan(lat) or math.isnan(lon):
            raise LookupError("This is not a valid zipcode")

        self._lat = lat
        self._lon = lon
        self._loc_name = loc_name
        self._load_temps()

    @property
    def zip_code(self):
        """Get the zip code."""
        return self._zip_code

    @property
    def start(self):
        """Get the start date."""
        return self._start

    @start.setter
    def start(self, value):
        """Set the start date."""
        self._start = value

    @property
    def end(self):
        """Get the end date."""
        return self._end

    @end.setter
    def end(self, value):
        """Set the end date."""
        self._end = value

    @property
    def loc_name(self):
        """Get the location name."""
        return self._loc_name

    def _load_temps(self):
        """Protected method to load temperature data.

        It loads hard-coded fake data.
        """
        self._temp_list = [
            ("2020-01-01", 29.0),
            ("2020-01-02", 30.0),
            ("2020-01-03", 31.0),
            ("2020-01-04", 29.5),
            ("2020-01-05", 30.5),
            ("2020-01-06", 31.5),
            ("2020-01-07", 28.5),
            ("2020-01-08", 29.5),
            ("2020-01-09", 30.5),
            ("2020-01-10", 30.0),
            ("2020-01-11", 31.0)
        ]

    def average_temp(self):
        """Calculate and returns the average of all stored temperatures."""
        if not self._temp_list:
            return None
        total_temp = sum(temp for _, temp in self._temp_list)
        return total_temp / len(self._temp_list)

    def get_temp_list(self):
        """Get temperature data."""
        return self._temp_list

    def extreme_days(self, threshold: float):
        """
        Return a list of (date, temperature) tuples where the temperature exceeds the threshold.

        Parameters:
        threshold (float): The temperature threshold to filter days.

        Returns:
        list: List of (date, temperature) tuples.
        """
        return [(date, temp) for date, temp in self._temp_list if temp > threshold]


def create_dataset():
    """Ask for the user's zipcode."""
    zip_code = input("Please enter a zipcode: ")
    try:
        return HistoricalTemps(zip_code)
    except LookupError:
        print("Data could not be loaded. Please check that the zip code"
              " is correct and that you have a working internet connection")
        return None


def compare_average_temps(dataset_one, dataset_two):
    """Compare the average temperatures of two HistoricalTemps datasets."""
    if dataset_one._temp_list is None or dataset_two._temp_list is None:
        print("Both datasets must be loaded to compare.")
        return

    avg_temp_one = dataset_one.average_temp()
    avg_temp_two = dataset_two.average_temp()

    print(f"The average temperature for {dataset_one.loc_name} was"
          f" {avg_temp_one:.2f} degrees Celsius")
    print(f"The average temperature for {dataset_two.loc_name} was"
          f" {avg_temp_two:.2f} degrees Celsius")


def print_menu(dataset_one=None, dataset_two=None):
    """Print the menu options."""
    print("Main Menu")
    if dataset_one:
        print(f"1 - Replace {dataset_one.loc_name}")
    else:
        print("1 - Load dataset one")
    if dataset_two:
        print(f"2 - Replace {dataset_two.loc_name}")
    else:
        print("2 - Load dataset two")
    print("3 - Compare average temperatures")
    print("4 - Dates above threshold temperature")
    print("5 - Highest historical dates")
    print("6 - Change start and end dates for dataset one")
    print("7 - Change start and end dates for dataset two")
    print("9 - Quit")


def print_extreme_days(dataset: HistoricalTemps):
    """
    Print the dates and temperatures where the temperature exceeded a user-defined threshold.

    Parameters:
    dataset (HistoricalTemps): The HistoricalTemps object with loaded data.
    """
    if dataset._temp_list is None:
        print("Please load this dataset first")
        return

    try:
        threshold = float(input("List days above what temperature? "))
    except ValueError:
        print("Please enter a valid temperature")
        return

    extreme_days_list = dataset.extreme_days(threshold)

    print(f"There are {len(extreme_days_list)} days above {threshold} degrees in {dataset.loc_name}")
    for date, temp in extreme_days_list:
        print(f"{date}: {temp}")


def menu():
    """Produce answer based on the selection of the user."""
    dataset_one = None
    dataset_two = None

    number = 0
    while number != 9:
        print_menu(dataset_one, dataset_two)
        try:
            number = int(input("What is your choice? "))
        except ValueError:
            print("Please enter a number only")
            continue

        match number:
            case 1:
                dataset_one = create_dataset()
            case 2:
                dataset_two = create_dataset()
            case 3:
                if dataset_one is None or dataset_two is None:
                    print("Please load two datasets first")
                else:
                    compare_average_temps(dataset_one, dataset_two)
            case 4:
                if dataset_one is None:
                    print("Please load dataset one first")
                else:
                    print_extreme_days(dataset_one)
            case 5:
                print("selection five is not functional yet")
            case 6:
                print("selection six is not functional yet")
            case 7:
                print("selection seven is not functional yet")
            case 9:
                print("Goodbye!  Thank you for using the database")
            case _:
                print("That's not a valid selection")


if __name__ == '__main__':
    main()
