from collections import OrderedDict

# Read the number of items
n = input().strip()
n=int(n)

# Initialize an OrderedDict to store item names and their cumulative net prices
od = OrderedDict()

# Process each item entry
for _ in range(n):
    item, price = input().strip().rsplit(maxsplit=1)
    price = int(price)
    
    if item in od:
        od[item] += price  # Add price to the existing entry
    else:
        od[item] = price  # Initialize with the input price

# Print the results in the order of their first occurrence
for k, v in od.items():  # Use .items() to get key-value pairs
    print(k, v)
