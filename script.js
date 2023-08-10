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

const itemsPerPage = 5;  
const data = [
    "Item 1", "Item 2", "Item 3", "Item 4", "Item 5",
    "Item 6", "Item 7", "Item 8", "Item 9", "Item 10",
];

const contentContainer = document.getElementById("contentContainer");
const pagination = document.getElementById("pagination");

function displayItems(pageNumber) {
    const startIndex = (pageNumber - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    const itemsToDisplay = data.slice(startIndex, endIndex);

    contentContainer.innerHTML = "";
    itemsToDisplay.forEach(item => {
        const itemElement = document.createElement("div");
        itemElement.textContent = item;
        contentContainer.appendChild(itemElement);
    });
}

function createPaginationButtons() {
    const pageCount = Math.ceil(data.length / itemsPerPage);
    for (let i = 1; i <= pageCount; i++) {
        const button = document.createElement("button");
        button.textContent = i;
        button.addEventListener("click", () => {
            displayItems(i);
        });
        pagination.appendChild(button);
    }
}

displayItems(1);  // Display initial page
createPaginationButtons();
