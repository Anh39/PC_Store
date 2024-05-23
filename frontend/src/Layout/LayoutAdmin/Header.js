import { MenuFoldOutlined, MenuUnfoldOutlined } from "@ant-design/icons";
import logoElink from "../../images/logo-elink.png";
import logoFoldElink from "../../images/logo-fold-elink.png";
import { Button } from "antd";
import { Link } from "react-router-dom";

function Header(props) {
    const { collapsed, setCollapsed } = props;
    return (
        <>
            <header className="layout-admin__header">
                <div className={"layout-admin__header-logo " + (collapsed && "layout-admin__header-logo--collapsed")}>
                    <img src={(collapsed ? logoFoldElink : logoElink)} alt="logo" />
                </div>
                <div className="layout-admin__header__nav">
                    <div className="layout-admin__header__nav-left">
                        <div
                            className="layout-admin__header__collapsed"
                            onClick={() => setCollapsed(!collapsed)}
                        >
                            {collapsed ? <MenuUnfoldOutlined /> : <MenuFoldOutlined />}
                        </div>
                        <div className="header__search">

                        </div>
                    </div>

                    <div className="header__nav-right">
                        <Button>
                            <Link to='/'>Trang chủ</Link>
                        </Button>
                        <Button>
                            <Link to='/logout'>Đăng xuất</Link>
                        </Button>
                    </div>
                </div>
            </header>
        </>
    )
}

export default Header;