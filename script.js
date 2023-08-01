const cart = {};
  const storedCart = getCookie("cart");
  if (storedCart) {
    Object.assign(cart, JSON.parse(storedCart));
    updateCartCount();
  }

  document.querySelectorAll(".add-to-cart-btn").forEach((button) => {
    button.addEventListener("click", (event) => {
      const productId = event.target.dataset.productId;

      if (cart[productId]) {
        cart[productId]++;
      } else {
        cart[productId] = 1;
      }

      updateCartCount();
      setCookie("cart", JSON.stringify(cart), 7);
    });
  });

  function updateCartCount() {
    let totalCount = 0;

    for (const productCount of Object.values(cart)) {
      totalCount += productCount;
    }

    document.getElementById("cart-count").innerText = totalCount;
  }
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