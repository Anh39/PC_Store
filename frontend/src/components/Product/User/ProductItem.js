import { useDispatch, useSelector } from "react-redux";
import { addToCart } from "../../../actions/cart";
import { Card } from "antd";
import { useNavigate } from "react-router-dom";

function ProductItem(props) {
    const { item } = props;
    const navigate = useNavigate();

    const dispatch = useDispatch();
    const cart = useSelector(state => state.cartReducer);

    const handleAddToCart = () => {
        if (cart.some(itemCart => itemCart.id === item.id)) {
            // dispatch(updateQuantity(item.id));
        } else {
            dispatch(addToCart(item.id, item));
        }
    }

    const ToDetail = () => {
        navigate(`/product/${item.id}`)
    }

    return (
        <>
            <Card
                hoverable
                bordered={false}
                size="small"
                onClick={ToDetail}
                cover={<img className="product__image mb-5" src={item.thumbnail} alt={item.title} />}
            >
                <h4 className="product__title mb-5">{item.title}</h4>
                <div className="product__price-new mb-5">
                    {(item.price * (100 - item.discountPercentage) / 100).toFixed(0)}$
                </div>
                <div className="product__price-old mb-5">{item.price}$</div>
                <div className="product__percent mb-5">{item.discountPercentage}%</div>
                <button >Mua ngay</button>
                <button onClick={handleAddToCart}>Thêm vào giỏ hàng</button>
            </Card>
        </>
    )
}

export default ProductItem;