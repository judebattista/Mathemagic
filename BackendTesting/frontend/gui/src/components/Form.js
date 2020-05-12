import React from 'react';
import { Form, Input, Button } from 'antd';
import axios from 'axios';

const FormItem = Form.Item;

class CustomForm extends React.Component {

    constructor(props) {
        super(props);
        this.handleFormSubmit = this.handleFormSubmit.bind(this);
    }

    handleFormSubmit = (event, requestType, articleID) => {
        
        //event.preventDefault();

        console.log("Test")
        
        const title = event.title;
        const content = event.content;

        console.log({title, content})
        // eslint-disable-next-line
        switch ( requestType ) {
            case 'post': //
                return axios.post('http://52.37.100.134:8000/api/',{
                    title: title,
                    content: content
                })
                .then(res => console.log(res))
                .catch(error => console.err(error));
            case 'put':
                return axios.put(`http://52.37.100.134:8000/api/${articleID}/`, {
                    title: title,
                    content: content
                })
                .then(res => console.log(res))
                .catch(error => console.log(error));
        }
    }
    render() {
        return (
        <div>
            <Form 
                onFinish={event => this.handleFormSubmit(
                    event,
                    this.props.requestType,
                    this.props.articleID )}
            >
            
            <FormItem label="Title" name="title">
                <Input placeholder="Put a title here" />
            </FormItem>
            <FormItem label="Content" name="content">
                <Input placeholder="Enter some content ..." />
            </FormItem>
            <FormItem>
                <Button
                    type='primary'
                    htmlType='submit'
                >
                    {this.props.btnText}
                </Button>
            </FormItem>
            </Form>
        </div>
        );
    }
}

export default CustomForm;