function addToCart(productName, productPrice) {
  let cart = JSON.parse(localStorage.getItem('cart')) || [];
  cart.push({ name: productName, price: productPrice });
  localStorage.setItem('cart', JSON.stringify(cart));
}


function displayCartItems() {
  let cart = JSON.parse(localStorage.getItem('cart')) || [];

  let cartItemsDiv = document.getElementById('cart-items');
  cartItemsDiv.innerHTML = '';

  cart.forEach((item) => {
    let itemDiv = document.createElement('div');
    itemDiv.innerHTML = `<p>${item.name} - $${item.price}</p>`;
    cartItemsDiv.appendChild(itemDiv);
  });
}

displayCartItems();
