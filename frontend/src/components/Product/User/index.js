import { useEffect, useState } from "react";
import { getProductList } from "../../../Services/productService";
import ProductItem from "./ProductItem";
import "./DisplayProduct.scss";
import { Col, Row } from "antd";

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
                <Row gutter={[10, 20]}>
                    {product.map(item => (
                        <Col span={6}>
                            <ProductItem item={item} key={item.id} />
                        </Col>
                    ))}
                </Row>
            </div>
        </>
    )
}

export default Product;