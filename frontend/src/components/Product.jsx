import React from "react";
import "../styles/Product.css";
import { useNavigate } from "react-router-dom";
import { auth_api } from "../api";
import { ACCESS_TOKEN } from "../constants";

function Product({ Product }) {
  const navigate = useNavigate();
  const addToCart = (e) => {
    e.preventDefault();
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (!token) {
      navigate("/login");
    }
    else {
      auth_api.post("/cart/", {
        product: Product.id,
      });  
    }
    
  };

  return (
    <div className="product-container">
      <p className="product-name">{Product.name}</p>
      <p className="product-price">{Product.price}</p>
      <p className="product-description">{Product.description}</p>
      <button className="add-to-cart" onClick={addToCart}>
        Add to Cart
      </button>
    </div>
  );
}

export default Product;
