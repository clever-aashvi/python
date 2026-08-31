actual_cost = float(input(" Please enter the actual product price:"))
sale_cost = float(input(" Please enter the sales amount:"))

if (sale_cost > actual_cost):
        amount = sale_cost - actual_cost
        print("total profit = {0}".format(amount))
else:
        print("No Profit!!!")