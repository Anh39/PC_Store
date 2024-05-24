import { Button, Dropdown, Input, Form, Row, Col } from "antd";
import { UnorderedListOutlined, LaptopOutlined, RightOutlined } from "@ant-design/icons";
import { Link, useNavigate } from "react-router-dom";
import { useSelector } from "react-redux";
import CartMini from "../../components/CartMini";
import { useEffect } from "react";
import { getCategoryList } from "../../Services/backend/product";
import Personal from "../../components/Personal";
import logoElink from "../../images/logo-elink.png";

// Laptop gaming, đồ họa

function Header(props) {
    const { token } = props;
    const isLogin = useSelector(state => state.loginReducer);
    console.log(isLogin);
    const navigate = useNavigate();
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
        navigate(`/search?keyword=${values.keyword || ''}`);
    }

    useEffect(() => {
        const fetchAPI = async () => {
            const data = await getCategoryList();
            console.log(data);
        }

        fetchAPI();
    }, []);

    return (
        <>
            <div className="header">
                <div style={{ display: "flex" }}>
                    <Dropdown menu={{ items, }} className="dropdown">
                        <div className="header__logo">
                            <UnorderedListOutlined className="header__menu--icon" />
                        </div>
                    </Dropdown>

                    <div className="header__logo">
                        <Link to="/"><img src={logoElink} alt="logo"/></Link>
                    </div>
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
                        <Personal />
                    </>) : (<>

                        <Button className="header__button--login" type="primary">
                            <Link to="/admin">Quản lí</Link>
                        </Button>
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