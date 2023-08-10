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

    def update_status(status, order_id):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "UPDATE Orders SET Status = %s WHERE OrderID = %s"
            values = (status, order_id)

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
    def __init__(self, product_id, picture_name, product_name, description, price, category_id, quantity, status):
        self.picture_name = picture_name
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price
        self.category_id = category_id
        self.quantity = quantity
        self.status = status


    def create(picture_name, product_name, description, price, category_id, quantity, status):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "INSERT INTO Product (PictureName, ProductName, Description, Price, CategoryID, Quantity, Status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (picture_name, product_name, description, price, category_id, quantity, status)

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

    def read_all():
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Product")
            row = cursor.fetchall()

            cursor.close()
            conn.close()

            return row

        except :
            conn.rollback()

    def update(product_name, description, price, category_id, quantity, product_id, status):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "UPDATE Product SET ProductName = %s, Description = %s, Price = %s, CategoryID = %s, Quantity = %s, Status = %s  WHERE ProductID = %s"
            values = (product_name, description, price, category_id, quantity, status, product_id)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return True  

        except :
            conn.rollback()  

    def disable_status(product_id):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "UPDATE Product SET Status = 0 WHERE ProductID = %s"
            values = (product_id)
            
            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()
        except:
            conn.rollback()

    def activate_status(product_id):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "UPDATE Product SET Status = 1 WHERE ProductID = %s"
            values = (product_id)
            
            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()
        except:
            conn.rollback()
    # 0: disabled
    # 1: activated
    def delete_by_id(product_id):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            query = "DELETE FROM Product WHERE ProductID = %s"
            values = (product_id)

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

                # for row in rows:
                #     category_id = row[0]
                #     category_name = row[1]
                #     description = row[2]
                #     stt = row[3]

                #     category = Categories(category_id, category_name, description, stt)
                #     print(f"Category name: {category.category_name}")
                #     print(f"Description: {category.description}")
                #     print(f"STT: {category.stt}")
                #     print("-------------------------")
            return rows
            
        except Exception as e:
            conn.rollback()
            print(f"Error: {str(e)}")


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
    ("product1.jpg", "Men's Striped Button-Down Shirt", "A classic and stylish men's button-down shirt with a timeless vertical stripe pattern for a touch of sophistication. Made from high-quality cotton fabric, ensuring comfort and durability.", 19.99, 2, 50, 1),
    ("product2.jpg", "Women's Slim Fit Dark Wash Jeans", "Versatile and flattering women's dark wash jeans crafted from premium denim fabric. Features a hint of stretch for a comfortable fit, and pairs well with various tops and shoes", 29.99, 2, 30, 1),
    ("product3.jpg", " Men's Classic Canvas Sneakers", "Stylish and comfortable men's canvas sneakers with a durable upper, padded collar, and cushioned insole. Suitable for various activities with excellent traction", 59.99, 5, 20, 1),
    ("product4.jpg", "Women's Strappy Flat Sandals", "Comfortable and chic women's flat sandals with multiple crisscross straps for a secure fit. Made from synthetic materials, perfect for warm weather. ", 24.99, 5, 15, 1),
    ("product5.jpg", "Men's Stainless Steel Chronograph Watch", "A sophisticated men's stainless steel chronograph watch featuring a sleek design, precise timekeeping, and water resistance. ", 79.99, 10, 10, 1),
    ("product6.jpg", "Women's Sterling Silver Charm Bracelet", "An elegant sterling silver charm bracelet with intricate details, adding a touch of charm to any outfit", 12.99, 10, 25, 1),
    ("product7.jpg", "Unisex Water-Resistant Laptop Backpack", "A durable and water-resistant laptop backpack with multiple compartments and padded laptop sleeve. Comfortable for all-day wear and suitable for various needs.", 39.99, 5, 10, 1),
    ("product8.jpg", "Protective Neoprene Laptop Sleeve", "Keep your laptop safe with this protective neoprene laptop sleeve. Offers shock absorption and easy transport.", 19.99, 1, 20, 1),
    ("product9.jpg", "Wireless Over-Ear Noise-Canceling Headphones", "Enjoy high-quality audio with wireless noise-canceling headphones, featuring Bluetooth connectivity and exceptional sound clarity. ", 49.99, 1, 15, 1),
    ("product10.jpg", "Portable Bluetooth Speaker with Enhanced Bass", "Take your music anywhere with this compact Bluetooth speaker, delivering impressive sound quality and long playtime. ", 29.99, 1, 10, 1),
    ("product11.jpg", "Adventures in Wonderland: The Complete Lewis Carroll Collection", "Take your music anywhere with this compact Bluetooth speaker, delivering impressive sound quality and long playtime.", 29.99, 3, 30, 1),
    ("product12.jpg", "Elegance Marble Coasters Set", "Add elegance to your home with these exquisite marble coasters, each showcasing unique veining patterns. Protect surfaces while impressing guests.", 39.99, 4, 25, 1),
    ("product13.jpg", "Premium Yoga Mat with Alignment Lines", '''Elevate your yoga practice with this eco-friendly TPE yoga mat. Featuring alignment lines for precise poses and a non-slip surface for stability, it's the perfect companion for a fulfilling yoga session. Dimensions: 72" x 24".''', 49.99, 9, 65, 1),
    ("product14.jpg", "Glow Radiance Vitamin C Serum", "Illuminate your complexion with our antioxidant-rich serum. Achieve a healthy, youthful glow effortlessly.", 12.99, 6, 120, 1),
    ("product15.jpg", "Adventure Explorer Outdoor Play Set", "Ignite your child's imagination with our Adventure Explorer Outdoor Play Set. This versatile set includes a sturdy treehouse, swing, and slide, providing hours of outdoor fun. Crafted with safety in mind, it encourages active play and creative adventures. Let your child's imagination run wild with this ultimate playtime companion.", 199.99, 7, 75, 1),
    ("product16.jpg", "Strategy Board Games Bundle", "Elevate family game night with our Strategy Board Games Bundle. This collection includes classic titles like Chess, Checkers, and Go, offering endless entertainment and mental stimulation. Perfect for all ages, it's a great way to bond, strategize, and have fun together. Unleash your inner tactician with this diverse board game set.", 49.99, 7, 200, 1),
    ("product17.jpg", "UltraGrip All-Season Car Tires", "Experience superior traction in all weather conditions with our UltraGrip All-Season Car Tires. Designed for optimal performance on wet, dry, and snowy roads, these tires provide safety and control. Enjoy a smooth and comfortable ride while conquering any road ahead.", 89.99, 8, 64, 1),
    ("product18.jpg", "AutoGuard Dash Cam Pro", "Capture every moment on the road with the AutoGuard Dash Cam Pro. Equipped with advanced features like 4K recording, GPS tracking, and collision detection, it ensures your safety and peace of mind. Record your journeys, monitor surroundings, and document incidents effortlessly. Drive confidently with this high-tech automotive companion.", 149.99, 8, 20, 1),
    
]


# for product in products:
#     picture_name, product_name, description, price, category_id, quantity, status = product
#     Product.create(picture_name, product_name, description, price, category_id, quantity, status)

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



#Product.reset_identity_column()