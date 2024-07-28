import { useState, useEffect } from "react";
import api from "../api";
import "../styles/Home.css";
import Product from "../components/Product";

function Home() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    getProducts();
  }, []);

  const getProducts = () => {
    api
      .get("/products/list/")
      .then((res) => res.data)
      .then((data) => {
        setProducts(data);
        console.log(data);
      })
      .catch((err) => alert(err));
  };

  return (
    <div>
      <div>
        <h2>Products</h2>
        {products.map((product) => (
          <Product Product={product} key={product.id}></Product>
        ))}
      </div>
    </div>
  );
}

export default Home;
