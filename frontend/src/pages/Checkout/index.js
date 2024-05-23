import { Card, Col, Form, Input, Row } from "antd";

const { Item } = Form;

function Checkout() {

    const rules = [
        {
            required: true,
            message: 'Bắt buộc!'
        }
    ]

    const onFinish = (e) => {

    }
    return (
        <>
            <Row justify="center">
                <Col span={12}>
                    <Card title="Thanh toán">
                        <Form onFinish={onFinish} layout="vertical">
                            <Item label="Tên" name="name" rules={rules}>
                                <Input />
                            </Item>
                            <Item label="Số điện thoại" name="phone" rules={rules}>
                                <Input />
                            </Item>
                            <Item label="Email" name="email" rules={rules}>
                                <Input />
                            </Item>

                            <Item label="Địa chỉ" name="address" rules={rules}>
                                <Input.Password />
                            </Item>

                            <Item>
                                
                            </Item>
                        </Form>
                    </Card>
                </Col>
            </Row>
        </>
    )
}

export default Checkout;