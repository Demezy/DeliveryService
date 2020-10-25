console.log("Shopping cart is ready");
let carts = document.querySelectorAll(".add-cart");
let delCarts = document.querySelectorAll(".remove-cart");

for (let i = 0; i < carts.length; i++) {
    carts[i].addEventListener("click", () => {
        cartNumbers();
    });
    delCarts[i].addEventListener("click", () => {
        removeCart();
    });
}

let basket = document.querySelector("span.basket")

function removeCart() {
    localStorage.setItem("cartNumbers", 0);
    basket.textContent = 0;
}

function cartNumbers() {
    productNumbers = parseInt(localStorage.getItem("cartNumbers"));
    if (productNumbers) {
        localStorage.setItem("cartNumbers", productNumbers + 1);
        basket.textContent = productNumbers + 1;
    } else {
        localStorage.setItem("cartNumbers", 1);
        basket.textContent = 1;
    }
}
