import * as icons from "@ant-design/icons";
import { Menu } from "antd";
import { Link } from "react-router-dom";

function MenuSider() {
    const items = [
        {
            key: "admin",
            label: <Link to="/admin">Quản lí sản phẩm</Link>,
            icon: <icons.PlusCircleOutlined />
        },
        {
            key: "menu-2",
            label: "Danh sách mua hàng",
            icon: <icons.CheckOutlined />,
        },
        {
            key: "menu-3",
            label: "Menu 3",
            icon: <icons.HighlightOutlined />
        }
    ];
    return (
        <>
            <Menu mode="inline" items={items}
                defaultSelectedKeys={["admin"]}
                defaultOpenKeys={["admin"]}
            />
        </>
    )
}

export default MenuSider;