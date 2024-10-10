<template>
  <view class="container">

    <view class="member-list">
      <view class="member-item" v-for="(member, index) in members" :key="index">
        <text class="member-name">{{ member }}</text>
      </view>
    </view>

    <button class="recommend-button" @click="recommendMember">推荐成员</button>
  </view>
</template>

<script>
export default {
  data() {
    return {
      members: [
        '成员一',
        '成员二',
        '成员三',
        '成员四',
        '成员五',
        // 可以添加更多成员名称
      ],
    };
  },
  methods: {
    recommendMember() {
      // 推荐成员的逻辑
      uni.showToast({
        title: '推荐成员功能待实现',
        icon: 'none',
        duration: 2000
      });
      // 在这里可以跳转到推荐成员页面
      // uni.navigateTo({ url: '/pages/recommendMember/recommendMember.vue' });
    }
  }
};
</script>

<style scoped>
.container {
  padding: 20px;
}

.member-list {
  margin-bottom: 20px;
}

.member-item {
  padding: 15px;
  margin-bottom: 10px;
  background-color: #f0f0f0;
  border-radius: 5px;
}

.member-name {
  font-size: 18px;
  font-weight: bold;
}

.recommend-button {
  height: 50px;
  width: 100%;
  background-color: #007AFF;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px;
}
</style>
