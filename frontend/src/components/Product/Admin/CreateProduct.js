import { useEffect, useState } from "react";
import { Button, Form, Input, InputNumber, Modal, Select, message } from "antd";
import { getCategoryList } from "../../../Services/categoryService";
import { createProduct } from "../../../Services/backend/product";

const { Option } = Select;

function CreateProduct(props) {
    const { onReload } = props;
    const [showModal, setShowModal] = useState(false);
    const [dataCategory, setDataCategory] = useState([]);
    const [form] = Form.useForm();
    const [messageApi, contextHolder] = message.useMessage();

    const handleSubmit = async (data) => {
        const product_id = await createProduct(data);
        if (product_id != null) {
            console.log(product_id);
            form.resetFields();
            messageApi.open({
                type: 'success',
                content: "Tạo mới sản phẩm thành công"
            });
            onReload();
        } else {
            messageApi.open({
                type: 'error',
                content: "Tạo phòng thất bại"
            });
        }
    }

    const rules = [
        {
            required: true,
            message: "bắt buộc"
        }
    ];

    useEffect(() => {
        const fetchApi = async () => {
            // const result = await getCategoryList();
            // console.log(result);
            // setDataCategory(result);
        }

        fetchApi();
    }, []);

    const customStyles = {
        content: {
            top: '50%',
            left: '50%',
            right: 'auto',
            bottom: 'auto',
            marginRight: '-50%',
            transform: 'translate(-50%, -50%)',
        },
    };

    const openModal = () => {
        setShowModal(true);
    }

    const closeModal = () => {
        setShowModal(false);
    }
    return (
        <>
            {contextHolder}

            <Button onClick={openModal} required>Tạo sản phẩm mới</Button>

            <Modal
                open={showModal}
                onCancel={closeModal}
                style={customStyles}
            >
                <Form layout="vertical" name="create-room" onFinish={handleSubmit} form={form}>
                    <Form.Item
                        name="name"
                        label="Tiêu đề"
                        rules={rules}
                    >
                        <Input />
                    </Form.Item>

                    <Form.Item
                        name="price"
                        label="Giá"
                        rules={rules}
                    >
                        <InputNumber min={1} />
                    </Form.Item>

                    <Form.Item
                        name="discountPercentage"
                        label="Tỉ lệ giảm giá"
                        rules={rules}
                    >
                        <InputNumber min={0} />
                    </Form.Item>


                    <Form.Item
                        name="stock"
                        label="Số lượng còn lại"
                    >
                        <InputNumber min={1} />
                    </Form.Item>

                    <Form.Item name="category" label="Danh mục">
                        <Select>
                            {dataCategory.map((item, index) => (
                                <Option key={index}>{item}</Option>
                            ))}
                        </Select>
                    </Form.Item>
                    
                    <Form.Item
                        name="thumbnail"
                        label="Đường dẫn ảnh"
                    >
                        <Input.TextArea showCount maxLength={10000} />
                    </Form.Item>
                    <Form.Item
                        name="description"
                        label="Mô tả"
                    >
                        <Input.TextArea showCount maxLength={10000} />
                    </Form.Item>
                    <Form.Item>
                        <Button type="primary" htmlType="Submit" >Tạo mới</Button>
                    </Form.Item>
                </Form>
                
            </Modal>
        </>
    )
}

export default CreateProduct;