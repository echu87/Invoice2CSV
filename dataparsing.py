from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter
from openpyxl import load_workbook
import os


wb = load_workbook(filename = '"E:\Documents\Git\Data for parsing\Brookfield AP Tracker 2017\\02 February 2017\Accounts Payable Tracker 02 February 2017 Updated 03-24-2017.xlsx"')
sheet_ranges = wb['range names']
print(sheet_ranges['D18'].value)