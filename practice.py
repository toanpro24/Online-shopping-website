import pymssql

def connect_to_database():
    server = '127.0.0.1'
    database = 'Shopping'
    username = 'Toan'
    password = 'abc123'

    return pymssql.connect(server, username, password, database)

class OrderDetails:
    def __init__(self, order_id, product_id, quantity, price):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    def create(order_id, product_id, quantity, price):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "INSERT INTO OrderDetails (OrderID, ProductID, Quantity, Price) VALUES (%s, %s, %s, %s)"
            values = (order_id, product_id, quantity, price)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True  

        except :
            conn.rollback() 

    def read(order_id):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "SELECT * FROM OrderDetails WHERE OrderID = %s"
            values = (order_id,)

            cursor.execute(query, values)
            row = cursor.fetchone()

            cursor.close()
            conn.close()

            if row:
                return OrderDetails(*row)
            else:
                return None  

        except:
            conn.rollback()

    def read_all():
        conn = connect_to_database()
        cursor = conn.cursor()

    
        query = "SELECT * FROM OrderDetails"
        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows

    def update(self):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "UPDATE OrderDetails SET ProductID = %s, Quantity = %s, Price = %s WHERE OrderID = %s"
            values = (self.product_id, self.quantity, self.price, self.order_id)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True  

        except:
            conn.rollback()  

    def delete(self):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "DELETE FROM OrderDetails WHERE OrderID = %s"
            values = (self.order_id,)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True 

        except:
            conn.rollback()  
    def delete_all():
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "DELETE FROM OrderDetails"

            cursor.execute(query)
            conn.commit()

            cursor.close()
            conn.close()

            return True 

        except:
            conn.rollback()

    def reset_identity_column():
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM OrderDetails")
            conn.commit()

            cursor.execute("DBCC CHECKIDENT ('OrderDetails', RESEED, 0)")
            conn.commit()

            cursor.close()
            conn.close()

            return True  

        except:
            conn.rollback() 
class Orders:
    def __init__(self, order_id, customer_id, order_date, total_price, status):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date
        self.total_price = total_price
        self.status = status

    def create(customer_id, order_date, total_price, status):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "INSERT INTO Orders (CustomerID, OrderDate, TotalPrice, Status) VALUES (%s, %s, %s, %s)"
            values = (customer_id, order_date, total_price, status)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True  

        except:
            conn.rollback() 


    def read(order_id):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "SELECT * FROM Orders WHERE OrderID = %s"
            values = (order_id,)

            cursor.execute(query, values)
            row = cursor.fetchone()

            cursor.close()
            conn.close()

            if row:
                return Orders(*row)
            else:
                return None  

        except:
            conn.rollback()

    def update(self):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "UPDATE Orders SET CustomerID = %s, OrderDate = %s, TotalPrice = %s, Status = %s WHERE OrderID = %s"
            values = (self.customer_id, self.order_date, self.total_price, self.status, self.order_id)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True  

        except:
            conn.rollback() 

    def delete(self):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "DELETE FROM Orders WHERE OrderID = %s"
            values = (self.order_id,)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True 

        except:
            conn.rollback()

    def delete_multiple_rows(self,other):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "DELETE FROM Orders WHERE OrderID BETWEEN %s AND %s"
            values = (self.order_id, other.order_id)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True
        
        except:
            conn.rollback()
    def delete_all():
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "DELETE FROM Orders"

            cursor.execute(query)
            conn.commit()

            cursor.close()
            conn.close()

            return True 

        except:
            conn.rollback()

    def reset_identity_column():
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM Orders")
            conn.commit()

            cursor.execute("DBCC CHECKIDENT ('Orders', RESEED, 0)")
            conn.commit()

            cursor.close()
            conn.close()

            return True  

        except:
            conn.rollback() 

class Product:
    def __init__(self, picture_name, product_id, product_name, description, price, category_id, quantity):
        self.picture_name = picture_name
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price
        self.category_id = category_id
        self.quantity = quantity


    def create(picture_name, product_name, description, price, category_id, quantity):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "INSERT INTO Product (PictureName, ProductName, Description, Price, CategoryID, Quantity) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (picture_name, product_name, description, price, category_id, quantity)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True  

        except:
            conn.rollback() 

    
    def read(product_id):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "SELECT * FROM Product WHERE ProductID = %s"
            values = (product_id,)

            cursor.execute(query, values)
            row = cursor.fetchone()

            cursor.close()
            

            if row:
                return Product(*row)
            else:
                return None  

        except :
            conn.rollback()

    def update(self):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "UPDATE Product SET ProductName = %s, Description = %s, Price = %s, CategoryID = %s, Quantity = %s WHERE ProductID = %s"
            values = (self.product_name, self.description, self.price, self.category_id, self.quantity, self.product_id)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True  

        except :
            conn.rollback()  

    def delete_by_id(self):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "DELETE FROM Product WHERE ProductID = %s"
            values = (self.product_id,)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True 

        except:
            conn.rollback()

    def delete_all():
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "DELETE FROM Product"

            cursor.execute(query)
            conn.commit()

            cursor.close()
            conn.close()

            return True 

        except:
            conn.rollback() 

    def select_by_category_id(self):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "SELECT FROM Product WHERE CategoryID = %s"
            value = self.category_id

            cursor.execute(query, value)
            conn.commit()

            cursor.close()
            conn.close()

            return True
        
        except:
            conn.rollback()

    def reset_identity_column():
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM Product")
            conn.commit()

            cursor.execute("DBCC CHECKIDENT ('Product', RESEED, 0)")
            conn.commit()

            cursor.close()
            conn.close()

            return True  

        except:
            conn.rollback() 

