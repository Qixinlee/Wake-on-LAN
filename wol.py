# Author: liqixin
# Mail: hi@qixinlee.com
# Web: https://www.qixinlee.com

import streamlit as st
import wakeonlan

# 设置页面标题
st.title("WOL 唤醒工具")

# 在页面上添加输入框，用于输入目标主机的 MAC 地址
mac_address = st.text_input("请输入目标主机的 MAC 地址：", key="mac_input")

# 使用st.empty()创建一个占位符，用于在条件满足时显示警告信息
warning_placeholder = st.empty()

# 在页面上添加一个按钮，用于发送魔法包
if st.button("唤醒主机"):
    # 检查 MAC 地址是否为空
    if not mac_address:
        # 在占位符中显示警告信息
        warning_placeholder.warning("请输入目标主机的 MAC 地址。")
    else:
        # 发送魔法包
        wakeonlan.send_magic_packet(mac_address)
        st.success(f"已发送魔法包到 {mac_address}，尝试唤醒主机。")