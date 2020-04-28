import React from 'react';
import { Card } from 'antd';
import axios from 'axios';



class ArticleDetail extends React.Component {

    state = {
        article: {}
    }

    componentDidMount() { // called every time the component is mounted
        const articleID = this.props.match.params.articleID;
        axios.get(`http://127.0.0.1:8000/api/${articleID}`) //api URL here
            .then(res => {
                this.setState({
                    article: res.data
                });
            })
    }

    render() {
        return (
            <Card title = {this.state.article.title}>
                <p>{this.state.article.content}</p>
            </Card>
        );
    };
};

export default ArticleDetail; //