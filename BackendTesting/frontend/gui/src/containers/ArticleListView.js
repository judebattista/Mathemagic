import React from 'react';

import Article from '../components/Article';
import CustomForm from '../components/Form'

import axios from 'axios';



class ArticleList extends React.Component {

    state = {
        articles: []
    }

    componentDidMount() { // called every time the component is mounted
        axios.get('http://52.37.100.134:8000/api/') //api URL here
            .then(res => {
                this.setState({
                    articles: res.data
                });
            })
    }

    render() {
        return (
                <div>
                    <Article data={this.state.articles}/>
                    <br/>
                    <h2>Create an article</h2>
                    <CustomForm
                        requestType="post"
                        articleID={null}
                        btnText="Create" />
                </div>               
        )
    }
}

export default ArticleList;