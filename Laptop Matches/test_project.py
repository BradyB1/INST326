import sys
import os
import unittest
import Project as pr
import pandas as pd


class TestMethods(unittest.TestCase):
    def test_price_display_sorts_ascending(self):  # Carlos & Matthew
        laptops = []
        laptops.append(pr.Laptop(0, "HP", "Ultrabook", " ",
                                 " ", " ", " ", " ", " ", " ", " ", 963))
        laptops.append(pr.Laptop(0, "Apple", "Ultrabook", " ",
                                 " ", " ", " ", " ", " ", " ", " ", 863))

        actual = pr.price_display(laptops, "a")
        self.assertEqual(actual[0].price, 863)

    def test_price_display_sorts_descending(self):  # Carlos & Matthew
        laptops = []
        laptops.append(pr.Laptop(0, "Apple", "Ultrabook", " ",
                                 " ", " ", " ", " ", " ", " ", " ", 863))
        laptops.append(pr.Laptop(0, "HP", "Ultrabook", " ",
                                 " ", " ", " ", " ", " ", " ", " ", 963))

        actual = pr.price_display(laptops, "d")
        self.assertEqual(actual[0].price, 963)

    def test_price_loop(self):  # Brady
        laptops = []

        data = [0, "HP", "Ultrabook", "na", "na", "na", "na", "na", "na", "na", "na", 963], [1, "Apple", "Ultrabook", "na", "na", "na", "na", "na", "na", "na", "na", 863], [
            2, "Apple", "Ultrabook", "na", "na", "na", "na", "na", "na", "na", "na", 1200], [3, "Apple", "Ultrabook", "na", "na", "na", "na", "na", "na", "na", "na", 1500]
        df = pd.DataFrame(data, columns=[
                          "ID", "Company", "TypeName", "Inches", "ScreenResolution", "Cpu", "Ram", "Memory", "Gpu", "OpSys", "Weight", "Price"])

        price = 900
        actual = pr.price_loop(df, price)
        self.assertEqual(actual[0].id, 0)
        self.assertEqual(actual[1].id, 1)

    def test_specs_filter(self):  # Brady
        data = [0, "HP", "Ultrabook", "na", "na", "na", "na", "na", "na", "na", "na", 963], [1, "Apple", "Ultrabook", "na", "na", "na", "na", "na", "na", "na", "na", 863], [
            2, "Apple", "Ultrabook", "na", "na", "na", "na", "na", "na", "na", "na", 1200], [3, "Apple", "Ultrabook", "na", "na", "na", "na", "na", "na", "na", "na", 1500]
        df = pd.DataFrame(data, columns=[
                          "ID", "Company", "TypeName", "Inches", "ScreenResolution", "Cpu", "Ram", "Memory", "Gpu", "OpSys", "Weight", "Price"])
        specs = {}
        specs["Company"] = "Apple"
        specs["Price"] = 863
        actual = pr.specs_filter(specs, df)
        self.assertEqual(actual[0].id, 1)

    def test_specs_filter_not_two(self):  # Luis
        data = [0, "HP", "Ultrabook", "na", "na", "na", "na", "na", "na", "na", "na", 963], [1, "Apple", "Ultrabook", "na", "na", "na", "na", "na", "na", "na", "na", 863], [
            2, "Apple", "Ultrabook", "na", "na", "na", "na", "na", "na", "na", "na", 1200], [3, "Apple", "Ultrabook", "na", "na", "na", "na", "na", "na", "na", "na", 1500]
        df = pd.DataFrame(data, columns=[
                          "ID", "Company", "TypeName", "Inches", "ScreenResolution", "Cpu", "Ram", "Memory", "Gpu", "OpSys", "Weight", "Price"])
        specs = {}
        specs["Company"] = "Apple"
        specs["Price"] = 100000
        actual = pr.specs_filter(specs, df)
        self.assertEqual(len(actual), 0)

    def test_specs_filter_only_one_spec(self):  # Luis
        data = [0, "HP", "Ultrabook", "na", "na", "na", "na", "na", "na", "na", "na", 963], [1, "Apple", "Ultrabook", "na", "na", "na", "na", "na", "na", "na", "na", 863], [
            2, "Apple", "Ultrabook", "na", "na", "na", "na", "na", "na", "na", "na", 1200], [3, "Apple", "Ultrabook", "na", "na", "na", "na", "na", "na", "na", "na", 1500]
        df = pd.DataFrame(data, columns=[
                          "ID", "Company", "TypeName", "Inches", "ScreenResolution", "Cpu", "Ram", "Memory", "Gpu", "OpSys", "Weight", "Price"])
        specs = {}
        specs["Company"] = "Apple"
        actual = pr.specs_filter(specs, df)
        self.assertEqual(len(actual), 0)

    if __name__ == '__main__':
        unittest.main()
