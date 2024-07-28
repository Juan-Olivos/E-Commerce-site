import React from "react";
import "../styles/CartItem.css"
import api from "../api";

function CartItem({ Item, onDelete, onIncrement, onDecrement }) {


    return (
        <div className="CartItem-container">
            <p className="CartItem-title">Product Name: {Item.product_name}</p>
            <p className="CartItem-title">Quantity: {Item.quantity}</p>
            <button className="increment-quantity" onClick={() => onIncrement(Item.id)}>Increment</button>
            <button className="decrement-quantity" onClick={() => onDecrement(Item.id)}>Decrement</button>
            <button className="delete-button" onClick={() => onDelete(Item.id)}>Delete</button>
        </div>
    );
}

export default CartItem;