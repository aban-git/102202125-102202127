<template>
  <view class="container">
    <!-- 姓名输入框 -->
    <view class="input-item">
      <text>姓名：</text>
      <input type="text" placeholder="请输入姓名" v-model="name" />
    </view>

    <!-- 性别选择 -->
    <view class="input-item">
      <text>性别：</text>
      <picker mode="selector" :range="genders" v-model="gender">
        <view class="picker">{{ genders[gender] || '请选择性别' }}</view>
      </picker>
    </view>

    <!-- 出生日期选择 -->
    <view class="input-item">
      <text>出生日期：</text>
      <picker mode="date" v-model="birthDate">
        <view class="picker">{{ birthDate || '请选择出生日期' }}</view>
      </picker>
    </view>

    <!-- 电话号码输入框 -->
    <view class="input-item">
      <text>电话号码：</text>
      <input type="text" placeholder="请输入电话号码" v-model="phone" />
    </view>

    <!-- 邮箱输入框 -->
    <view class="input-item">
      <text>邮箱：</text>
      <input type="email" placeholder="请输入邮箱" v-model="email" />
    </view>

    <!-- 年级输入框 -->
    <view class="input-item">
      <text>年级：</text>
      <input type="text" placeholder="请输入年级" v-model="grade" />
    </view>

    <!-- 学院+专业输入框 -->
    <view class="input-item">
      <text>学院+专业：</text>
      <input type="text" placeholder="请输入学院+专业" v-model="major" />
    </view>

    <!-- 学号输入框 -->
    <view class="input-item">
      <text>学号：</text>
      <input type="text" placeholder="请输入学号" v-model="studentId" />
    </view>

    <!-- 提交按钮 -->
    <view class="button">
      <button type="primary" @click="submitProfile">提交</button>
    </view>
  </view>
</template>

<script>
import NavBar from '@/components/NavBar.vue';

export default {
  components: {
    NavBar
  },
  data() {
    return {
      name: '',
      gender: 0, // 默认选择第一个性别
      birthDate: '',
      phone: '',
      email: '',
      grade: '',
      major: '',
      studentId: '',
      genders: ['男', '女'], // 性别选项
    };
  },
  mounted() {
    this.getProfile(); // 页面加载时获取用户信息
  },
  methods: {
    getProfile() {
      const access = uni.getStorageSync('access');
      uni.request({
        url: 'http://127.0.0.1:8000/api/accounts/basicInfo/', // 获取用户信息的接口
        method: 'GET',
        header: {
          'Authorization': `Bearer ${access}`
        },
        success: (res) => {
          if (res.statusCode === 200) {
            // 填充用户信息
            const profile = res.data;
            this.name = profile.name;
            this.gender = this.genders.indexOf(profile.gender); // 根据性别设置默认值
            this.birthDate = profile.birthDate;
            this.phone = profile.phone;
            this.email = profile.email;
            this.grade = profile.grade;
            this.major = profile.major;
            this.studentId = profile.studentId;
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
    submitProfile() {
        if (!this.name || !this.phone || !this.email || !this.grade || !this.major || !this.studentId) {
            uni.showToast({
                title: '请填写完整信息',
                icon: 'none'
            });
            return;
        }
    
        const access = uni.getStorageSync('access');
        const updatedProfile = {
            name: this.name,
            gender: this.genders[this.gender],
            birthDate: this.birthDate,
            phone: this.phone,
            email: this.email,
            grade: this.grade,
            major: this.major,
            studentId: this.studentId,
        };
    
        uni.request({
            url: 'http://127.0.0.1:8000/api/accounts/basicInfo/',
            method: 'PUT',
            header: {
                'Authorization': `Bearer ${access}`,
                'Content-Type': 'application/json'
            },
            data: updatedProfile,
            success: (res) => {
                if (res.statusCode === 200) {
                    uni.showToast({
                        title: '资料更新成功',
                        icon: 'success'
                    });
                } else {
                    uni.showToast({
                        title: `更新资料失败: ${res.data.message || '未知错误'}`,
                        icon: 'none'
                    });
                }
            },
            fail: (err) => {
                uni.showToast({
                    title: `网络错误: ${err.errMsg}`,
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
  padding-bottom: 60px; /* 留出底部导航栏的空间 */
}

.input-item {
  margin-bottom: 15px;
  display: flex;
  align-items: center; /* 垂直居中 */
}

input {
  flex: 1; /* 填满剩余空间 */
  height: 40px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-left: 10px; /* 左侧留出间距 */
}

.picker {
  flex: 1; /* 填满剩余空间 */
  height: 40px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-left: 10px; /* 左侧留出间距 */
}

.button {
  margin-top: 20px;
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
