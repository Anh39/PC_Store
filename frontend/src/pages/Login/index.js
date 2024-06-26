import { Button, Card, Col, Form, Input, Row } from "antd";
import { login } from "../../Services/userService";
import { useNavigate } from "react-router-dom";
import { setCookie } from "../../helpers/cookie";
import { useDispatch } from "react-redux";
import { checkLogin } from "../../actions/login";

function Login() {
    const navigate = useNavigate();
    const dispatch = useDispatch();

    const rules = [
        {
            required: true,
            message: 'Bắt buộc!'
        }
    ];

    const onFinish = async (e) => {
        const response = await login(e.email, e.password);
        // if (response.length > 0) {
        //     console.log(response);
        //     setCookie("id", response[0].id, 1);
        //     setCookie("username", response[0].username, 1);
        //     setCookie("email", response[0].email, 1);
        //     setCookie("token", response[0].token, 1);
        //     dispatch(checkLogin(true));
        //     navigate("/");
        // } else {
        //     alert("Login failed");
        // }
        if (response.success) {
            console.log(response);
            setCookie("token", response.token, 1);
            dispatch(checkLogin(true));
            navigate("/");
        } else {
            alert("Login failed");
        }
    }

    return (
        <>
            <Row justify="center">
                <Col span={12}>
                    <Card title="Đăng nhập">
                        <Form onFinish={onFinish} layout="vertical">
                            <Form.Item label="Email" name="email" rules={rules}>
                                <Input />
                            </Form.Item>

                            <Form.Item label="Password" name="password" rules={rules}>
                                <Input.Password />
                            </Form.Item>

                            <Form.Item>
                                <Button type="primary" htmlType="submit">
                                    Đăng nhập
                                </Button>
                            </Form.Item>
                        </Form>
                    </Card>
                </Col>
            </Row>
        </>
    )
}

export default Login;