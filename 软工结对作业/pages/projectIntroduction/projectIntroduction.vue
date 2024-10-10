<template>
  <view class="container">
    <text class="title">项目简介</text>

    <!-- 项目名称 -->
    <view class="input-item">
      <text>项目名称：</text>
      <input type="text" placeholder="请输入项目名称" v-model="projectName" />
    </view>

    <!-- 创建人 -->
    <view class="input-item">
      <text>创建人：</text>
      <input type="text" placeholder="请输入创建人姓名" v-model="creator" />
    </view>

    <!-- 项目简介 -->
    <view class="input-item">
      <text>项目简介：</text>
      <textarea placeholder="请输入项目简介" v-model="projectIntroduction" rows="4" />
    </view>

    <!-- 项目要求 -->
    <view class="input-item">
      <text>项目要求：</text>
      <textarea placeholder="请输入项目要求" v-model="projectRequirements" rows="4" />
    </view>

    <!-- 提交按钮 -->
    <view class="button-container">
      <button class="submit-button" @click="submitDetails">提交</button>
    </view>
    
  </view>
</template>

<script>
export default {
  data() {
    return {
      projectName: '', // 项目名称
      creator: '', // 创建人
      projectIntroduction: '', // 项目简介
      projectRequirements: '' // 项目要求
    };
  },
  mounted() {
    this.getProfile(); // 页面加载时获取用户信息
  },
  methods: {
      async submitDetails() {
        if (!this.projectName || !this.creator || !this.projectIntroduction || !this.projectRequirements) {
          uni.showToast({
            title: '请填写完整信息',
            icon: 'none'
          });
          return;
        }    
      },
	  getProfile() {
	    const access = uni.getStorageSync('access');
	    uni.request({
	      url: 'http://127.0.0.1:8000/api/accounts/projectCreate/', // 获取用户信息的接口
	      method: 'GET',
	      header: {
	        'Authorization': `Bearer ${access}`
	      },
	      success: (res) => {
	        if (res.statusCode === 200) {
	          // 填充用户信息
	          const profile = res.data;
	          this.projectName = profile.name;
			  this.creator = profile.owner;
	          this.projectIntroduction = profile.description;
	          this.projectRequirements = profile.requirements;
	        } else {
	          uni.showToast({
	            title: '获取资料失败',
	            icon: 'none'
	          });
	        }
	      },
	      fail: () => {
	        uni.showToast({
	          title: '网络错误',
	          icon: 'none'
	        });
	      }
	    });
	  },
    
    }
};
</script>

<style scoped>
.container {
  padding: 20px;
}

.title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.input-item {
  margin-bottom: 15px;
  display: flex;
  flex-direction: column;
}

input, textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

textarea {
  resize: none; /* 禁止调整文本框大小 */
}

.button-container {
  margin-top: 20px;
}

.submit-button {
  width: 100%;
  height: 50px;
  background-color: #007AFF;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 18px;
  cursor: pointer;
}

.project-info {
  margin-top: 20px;
  border-top: 1px solid #ccc;
  padding-top: 15px;
}

.info-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
}

.info-item {
  margin-bottom: 10px;
  font-size: 16px;
}
</style>
