let totalCount = 0;
document.querySelectorAll(".add-to-cart-btn").forEach((button) => {
    button.addEventListener("click", (event) => {
        const productId = event.target.dataset.productId;
        const productName = event.target.dataset.productName;
        const productPicture = event.target.dataset.productPicture;
        const productPrice = parseFloat(event.target.dataset.productPrice);
        const username = getCookie("remembered_username")
        data = {};
        data['ProductID'] = productId;
        data['ProductName'] = productName;
        data['PictureName'] = productPicture;
        data['ProductPrice'] = productPrice;
        data['Quantity'] = 1;
        data['Username'] = username
        fetch("/addtocart", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json', 
            },
            body: JSON.stringify(data),
        });
        addToCart(productId, productPicture, productName, productPrice, username);
        updateCartCount();
        
    });
});
function addToCart(productId, productPicture, productName, productPrice, username) {
    let cart = JSON.parse(getCookie("cartdetail")) || [];

    const existingProduct = cart.find((item) => item.id === productId);
    if (existingProduct) {
        existingProduct.quantity++;
    } else {
        cart.push({ id: productId, picture: productPicture, name: productName, price: productPrice, quantity: 1, customer: username });
    }
    location.reload();
    alert(`${productName} has been added to your cart!`);
    updateCartCount();
    console.log(totalCount);
    setCookie("cartdetail", JSON.stringify(cart), 7);
  }

function updateCartCount() {
    totalCount += 1;
    document.getElementById("cart-count").innerText = totalCount;
}



document.addEventListener('DOMContentLoaded', function() {
    const ProductSearch = document.getElementById('searchbar');

    function performSearch(searchTerm) {
        data = {};
        data['searchTerm'] = searchTerm;
        // fetch("/search", {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json', 
        //     },
        //     body: JSON.stringify(data),
        // });
        const queryString = encodeURIComponent(JSON.stringify(data));

        fetch(`/search?data=${queryString}`, {
            method: 'GET',
        });
        location.href = `/search?data=${queryString}`;
    }

    function handleEnterKey(event) {
        if (event.key === 'Enter') {
            const searchTerm = event.target.value;
            performSearch(searchTerm);
        }
    }
    
    if (ProductSearch) {
        ProductSearch.addEventListener('keydown', event => handleEnterKey(event));
    }
});
function setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = "expires=" + date.toUTCString();
    document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

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


const buttonsContainer = document.getElementById("buttons");
function updateButtons(totalPages) {
    buttonsContainer.innerHTML = ""; 

    for (let i = 1; i <= totalPages; i++) {
        const button = document.createElement("button");
        button.textContent = i;
        button.addEventListener("click", () => {
            loadPage(i);
        });
        buttonsContainer.appendChild(button);
    }
}
function loadPage(pageNumber) {
    data = {};
    data['pagenumber'] = pageNumber;
    const queryString = encodeURIComponent(JSON.stringify(data));
    fetch(`/get_paginated_data?page=${queryString}`, {
        method: 'GET',
    });
    location.href = `/get_paginated_data?page=${queryString}`;
    updateButtons(pageNumber);
}


