import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getProductDetail } from "../../../Services/backend/product";
import { Button, Flex, Tabs } from "antd";
import { useDispatch, useSelector } from "react-redux";
import { addToCart } from "../../../actions/cart";

function ProductDetail() {

    const params = useParams();
    const [product, setProduct] = useState();

    const dispatch = useDispatch();
    const cart = useSelector(state => state.cartReducer);

    const handleAddToCart = () => {
        if (cart.some(itemCart => itemCart.id === params.id)) {
            // dispatch(updateQuantity(item.id));
        } else {
            dispatch(addToCart(params.id, params));
        }
    }

    useEffect(() => {
        const fetchAPI = async () => {
            const response = await getProductDetail(params.id); 
            setProduct(response);
        };
        fetchAPI();
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    return (
        <>
            {product && (
                <>
                    <h1 style={{ margin: 20 }}>{product.name}</h1>

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

                            <Button type="primary" >Mua ngay</Button>
                            <Button onClick={handleAddToCart}>Thêm vào giỏ hàng</Button>
                        </div>
                    </Flex>
                </>
            )}
        </>
    )
}

export default ProductDetail;