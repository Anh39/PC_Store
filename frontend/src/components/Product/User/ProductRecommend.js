/* eslint-disable react-hooks/exhaustive-deps */
import { useEffect, useState } from "react";
import { recommendProduct } from "../../../Services/backend/recommend";
import { Link, useNavigate } from "react-router-dom";

function ProductRecommend(props) {
    const { id } = props;
    const navigate = useNavigate();
    const [recommend, setRecommend] = useState([]);
    const fetchAPI = async () => {
        try {
            const response = await recommendProduct(id);
            if (response.length > 0) {
                setRecommend(response);
            }
        } catch (error) {
            console.error("Failed to fetch recommendations:", error);
        }
    }

    useEffect(() => {
        fetchAPI();
    }, [id]);

    const ToDetail = (id) => {
        navigate(`/product/${id}`);
    }

    return (
        <>
            <div className="product">
                {recommend && (recommend.map((item, index) => (
                    <div className="product__item" key={item.index}>
                        <div>
                            <img className="product__img" src={item.thumbnail} alt={item.title} onClick={() => ToDetail(item.id)} />
                            <h4 className="product__title"> <Link to={`/product/${item.id}`}>{item.name}</Link></h4>
                        </div>
                        <div>
                            <div className="product__price-new">{item.price}đ</div>
                            <div className="product__price-old">{item.full_price}</div>
                        </div>
                    </div>
                )))}
            </div>
        </>
    )
}

export default ProductRecommend;