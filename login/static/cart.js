document.addEventListener("DOMContentLoaded", function () {
    const addToCartButtons = document.querySelectorAll(".add-to-cart-btn");

    addToCartButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            const productCard = button.closest(".product-card");
            const productTitle = productCard.querySelector(".product-title").innerText;
            const productPrice = productCard.querySelector(".product-price").innerText;

            // Create a new cart item
            const cartItem = document.createElement("div");
            cartItem.classList.add("cart-item");
            cartItem.innerHTML = `
                <div class="cart-item-title">${productTitle}</div>
                <div class="cart-item-price">${productPrice}</div>
            `;

            // Append the cart item to the cart container
            const cartContainer = document.querySelector(".listCart");
            cartContainer.appendChild(cartItem);
        });
    });
});
