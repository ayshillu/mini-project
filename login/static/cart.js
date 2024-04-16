document.addEventListener('DOMContentLoaded', function () {
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            const productId = button.getAttribute('data-product-id');
            addToCart(productId);
        });
    });

    function addToCart(productId) {
        fetch('/add_to_cart/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: `product_id=${productId}`
        })

            .then(response => {
                if (response.ok) {
                    // Handle success, maybe show a message to the user
                    console.log('Product added to cart successfully');
                    window.location.href = '/cart/';  // Redirect to the cart page
                } else {
                    // Handle error response
                    console.error('Failed to add product to cart');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
