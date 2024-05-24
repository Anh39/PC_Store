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
                                        label: `H${id} `,
                                        key: id,
                                        children: <div className="image" >
                                            <img src={image} alt="nothing" />
                                        </div>,
                                    };
                                })}
                            />
                        </div>
                        <div style={{ margin: 20 }}>
                            <ul>
                                <h4>Thông tin cơ bản</h4>
                                {product.basic_infos.map((item, index) => (
                                    <li key={index}>{item}</li>
                                ))}
                            </ul>
                            <div className="product__price-new">
                                {product.price} VND
                            </div>
                            <div className="product__price-old">{product.full_price}</div>

                            <Button type="primary" >Mua ngay</Button>
                            <Button onClick={handleAddToCart}>Thêm vào giỏ hàng</Button>
                        </div>
                        <div>
                            {product.detail_infos.map((item, index) => (
                                <li key={index}>{item}</li>
                            ))}
                        </div>
                    </Flex>

                    <div style={{ margin: 20 }}>
                        <h2>Giới thiệu</h2>
                        <p>
                            { }
                        </p>
                    </div>
                </>
            )}
        </>
    )
}

export default ProductDetail;