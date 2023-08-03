import http.cookies
from http import cookies
from http.server import BaseHTTPRequestHandler
import os
import practice
import urllib.parse
from urllib.parse import parse_qs
from datetime import datetime, timedelta
import datetime
import time
import requests
from http.server import HTTPServer
import smtplib
from email.mime.text import MIMEText
import json
import sqlite3

# Connect to SQL Server

conn = practice.connect_to_database()
cursor = conn.cursor()

class Server(BaseHTTPRequestHandler):
    def do_login(self, username):
     ##-------###
        expiration_date = datetime.datetime.utcnow() + datetime.timedelta(days=1)
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
                self.path = '/admin_product_table.html'
                return cookies
        self.path = '/admin.html'

    def add_product(picture_name, product_name, description, price, category_id, quantity):
        success = practice.Product.create(picture_name, product_name, description, price, category_id, quantity)
        if success:
            print("Product added successfully!")
        else:
            print("Failed to add product.")
  
    def update_product(product_id, product_name, description, price, category_id, quantity):
        
        product = practice.Product.read(product_id)
        if product:
        
            product.product_name = product_name
            product.description = description
            product.price = price
            product.category_id = category_id
            product.quantity = quantity

            
            success = product.update()
            if success:
                print("Product updated successfully!")
            else:
                print("Failed to update product.")
        else:
            print("Product not found.")
    
    def delete_product(product_id):
        product = practice.Product.read(product_id)
        if product:

            success = product.delete_by_id()
            if success:
                print("Product deleted successfully!")
            else:
                print("Failed to delete product.")
        else:
            print("Product not found.")


    def do_GET(self):
        if ".jpg" in self.path:
            root_path = "C:/Users/phamc/OneDrive/Documents/Chú Nam"
            root_path += self.path
            self.path = root_path

            with open(self.path, 'rb') as f:
                picture_content = f.read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(picture_content)

        if self.path == '/':
            cookies = self.do_home_page()
            if self.path == '/admin_product_table.html':
                username = cookies['remembered_username'].value
        if self.path.startswith("/search"):
            query_string = self.path.split('?', 1)[1]
            query_params = urllib.parse.parse_qs(query_string)
            
            json_data = query_params.get('data')
            if json_data:
                # Convert the JSON data back to a dictionary
                data = json.loads(json_data[0])

            column = data.get('column')
            search_term = data.get('searchTerm')
            if column and search_term:
                if "'s" in search_term:
                    index = search_term.find("'s")
                    search_term = search_term[:index] + "'" + search_term[index:]
                query = f"SELECT * FROM Product WHERE {column} LIKE '%{search_term}%'"
                cursor.execute(query)

                search_results = cursor.fetchall()
                new_html = ""
                for product in search_results:
                    product = list(product)
                    product[1] = "Images/" + product[1]
                    new_html += f'''<tr><td data-column-name = 'ProductID'>{product[0]}</td>
                    <td ><img src="{product[1]}"></td>
                    <td data-column-name = 'ProductName'>{product[2]}</td>
                    <td data-column-name = 'Description'>{product[3]}</td>
                    <td data-column-name = 'Price'>{product[4]}</td>
                    <td data-column-name = 'CategoryID'>{product[5]}</td>
                    <td data-column-name = 'Quantity'>{product[6]}</td>
                    <td><button class="edit-button">Edit</button></td>
                    <td><button class = "delete-button">Delete</button></td>
                    </tr>
                    '''
                with open('admin_product_table.html', 'r') as f:
                    html_content = f.read()
                modified_html_content = html_content.replace('<div id = "product_table"></div>', new_html)
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(modified_html_content.encode('utf-8'))
                return

        if self.path == '/home':
            self.path = '/admin_product_table_redirect.html'
            product_data = practice.Product.read_all()
            product_html = ""
            for product in product_data:
                product = list(product)
                product[1] = "Images/" + product[1]
                product_html += f'''<tr><td data-column-name = 'ProductID'>{product[0]}</td>
                    <td ><img src="{product[1]}"></td>
                    <td data-column-name = 'ProductName'>{product[2]}</td>
                    <td data-column-name = 'Description'>{product[3]}</td>
                    <td data-column-name = 'Price'>{product[4]}</td>
                    <td data-column-name = 'CategoryID'>{product[5]}</td>
                    <td data-column-name = 'Quantity'>{product[6]}</td>
                    <td><button class="edit-button">Edit</button></td>
                    <td><button class = "delete-button">Delete</button></td>
                    </tr>'''
            with open(self.path[1:], 'r') as f:
                html_content = f.read()
            html_content = html_content.replace('<div id = "product_catalog"></div>', product_html)
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(html_content.encode('utf-8'))
            return
        try:
            split_path = os.path.splitext(self.path)
            request_extension = split_path[1]
            if request_extension != ".py":
                if self.path == "/":
                    self.path = "/admin.html"
                with open(self.path[1:], 'r') as f:
                    html_content = f.read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(html_content, 'utf-8'))

            else:
                f = "File not found"
                self.send_error(404,f) 
                
        except:
            f = "File not found"
            self.send_error(404,f)


    def do_POST(self):
        if self.path == "/update":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            product_id = data.get('ProductID')
            product_name = data.get('ProductName')
            description = data.get('Description')
            price = data.get('Price')
            category_id = data.get('CategoryID')
            quantity = data.get('Quantity')
            practice.Product.update(product_name, description, price, category_id, quantity, product_id)
            return
        if self.path == "/delete":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            product_id = data.get('ProductID')
            practice.Product.disable_status(product_id)
            return
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
                product_data = practice.Product.read_all()
                product_html = ""
                for product in product_data:
                    product = list(product)
                    product[1] = "Images/" + product[1]
                    product_html += f'''<tr><td data-column-name = 'ProductID'>{product[0]}</td>
                    <td ><img src="{product[1]}"></td>
                    <td data-column-name = 'ProductName'>{product[2]}</td>
                    <td data-column-name = 'Description'>{product[3]}</td>
                    <td data-column-name = 'Price'>{product[4]}</td>
                    <td data-column-name = 'CategoryID'>{product[5]}</td>
                    <td data-column-name = 'Quantity'>{product[6]}</td>
                    <td><button class = "edit-button">Edit</button></td>
                    <td><button class = "delete-button">Delete</button></td>
                    </tr>'''
                with open('admin_product_table.html', 'r') as f:
                    html_content = f.read()
                modified_html_content = html_content.replace('<div id = "product_table"></div>', product_html)
                self.wfile.write(bytes(modified_html_content, encoding = 'utf-8'))
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
        

HOST_NAME = 'localhost'
PORT = 8005
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