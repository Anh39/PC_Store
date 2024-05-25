/* eslint-disable no-unused-vars */
import { useEffect, useState } from "react";
import { Button, Form, Input, InputNumber, Modal, Select, Space, Spin, notification } from "antd";
import { editProduct } from "../../../Services/productService";
import { EditOutlined } from "@ant-design/icons";
import { getCategoryList, getProductDetail } from "../../../Services/backend/product";
import { MinusCircleOutlined, PlusOutlined } from "@ant-design/icons";

const { Option } = Select;

function EditProduct(props) {
    const { item, onReload } = props;
    const [form] = Form.useForm();
    const [showModal, setShowModal] = useState(false);
    const [api, contextHolder] = notification.useNotification();
    const [dataCategory, setDataCategory] = useState([]);
    const [spinning, setSpinning] = useState(false);

    const [product, setProduct] = useState();

    const rules = [
        {
            required: true,
            message: "bắt buộc"
        }
    ];

    useEffect(() => {
        const fetchApi = async () => {
            const category = await getCategoryList();
            const productDetail = await getProductDetail(item.id);
            setDataCategory(category);
            setProduct(productDetail);
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
        form.resetFields(); 
    }

    const handleSubmit = async (e) => {
        console.log(e);
        // setSpinning(true);
        // const result = await editProduct(item.id, e);
        // setTimeout(() => {
        //     if (result) {
        //         form.resetFields();
        //         api.success({
        //             message: "Cập nhật sản phẩm thành công"
        //         });
        //         setShowModal(false);
        //         onReload();
        //     } else {
        //         api.error({
        //             message: "Cập nhật sản phẩm thất bại"
        //         });
        //     }
        //     setSpinning(false);
        // }, 100);
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
                    {product && (<Form
                        layout="vertical"
                        name="update-room"
                        onFinish={handleSubmit}
                        form={form}
                        initialValues={product}
                    >
                        <Form.Item
                            name="title"
                            label="Tiêu đề"
                        >
                            <Input defaultValue={product.name} />
                        </Form.Item>

                        <Form.Item
                            name="price"
                            label="Giá"
                        >
                            <InputNumber min={1} defaultValue={product.price} />
                        </Form.Item>

                        <Form.List name="images" preserve={false}>
                            {(fields, { add, remove }) => (
                                <>
                                    {fields.map((value, index) => (
                                        <Space style={{ display: 'flex', marginBottom: 8 }} align="baseline">
                                            <Form.Item
                                                name={`${index}`}
                                                label={index === 0 ? 'Hình ảnh' : ''}
                                            >
                                                <Input style={{ width: 450 }} placeholder="url" defaultValue={product.images[index]} />
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

                        <Form.Item name="category" label="Danh mục">
                            <Select defaultValue={product.category}>
                                {dataCategory.map((item, index) => (
                                    <Option key={index}>{item}</Option>
                                ))}
                            </Select>
                        </Form.Item>

                        <Form.List name="basic_infos">
                            {(fields, { add, remove }) => (
                                <>
                                    {fields.map((value, index) => (
                                        <Space style={{ display: 'flex', marginBottom: 8 }} align="baseline">
                                            <Form.Item
                                                name={`${index}`}
                                                label={index === 0 ? 'Thông tin' : ''}
                                            >
                                                <Input style={{ width: 450 }} placeholder="Information" defaultValue={product.basic_infos[index]} />
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
                            <Button type="primary" htmlType="Submit" >Cập nhật</Button>
                        </Form.Item>
                    </Form>)}
                </Spin>
            </Modal>
        </>
    )
}

export default EditProduct;