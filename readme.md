# WOL 唤醒工具

这是一个使用 Python 和 Streamlit 框架开发的 WOL（Wake-on-LAN）唤醒工具。它允许用户通过网页界面输入目标主机的 MAC 地址，并发送魔法包来尝试唤醒主机。

## 功能

- 输入目标主机的 MAC 地址
- 发送 WOL 魔法包
- 实时反馈唤醒状态

## 安装与运行

1. 确保你已经安装了 Python 环境。
2. 安装依赖库：
   ```bash
   pip install streamlit wakeonlan
   ```
3. 运行应用：
   ```bash
   streamlit run app.py
   ```
4. 打开浏览器，访问 `URL_ADDRESS 即可使用。

 使用说明

## 使用方法
1. 在网页界面的输入框中输入目标主机的 MAC 地址。
2. 点击 "唤醒主机" 按钮。
3. 如果 MAC 地址为空，将会显示警告信息。
4. 如果发送成功，将会显示成功消息。