class Customer:
    def __init__(self, customer_id, username, customer_name, password, email, address, phone_number):
        self.customer_id = customer_id
        self.username = username
        self.customer_name = customer_name
        self.password = password
        self.email = email
        self.address = address
        self.phone_number = phone_number


    def create(username, customer_name, password, email, address, phone_number):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "INSERT INTO Customer (Username, CustomerName, Password, Email, Address, PhoneNumber) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (username, customer_name, password, email, address, phone_number)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True  

        except :
           conn.rollback()


    def read(customer_id):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "SELECT * FROM Customer WHERE CustomerID = %s"
            values = (customer_id,)

            cursor.execute(query, values)
            row = cursor.fetchone()

            cursor.close()
            conn.close()

            if row:
                return Customer(*row)
            else:
                return None 

        except:
            conn.rollback()

    def update(self):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "UPDATE Customer SET CustomerName = %s, Password = %s, Email = %s, Address = %s, PhoneNumber = %s WHERE CustomerID = %s"
            values = (self.customer_name, self.password, self.email, self.address, self.phone_number, self.customer_id)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True  

        except:
            conn.rollback()

    def delete(self):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "DELETE FROM Customer WHERE CustomerID = %s"
            values = (self.customer_id,)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True 

        except:
           conn.rollback()
    def delete_all():
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "DELETE FROM Customer"

            cursor.execute(query)
            conn.commit()

            cursor.close()
            conn.close()

            return True 

        except:
            conn.rollback()

    def reset_identity_column():
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM Customer")
            conn.commit()

            cursor.execute("DBCC CHECKIDENT ('Customer', RESEED, 0)")
            conn.commit()

            cursor.close()
            conn.close()

            return True  # Indicate successful reset

        except:
            conn.rollback()



class Categories:
    def __init__(self, category_id, category_name, description, stt):
        self.category_id = category_id
        self.category_name = category_name
        self.description = description
        self.stt = stt

    def create(category_name, description, stt):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "INSERT INTO Categories(CategoryName, Description, STT) VALUES (%s, %s, %s)"
           
            values = (category_name, description, stt)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True  

        except:
           conn.rollback()

    def read(category_id):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "SELECT * FROM Categories WHERE CategoryID = %s"
            values = (category_id,)

            cursor.execute(query, values)
            row = cursor.fetchone()
            
            cursor.close()
            conn.close()

            if row:
                return Categories(*row)
            else:
                return None
              

        except:
           conn.rollback()
    def read_all():
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "SELECT * FROM Categories"
            cursor.execute(query)

            rows = cursor.fetchall()

            for row in rows:
                category_name = row[1]
                description = row[2]
                stt = row[3]

                category = Categories(category_name, description, stt)
                print(f"Category name: {category.category_name}")
                print(f"Deescription: {category.description}")
                print(f"STT: {category.stt}")
                print("-------------------------")

            cursor.close()
            conn.close()

        except:
            conn.rollback()
    def update(self):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "UPDATE Categories SET CategoryName = %s, Description = %s, STT = %s WHERE CategoryID = %s"
            values = (self.category_name, self.description, self.stt, self.category_id)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True  

        except:
            conn.rollback()

    def delete_by_id(self):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "DELETE FROM Categories WHERE CategoryID = %s"
            values = (self.category_id,)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True 

        except:
            conn.rollback()  
    def delete_all():
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "DELETE FROM Categories"

            cursor.execute(query)
            conn.commit()

            cursor.close()
            conn.close()

            return True 

        except:
            conn.rollback()

    def reset_identity_column():
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM Categories")
            conn.commit()

            cursor.execute("DBCC CHECKIDENT ('Categories', RESEED, 0)")
            conn.commit()

            cursor.close()
            conn.close()

            return True  

        except:
            conn.rollback()    

    def sort_by_stt():
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "Select * FROM Categories ORDER BY STT DESC"
            cursor.execute(query)
            conn.commit()

            cursor.close()
            conn.close()

            return True  
        
        except:
            conn.rollback()

