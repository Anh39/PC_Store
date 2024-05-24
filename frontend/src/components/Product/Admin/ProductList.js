import { useEffect, useState } from "react";
import EditProduct from "./EditProduct";
import DeleteProduct from "./DeleteProduct";
import { getProductList } from "../../../Services/backend/product";

function ProductList(props) {
    const { reload } = props;
    const [data, setData] = useState([]);
    const [editRedload, setEditRedload] = useState(false);

    const handleReload = () => {
        setEditRedload(!editRedload);
    }

    useEffect(() => {
        const fetchAPI = async () => {
            const result = await getProductList();
            setData(result);
        }

        fetchAPI();
    }, [reload, editRedload]);

    return (
        <>
            <div className="product__list">
                {data.map(item => (
                    <div className="product__item" key={item.index}>
                        <img className="product__img" src={item.thumbnail} alt={item.title} />
                        <h4 className="product__title">{item.name}</h4>
                        <div className="product__price">{item.price}đ</div>
                        <EditProduct item={item} onReload={handleReload} />
                        <DeleteProduct item={item} onReload={handleReload} />
                    </div>
                ))}
            </div>
        </>
    )
}

export default ProductList;