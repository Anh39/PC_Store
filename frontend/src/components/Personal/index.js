import { Button, Dropdown } from "antd";
import { Link } from "react-router-dom";
import { useEffect } from "react";

function Personal() {

    const items = [
        {
            key: 'resetpassword',
            label: <Link to="/resetpassword">Đổi mật khẩu</Link>
        },
        {
            key: 'logout',
            label: <Link to="/logout">Đăng xuất</Link>
        },
        {
            key: 'history',
            label: <Link to='/history'>Lịch sử thanh toán</Link>
        }
    ];

    const fetchAPI = async () => {
        
    }

    

    useEffect(() => {
        fetchAPI();
    }, []);

    return (
        <>
            <Dropdown
                menu={{ items }}
                trigger={['click']}
            >
                <Button>
                    Personal
                </Button>
            </Dropdown>

            
        </>
    )
}

export default Personal;