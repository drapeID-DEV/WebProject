const categoriesBtn = document.querySelectorAll('.category-btn');

const productsContainer = document.querySelector(".products-container");

const productsData = JSON.parse(
    document.getElementById("products_json").textContent
);

categoriesBtn.forEach(button => {
    button.addEventListener("click", () => {
        targetCategory = button.getAttribute("data-category");

        productsContainer.innerHTML = ""
        filterProducts(targetCategory);
    });
});

function filterProducts(category) {
    productsData.forEach(product => {
        if(product.category == category) {
            const newProduct = document.createElement("div");
            newProduct.textContent = product.title
            newProduct.classList.add("product-card")
            productsContainer.appendChild(newProduct);
        };
    });
};