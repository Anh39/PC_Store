import { Table } from "antd";
import { useEffect, useState } from "react";
import { getHistory } from "../../Services/backend/transaction";

function History() {
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchAPI = async () => {
            const result = await getHistory();
            setData(result);
        }
        fetchAPI();
    }, []);

    console.log(data[0].items);

    const columns = [
        {
            title: "ID",
            dataIndex: "id",
            key: "id"
        },
        {
            title: "Ảnh",
            dataIndex: "thumbnail",
            key: "thumbnail",
            render: (text) => <img src={text} style={{width: 100}} alt={text} />
        },
        {
            title: "Tên",
            dataIndex: "name",
            key: "name"
        },
        {
            title: "Đơn giá",
            dataIndex: "price",
            key: "price"
        },
        {
            title: "Số lượng",
            dataIndex: "amount",
            key: "amount"
        }
    ]
    return (
        <>
            <Table dataSource={data && (data[0].items)} columns={columns}/>
        </>
    )
}

export default History;