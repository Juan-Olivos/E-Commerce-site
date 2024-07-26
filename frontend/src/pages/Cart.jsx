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
            .get("/user/cart/")
            .then((res) => res.data)
            .then((data) => {
                setItems(data);
                console.log(data);
            })
            .catch((err) => alert(err));
    }

  return (
    <div>
      <div>
        <h2>Test Items</h2>
        {items.map((item) => (
          <CartItem Item={item} key={item.id}></CartItem>
        ))}
      </div>
    </div>
  );
}

export default Home;
