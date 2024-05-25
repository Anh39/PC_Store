import { useEffect, useState } from "react";
import { getCategoryProduct } from "../../Services/backend/product";
import ProductItem from "../../components/Product/User/ProductItem";

function PC() {
    const [pc, setPC] = useState();

    useEffect(() => {
        const fetchAPI = async () => {
            const data = await getCategoryProduct('pc');
            setPC(data);
            console.log(data);
        }
        fetchAPI();
    }, []);
    
    return (
        <>
            {pc && (
                <div className="product">
                    {pc.map((item, index) => (
                        <ProductItem item={item} />
                    ))}
                </div>
            )}
        </>
    )
}

export default PC;