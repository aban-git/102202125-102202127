<template>
  <view class="container">
    <!-- 显示程序名称 -->
    <view class="title">ProjectPartner</view>

    <!-- 账号输入框 -->
    <view class="input-item">
      <input type="text" placeholder="请输入账号" v-model="account" />
    </view>

    <!-- 密码输入框 -->
    <view class="input-item">
      <input type="password" placeholder="请输入密码" v-model="password" />
    </view>

    <!-- 确认密码输入框 -->
    <view class="input-item">
      <input type="password" placeholder="请确认密码" v-model="confirmPassword" />
    </view>

    <!-- 姓名输入框 -->
    <view class="input-item">
      <input type="text" placeholder="请输入姓名" v-model="name" />
    </view>

    <!-- 学校输入框 -->
    <view class="input-item">
      <input type="text" placeholder="请输入学校" v-model="school" />
    </view>

    <!-- 专业输入框 -->
    <view class="input-item">
      <input type="text" placeholder="请输入专业" v-model="major" />
    </view>

    <!-- 注册按钮 -->
    <view class="button">
      <button type="primary" @click="register">注册</button>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      account: '',
      password: '',
      confirmPassword: '',
      name: '',
      school: '',
      major: ''
    };
  },
  methods: {
    register() {
          // 注册按钮点击事件的逻辑，可以加入校验
          if (!this.account || !this.password || !this.confirmPassword || !this.name || !this.school || !this.major) {
            uni.showToast({
              title: '请填写完整信息',
              icon: 'none'
            });
            return;
          }
    
          if (this.password !== this.confirmPassword) {
            uni.showToast({
              title: '密码和确认密码不一致',
              icon: 'none'
            });
            return;
          }
    	  uni.request({
    	        url: 'http://127.0.0.1:8000/api/accounts/register/',
    	        method: 'POST',
    	        data: {
    	          username: this.account,
    	          password: this.password,
    	          password2: this.confirmPassword,
    	          name: this.name,
    	          major: this.major,
    	          school: this.school,
    	        },
    	        success: (res) => {
    	          if (res.statusCode === 201) {
    	            uni.showToast({
    	              title: '注册成功',
    	              icon: 'success'
    	            });
    	            // 存储 Token
    	            uni.setStorageSync('access', res.data.access);
    	            uni.setStorageSync('refresh', res.data.refresh);
    	            // 跳转到登录或主页面
    	          } else {
    	            uni.showToast({
    	              title: res.data.detail || '注册失败',
    	              icon: 'none'
    	            });
    	          }
    	        },
    	        fail: (error) => {
    			  console.error(error);
    	          uni.showToast({
    	            title: '网络错误',
    	            icon: 'none'
    	          });
    	        }
    	      });  
        }
	}	
};
</script>

<style scoped>
.container {
  padding: 20px;
  background-image: url('..\background1.png'); /* 背景图片 */
  background-size: cover;
  background-position: center;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title {
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 40px;
  color: #fff;
  text-align: center;
}

.input-item {
  margin-bottom: 15px;
  width: 100%;
}

input {
  width: 100%;
  height: 40px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.button {
  margin-top: 20px;
  width: 100%;
}

button {
  width: 100%;
  height: 40px;
  background-color: #007AFF;
  color: white;
  border: none;
  border-radius: 5px;
}
</style>