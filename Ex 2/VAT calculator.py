print("Enter the amount of the product")
cp = float(input())
print("Enter the vat %age")
perc = float(input())

vat = float(cp/perc)

print("The total amount is {}".format(float(cp+vat)))
