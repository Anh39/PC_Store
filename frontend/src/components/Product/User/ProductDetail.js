import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getProductDetail } from "../../../Services/productService";
import { Flex, Tabs } from "antd";

function ProductDetail() {

    const params = useParams();
    const [product, setProduct] = useState();

    useEffect(() => {
        const fetchAPI = async () => {
            const response = await getProductDetail(params.id);
            const data = {
                ...response,
            };
            setProduct(data);
        };
        fetchAPI();
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    return (
        <>
            {product && (
                <>
                    <h1 style={{ margin: 20 }}>{product.title}</h1>

                    <Flex >
                        <div className="Tabs">
                            <Tabs
                                tabPosition="bottom"
                                items={product.images.map((image, index) => {
                                    const id = String(index + 1);
                                    return {
                                        label: `Hình ${id} `,
                                        key: id,
                                        children: <div className="image" >
                                            <img src={image} alt="nothing" />
                                        </div>,
                                    };
                                })}
                            />
                        </div>
                        <div style={{ margin: 20 }}>
                            <p><strong>Mô tả:</strong> {product.description}</p>
                            <p><strong>Hãng:</strong> {product.brand}</p>
                            <p><strong>Loại:</strong> {product.category}</p>
                            <p><strong>Còn lại:</strong> {product.stock}</p>
                        </div>
                    </Flex>
                </>
            )}
        </>
    )
}

export default ProductDetail;