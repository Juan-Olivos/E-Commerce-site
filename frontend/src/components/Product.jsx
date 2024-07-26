import React from "react";
import "../styles/Product.css"

function Product({ Product }) {

    return (
        <div className="product-container">
            <p className="product-name">{Product.name}</p>
            <p className="product-price">{Product.price}</p>
            <p className="product-description">{Product.description}</p>
            
            {/* <button className="delete-button" onClick={() => onDelete(Product.id)}>
                Delete
            </button> */}
        </div>
    );
}

export default Product