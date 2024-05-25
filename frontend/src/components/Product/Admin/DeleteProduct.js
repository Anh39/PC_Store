import { Button, Popconfirm } from "antd";
import { DeleteOutlined } from "@ant-design/icons";
import { deleteProduct } from '../../../Services/productService';

function DeleteProduct(props) {
    const { item, onReload } = props;

    const deleteItem = async () => {
        const result = await deleteProduct(item.id);
        if (result) {
            onReload();
            alert("Xóa sản phẩm thành công");
        } else {
            alert("Xóa sản phẩm thất bại");
        }
    }

    const handleDelete = () => {
        deleteItem();
    }

    return (
        <>
            <Popconfirm title="Bạn có chắc muốn xóa không" onConfirm={handleDelete}>
                <Button danger icon={<DeleteOutlined />} />
            </Popconfirm>
        </>
    )
}

export default DeleteProduct;