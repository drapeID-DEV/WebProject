const categoriesBtn = document.querySelectorAll('.category-btn');

const productsContainer = document.querySelector(".products-container");

const productTemplate = document.getElementById("product-template");

const productsData = JSON.parse(
    document.getElementById("products_json").textContent
);

function renderProducts(productsToRender) {
    productsContainer.innerHTML = "";

    productsToRender.forEach(product => {
        const productClone = productTemplate.content.cloneNode(true);

        productClone.querySelector(".product-name").textContent = product.title;
        productClone.querySelector(".product-price").textContent = `Price: ${product.price}₴`;
        productClone.querySelector(".image-container").textContent = `${product.title} image`;
        productClone.querySelector(".details-btn").setAttribute("href", `/products/${product.id}`);
        productClone.querySelector(".update-btn").setAttribute("href", `/products/update/${product.id}`);
        productClone.querySelector(".delete-btn").setAttribute("href", `/products/delete/${product.id}`);
        productClone.querySelector(".add-btn").setAttribute("href", `/cart/add/${product.id}/`);
        productsContainer.appendChild(productClone);
    })
}

renderProducts(productsData);

function filterProductsByCategory(category) {
    const filteredProducts = productsData.filter(product => product.category == category);
    renderProducts(filteredProducts);
};

categoriesBtn.forEach(button => {
    button.addEventListener("click", () => {
        targetCategory = button.getAttribute("data-category");
        filterProductsByCategory(targetCategory);
    });
});