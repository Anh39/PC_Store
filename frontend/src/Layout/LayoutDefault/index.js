import { Layout } from "antd";
import "./LayoutDefault.css";
import Header from "./Header";
import Footer from "./Footer";
import Main from "./Main";
import { getCookie } from "../../helpers/cookie";
import { useSelector } from "react-redux";

function LayoutDefault() {
    const token = getCookie("token");
    const isLogin = useSelector(state => state.loginReducer);
    console.log(isLogin);
    return (
        <>
            <Layout className="layout-default">
                <Header token={token} />
                <div className="below-header">
                    <Main />
                    <Footer />
                </div>
            </Layout>
        </>
    )
}

export default LayoutDefault;