import React from 'react';
import ReactDOM from 'react-dom';
import 'antd/dist/antd.css';
import './index.css';
import { Layout, Menu, Breadcrumb } from 'antd';
import { Input, Space } from 'antd';
import { AudioOutlined } from '@ant-design/icons';


const { Header, Content, Footer } = Layout;
const suffix = (
  <AudioOutlined
    style={{
      fontSize: 16,
      color: '#1890ff',
    }}
  />
);

const handleChatbot = (event) => {
  window.location.replace ('Chatbot.js')
}
const handleOverview = (event) => {
  alert("Hallo")
}
const handleVoicebot = (event) => {
  alert("Hallo")
}
ReactDOM.render(
  <Layout className="layout">
    <Header>
      <div className="logo" />
      <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
        <Menu.Item key="1" onClick={handleOverview}>Overview</Menu.Item>
        <Menu.Item key="2" onClick={handleVoicebot}>Voice Bot</Menu.Item>
        <Menu.Item key="3" onClick={handleChatbot}>Chatbot</Menu.Item>
      </Menu>
    </Header>
    <Content style={{ padding: '0 50px' }}>
      <Breadcrumb style={{ margin: '16px 0' }}>
      </Breadcrumb>
    </Content>
    <Footer style={{ textAlign: 'center' }}>Made with love by Domenic</Footer>
  </Layout>,
  document.getElementById('container'),
);