class Cart:
    def __init__(self, customer_id, product_id, picture_name, product_name, quantity, total_price):
        self.customer_id = customer_id
        self.product_id = product_id
        self.picture_name = picture_name
        self.product_name = product_name
        self.quantity = quantity
        self.total_price = total_price

    def create(customer_id, product_id, picture_name, product_name, quantity, total_price):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "INSERT INTO Cart (CustomerID, ProductID, PictureName, ProductName, Quantity, TotalPrice) VALUES (%s, %s, %s, %s, %s, %s)"
           
            values = (customer_id, product_id, picture_name, product_name, quantity, total_price)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True  

        except:
           conn.rollback()

    def read_by_customer_id(customer_id):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "SELECT * FROM Cart WHERE CustomerID = %s"
            values = (customer_id)

            cursor.execute(query, values)
            row = cursor.fetchone()
            
            cursor.close()
            conn.close()

            if row:
                return Cart(*row)
            else:
                return None
              

        except:
           conn.rollback()
    def read_all():
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "SELECT * FROM Cart"
            cursor.execute(query)

            rows = cursor.fetchall()

            cursor.close()
            conn.close()

            if rows:
                return Cart(*rows)
            else:
                return None
            
        except:
            conn.rollback()

    def update_quantity(self):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "UPDATE Cart SET Quantity = %s WHERE ProductID = %s"
            values = (self.quantity, self.product_id)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True  

        except:
            conn.rollback()

    def delete_by_id(self):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "DELETE FROM Cart WHERE ProductID = %s"
            values = (self.product_id)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True 

        except:
            conn.rollback()  

    def delete_all():
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "DELETE FROM Cart"

            cursor.execute(query)
            conn.commit()

            cursor.close()
            conn.close()

            return True 

        except:
            conn.rollback()

    def reset_identity_column():
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM Cart")
            conn.commit()

            cursor.execute("DBCC CHECKIDENT ('Cart', RESEED, 0)")
            conn.commit()

            cursor.close()
            conn.close()

            return True  

        except:
            conn.rollback()    

create_customers = [
    ('johndoe', 'John Doe', 'password1', 'john@example.com', '123 Main St', '1234567890'),
    ('janesmith', 'Jane Smith', 'password2', 'jane@example.com', '456 Elm St', '0987654321'),
    ('michaeljohnson', 'Michael Johnson', 'password3', 'michael@example.com', '789 Oak St', '9876543210'),
    ('emilydavis', 'Emily Davis', 'password4', 'emily@example.com', '321 Pine St', '5678901234'),
    ('robertwilson', 'Robert Wilson', 'password5', 'robert@example.com', '654 Cedar St', '4321098765'),
    ('oliviaclark', 'Olivia Clark', 'password6', 'olivia@example.com', '987 Walnut St', '6789012345'),
    ('jamesrodriguez', 'James Rodriguez', 'password7', 'james@example.com', '543 Maple St', '2109876543'),
    ('sophialee','Sophia Lee', 'password8', 'sophia@example.com', '876 Birch St', '3456789012'),
    ('alexanderwright','Alexander Wright', 'password9', 'alexander@example.com', '234 Oak St', '7890123456'),
    ('isabellaadams','Isabella Adams', 'password10', 'isabella@example.com', '567 Pine St', '1234567890')
]

# for customer_data in create_customers:
#     username, customer_name, password, email, address, phone_number = customer_data
#     Customer.create(username, customer_name, password, email, address, phone_number)

