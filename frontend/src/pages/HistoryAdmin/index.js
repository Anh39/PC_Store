import { Table } from "antd";
import { useEffect, useState } from "react";
import { getHistory } from "../../Services/backend/transaction";

function HistoryAdmin() {
    const [data, setData] = useState([]);

    const fetchAPI = async () => {
        const result = await getHistory();
        const updatedData = result.map(order => {
            const total = order.items.reduce((sum, item) => sum + item.price, 0);
            return { ...order, total }; // Thêm tổng giá tiền vào dữ liệu
        });

        setData(updatedData);
    }

    useEffect(() => {
        fetchAPI();
    }, []);

    console.log(data);

    const columns = [
        {
            title: 'User ID',
            dataIndex: 'user_id',
            key: 'id',
        },
        {
            title: 'Thời gian tạo',
            dataIndex: 'time_created',
            key: 'time_created',
        },
        {
            title: 'Tổng giá',
            dataIndex: 'total',
            key: 'total',
        },
        {
            title: 'Trạng thái',
            dataIndex:'status',
            key:'status',
        },
    ]

    return (
        <>
            <Table dataSource={data && (data)} columns={columns}/>
        </>
    )
}

export default HistoryAdmin;