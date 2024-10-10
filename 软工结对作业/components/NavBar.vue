<!-- components/NavBar.vue -->
<template>
  <view class="navbar">
    <view
      class="nav-item"
      :class="{ active: activeTab === 0 }"
      @click="navigateTo('/pages/main/main')"
    >
      <text>主界面</text>
    </view>
    <view
      class="nav-item"
      :class="{ active: activeTab === 1 }"
      @click="navigateTo('/pages/project/project')"
    >
      <text>项目详情</text>
    </view>
    <view
      class="nav-item"
      :class="{ active: activeTab === 2 }"
      @click="navigateTo('/pages/contact/contact')"
    >
      <text>联系人</text>
    </view>
    <view
      class="nav-item"
      :class="{ active: activeTab === 3 }"
      @click="navigateTo('/pages/profile/profile')"
    >
      <text>个人信息</text>
    </view>
  </view>
</template>

<script>
export default {
  props: {
    activeTab: {
      type: Number,
      default: 0
    }
  },
  methods: {
    navigateTo(url) {
      uni.navigateTo({
        url: url
      });
    }
  }
};
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-around;
  align-items: center;
  background-color: #f8f8f8;
  padding: 10px 0;
  position: fixed;
  bottom: 0;
  width: 100%;
  border-top: 1px solid #ddd;
}

.nav-item {
  text-align: center;
  flex: 1;
  font-size: 16px;
  color: #333;
}

.nav-item.active {
  color: #4caf50;
  font-weight: bold;
}
</style>
