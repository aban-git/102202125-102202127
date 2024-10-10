<template>
  <view class="container">
    <!-- 顶部的艺术字 ProjectPartner -->
    <view class="art-title">
      <text class="project-title">ProjectPartner</text>
    </view>

    <!-- 上半部分背景和艺术字 -->
    <view class="header">
      <text class="title">一起来组队项目吧！</text>
    </view>

    <!-- 按钮组 -->
    <view class="button-group">
      <button class="nav-button" @click="navigateTo('projectCreate')">项目创建</button>
      <button class="nav-button" @click="navigateTo('projectSquare')">项目广场</button>
      <button class="nav-button" @click="navigateTo('notification')">消息通知</button>
      <button class="nav-button" @click="navigateTo('memberRecommendation')">项目成员推荐</button>
    </view>

    <nav-bar :activeTab="0" /> <!-- 导航栏 -->
  </view>
</template>

<script>
export default {
  methods: {
    navigateTo(page) {
      // 根据不同的页面跳转
      uni.navigateTo({
        url: `/pages/${page}/${page}`
      });
    }
  }
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  padding: 20px;
  box-sizing: border-box;
  background-color: #90EE90; /* 设置整个界面的背景颜色为浅绿色 */
}

.art-title {
  margin-top: 10px; /* 调整与顶部的距离 */
  text-align: center;
}

.project-title {
  font-size: 48px;
  font-weight: bold;
  font-family: 'Arial', sans-serif;
  color: #1E90FF; /* 深蓝色字体 */
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); /* 添加文字阴影，形成艺术字效果 */
}

.header {
  width: 100%;
  height: 50%; /* 上半部分占页面50% */
  background-image: url('..\\cloud.jpg'); /* 云朵的背景图片 */
  background-color: #87CEEB; /* 天蓝色背景 */
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;
  border-bottom-left-radius: 30px;
  border-bottom-right-radius: 30px;
}

.title {
  font-size: 70px;
  font-weight: bold;
  color: #aa0000; /* 红色文字，与天蓝色背景形成对比 */
}

.button-group {
  display: flex;
  justify-content: space-around; /* 按钮横向排列 */
  width: 100%;
  margin-top: 20px; /* 按钮组与上半部分有一定距离 */
}

.nav-button {
  width: 160px; /* 按钮宽度 */
  height: 160px; /* 按钮高度，使其变为圆形 */
  background-color: #007AFF;
  color: white;
  border: none;
  border-radius: 50%; /* 圆形按钮 */
  font-size: 14px;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>