categories = [
    ("Electronics", "Category for electronic devices", '1'),
    ("Clothing", "Category for clothing items",'2'),
    ("Books", "Category for books and publications",'3'),
    ("Home", "Category for home and kitchen products",'4'),
    ("Sports", "Category for sports and outdoor equipment",'5'),
    ("Beauty", "Category for beauty and personal care products",'6'),
    ("Games", "Category for toys and games",'7'),
    ("Automotive", "Category for automotive products",'8'),
    ("Health", "Category for health and wellness items",'9'),
    ("Jewelry", "Category for jewelry and accessories",'10')
]
# for category in categories:
#     category_name, description, stt = category
#     Categories.create(category_name,description, stt)
products = [
    ("product1.jpg", "Men's Striped Button-Down Shirt", "This men's striped button-down shirt offers a classic and stylish look suitable for various occasions. Made from high-quality cotton fabric, it ensures comfort, breathability, and durability. The shirt features a timeless vertical stripe pattern in shades of blue and white, adding a touch of sophistication to your ensemble.", 19.99, 2, 50),
    ("product2.jpg", "Women's Slim Fit Dark Wash Jeans", "These women's slim fit dark wash jeans are a versatile and stylish addition to any wardrobe. Crafted from premium denim fabric, these jeans offer a flattering and comfortable fit with a hint of stretch for ease of movement. The dark wash adds a touch of sophistication and pairs well with a variety of tops and shoes.", 29.99, 2, 30),
    ("product3.jpg", " Men's Classic Canvas Sneakers", "These men's classic canvas sneakers combine style and comfort, making them a must-have footwear choice. The sneakers feature a durable canvas upper that offers breathability and a timeless look. With a lace-up closure, padded collar, and cushioned insole, these sneakers provide a snug fit and all-day comfort. The rubber outsole offers excellent traction, making them suitable for various activities and terrains. Whether you're strolling around the city or running errands, these versatile sneakers will elevate your casual style.", 59.99, 5, 20),
    ("product4.jpg", "Women's Strappy Flat Sandals", "Step into comfort and style with these women's strappy flat sandals. Designed for warm weather and casual occasions, these sandals feature multiple crisscross straps that provide a secure and adjustable fit. The sandals are made from synthetic materials, ensuring durability and easy maintenance. The flat sole offers comfort for all-day wear, while the open-toe design keeps your feet cool. Perfect for pairing with summer dresses or shorts, these strappy flat sandals are a go-to choice for effortless style.", 24.99, 5, 15),
    ("product5.jpg", "Men's Stainless Steel Chronograph Watch", "Add a touch of elegance and functionality to your wrist with this men's stainless steel chronograph watch. The watch showcases a sleek and masculine design with a stainless steel case and bracelet. The chronograph feature allows you to track elapsed time with precision, while the date window adds practicality. With water resistance and a reliable quartz movement, this watch is suitable for everyday wear and various activities. Make a bold statement with this sophisticated timepiece that seamlessly blends style and functionality.", 79.99, 10, 10),
    ("product6.jpg", "Women's Sterling Silver Charm Bracelet", "This women's sterling silver charm bracelet is a charming accessory that complements any outfit. Crafted from high-quality sterling silver, the bracelet features a link chain with various dangling charms. The adjustable length ensures a comfortable fit, and the lobster clasp provides secure closure. The intricate details and polished finish add a touch of elegance, making this bracelet a versatile piece for both casual and formal occasions. Express your personal style and capture attention with this beautiful sterling silver charm bracelet.", 12.99, 10, 25),
    ("product7.jpg", "Unisex Water-Resistant Laptop Backpack", "Stay organized and carry your essentials in style with this unisex water-resistant laptop backpack. The backpack is made from durable nylon material that offers water resistance, protecting your belongings in light rain or accidental spills. With multiple compartments and pockets, including a padded laptop sleeve, it provides ample storage and organization options. The adjustable shoulder straps and back padding ensure comfortable carrying, even during long commutes. Whether you're a student, professional, or traveler, this versatile backpack is designed to meet your needs while keeping your belongings safe and secure.", 39.99, 5, 10),
    ("product8.jpg", "Protective Neoprene Laptop Sleeve", "Keep your laptop safe and secure with this protective neoprene laptop sleeve. The sleeve is designed to fit most standard laptops, providing a snug and cushioned fit. The neoprene material offers shock absorption and protects against scratches, bumps, and dust. The slim and lightweight design allows for easy transport in a bag or on its own. Whether you're commuting, traveling, or working from a café, this laptop sleeve ensures your device stays protected and adds a touch of style.", 19.99, 1, 20),
    ("product9.jpg", "Wireless Over-Ear Noise-Canceling Headphones", "Immerse yourself in high-quality audio with these wireless over-ear noise-canceling headphones. The headphones feature advanced noise-canceling technology, reducing unwanted background noise and providing a more focused listening experience. With Bluetooth connectivity,you can enjoy wireless freedom and easily connect to your devices. The over-ear design and cushioned ear cups offer comfort for extended wear. The headphones deliver rich and immersive sound, with deep bass and crisp highs, perfect for music enthusiasts and audiophiles. With a long battery life and convenient controls, these headphones are ideal for travel, work, or leisure, allowing you to enjoy your favorite music with exceptional clarity and convenience.", 49.99, 1, 15),
    ("product10.jpg", "Portable Bluetooth Speaker with Enhanced Bass", "Take your music wherever you go with this portable Bluetooth speaker. The speaker boasts a compact and lightweight design, making it easy to carry in your backpack or purse. Despite its size, it delivers impressive sound quality with enhanced bass, providing a rich and immersive listening experience. With Bluetooth connectivity, you can wirelessly connect your devices and stream music effortlessly. The speaker also features a built-in rechargeable battery that offers long playtime, allowing you to enjoy your favorite tunes for hours. Whether you're at a picnic, party, or beach, this portable Bluetooth speaker ensures a vibrant and enjoyable audio experience.", 29.99, 1, 10),
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



#Orders.reset_identity_column()
#Cart.reset_identity_column()