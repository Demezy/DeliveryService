console.log("Shopping cart is ready");

let productList = {};
let basket = document.querySelector("span.basket");
let carts = document.querySelectorAll(".add-cart");
let delCarts = document.querySelectorAll(".remove-cart");

// let btns = document.querySelectorAll(".btn-group")
// console.log(btns[1].children)
for (let i = 0; i < carts.length; i++) {
    carts[i].addEventListener("click", () => {
        cartNumbers(carts[i]);
    });
    delCarts[i].addEventListener("click", () => {
        removeCart(carts[i]);
    });
    // console.log(carts[i])
    productList[carts[i].getAttribute("value")] = {
        "price": carts[i].parentElement.children[0].value,
        "inCart": 0
    };
    // console.log(carts[i].getAttribute("value"));
    // console.log(carts[i].parentElement.children[0])
}

// localStorage[product.value] = parseInt(localCart[product.value]) + 1

function removeCart(product) {
    localStorage.removeItem(product.value);
    basket.textContent = 0;
}

function cartNumbers(product) {
    console.log(product.value);
    let productNumbers = parseInt(localStorage.getItem("countOfProducts"));
    if (productNumbers) {
        localStorage.setItem("countOfProducts", productNumbers + 1);

    } else {
        localStorage.setItem("countOfProducts", 1);
    }
    basket.textContent = productNumbers + 1;
    setItem(product);
}

function setItem(product) {
    console.log(product.value);
    let localCart = JSON.parse(localStorage.getItem("localCart"));
    if (localCart == null) {
        localCart = {product.value
    :
        {
            "count"
        :
            product.inCart, "price"
        :
            product.price
        }
    }
    } else {
        if (localCart[value].inCart != null) {
            localCart = {
                ...localCart,
                [value]: product
            }
        }
        localCart[value].inCart += 1
    }

// parseInt(localCart[product.value]) + 1
    console.log(localCart)
    localStorage.setItem("localCart", JSON.stringify(localCart))
}

// console.log("shopping_cart.js");
// console.log(productList);
// productList["test2"] = 21321
