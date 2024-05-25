import { useEffect, useState } from "react";
import { getProductList } from "../../../Services/backend/product";
import ProductItem from "./ProductItem";
import "./DisplayProduct.scss";

function Product() {

    const [product, setProduct] = useState([]);

    useEffect(() => {
        const fetchAPI = async () => {
            const data = await getProductList();
            setProduct(data);
        }
        fetchAPI();
    }, []);

    return (
        <>
            <div className="product">
                {product.map(item => (
                    <ProductItem item={item} key={item.id} />
                ))}
            </div>
        </>
    )
}

export default Product;