<template>
  <view class="container">
    <!-- 显示程序名称 -->
    <view class="title">ProjectPartner</view>

    <!-- 账号输入框 -->
    <view class="input-group">
      <text class="label">账号:</text>
      <input
        v-model="username"
        class="input"
        placeholder="请输入账号"
        type="text"
      />
    </view>

    <!-- 密码输入框 -->
    <view class="input-group">
      <text class="label">密码:</text>
      <input
        v-model="password"
        class="input"
        placeholder="请输入密码"
        type="password"
      />
    </view>

    <!-- 按钮组 -->
    <view class="button-group">
      <button class="btn register-btn" @click="goToRegister">注册</button>
      <button class="btn login-btn" @click="login">登录</button>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    goToRegister() {
      // 跳转到注册页面的逻辑
      uni.navigateTo({
        url: '/pages/register/register'
      });
    },
    
    login() {
        if (this.username && this.password) {
          uni.request({
            url: 'http://127.0.0.1:8000/api/accounts/login/',
            method: 'POST',
            data: {
              username: this.username,
              password: this.password
            },
            success: (res) => {
              if (res.statusCode === 200) {
                uni.showToast({
                  title: '登录成功',
                  icon: 'success'
                });
                // 存储 Token
                uni.setStorageSync('access', res.data.token.access);
                uni.setStorageSync('refresh', res.data.token.refresh);
                uni.switchTab({
                  url: '/pages/main/main',
                  success: () => {
                          console.log('跳转成功到主页面');
                        },
                        fail: (err) => {
                          console.error('跳转失败:', err);
                        }
                });
                // 跳转到主页面
              } else {
                uni.showToast({
                  title: res.data.detail || '登录失败',
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
        } else {
          uni.showToast({
            title: '请填写账号和密码',
            icon: 'none'
          });
        }
      }
  }
};
</script>

<style scoped>
.container {
  padding: 20px;
  background-image: url('../background1.png'); /* 背景图片 */
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

.input-group {
  margin-bottom: 20px;
  width: 100%;
}

.label {
  display: block;
  margin-bottom: 10px;
  font-size: 16px;
  color: white;
}

.input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.button-group {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  color: #fff;
  cursor: pointer;
}

.register-btn {
  background-color: #007aff;
}

.login-btn {
  background-color: #28a745;
}
</style>