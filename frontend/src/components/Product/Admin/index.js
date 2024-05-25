import { useState } from "react";
import CreateProduct from "./CreateProduct";
import "./manageProduct.css";
import ProductList from "./ProductList";

function Product() {
    const [reload, setReload] = useState(false);

    const handleReload = () => {
        setReload(!reload);
    }
    
    return (
        <>
            <h2>Danh sách sản phẩm</h2>
            <CreateProduct onReload={handleReload}/>
            <ProductList reload={reload}/>
        </>
    )   
}

export default Product;