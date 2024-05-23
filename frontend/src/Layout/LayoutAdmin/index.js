/* eslint-disable no-unused-vars */
import { useState } from "react";
import { useSelector } from "react-redux";
import './LayoutAdmin.scss';
import { Layout } from "antd";
import Header from "./Header";
import MenuSider from "./MenuSider";
import { Outlet } from "react-router-dom";

const { Sider, Content } = Layout;

function LayoutAdmin() {
    const isLogin = useSelector(state => state.LoginReducer);
    const [collapsed, setCollapsed] = useState(false);
    
    return (
        <>
            <Layout className="layout-admin">
                <Header collapsed={collapsed} setCollapsed={setCollapsed} />
                <Layout
                    className={
                        "layout-admin__main " + (collapsed && "layout-admin__main--fold")
                    }
                >
                    <Sider
                        breakpoint="lg"
                        className="layout-admin__sider"
                        theme="light"
                        width={250}
                        collapsed={collapsed}
                        onBreakpoint={(e) => setCollapsed(e)}
                    >
                        <MenuSider />
                    </Sider>
                    <Content className="layout-admin__content">
                        <Outlet />
                    </Content>
                </Layout>
            </Layout>
        </>
    )
}

export default LayoutAdmin;