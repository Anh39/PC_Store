import { Button, Dropdown, Input, Form, Row, Col } from "antd";
import { UnorderedListOutlined, LaptopOutlined, RightOutlined } from "@ant-design/icons";
import { Link } from "react-router-dom";
import { useSelector } from "react-redux";
import CartMini from "../components/CartMini";

// Laptop gaming, đồ họa

function Header(props) {
    const { token } = props;
    const isLogin = useSelector(state => state.loginReducer);
    console.log(isLogin);
    const items = [
        {
            key: "0",
            label: <div className="dropdown__item">
                <div className="dropdown__item--right">
                    <div className="dropdown__item--icon"><LaptopOutlined /></div>
                    <div className="dropdown__item--content">Laptop, Macbook, Surface</div>
                </div>
                <div className="dropdown__item--right dropdown__item--icon"><RightOutlined /></div>
            </div>
        },
        {
            key: "1",
            label: <div className="dropdown__item">
                <div className="dropdown__item--right">
                    <div className="dropdown__item--icon"><LaptopOutlined /></div>
                    <div className="dropdown__item--content">Laptop, Macbook, Surface</div>
                </div>
                <div className="dropdown__item--right dropdown__item--icon"><RightOutlined /></div>
            </div>
        }
    ];

    const handleFinish = (values) => {
        console.log(values);
    }

    return (
        <>
            <div className="header">
                <Dropdown menu={{ items, }} className="dropdown">
                    <div className="header__logo">
                        <UnorderedListOutlined className="header__menu--icon" />
                    </div>
                </Dropdown>

                <div className="header__logo">
                    <Link to="/">Logo</Link>
                </div>


                <Form className="header__search" onFinish={handleFinish}>
                    <Row gutter={[12, 12]}>
                        <Col xl={20} lg={16} md={12}>
                            <Form.Item name="keyword">
                                <Input className="header__search--input" placeholder="Tìm kiếm" />
                            </Form.Item>
                        </Col>
                        <Col xl={4}>
                            <Form.Item>
                                <Button type="primary" htmlType="submit">Tìm</Button>
                            </Form.Item>
                        </Col>
                    </Row>
                </Form>

                <div className="header__button">
                    <div className="header__cart">
                        <CartMini />
                    </div>
                    {token ? (<>
                        {/* <Button className="header__button--login" type="primary">
                            <Link to="/login">Đăng nhập</Link>
                        </Button> */}
                        <Button className="header__button--logout">
                            <Link to="/logout">Đăng xuất</Link>
                        </Button>
                    </>) : (<>
                        <Button className="header__button--login" type="primary">
                            <Link to="/login">Đăng nhập</Link>
                        </Button>
                        <Button className="header__button--register">
                            <Link to="/register">Đăng kí</Link>
                        </Button>
                    </>)}
                </div>
            </div>
        </>
    )
}

export default Header;