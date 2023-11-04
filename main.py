from insert_category import insert_category
from insert_product import insert_product

# Title = input("Title: ")
# Description = input("Description: ")

# insert_category(Title = Title, Description = Description)



Title = input("Title: ")
Color = input("Color: ")
Price = float(input("Price: "))
Category_id = int(input("Category id: "))

insert_product(Title = Title, Color = Color, Price = Price, Category_id = Category_id)