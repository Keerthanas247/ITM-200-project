# Step 1 Reading CSV File and Step 2:Total Sale
import csv

year_totals = {}
header = []

with open(r'C:\Users\keert\Downloads\Data.csv', 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:

        if not header:
            header = row

        else:
            year = int(row[0])
            year_total = sum([int(x.replace(',', '')) for x in row[1:]])
            year_totals[year] = year_total

with open('stats.txt', 'w') as file:
    for year in range(2012, 2022):
        if year in year_totals:
            line = f"{year}: {year_totals[year]:,}\n"
        else:
            line = f"{year}: 0\n"

        file.write(line)
# Step 3: Bar Plot
import matplotlib.pyplot as plt

# Read the data from the file
with open('stats.txt', 'r') as file:
    data = file.readlines()

years = []
sales = []

# Extract the years and sales from the data
for line in data:
    year, sales_str = line.strip().split(': ')
    years.append(int(year))
    sales.append(int(sales_str.replace(',', '')))

# Create the bar plot
plt.bar(years, sales)

# Set the plot title and axis labels
plt.title('Total Sales per Year')
plt.xlabel('Year')
plt.ylabel('Total Sales')

# Show the plot
plt.show()

# Step 4: Sale Estimation
# Calculate total sales in first 6 months of 2021 and 2022
import csv

with open(r'C:\Users\keert\Downloads\Data.csv', 'r') as file:
    csv_reader = csv.reader(file)

    # skip header row
    next(csv_reader)

    # initialize sales totals
    sales_2021 = 0
    sales_2022 = 0

    # iterate over rows
    for row in csv_reader:
        if int(row[0]) == 2021:
            sales_2021 += sum([int(x.replace(',', '')) for x in row[1:7]])
        elif int(row[0]) == 2022:
            sales_2022 += sum([int(x.replace(',', '')) for x in row[1:7]])

# Calculate sales growth rate for the first 6 months of 2022
sgr = (sales_2022 - sales_2021) / sales_2022
rounded_sgr = round(sgr,2)
with open('stats.txt','a') as f:
    f.write(f'Sales Growth Rate: {rounded_sgr}\n') # Input value in stats.txt file

#estimate the sales in each month for the last six months (Jul to Dec) of 2022
estimated_sales = []
for month in range(8, 14):
    with open('Data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        sales_2021_monthly = int(next(row[month-1].replace(',', '') for row in csv_reader if row[0] == '2021'))
        estimated_sales.append(sales_2021_monthly + sales_2021_monthly * sgr)


# Write estimated sales for last six months in stats.txt file
with open('stats.txt', 'a') as file:
    file.write("Estimated Sales for Last Six Months of 2022:\n")
    for month, sales in zip(['July', 'August', 'September', 'October', 'November', 'December'], estimated_sales):
        file.write(f"{month}-2022: {sales:,.0f}\n")

#Step 5: Horizontal Bar Plot
import matplotlib.pyplot as plt

# Read the estimated sales data from the stats.txt file
estimated_sales = []
with open('stats.txt', 'r') as file:
    for line in file:
        if line.startswith('Estimated Sales for Last Six Months of 2022:'):
            break
    for line in file:
        month, sales_str = line.strip().split(': ')
        estimated_sales.append(float(sales_str.replace(',', '')))

# Define the month names for the x-axis labels
month_names = ['July', 'August', 'September', 'October', 'November', 'December']

# Create the horizontal bar plot
plt.barh(month_names, estimated_sales)

# Set the plot title and axis labels
plt.title('Estimated Sales for Last Six Months of 2022')
plt.xlabel('Estimated Sales')
plt.ylabel('Month')

# Show the plot
plt.show()
