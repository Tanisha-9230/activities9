'''Tour Expenditure at Given Hotel 

The family has spent the vacation in Goa and now they are returning home to do so they will have to check out from the hotel.

Tariff on Room: Delux Room- 7500 INR

                            Non AC Room- 4500 INR 

You  as a developer has to create a program for a hotel owner which has the following requirements,

The program should begin with taking input from the checkout counter 

Type of room booked 
Total number of days 
Total Amount on Food (Amount is expected )
There are the following cases to be considered while generating a bill.

The tax on food amount is dependent on the type of room booked.

Tax on food for the deluxe room will be billed  18% of the total food amount.

Tax on food for the Non AC room will be billed  5% of the total food amount.

You are supposed to include a tip of 10% on the food amount.

The output from your program should include;

The  Room Tariff on the number of days spend, GST on a meal(Breakdown of GST is necessary based on CGST and SGST and same has to get reflected on console ) 

The tip amount, and the grand total for the meal including both the tax and the tip.

Format the output so that all of the values are displayed using two decimal places.'''

room=input("Enter the room type: ")
number_of_days=int(input("Enter the total number of days: "))
food_amount=float(input("Enter the food amount: "))
if room=="deluex":
    room_tarrif=7500*number_of_days
else:
    room_tarrif=4500*number_of_days
    
tip_amount=food_amount*0.1  
if room=="deluex":
    food_tax=0.18*food_amount
else:
    food_tax=0.05*food_amount
total_bill=food_amount+tip_amount+room_tarrif+food_tax
print(f"room tarrif:{room_tarrif}")
print(f"total tip amount:{round(tip_amount)}")
print(f"food_amount GST cgst:{round(food_tax*0.5,2)} and sgst:{round(food_tax*0.5,2)}")
print(f"total bill payment:{round(total_bill,2)}")