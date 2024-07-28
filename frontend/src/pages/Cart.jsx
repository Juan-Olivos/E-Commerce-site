import { useState, useEffect } from "react";
import api from "../api";
import "../styles/Home.css";
import CartItem from "./CartItem";

function Home() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    getItems();
  }, []);

  const getItems = () => {
    api
      .get("/cart/")
      .then((res) => res.data)
      .then((data) => {
        setItems(data);
        console.log(data);
      })
      .catch((err) => alert(err));
  };

  const onIncrement = (id) => {
    api
      .patch(`/cart/update/${id}`, { action: "add" })
      .then((res) => {
        if (res.status === 200);
        else alert("Failed to update item.");
        getItems();
      })
      .catch((error) => alert(error));
  };

  const onDecrement = (id) => {
    api
      .patch(`/cart/update/${id}`, { action: "sub" })
      .then((res) => {
        if (res.status === 200);
        else alert("Failed to update item.");
        getItems();
      })
      .catch((error) => alert(error));
  };

  const deleteCartItem = (id) => {
    api
      .delete(`/cart/delete/${id}`)
      .then((res) => {
        if (res.status === 204);
        else alert("Failed to delete item.");
        getItems();
      })
      .catch((error) => alert(error));
  };

  return (
    <div>
      <div>
        <h2>Cart items</h2>
        {items.map((item) => (
          <CartItem
            Item={item}
            onDelete={deleteCartItem}
            onIncrement={onIncrement}
            onDecrement={onDecrement}
            key={item.id}
          ></CartItem>
        ))}
      </div>
    </div>
  );
}

export default Home;
