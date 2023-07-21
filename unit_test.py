import practice

object_1 = practice.Categories(1, "Electronics", "Category for electronic devices", '1')
object_2 = practice.Customer(5,'Robert Wilson', 'password5', 'robert@example.com', '654 Cedar St', '4321098765')
create_customers = [
    ('John Doe', 'password1', 'john@example.com', '123 Main St', '1234567890'),
    ('Jane Smith', 'password2', 'jane@example.com', '456 Elm St', '0987654321'),
    ('Michael Johnson', 'password3', 'michael@example.com', '789 Oak St', '9876543210'),
    ('Emily Davis', 'password4', 'emily@example.com', '321 Pine St', '5678901234'),
    ('Robert Wilson', 'password5', 'robert@example.com', '654 Cedar St', '4321098765'),
    ('Olivia Clark', 'password6', 'olivia@example.com', '987 Walnut St', '6789012345'),
    ('James Rodriguez', 'password7', 'james@example.com', '543 Maple St', '2109876543'),
    ('Sophia Lee', 'password8', 'sophia@example.com', '876 Birch St', '3456789012'),
    ('Alexander Wright', 'password9', 'alexander@example.com', '234 Oak St', '7890123456'),
    ('Isabella Adams', 'password10', 'isabella@example.com', '567 Pine St', '1234567890')
]

# for customer_data in create_customers:
#     customer_name, password, email, address, phone_number = customer_data
#     Customer.create(customer_name, password, email, address, phone_number)

categories = [
    ("Electronics", "Category for electronic devices", '1'),
    ("Clothing", "Category for clothing items",'2'),
    ("Books", "Category for books and publications",'3'),
    ("Home_and_Kitchen", "Category for home and kitchen products",'4'),
    ("Sports_and_Outdoors", "Category for sports and outdoor equipment",'5'),
    ("Beauty_and_Personal Care", "Category for beauty and personal care products",'6'),
    ("Toys_and_Games", "Category for toys and games",'7'),
    ("Automotive", "Category for automotive products",'8'),
    ("Health_and_Wellness", "Category for health and wellness items",'9'),
    ("Jewelry", "Category for jewelry and accessories",'10')
]

# practice.Categories.reset_identity_column()
# for category in categories:
#     category_name, description, stt = category
#     practice.Categories.create(category_name,description, stt)

products = [
    ("product1.jpg", "Shirt", "Cotton shirt", 19.99, 2, 50),
    ("product2.jpg", "Jeans", "Slim-fit jeans", 29.99, 2, 30),
    ("product3.jpg", "Sneakers", "Running shoes", 59.99, 5, 20),
    ("product4.jpg", "Sandals", "Casual sandals", 24.99, 5, 15),
    ("product5.jpg", "Watch", "Stainless steel watch", 79.99, 10, 10),
    ("product6.jpg", "Bracelet", "Leather bracelet", 12.99, 10, 25),
    ("product7.jpg", "Backpack", "Waterproof backpack", 39.99, 5, 10),
    ("product8.jpg", "Laptop Sleeve", "Neoprene laptop sleeve", 19.99, 1, 20),
    ("product9.jpg", "Headphones", "Wireless headphones", 49.99, 1, 15),
    ("product10.jpg", "Bluetooth Speaker", "Portable Bluetooth speaker", 29.99, 1, 10),
]

# for product in products:
#     picture_name, product_name, description, price, category_id, quantity = product
#     Product.create(picture_name, product_name, description, price, category_id, quantity)

orders = [
    (1, '2023-06-01', 50.99, 1),
    (1, '2023-06-02', 30.50, 2),
    (2, '2023-06-03', 75.25, 3),
    (3, '2023-06-04', 99.99, 1),
    (2, '2023-06-05', 45.75, 2),
    (4, '2023-06-06', 85.00, 3),
    (5, '2023-06-07', 120.75, 1),
    (3, '2023-06-08', 60.49, 2),
    (4, '2023-06-09', 40.25, 3),
    (5, '2023-06-10', 95.99, 1)
]
#Pending = 1
#Shipped = 2
#Delivered = 3

# for order in orders:
#     customer_id, order_date, total_price, status = order
#     Orders.create(customer_id, order_date, total_price, status)

order_details = [
    (1, 1, 2, 25.49),
    (2, 2, 1, 12.99),
    (3, 3, 1, 10.99),
    (4, 4, 2, 8.99),
    (5, 5, 1, 20.25),
    (6, 6, 2, 15.75),
    (7, 7, 1, 9.99),
    (8, 8, 3, 6.99),
    (9, 9, 2, 5.50),
    (10, 10, 1, 10.25),
]


# for order_detail in order_details:
#     order_id, product_id, quantity, price = order_detail
#     OrderDetails.create(order_id, product_id, quantity, price)
    





# Customer.delete_all()

# print(category_name, ' , ', description, ', ' ,stt)
# conn.commit()
# cursor.execute("SELECT * FROM Customer")
# row_1 = cursor.fetchone()

# while row_1:
#     print(row_1)
#     row_1 = cursor.fetchone()
# cursor.execute("SELECT * FROM CATEGORIES")

# conn = pymssql.connect(server, username, password, database)
# cursor = conn.cursor()

# row_2 = cursor.fetchone()
# while row_2:
#     print(row_2)
#     row_2 = cursor.fetchone()


#temp1 = Product.read(85)
# print(temp1.description)
# temp1.quantity = 50
# Product.update(temp1)

# all = OrderDetails.read_all()
# for x in all:
#     print(x)

# temp2 = OrderDetails.read(40)
# temp2.price = 19.99
# OrderDetails.update(temp2)
# OrderDetails.delete(temp2)

# temp3 = Orders.read(38)
# temp4 = OrderDetails.read(38)
# print(temp3.order_date)
# temp3.status = 3
# temp3.order_date = '2023-06-09'
# Orders.update(temp3)
# OrderDetails.delete(temp4)
# Orders.delete(temp3)


#OrderDetails.delete_all()
# Orders.delete_all()
#Orders.reset_identity_column()
#Product.delete_all()
#Product.reset_identity_column()

# temp = Orders.read(12)
# temp2 = Orders.read(20)
# Orders.delete_multiple_rows(temp,temp2)
#practice.Categories.delete_all()

#<img src='{product[1]}' width='300' height='400'>x 