/* eslint-disable no-unused-vars */
import { useEffect, useState } from "react";
import { Button, Form, Input, InputNumber, Modal, Select, Spin, notification } from "antd";
import { editProduct } from "../../../Services/productService";
import { EditOutlined } from "@ant-design/icons";
import { getCategoryList } from "../../../Services/categoryService";

const { Option } = Select;

function EditProduct(props) {
    const { item, onReload } = props;
    const [form] = Form.useForm();
    const [showModal, setShowModal] = useState(false);
    const [api, contextHolder] = notification.useNotification();
    const [data, setData] = useState(item);
    const [dataCategory, setDataCategory] = useState([]);
    const [spinning, setSpinning] = useState(false);

    const rules = [
        {
            required: true,
            message: "bắt buộc"
        }
    ];

    useEffect(() => {
        const fetchApi = async () => {
            const category = await getCategoryList();
            setDataCategory(category);
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

    const handleSubmit = async (e) => {
        setSpinning(true);
        const result = await editProduct(item.id, data);
        setTimeout(() => {
            if (result) {
                api.success({
                    message: "Cập nhật sản phẩm thành công"
                });
                setShowModal(false);
                onReload();
            } else {
                api.error({
                    message: "Cập nhật phòng thất bại"
                });
            }
            setSpinning(false);
        }, 3000);
    }
    return (
        <>
            {contextHolder}
            <Button type="primary" onClick={openModal}>
                <EditOutlined />
            </Button>

            <Modal
                open={showModal}
                onCancel={closeModal}
                style={customStyles}
                footer={null}
            >
                <Spin spinning={spinning} tip="Đang cập nhật">
                    <Form
                        layout="vertical"
                        name="update-room"
                        onFinish={handleSubmit}
                        form={form}
                        initialValues={data}
                    >
                        <Form.Item
                            name="title"
                            label="Tiêu đề"
                        >
                            <Input defaultValue={data.title} />
                        </Form.Item>

                        <Form.Item
                            name="price"
                            label="Giá"
                            rules={rules}
                        >
                            <InputNumber min={1} defaultValue={data.price} />
                        </Form.Item>

                        <Form.Item
                            name="discountPercentage"
                            label="Giảm giá"
                            rules={rules}
                        >
                            <InputNumber min={1} defaultValue={data.discountPercentage} />
                        </Form.Item>

                        <Form.Item
                            name="stock"
                            label="Số lượng còn lại"
                            rules={rules}
                        >
                            <InputNumber min={1} defaultValue={data.stock} />
                        </Form.Item>

                        <Form.Item
                            name="thumbnail"
                            label="Đương dẫn ảnh"
                        >
                            <Input defaultValue={data.thumbnail} />
                        </Form.Item>

                        <Form.Item name="category" label="Danh mục">
                            <Select defaultValue={data.category}>
                                {dataCategory.map((item, index) => (
                                    <Option key={index}>{item}</Option>
                                ))}
                            </Select>
                        </Form.Item>

                        <Form.Item
                            name="description"
                            label="Mô tả"
                        >
                            <Input.TextArea showCount maxLength={10000} />
                        </Form.Item>

                        <Form.Item>
                            <Button type="primary" htmlType="Submit" >Cập nhật</Button>
                        </Form.Item>
                    </Form>
                </Spin>
            </Modal>
        </>
    )
}

export default EditProduct;