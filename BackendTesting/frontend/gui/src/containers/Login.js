import React from 'react';
import { Form, Input, Button, Spin } from 'antd';
//import { FormComponentProps } from 'antd/lib/form'; // https://github.com/ant-design/ant-design/issues/9331
import { connect } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { LoadingOutlined } from '@ant-design/icons';
import * as actions from '../store/actions/auth';




const antIcon = <LoadingOutlined style={{ fontSize: 24 }} spin />;

class NormalLoginForm extends React.Component {
    handleSubmit = (event) => {
        //event.preventDefault();
        //Form validation should happen here...
        console.log(event.username, event.password);
        this.props.onAuth(event.username, event.password, false);
        this.props.history.push('/');
    }

    render() { 
        
        let errorMessage = null;
        if (this.props.error) {
            errorMessage = (
            <p>{this.props.error.message}</p>
            );
        }
    
        return (
            <div>

                {errorMessage}

                { 
                
                    this.props.loading ?

                    <Spin indicator={antIcon} />

                    :
                    
                    <Form
                        className="login-form"
                        onFinish={(event) => this.handleSubmit(event)}
                    >
                        <Form.Item
                            label="Username"
                            name="username"
                            rules={[{ required: true, message: 'Please input your username!' }]}
                        >   
                            <Input />
                        </Form.Item>

                        <Form.Item
                            label="Password"
                            name="password"
                            rules={[{ required: true, message: 'Please input your password!' }]}
                        >
                        <   Input.Password />
                        </Form.Item>

                        <Form.Item>

                            <Button type="primary" htmlType="submit" style={{marginRight: '10px'}}>
                                Login
                            </Button>

                        or

                            <NavLink 
                                style={{marginRight: '10px'}} 
                                to='/signup/'
                            > signup
                            </NavLink>

                        </Form.Item>
                    </Form> 
                    
                }
                
            </div>
        );
    }
};

//const WrappedNormalLoginForm = Form.create({})(NormalLoginForm);

const mapStateToProps = (state) => {
    return {
        loading: state.loading,
        error: state.error
    }
}

const mapDispatchToProps = dispatch => {
    return {
        onAuth: (username, password) => dispatch(actions.authLogin(username, password))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(NormalLoginForm);