import React from "react";
import "../styles/Product.css";
import api from "../api";

function Product({ Product }) {

    const product_id = Product.product;
    const addToCart = (e) => {
        e.preventDefault();
        api
            .post("/cart/", {
                product: Product.id,
            })
  };

  return (
    <div className="product-container">
      <p className="product-name">{Product.name}</p>
      <p className="product-price">{Product.price}</p>
      <p className="product-description">{Product.description}</p>
      <button className="add-to-cart" onClick={addToCart}>Add to Cart</button> 
      {/* <button className="delete-button" onClick={() => onDelete(Product.id)}>
                Delete
            </button> */}
    </div>
  );
}

export default Product;
