import { useEffect, useState } from "react";
import { getCategoryProduct } from "../../Services/backend/product";
import ProductItem from "../../components/Product/User/ProductItem";

function Laptop() {
    const [laptop, setLaptop] = useState();

    useEffect(() => {
        const fetchAPI = async () => {
            const data = await getCategoryProduct('laptop');
            setLaptop(data);
            console.log(data);
        }
        fetchAPI();
    }, []);

    return (
        <>
            {laptop && (
                <div className="product">
                    {laptop.map((item, index) => (
                        <ProductItem item={item} />
                    ))}
                </div>
            )}
        </>
    )
}

export default Laptop;