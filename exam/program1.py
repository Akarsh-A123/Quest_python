'''Lauren has a chart of distinct project prices for house over the next several years.she must buy thehouse in one
year and sell it in another and she must do so at a loss she wants to minimize ''' 

no_of_years = int(input("Enter the number of years "))
house_price = []
for i in range(no_of_years):
    print(f"Enter the projected price for the house {i+1} year")
    house_price.append(int(input()))

print(house_price)
def min_house_price(no_of_years,house_price):
    minimun_price = 0
    minimum_price_list = []
    for i in range(0,no_of_years):
        for j in range(0,no_of_years):
            if(house_price[i]-house_price[j]<0):
                minimun_price = (house_price[i]-house_price[j])*-1
                minimum_price_list.append(minimun_price)
    return minimum_price_list


min_house_price_list = min_house_price(no_of_years,house_price)
print(f'minimum amount of money lauren must lose {min(min_house_price_list)} Rs')
    
