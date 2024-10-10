<template>
  <view class="chat-container">
    <!-- 顶部显示聊天对象的名字 -->
    <view class="chat-header">
      <text>{{ contactName }}</text>
    </view>

    <!-- 聊天内容显示区 -->
    <scroll-view class="chat-content" scroll-y="true">
      <!-- 每条消息 -->
      <view
        v-for="(message, index) in messages"
        :key="index"
        :class="['chat-message', message.isSelf ? 'self' : 'other']"
      >
        <!-- 左侧或右侧显示头像 -->
        <view :class="['chat-item', message.isSelf ? 'self' : 'other']">
          <!-- 头像 -->
          <image
            :src="message.isSelf ? '/static/avatar-default.png' : '/static/avatar-default.png'"
            class="chat-avatar"
            @click="goToProfile(message.isSelf)"
          />
          <!-- 聊天消息内容 -->
          <text class="chat-text">{{ message.text }}</text>
        </view>
      </view>
    </scroll-view>

    <!-- 底部聊天输入栏 -->
    <view class="chat-input-bar">
      <input
        type="text"
        v-model="newMessage"
        placeholder="输入消息"
        @keyup.enter="sendMessage"
      />
      <button @click="sendMessage">发送</button>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      contactName: '', // 聊天对象的名字
      newMessage: '', // 新消息的内容
      messages: [
        // 聊天消息列表
        { text: '你好！', isSelf: false },
        { text: '你好，请问有什么事吗？', isSelf: true }
      ],
    };
  },
  methods: {
    // 发送消息
    sendMessage() {
      if (this.newMessage.trim()) {
        // 将新消息添加到消息列表
        this.messages.push({ text: this.newMessage, isSelf: true });
        // 清空输入框
        this.newMessage = '';
      }
    },
    // 跳转到基本资料页面
    goToProfile(isSelf) {
      const url = isSelf ? '/pages/profile/profile' : '/pages/contact-profile/contact-profile';
      uni.navigateTo({
        url: url
      });
    }
  },
  mounted() {
    // 获取聊天对象的名字（通过 URL 参数传递）
    const query = this.$route.query;
    this.contactName = query.contactName || '联系人';
  }
};
</script>

<style scoped>
/* 整体布局 */
.chat-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

/* 顶部标题栏样式 */
.chat-header {
  padding: 10px;
  background-color: #f8f8f8;
  text-align: center;
  font-weight: bold;
  border-bottom: 1px solid #ddd;
}

/* 聊天内容区域，允许滚动 */
.chat-content {
  flex: 1;
  padding: 10px;
  overflow-y: auto;
}

/* 每条消息的布局样式 */
.chat-item {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.self {
  justify-content: flex-end;
}

.other {
  justify-content: flex-start;
}

/* 头像样式 */
.chat-avatar {
  width: 40px;
  height: 40px;
  border-radius: 20px;
}

/* 发送者的消息显示在左边，头像在右边 */
.self .chat-avatar {
  margin-left: 10px;
  order: 2;
}

.self .chat-text {
  order: 1;
  background-color: #d1f0ff;
  margin-right: 10px;
}

/* 接收者的消息显示在右边，头像在左边 */
.other .chat-avatar {
  margin-right: 10px;
  order: 1;
}

.other .chat-text {
  order: 2;
  background-color: #f1f1f1;
  margin-left: 10px;
}

/* 消息文本样式 */
.chat-text {
  max-width: 60%;
  padding: 10px;
  border-radius: 10px;
  background-color: #f1f1f1;
}

/* 底部输入栏样式 */
.chat-input-bar {
  display: flex;
  padding: 10px;
  border-top: 1px solid #ddd;
  background-color: #f8f8f8;
}

.chat-input-bar input {
  flex: 1;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.chat-input-bar button {
  margin-left: 10px;
  padding: 8px 16px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
