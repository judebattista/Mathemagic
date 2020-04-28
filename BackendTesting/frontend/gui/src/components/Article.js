import React from 'react';
import { List, Avatar } from 'antd';

const Article = (props) => {
    return (
        <List
        itemLayout="horizontal"
        dataSource={props.data}
        renderItem={item => (
            <List.Item>
            <List.Item.Meta
                avatar={<Avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" />}
                title={<a href={`/${item.id}`}>{item.title}</a>}
                description="Ant Design, a design language for background applications, is refined by Ant UED Team"
            />
            </List.Item>
        )}
        />
    );
}

export default Article;