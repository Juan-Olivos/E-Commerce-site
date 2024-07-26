import React from "react";
import "../styles/CartItem.css"

function CartItem({ Item }) {

    return (
        <div className="CartItem-container">
            <p className="CartItem-title">{Item.title}</p>
            
            {/* <button className="delete-button" onClick={() => onDelete(CartItem.id)}>
                Delete
            </button> */}
        </div>
    );
}

export default CartItem;