import React from 'react';

import Article from '../components/Article';

import axios from 'axios';



class ArticleList extends React.Component {

    state = {
        articles: []
    }

    componentDidMount() { // called every time the component is mounted
        axios.get('http://127.0.0.1:8000/api/') //api URL here
            .then(res => {
                this.setState({
                    articles: res.data
                });
            })
    }

    render() {
        return (
                <Article data={this.state.articles}/>
        );
    };
};

export default ArticleList;