import { useEffect, useState } from "react";
import { Button, Form, Input, InputNumber, Modal, Select, Space, message } from "antd";
import { getCategoryList } from "../../../Services/backend/product";
import { createProduct } from "../../../Services/backend/product";
import { MinusCircleOutlined, PlusOutlined } from "@ant-design/icons";

const { Option } = Select;

function CreateProduct(props) {
    const { onReload } = props;
    const [showModal, setShowModal] = useState(false);
    const [dataCategory, setDataCategory] = useState([]);
    const [form] = Form.useForm();
    const [messageApi, contextHolder] = message.useMessage();

    const handleSubmit = async (data) => {
        console.log(data);
        // const product_id = await createProduct(data);
        // if (product_id != null) {
        //     console.log(product_id);
        //     form.resetFields();
        //     messageApi.open({
        //         type: 'success',
        //         content: "Tạo mới sản phẩm thành công"
        //     });
        //     onReload();
        // } else {
        //     messageApi.open({
        //         type: 'error',
        //         content: "Tạo phòng thất bại"
        //     });
        // }
    }

    const rules = [
        {
            required: true,
            message: "bắt buộc"
        }
    ];

    useEffect(() => {
        const fetchApi = async () => {
            const result = await getCategoryList();
            console.log(result);
            setDataCategory(result);
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
                        name="stock"
                        label="Số lượng còn lại"
                    >
                        <InputNumber min={1} />
                    </Form.Item>

                    <Form.Item name="category" label="Danh mục">
                        <Select>
                            {dataCategory.map((item, index) => (
                                <Option key={index} value={item}>{item}</Option>
                            ))}
                        </Select>
                    </Form.Item>

                    <Form.List name="images" preserve={false} label="Link hình ảnh">
                        {(fields, { add, remove }) => (
                            <>
                                {fields.map((value, index) => (
                                    <Space style={{ display: 'flex', marginBottom: 8 }} align="baseline">
                                        <Form.Item
                                            name={`${index}`}
                                            label={index === 0 ? 'Hình ảnh' : ''}
                                        >
                                            <Input style={{ width: 450 }} placeholder="url" />
                                        </Form.Item>
                                        <MinusCircleOutlined onClick={() => remove(index)} />
                                    </Space>
                                ))}
                                <Form.Item>
                                    <Button type="dashed" onClick={() => add()} block icon={<PlusOutlined />}>
                                        Thêm
                                    </Button>
                                </Form.Item>
                            </>
                        )}
                    </Form.List>

                    <Form.List name="basic_infos" preserve={false}>
                        {(fields, { add, remove }) => (
                            <>
                                {fields.map((value, index) => (
                                    <Space style={{ display: 'flex', marginBottom: 8 }} align="baseline">
                                        <Form.Item
                                            name={`${index}`}
                                            label={index === 0 ? 'Thông tin' : ''}
                                        >
                                            <Input style={{ width: 450 }} placeholder="Information" />
                                        </Form.Item>
                                        <MinusCircleOutlined onClick={() => remove(index)} />
                                    </Space>
                                ))}
                                <Form.Item>
                                    <Button type="dashed" onClick={() => add()} block icon={<PlusOutlined />}>
                                        Thêm
                                    </Button>
                                </Form.Item>
                            </>
                        )}
                    </Form.List>

                    <Form.Item>
                        <Button type="primary" htmlType="Submit" >Tạo mới</Button>
                    </Form.Item>
                </Form>

            </Modal>
        </>
    )
}

export default CreateProduct;