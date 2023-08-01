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
        

    def do_GET(self):
        if self.path == '/':
           cookies = self.do_home_page()
        try:
            split_path = os.path.splitext(self.path)
            request_extension = split_path[1]
            if request_extension != ".py":
                if ('/index.html' or '/main.css' in self.path) and '/index3.html' not in self.path:
                    cursor.execute("SELECT * FROM Categories")
                    categories_data = cursor.fetchall()

                    table_html = "<div style = 'width:110%'>"
                    for category in categories_data:
                        table_html += f"<a class = 'navbar' href='/?CategoryID={category[0]}' target='_blank'>{category[1]}</a>"
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
                                        <a href = '/?ProductID={product[0]}' target='_blank'><img src='Images/product1.jpg' alt= '{product[2]}' style='width:100%'></a>
                                        <a href = '/?ProductID={product[0]}' target='_blank' style ='text-decoration: none;'><h2 class="a-size-base-plus a-color-base a-text-normal">{product[2]}</h2></a>
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
                                                            <img src='Images/{chosen_product[1]}.jpg' alt = '{chosen_product[2]}'>
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
                                chosen_product_html += f'''<p>In stock</p><button class='add-to-cart-btn' 
                                                        data-product-name = 'Product{chosen_product[2]}' 
                                                        data-product-price = '{chosen_product[4]}' 
                                                        data-product-id = 'product{chosen_product[0]}'>Add to Cart</button></div></div>'''
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
                        
                    product_html = "<div id = 'container'><div id = 'row'>"
                    index = 0
                    for product in products_data:
                        product_html += f"""
                                    <div class='element'>
                                        <a href = '/?ProductID={product[0]}' target='_blank'><img src='Images/product1.jpg' alt= '{product[2]}' style='width:100%'></a>
                                        <a href = '/?ProductID={product[0]}' target='_blank' style ='text-decoration: none;'><h2 class="a-size-base-plus a-color-base a-text-normal">{product[2]}</h2></a>
                                        <p class = 'price'>${product[4]}</p>
                                    </div>
                                """  
                        index += 1 
                        if index == 5:
                            product_html += "</div><div id = 'row'>"
                            index = 0
                    product_html += "</div></div>"    
                    modified_html_content = table_html + product_html
                    if(self.path == "/login"):
                        self.path = "/index3.html"
                    with open(self.path[1:], 'r') as f:
                        html_content = f.read()
                    modified_html_content = html_content.replace('<div id="link-container"></div>', modified_html_content)
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(bytes(modified_html_content, 'utf-8'))

                elif ('/index3.html' or '/main.css' in self.path) and '/index.html' not in self.path:
                    with open('index3.html', 'r') as f:
                        html_content = f.read()

                    username = cookies['remembered_username'].value
                    welcome_message = "<div class = 'welcome'>"
                    welcome_message += f"<p style = 'color:white' 'font-size:20px'>Welcome back {username}</p></div>"
                    
                    html_content = html_content.replace('<div id = "welcome"></div>', welcome_message)
                    modified_html_content = html_content.replace('<div id="link-container"></div>', self.get_data_html())
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(bytes(modified_html_content, 'utf-8'))
                
                
            else:
                f = "File not found"
                self.send_error(404,f)
        except:
            f = "File not found"
            self.send_error(404,f)
    
    
    def do_POST(self):
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
            self.do_login(username)

            with open('index3.html', 'r') as f:
                html_content = f.read()
               
            welcome_message = '<div class = "welcome">'
            welcome_message += f'<p style = "color:red" "font-size:20px">Welcome back {username}</p></div>'
            
            html_content = html_content.replace('<div id = "welcome"></div>', welcome_message)
            modified_html_content = html_content.replace('<div id="link-container"></div>', self.get_data_html())
            self.wfile.write(bytes(modified_html_content, encoding='utf-8'))
            return
        else:
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
        

    def get_data_html(self):
            cursor.execute("SELECT * FROM Categories")
            categories_data = cursor.fetchall()

            table_html = "<div style = 'width:110%'>"
            for category in categories_data:
                table_html += f"<a class='navbar' href='/?CategoryID={category[0]}' target='_blank'>{category[1]}</a>"
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
                                <a href='/?ProductID={product[0]}' target='_blank'><img src='Images/product1.jpg' alt='{product[2]}' style='width:100%'></a>
                                <a href='/?ProductID={product[0]}' target='_blank' style='text-decoration: none;'><h2 class="a-size-base-plus a-color-base a-text-normal">{product[2]}</h2></a>
                                <p class='price'>${product[4]}</p>
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
                        <a href='/?ProductID={product[0]}' target='_blank'><img src='Images/product1.jpg' alt='{product[2]}' style='width:100%'></a>
                        <a href='/?ProductID={product[0]}' target='_blank' style='text-decoration: none;'><h2 class="a-size-base-plus a-color-base a-text-normal">{product[2]}</h2></a>
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

if __name__ == "__main__":
    httpd = HTTPServer((HOST_NAME,PORT),Server)
    print(time.asctime(), "Start Server - %s:%s"%(HOST_NAME,PORT))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(),'Stop Server - %s:%s' %(HOST_NAME,PORT))   