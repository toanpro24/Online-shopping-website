function displayCartItems() {
    let cart = JSON.parse(getCookie("cartdetail")) || []; 

    console.log('Cart-data', cart);

    let cartItemsList = document.getElementById('cart-items');
    let totalPriceElement = document.getElementById('total-price');
    let totalPrice = 0;

    cartItemsList.innerHTML = '';

    if (Array.isArray(cart)) { 
        cart.forEach((item, index) => {
            let total = item.price * item.quantity;
            totalPrice += total;
            let tableRow = document.createElement('tr');
            tableRow.innerHTML = `
                <td>${index + 1}</td>
                <td><img src="${item.picture}"></td>
                <td>${item.name} <input type="button" value="Delete" onclick="deleteRow(this)"></td>
                <td>
                    <select onchange="updateQuantity(${index}, this.value)">${generateQuantityOptions(item.quantity)}</select>
                </td>
                <td class="total-price-cell">$${total.toFixed(2)}</td>
            `;
            cartItemsList.appendChild(tableRow);
        });
    } else {
        console.log('Cart data is not an array.'); 
    }

    totalPriceElement.innerText = `$${totalPrice.toFixed(2)}`;
    let totalItems = 0;
    cart.forEach(item => {
        totalItems += item.quantity;
    }); 
    let total_Items_Element = document.getElementById("total-items");
    total_Items_Element.innerText = totalItems;

    if (cart.length > 0) {
        cartTable.style.display = "table";
        emptyCartMessage.style.display = "none";
        proceedToCheckoutBtn.style.display = "inline-block";
      } else {
        cartTable.style.display = "none";
        emptyCartMessage.style.display = "block";
        proceedToCheckoutBtn.style.display = "none";
      }

}
function generateQuantityOptions(selectedQuantity) {
    
    let options = '';
    for (let i = 1; i <= 5; i++) {
        if (i === selectedQuantity) {
            options += `<option value="${i}" selected>${i}</option>`;
        } else {
            options += `<option value="${i}">${i}</option>`;
        }
    }
    return options;
}

function updateQuantity(itemIndex, newQuantity) {
    let cart = JSON.parse(getCookie("cartdetail"));
    cart[itemIndex].quantity = parseInt(newQuantity);

    let item = cart[itemIndex];
    let newTotal = item.price * item.quantity;
    let totalCell = document.getElementsByClassName("total-price-cell")[itemIndex];
    totalCell.innerText = `$${newTotal.toFixed(2)}`;


    let totalPrice = 0;
    cart.forEach(item => {
        totalPrice += item.price * item.quantity;
    });


    let totalPriceElement = document.getElementById("total-price");
    totalPriceElement.innerText = `$${totalPrice.toFixed(2)}`;

    setCookie("cartdetail", JSON.stringify(cart), 30);
    location.reload();
}


function deleteRow(r) {
    var i = r.parentNode.parentNode.rowIndex;
    document.getElementById("cartTable").deleteRow(i);
    let cart = JSON.parse(getCookie("cartdetail"));
    cart.splice(i - 1, 1)
    setCookie("cartdetail", JSON.stringify(cart), 30); 
    location.reload();
}

function proceedToCheckout() {
    data = {};
    let username = getCookie("remembered_username");
    let cart = JSON.parse(getCookie("cartdetail")) || [];
    let totalPrice = 0;
    cart.forEach(item => {
        totalPrice += item.price * item.quantity;
    });
    data['username'] = username;
    data['total_price'] = totalPrice;
    data['cart'] = cart;

    fetch("/checkout", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    document.cookie = "cookiename=cart ; expires = Thu, 01 Jan 1970 00:00:00 GMT"
    document.cookie = "cookiename=cartdetail ; expires = Thu, 01 Jan 1970 00:00:00 GMT"
}


// function myFunction() {
//     alert('Hello');
//     location.href = "/checkout.html";
// }

function getCookie(name) {
    const cookieName = name + "=";
    const decodedCookie = decodeURIComponent(document.cookie);
    const cookieArray = decodedCookie.split(';');
    for (let i = 0; i < cookieArray.length; i++) {
        let cookie = cookieArray[i];
        while (cookie.charAt(0) === ' ') {
        cookie = cookie.substring(1);
        }
        if (cookie.indexOf(cookieName) === 0) {
        return cookie.substring(cookieName.length, cookie.length);
        }
    }
    return null;
}
function setCookie(name, value, days) {
    let expires = "";
    if (days) {
        let date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}


displayCartItems();