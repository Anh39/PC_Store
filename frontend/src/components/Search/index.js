/* eslint-disable no-unused-vars */
/* eslint-disable react-hooks/exhaustive-deps */
import { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { getProductList } from "../../Services/productService";
import { Tag } from "antd";
import SearchList from "./SearchList";
import "../Product/User/DisplayProduct.scss";

function Search() {
    const [searchParams, setSearchParams] = useSearchParams();
    const [data, setData] = useState();
    const keywordSearch = searchParams.get("keyword") || '';

    const fetchAPI = async () => {
        const response = await getProductList();
        if (response) {
            const newData = response.filter((item) => {
                const keyword = item.title.toLowerCase();
                const searchKeyword = keywordSearch.toLowerCase();  
                return keyword.includes(searchKeyword);
            });
            setData(newData);
        }

    };

    useEffect(() => {
        fetchAPI();
    }, []);

    const Reload = () => {
        fetchAPI();
    }

    return (
        <>
            <div>
                <strong>Kết quả tìm kiếm:</strong>
                {keywordSearch && <Tag>{keywordSearch}</Tag>}
            </div>
            {data && (
                <SearchList data={data} onReload={Reload}/>
            )}
        </>
    )
}

export default Search;