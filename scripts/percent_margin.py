# percent_margin.py
#
# Calculate percentage of margin to price

cost = int(raw_input("COST: "))
p_margin = float(raw_input("Percentage Margin: "))

price = cost / (1 - (p_margin/100))
print "Selling price is %.4f" %price

