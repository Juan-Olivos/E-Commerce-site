import React from "react";
import "../styles/CartItem.css"

function CartItem({ Item }) {

    return (
        <div className="CartItem-container">
            <p className="CartItem-title">{Item.product.name}</p>
            <p className="CartItem-title">{Item.quantity}</p>
            
            {/* <button className="delete-button" onClick={() => onDelete(CartItem.id)}>
                Delete
            </button> */}
        </div>
    );
}

export default CartItem;