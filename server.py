import http.cookies
from http import cookies
from http.server import BaseHTTPRequestHandler
import os
import practice
from urllib.parse import parse_qs
from datetime import datetime, timedelta
import datetime
import time
import requests
from http.server import HTTPServer
import smtplib
from email.mime.text import MIMEText
import json

conn = practice.connect_to_database()
cursor = conn.cursor()


class Server(BaseHTTPRequestHandler):
    def do_login(self, username):
     ##-------###
        expiration_date = datetime.datetime.utcnow() + datetime.timedelta(days=7)

        # Create the cookie object and set its properties
        cookie = http.cookies.SimpleCookie()
        cookie['remembered_username'] = username
        cookie['remembered_username']['expires'] = expiration_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        self.send_response(200)
        self.send_header('Set-Cookie', cookie.output(header=''))
        self.end_headers()
        ##------###
        

    def do_home_page(self):
        cookie_header = http.cookies.SimpleCookie(self.headers.get('Cookie'))
        if cookie_header:
            cookies = http.cookies.SimpleCookie()
            cookies.load(cookie_header)
            if 'remembered_username' in cookies:
                self.path = '/index3.html'
                return cookies
        self.path = '/index.html'
        
    # def generateQuantityOptions(self, selectedQuantity) :
    #     options = ''
    #     for i in range(1,11):
    #         if (i == selectedQuantity):
    #             options += f"<option value='{i}' selected>{i}</option>"
    #         else:
    #             options += f"<option value='{i}'>{i}</option>"

    #     return options
    
    # def updateQuantity(itemIndex, newQuantity):
    #     cursor.execute("UPDATE Cart Set Quantity = %s WHERE ProductID = %s", (newQuantity, itemIndex))
    #     cursor.execute("SELECT Price FROM Cart Where ProductID = %s", itemIndex)
    #     item_price = cursor.fetchone()
    #     new_subtotal_price = item_price * newQuantity
    #     cursor.execute("UPDATE Cart SET SubtotalPrice = %s", new_subtotal_price)
    #     conn.commit()


    def do_GET(self):
        #handle picture
        if ".jpg" in self.path:
            root_path = "C:/Users/phamc/OneDrive/Documents/Chú Nam"
            root_path += self.path
            self.path = root_path

            with open(self.path, 'rb') as f:
                picture_content = f.read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(picture_content)

        #home page    
        if self.path == '/':
            cookies = self.do_home_page()
            if self.path == '/index3.html':
                username = cookies['remembered_username'].value


        #checkout page
        if self.path == "/checkout":
            cookies = self.do_home_page()
            username = cookies['remembered_username'].value
        #     # smtp_server = 'smtp.gmail.com'
        #     # smtp_port = 587
        #     # from_email = 'canhtoan0411@gmail.com'
        #     # from_password = 'tpvnwksgbbqvipvu'

        #     # to_email = 'phamcanhtoan04@gmail.com'
        #     # subject = 'Order from Toan'
        #     # body = f'Hello Toan,\n\nYour order has been received and is being processed. Thank you for shopping with us!\n\nBest regards,\nThuan Phat Team'

        #     # msg = MIMEText(body)
        #     # msg['Subject'] = subject
        #     # msg['From'] = from_email
        #     # msg['To'] = to_email
            
            
            




            self.path = "/checkout.html"
            with open(self.path[1:], 'r') as f:
                        html_content = f.read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(html_content, 'utf-8'))
            return
            # try:
            #     server = smtplib.SMTP(smtp_server, smtp_port)
            #     server.starttls()
            #     server.login(from_email, from_password)
            #     server.sendmail(from_email, to_email, msg.as_string())
            #     server.quit()
            #     print("Email sent successfully.")
            #     return
            # except Exception as e:
            #     print(f"Error sending email: {e}")

        # if self.path == "/cart":
        #     index = 0
        #     cursor.execute("SELECT * FROM Cart")
        #     cart_detail = cursor.fetchall()
        #     print(cart_detail)
        #     cart = ""
        #     for tup in cart_detail:
        #         index += 1
        #         cart += f'''<tr><td>{index}</td>
        #             <td><img src="{tup[2]}"></td>
        #             <td>{tup[3]} <input type="button" value="Delete" onclick="deleteRow(this)"></td>
        #             <td>
        #                 <select onchange="updateQuantity({index - 1}, this.value)">{self.generateQuantityOptions(tup[4])}</select>
        #             </td>
        #             <td class="total-price-cell">${tup[6]}</td></tr>
        #         '''
        #     self.path = "/cart.html"
        #     with open(self.path[1:], 'r') as f:
        #         html_content = f.read()
        #     modified_html_content = html_content.replace('<div id="cart-items"></div>', cart)
        #     self.send_response(200)
        #     self.end_headers()
        #     self.wfile.write(bytes(modified_html_content, 'utf-8'))
            
        #     return

            
        try:
            split_path = os.path.splitext(self.path)
            request_extension = split_path[1]
            if request_extension != ".py":
                 
                #user profile page
                if self.path.startswith('/profile/'):
                    username = self.path.split('/')[2]
                    cursor.execute("SELECT * FROM Customer")
                    customers_data = cursor.fetchall()
                    for customer in customers_data:
                        if self.path == f"/profile/{customer[1]}":
                            customer_id = customer[0]
                            cursor.execute("SELECT * FROM Customer WHERE CustomerID = %s", customer_id)
                            chosen_customer = cursor.fetchone()
                            chosen_customer_html = ""
                            chosen_customer_html += f'''
                            <div>
                            <h1>Your account's information</h1>
                            <p>Username: {chosen_customer[1]}</p>
                            <p>Customer name: {chosen_customer[2]}</p>
                            <p>Password: <span id="passwordValue">************</span></p>
                            <p>Email: {chosen_customer[4]}</p>
                            <p>Address: {chosen_customer[5]}</p>
                            <p>Phone number: {chosen_customer[6]}</p>
                            </div>
                            '''
                            self.path = "/customer.html"
                            with open(self.path[1:], 'r') as f:
                                html_content = f.read()
                            modified_html_content = html_content.replace('<div id="customer-container"></div>', chosen_customer_html)
                            self.send_response(200)
                            self.end_headers()
                            self.wfile.write(bytes(modified_html_content, 'utf-8'))
                            return
                #categories and products page   
                if ('/index.html' or '/main.css' in self.path) and '/index3.html' not in self.path:
                    #categories
                    cursor.execute("SELECT * FROM Categories")
                    categories_data = cursor.fetchall()
                    table_html = "<div style = 'width:110%'>"
                    for category in categories_data:
                        table_html += f"<a class = 'navbar' href='/?CategoryID={category[0]}'>{category[1]}</a>"
                    table_html += "</div>"

                    for category in categories_data:
                        if self.path == f'/?CategoryID={category[0]}':
                            category_id = category[0]
                            cursor.execute("SELECT * FROM Product WHERE CategoryID = %s", category_id)
                            filtered_products = cursor.fetchall()
                            filtered_product_html = ""
                            for product in filtered_products:
                                filtered_product_html += f"""
                                    <div class='element'>
                                        <a href = '/?ProductID={product[0]}' ><img src='Images/{product[1]}' alt= "{product[2]}" style='width:100%'></a>
                                        <a href = '/?ProductID={product[0]}'  style ='text-decoration: none;'><h2 class="a-size-base-plus a-color-base a-text-normal">{product[2]}</h2></a>
                                        <p class = 'price'>${product[4]}</p>      
                                    </div>
                                """  
                            modified_html_content = table_html + filtered_product_html
                            self.path = "/index1.html"
                            with open(self.path[1:], 'r') as f:
                                html_content = f.read()
                            modified_html_content = html_content.replace('<div id="new_container"></div>', modified_html_content)
                            self.send_response(200)
                            self.end_headers()
                            self.wfile.write(bytes(modified_html_content, 'utf-8'))
                            return
                    
                    #products
                    cursor.execute("SELECT * FROM Product")
                    products_data = cursor.fetchall()

                    for product in products_data:
                        if self.path == f"/?ProductID={product[0]}":
                            product_id = product[0]
                            cursor.execute("SELECT * FROM Product WHERE ProductID = %s", product_id)
                            chosen_product = cursor.fetchone()
                            chosen_product_html = ""
                            chosen_product_html += f"""<div class = 'container'>
                                                            <div class = 'column'>
                                                            <img src='Images/{chosen_product[1]}' alt = "{chosen_product[2]}">
                                                            </div>
                                                            <div class = 'column'>
                                                                <p>{chosen_product[2]}</p>
                                                                <h1 class="a-size-base-plus a-text-bold"> About this item </h1>
                                                                <p>{chosen_product[3]}</p>
                                                            </div>
                                                            <div class = 'buy_column'>
                                                                <p>${chosen_product[4]}</p>
                                                            """
                            if chosen_product[6] > 0:
                                #add to cart info
                                chosen_product_html += f'''<p>In stock</p><input type= "submit" value = "Add to cart" class='add-to-cart-btn' 
                                                        data-product-name = "{chosen_product[2]}" 
                                                        data-product-picture = "Images/{chosen_product[1]}"
                                                        data-product-price = "{chosen_product[4]}" 
                                                        data-product-id = {chosen_product[0]}></div></div>'''
                            else:
                                chosen_product_html += f"<p>Out of stock</p></div></div>"
                            modified_html_content = table_html + chosen_product_html
                            self.path = "/index2.html"
                            with open(self.path[1:], 'r') as f:
                                html_content = f.read()
                            modified_html_content = html_content.replace('<div id="product_container"></div>', modified_html_content)
                            self.send_response(200)
                            self.end_headers()
                            self.wfile.write(bytes(modified_html_content, 'utf-8'))
                            return
                        
                    #5 products in a row    
                    product_html = "<div id = 'container'><div id = 'row'>"
                    index = 0
                    for product in products_data:
                        product_html += f"""
                                    <div class='element'>
                                        <a href = '/?ProductID={product[0]}' ><img src='Images/{product[1]}' alt= "{product[2]}" style='width:100%'></a>
                                        <a href = '/?ProductID={product[0]}'  style ='text-decoration: none;'><h2 class="a-size-base-plus a-color-base a-text-normal">{product[2]}</h2></a>
                                        <p class = 'price'>${product[4]}</p>
                                    </div>
                                """  
                        index += 1 
                        if index == 5:
                            product_html += "</div><div id = 'row'>"
                            index = 0
                    product_html += "</div></div>"    
                    modified_html_content = table_html + product_html
                    #log in first time
                    if(self.path == "/login"):
                        self.path = "/index3.html"
                    with open(self.path[1:], 'r') as f:
                        html_content = f.read()
                    modified_html_content = html_content.replace('<div id="link-container"></div>', modified_html_content)
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(bytes(modified_html_content, 'utf-8'))

                #log in not the first time
                elif ('/index3.html' or '/main.css' in self.path) and '/index.html' not in self.path:
                    #welcome 
                    welcome_message = f'<div class = "account"><a href="/profile/{username}" target="_blank" style = "color:white" "font-size:20px">Manage Account</a></div>'
                    welcome_message += f'''<div class = "welcome"><p style = "color:white" "font-size:20px">Welcome back {username}</p></div>'''
                    #user profile
                    if self.path == f"/?Username={username}":
                        cursor.execute("SELECT * FROM Customer")
                        customers_data = cursor.fetchall()
                        for customer in customers_data:
                            if self.path == f"/?Username={customer[1]}":
                                customer_id = customer[0]
                                cursor.execute("SELECT * FROM Customer WHERE CustomerID = %s", customer_id)
                                chosen_customer = cursor.fetchone()
                                chosen_customer_html = ""
                                chosen_customer_html += f'''
                                <div>
                                <h1>Your account's information</h1>
                                <p>Username: {chosen_customer[1]}</p>
                                <p>Customer name: {chosen_customer[2]}</p>
                                <p>Password: <span id="passwordValue">************</span></p>
                                <p>Email: {chosen_customer[4]}</p>
                                <p>Address: {chosen_customer[5]}</p>
                                <p>Phone number: {chosen_customer[6]}</p>
                                </div>
                                '''
                                self.path = "/customer.html"
                                with open(self.path[1:], 'r') as f:
                                    html_content = f.read()
                                modified_html_content = html_content.replace('<div id="customer-container"></div>', chosen_customer_html)
                                self.send_response(200)
                                self.end_headers()
                                self.wfile.write(bytes(modified_html_content, 'utf-8'))
                                return
                           
                    with open('index3.html', 'r') as f:
                        html_content = f.read()
                    html_content = html_content.replace('<div id = "welcome"></div>', welcome_message)
                    modified_html_content = html_content.replace('<div id="link-container"></div>', self.get_data_html())
                    
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(bytes(modified_html_content, 'utf-8'))                    
                    return
                   
            else:
                f = "File not found"
                self.send_error(404,f)
        except:
            f = "File not found"
            self.send_error(404,f)
    
    
    def do_POST(self):
        # if self.path == "/addtocart":
        #     content_length = int(self.headers['Content-Length'])
        #     post_data = self.rfile.read(content_length)
        #     data = json.loads(post_data)
        #     product_id = data.get('ProductID')
        #     product_name = data.get('ProductName')
        #     product_picture = data.get('PictureName')
        #     product_price = data.get('ProductPrice')
        #     product_quantity = data.get('Quantity')
        #     username = data.get('Username')

        #     cursor.execute("SELECT CustomerID from Customer WHERE Username = %s", username)
        #     row = cursor.fetchone()
        #     customer_id = row[0]
        #     product_id = int(product_id)
        #     cursor.execute("SELECT * FROM Cart")
        #     cart_data = cursor.fetchall()
            
        #     if cart_data:
        #         for dic in cart_data:
        #             dic = list(dic)
        #             dic[1] = int(dic[1])
        #             if product_id == dic[1]:
        #                 dic[4] += 1 
        #                 subtotal_price = product_price * dic[4]
        #                 cursor.execute("UPDATE Cart SET Quantity = %s, SubtotalPrice = %s WHERE ProductID = %s", (dic[4], subtotal_price, product_id))
        #                 conn.commit()
        #                 return
        #         product_quantity = 1
        #         cursor.execute("INSERT INTO Cart (CustomerID, ProductID, PictureName, ProductName, Quantity, Price, SubtotalPrice) VALUES(%s, %s, %s, %s, %s, %s, %s)", (customer_id, product_id, product_picture, product_name, product_quantity, product_price, product_price))
        #         conn.commit()
        #         return
        #     else:
        #         cursor.execute("INSERT INTO Cart (CustomerID, ProductID, PictureName, ProductName, Quantity, Price, SubtotalPrice) VALUES(%s, %s, %s, %s, %s, %s, %s)", (customer_id, product_id, product_picture, product_name, product_quantity, product_price, product_price))
        #         conn.commit()
        #         return 

            
        #get username and password 
        if self.path == "/login":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = post_data.decode('utf-8')
            form_data = parse_qs(post_data)
            if form_data != {}:
                username = form_data['username'][0]
                password = form_data['password'][0]
                
            else:
                return
                
            query = "SELECT * FROM Customer WHERE Username = %s AND Password = %s"
            cursor.execute(query, (username, password))
            customer = cursor.fetchone()
            
            if customer:
                #handle log in
                self.do_login(username)

                with open('index3.html', 'r') as f:
                    html_content = f.read()
                
                welcome_message = f'<div class = "account"><a href="/profile/{username}" target="_blank" style = "color:white" "font-size:20px">Manage Account</a></div>'
                welcome_message += f'''<div class = "welcome"><p style = "color:white" "font-size:20px">Welcome back {username}</p></div>'''
                
                html_content = html_content.replace('<div id = "welcome"></div>', welcome_message)
                modified_html_content = html_content.replace('<div id="link-container"></div>', self.get_data_html())
                self.wfile.write(bytes(modified_html_content, encoding='utf-8'))
                return
            else:
                #not logged in
                self.send_response(401)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                error_message = 'Login failed. Invalid credentials.'
                form_html = '''
                    <form action="/login" method="post">
                        <input class = "username_password"  type="text" name="username" placeholder="Username">
                        <input class = "username_password"  type="password" name="password" placeholder="Password">
                        <input type="submit" value="Login">
                    </form>
                    '''

                response_content = f'<p>{error_message}</p>{form_html}'
                self.wfile.write(bytes(response_content, 'utf-8'))
                return
        
        if self.path == "/checkout":
            with open('checkout.html', 'r') as f:
                html_content = f.read()
            self.wfile.write(bytes(html_content, encoding='utf-8'))
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            form_data = json.loads(post_data)
            username = form_data['username']
            total_price = form_data['total_price']
            cart = form_data['cart']
            cursor.execute("SELECT CustomerID from Customer WHERE Username = %s", username)
            customer_id = cursor.fetchone()
            order_date = datetime.datetime.utcnow()
            status = 1
            for items in cart:
                cursor.execute(f"INSERT INTO OrderDetails (ProductID, Quantity, Price) VALUES (%s, %s, %s)", ({items['ID']}, {items['Quantity']}, {items['Price']}))
            cursor.execute("INSERT INTO Orders (CustomerID, OrderDate, TotalPrice, Status) VALUES (%s, %s, %s, %s)", (customer_id, order_date, total_price, status))
            conn.commit()
            return
            
    def get_data_html(self):
            #root path of most pages: categories and products
            cursor.execute("SELECT * FROM Categories")
            categories_data = cursor.fetchall()

            table_html = "<div style = 'width:110%'>"
            for category in categories_data:
                table_html  += f"<a class='navbar' href='/?CategoryID={category[0]}' >{category[1]}</a>"
            table_html += "</div>"

            for category in categories_data:
                if self.path == f'/?CategoryID={category[0]}':
                    category_id = category[0]
                    cursor.execute("SELECT * FROM Product WHERE CategoryID = %s", category_id)
                    filtered_products = cursor.fetchall()
                    filtered_product_html = ""
                    for product in filtered_products:
                        filtered_product_html += f"""
                            <div class='element'>
                                <a href='/?ProductID={product[0]}' ><img src='Images/{product[1]}' alt="{product[2]}" style='width:100%'></a>
                                <a href='/?ProductID={product[0]}'  style='text-decoration: none;'><h2 class="a-size-base-plus a-color-base a-text-normal">{product[2]}</h2></a>
                                <p class='prices'>${product[4]}</p>
                            </div>
                        """
                    modified_html_content = table_html + filtered_product_html
                    self.path = "/index1.html"
                    with open(self.path[1:], 'r') as f:
                        html_content = f.read()
                    modified_html_content = html_content.replace('<div id="new_container"></div>', modified_html_content)
                    return modified_html_content

            cursor.execute("SELECT * FROM Product")
            products_data = cursor.fetchall()

            product_html = "<div id='container'><div id='row'>"
            index = 0
            for product in products_data:
                product_html += f"""
                    <div class='element'>
                        <a href='/?ProductID={product[0]}' ><img src='Images/{product[1]}' alt="{product[2]}" style='width:100%'></a>
                        <a href='/?ProductID={product[0]}'  style='text-decoration: none;'><h2 class="a-size-base-plus a-color-base a-text-normal">{product[2]}</h2></a>
                        <p class='price'>${product[4]}</p>
                    </div>
                """
                index += 1
                if index == 5:
                    product_html += "</div><div id='row'>"
                    index = 0
            product_html += "</div></div>"
            modified_html_content = table_html + product_html
            return modified_html_content


HOST_NAME = 'localhost'
PORT = 8000
#run server
if __name__ == "__main__":
    httpd = HTTPServer((HOST_NAME,PORT),Server)
    print(time.asctime(), "Start Server - %s:%s"%(HOST_NAME,PORT))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(),'Stop Server - %s:%s' %(HOST_NAME,PORT))   