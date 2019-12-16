


substring_list = ["mensa",  "date", "preis", "price"]

string_list = ['mensa_name', 'date', 'first', 'first_price', 'second', 'second_price', 'third', 'third_price']

for substring in substring_list:
    x = any(substring in string for string in string_list) 
    print(x)

    