<template>
  <view class="container">

    <view class="project-list">
      <view class="project-item" v-for="(project, index) in projects" :key="index">
        <text class="project-name">{{ project }}</text>
      </view>
    </view>

    <button class="upload-button" @click="uploadProject">上传项目</button>
  </view>
</template>

<script>
export default {
  data() {
    return {
      projects: [
        '项目一',
        '项目二',
        '项目三',
        '项目四',
        '项目五',
        // 可以添加更多项目名称
      ],
    };
  },
  methods: {
    uploadProject() {
      // 上传项目的逻辑
      uni.showToast({
        title: '上传项目功能待实现',
        icon: 'none',
        duration: 2000
      });
      // 在这里可以跳转到上传项目页面
      // uni.navigateTo({ url: '/pages/uploadProject/uploadProject.vue' });
    }
  }
};
</script>

<style scoped>
.container {
  padding: 20px;
}

.project-list {
  margin-bottom: 20px;
}

.project-item {
  padding: 15px;
  margin-bottom: 10px;
  background-color: #f0f0f0;
  border-radius: 5px;
}

.project-name {
  font-size: 18px;
  font-weight: bold;
}

.upload-button {
  height: 50px;
  width: 100%;
  background-color: #007AFF;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px;
}
</style>
