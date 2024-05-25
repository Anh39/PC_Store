import { Button, Card, Col, Form, Input, Row, message } from "antd";
import { useNavigate } from "react-router-dom";
import { change_user_info } from "../../Services/backend/user_info";

function ResetPassword() {
    const navigate = useNavigate();
    const rules = [
        {
            required: true,
            message: 'Bắt buộc!'
        }
    ];

    const onFinish = async (e) => {
        console.log(e);

        if (e.newPassword !== e.repeateNewPassword) {
            message.error("Mật khẩu mới và viết lại mật khẩu mới không khớp");
            return;
        }

        const response = await change_user_info(e.oldPassword, e.newPassword);

        if (response) {
            message.success("Đặt lại mật khẩu thành công");
            navigate("/");
        } else {
            message.error("Đặt lại mật khẩu thất bại");
        }
    }
    return (
        <>
            <Row justify="center">
                <Col span={12}>
                    <Card title="Đặt lại mật khẩu">
                        <Form onFinish={onFinish}>
                            <Form.Item label="Mật khẩu cũ" name="oldPassword" rules={rules} >
                                <Input.Password />
                            </Form.Item>
                            <Form.Item label="Mật khẩu mới" name="newPassword" rules={rules} >
                                <Input.Password />
                            </Form.Item>
                            <Form.Item label="Viết lại mật khẩu mới" name="repeateNewPassword" rules={rules} >
                                <Input.Password />
                            </Form.Item>
                            <Form.Item>
                                <Button type="primary" htmlType="submit">
                                    Đặt lại mật khẩu
                                </Button>
                            </Form.Item>
                        </Form>
                    </Card>
                </Col>
            </Row>
        </>
    )
}

export default ResetPassword;