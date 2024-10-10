<template>
  <view class="container">
    <nav-bar :activeTab="3" /> <!-- 导航栏 -->

    <!-- 背景部分 -->
    <view class="background">
      <text class="art-text">这里是你的项目</text>
    </view>

    <view class="button-group">
      <button class="nav-button" @click="navigateTo('taskManagement')">任务管理</button>
      <button class="nav-button" @click="navigateTo('projectIntroduction')">项目简介</button>
      <button class="nav-button" @click="navigateTo('projectMembers')">项目成员</button>
      <button class="nav-button" @click="navigateTo('memberInvitation')">成员邀请</button>
    </view>
  </view>
</template>

<script>
export default {
  methods: {
    navigateTo(page) {
      // 根据不同的页面跳转
      uni.navigateTo({
        url: `/pages/${page}/${page}` // 去掉.vue后缀
      });
    }
  }
};
</script>

<style scoped>
.container {
  padding: 20px;
  padding-bottom: 60px; /* 留出底部导航栏的空间 */
  position: relative; /* 为背景定位提供基础 */
}

/* 背景样式 */
.background {
  background-image: url('..\项目.jpg'); /* 替换为你的背景图片路径 */
  background-size: cover; /* 覆盖整个区域 */
  background-position: center; /* 居中显示 */
  height: 300px; /* 根据需要调整高度 */
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  margin-bottom: 20px; /* 为按钮组留出空间 */
}

/* 艺术字样式 */
.art-text {
  font-size: 30px; /* 根据需要调整字体大小 */
  font-weight: bold;
  color: white; /* 根据背景图片调整字体颜色 */
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* 添加阴影以增强可读性 */
}

/* 按钮组样式 */
.button-group {
  display: flex;
  flex-direction: column; /* 竖直排列按钮 */
  align-items: center; /* 按钮居中对齐 */
}

/* 按钮样式 */
.nav-button {
  width: 320px; /* 按钮宽度，设为长方形 */
  height: 120px; /* 按钮高度，拉长 */
  background-color: #007AFF;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px; /* 根据需要调整字体大小 */
  display: flex; /* 使用flex使文本居中 */
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  margin-bottom: 15px; /* 按钮间距 */
}
</style>