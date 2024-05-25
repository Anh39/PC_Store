import { useEffect, useState } from "react";
import { getCategoryProduct } from "../../Services/backend/product";
import ProductItem from "../../components/Product/User/ProductItem";

function Auxility() {
    const [auxility, setAuxility] = useState();

    useEffect(() => {
        const fetchAPI = async () => {
            const data = await getCategoryProduct('auxility');
            setAuxility(data);
            console.log(data);
        }
        fetchAPI();
    }, []);

    return (
        <>
            {auxility && (
                <div className="product">
                    {auxility.map((item, index) => (
                        <ProductItem item={item} />
                    ))}
                </div>
            )}
        </>
    )
}

export default Auxility;