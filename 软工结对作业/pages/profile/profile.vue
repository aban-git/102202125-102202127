<template>
  <view class="container">
    <NavBar :activeTab="3" />

    <!-- 头像区域 -->
    <view class="avatar-container">
      <view class="avatar-placeholder">
        <text class="avatar-text">头像</text> <!-- 头像文字提示 -->
      </view>
      <view class="user-info">
        <text class="username">用户名</text>
        <text class="user-signature">这是个人签名</text>
      </view>
    </view>

    <!-- 按钮容器 -->
    <view class="button-container">
      <button @click="navigateTo('basicInfo')">
        基本资料
        <text class="arrow-icon">→</text> <!-- 箭头图标 -->
      </button>
      <button @click="navigateTo('skillTree')">
        技能树
        <text class="arrow-icon">→</text> <!-- 箭头图标 -->
      </button>
      <button @click="navigateTo('projectExperience')">
        项目经历及获奖情况
        <text class="arrow-icon">→</text> <!-- 箭头图标 -->
      </button>
    </view>
  </view>
</template>

<script>
export default {
  methods: {
    navigateTo(page) {
      let url = '';
      switch (page) {
        case 'basicInfo':
          url = '/pages/basicInfo/basicInfo'; // 跳转到基本资料页面
          break;
        case 'skillTree':
          url = '/pages/skillTree/skillTree'; // 跳转到技能树页面
          break;
        case 'projectExperience':
          url = '/pages/projectExperience/projectExperience'; // 跳转到项目经历及获奖情况页面
          break;
      }
      uni.navigateTo({
        url: url
      });
    }
  }
};
</script>

<style scoped>
.container {
  padding: 20px;
  background-color: #f0f0f0; /* 设置整个页面背景颜色为灰色 */
  height: 100vh; /* 设置容器高度为视口高度，确保背景覆盖 */
}

/* 头像和用户信息样式 */
.avatar-container {
  display: flex;
  align-items: center; /* 垂直居中 */
  margin-bottom: 30px; /* 为按钮组留出空间 */
  background-color: white; /* 头像区域背景为白色 */
  padding: 15px; /* 内边距 */
  border-radius: 8px; /* 圆角 */
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); /* 添加阴影 */
}

.avatar-placeholder {
  width: 70px; /* 头像框宽度 */
  height: 70px; /* 头像框高度 */
  background-color: #007AFF; /* 蓝色背景 */
  border-radius: 50%; /* 圆形头像框 */
  display: flex;
  justify-content: center;
  align-items: center; /* 头像框内居中 */
  margin-right: 15px; /* 头像和文字之间的间距 */
}

.avatar-text {
  color: white; /* 头像文字颜色 */
}

/* 用户信息样式 */
.user-info {
  flex: 1; /* 让用户信息区域占满剩余空间 */
}

.username {
  font-size: 18px;
  font-weight: bold; /* 加粗字体 */
}

.user-signature {
  font-size: 14px;
  color: #666; /* 签名颜色 */
}

/* 按钮组样式 */
.button-container {
  display: flex;
  flex-direction: column; /* 垂直排列按钮 */
}

/* 按钮样式 */
button {
  display: flex; /* 使用flexbox布局 */
  justify-content: space-between; /* 内容两端对齐 */
  align-items: center; /* 垂直居中 */
  margin-bottom: 15px; /* 按钮之间的间距 */
  height: 60px; /* 按钮高度 */
  width: 100%; /* 按钮宽度 */
  background-color: transparent; /* 移除背景颜色 */
  color: black; /* 黑色字体 */
  border: 1px solid #ccc; /* 添加边框以增强可见性 */
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  padding: 0 15px; /* 内边距 */
}

.arrow-icon {
  margin-left: 10px; /* 箭头与按钮文本之间的间距 */
  font-size: 20px; /* 箭头图标字体大小 */
}

button:hover {
  background-color: #f0f0f0; /* 鼠标悬停时的背景颜色 */
}
</style>