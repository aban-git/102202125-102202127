<template>
  <view class="container">
    <text class="success-message">邀请成功！</text>
    <text class="details">您已成功邀请{{ name }}担任{{ role }}.</text>
    <button @click="goBack" class="back-button">返回</button>
  </view>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      role: ''
    };
  },
  onLoad(options) {
    this.name = options.name;
    this.role = options.role;
  },
  methods: {
    goBack() {
      uni.navigateBack();
    }
  }
};
</script>

<style scoped>
.container {
  padding: 20px;
  text-align: center;
}

.success-message {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.details {
  font-size: 18px;
  margin-bottom: 30px;
}

.back-button {
  height: 50px;
  background-color: #007AFF;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px;
}
</style>
