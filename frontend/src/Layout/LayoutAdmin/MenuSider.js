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
            label: <Link to="/historyadmin">Danh sách mua hàng</Link>,
            icon: <icons.CheckOutlined />,
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