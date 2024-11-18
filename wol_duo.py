# Author: liqixin
# Mail: hi@qixinlee.com
# Web: https://www.qixinlee.com

import streamlit as st
import wakeonlan

# 设置页面标题
st.title("WOL 唤醒工具")

# 预设的常用主机MAC地址列表
common_mac_addresses = {
    "Host 1": "00:11:22:33:44:55",
    "Host 2": "AA:BB:CC:DD:EE:FF",
    "Host 3": "11:22:33:44:55:66"
}

# 在页面上添加下拉框，用于选择目标主机
selected_host = st.selectbox("请选择要唤醒的主机：", list(common_mac_addresses.keys()))

# 获取用户选择的主机MAC地址
mac_address = common_mac_addresses[selected_host]

# 使用st.empty()创建一个占位符，用于在条件满足时显示警告信息
warning_placeholder = st.empty()

# 在页面上添加一个按钮，用于发送魔法包
if st.button("唤醒主机"):
    # 检查 MAC 地址是否为空
    if not mac_address:
        # 在占位符中显示警告信息
        warning_placeholder.warning("请选择要唤醒的主机。")
    else:
        # 发送魔法包
        wakeonlan.send_magic_packet(mac_address)
        st.success(f"已发送魔法包到 {mac_address}，尝试唤醒主机。")