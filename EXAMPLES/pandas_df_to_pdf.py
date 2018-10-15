#!/usr/bin/env python
import pandas as pd
import pdfkit  # <1>

# data from
# http://www.rita.dot.gov/bts/sites/rita.dot.gov.bts/files/publications/
# national_transportation_statistics/html/table_01_44.html

airports_df = pd.read_csv(  # <2>
    '../DATA/airport_boardings.csv',
    thousands=',',
    index_col=1
)

print("ENTIRE DATAFRAME")

print(airports_df.head(), "\n")

print("SELECTED COLUMNS WITH FILTERED ROWS")

columns_wanted = ['2001 Total', 'Airport']  # <3>
sort_col = '2001 Total'  # <4>
min_val = 20000000 # <5>
selector = airports_df['2001 Total'] > min_val  # <6>

print("COLUMN TOTALS")
selected_rows = airports_df[selector][columns_wanted]  # <7>

html = selected_rows.to_html('selected_rows.html')  # <8>

pdfkit.from_file('selected_rows.html', 'selected_rows.pdf') # <9>
