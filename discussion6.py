import unittest
import os
import csv


def load_csv(f):
    '''
    Params: 
        f, name or path or CSV file: string

    Returns:
        nested dict structure from csv
        outer keys are (str) years, values are dicts
        inner keys are (str) months, values are (str) integers
    
    Note: Don't strip or otherwise modify strings. Don't change datatypes from strings. 
    '''

    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)
    # use this 'full_path' variable as the file that you open
    with open(full_path) as fh:
        r = csv.reader(fh)
        rows = []
        print(f"Add the data from the csv")
        for row in r:
            print(f"Adding {row} to rows")
            rows.append(row)
        print(f"Final value of rows is {rows}")
    
    print("Create a dictionary d")
    d = {}
    header = row[0]
    for year in header[1:]:
        d[year] = {}
    print(f"Added the years, d is now {d}")
    print("Add all the rows, skipping the first one")
    for row in rows[1:]:
        for i in range(1, len(row[1:])+1):
            d[header[i]][row[0]] = row[i]
            print(f"Key is [{header[i]}]{row[0]} and data is {row[i]}")
    print(f"The dictionary from load_csv should look like: {d}")
    return d

def get_annual_max(d):
    '''
    Params:
        d, dict created by load_csv above

    Returns:
        list of tuples, each with 3 items: year (str), month (str), and max (int) 
        max is the maximum value for a month in that year, month is the corresponding month

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary.
        You'll have to change vals to int to compare them. 
    '''
    result = []

    for year, months in d.items():
        max_month = None
        max_value = float('-inf')

        for month, value in months.items():
            int_value = int(value)
            if int_value > max_value:
                max_value = int_value
                max_month = month

        if max_month:
            result.append((year, max_month, max_value))

    return result

def get_month_avg(d):
    '''
    Params: 
        d, dict created by load_csv above

    Returns:
        dict where keys are years and vals are floats rounded to nearest whole num or int
        vals are the average vals for months in the year

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary. 
        You'll have to make the vals int or float here and round the avg to pass tests.
    '''
    result = {}

    for year, months in d.items():
        total = 0
        count = 0

        for value in months.values():
            total += int(value)
            count += 1

        if count > 0:
            avg = round(total / count)
            result[year] = avg

    return result

class dis7_test(unittest.TestCase):
    '''
    you should not change these test cases!
    '''
    def setUp(self):
        self.flight_dict = load_csv('daily_visitors.csv')
        self.max_tup_list = get_annual_max(self.flight_dict)
        self.month_avg_dict = get_month_avg(self.flight_dict)

    def test_load_csv(self):
        self.assertIsInstance(self.flight_dict['2021'], dict)
        self.assertEqual(self.flight_dict['2020']['JUN'], '435')

    def test_get_annual_max(self):
        self.assertEqual(self.max_tup_list[2], ('2022', 'AUG', 628))

    def test_month_avg_list(self):
        self.assertAlmostEqual(self.month_avg_dict['2020'], 398, 0)

def main():
    unittest.main(verbosity=2)
    print("----------------------------------------------------------------------")
    flight_dict = load_csv('daily_visitors.csv')
    print("Output of load_csv:", flight_dict, "\n")
    print("Output of get_annual_max:", get_annual_max(flight_dict), "\n")
    print("Output of get_month_avg:", get_month_avg(flight_dict), "\n")


if __name__ == '__main__':
    main()
