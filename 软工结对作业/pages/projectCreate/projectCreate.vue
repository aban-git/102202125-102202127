<template>
  <view class="container">
    <!-- 如果需要使用 NavBar，添加在这里 -->
    <NavBar />

    <view class="form-group">
      <label for="projectName">项目名称:</label>
      <input type="text" id="projectName" v-model="projectName" placeholder="请输入项目名称" />
    </view>

    <view class="form-group">
      <label for="projectMembers">项目成员:</label>
      <input type="text" id="projectMembers" v-model="projectMembers" placeholder="请输入项目成员（以逗号分隔）" />
    </view>

    <view class="form-group">
      <label for="projectDescription">项目描述:</label>
      <textarea id="projectDescription" v-model="projectDescription" placeholder="请输入项目描述"></textarea>
    </view>

    <view class="form-group">
      <label for="projectRequirements">项目需求:</label>
      <textarea id="projectRequirements" v-model="projectRequirements" placeholder="请输入项目需求"></textarea>
    </view>

    <button class="submit-button" @click="submitProject">提交项目</button>
  </view>
</template>

<script>
import NavBar from '@/components/NavBar.vue'; // 确保路径正确

export default {
  components: {
    NavBar, // 注册组件
  },
  data() {
    return {
      projectName: '',
      projectMembers: '',
      projectDescription: '',
      projectRequirements: '',
    };
  },
  methods: {
    async submitProject() {
      const membersArray = this.projectMembers.split(',').map(member => member.trim());
      const projectData = {
        name: this.projectName,
        members: membersArray,
        description: this.projectDescription,
        requirements: this.projectRequirements
      };

      try {
        const response = await this.createProject(projectData);
        if (response.statusCode === 201) {
          uni.showToast({
            title: '项目创建成功',
            icon: 'success',
            duration: 2000
          });
          this.resetForm();
        } else {
          uni.showToast({
            title: '项目创建失败',
            icon: 'none',
            duration: 2000
          });
        }
      } catch (error) {
        console.error('创建项目失败:', error);
        uni.showToast({
          title: '项目创建失败',
          icon: 'none',
          duration: 2000
        });
      }
    },
    createProject(projectData) {
      const token = uni.getStorageSync('access'); // 确保使用正确的键名

      console.log('Access Token:', token); // 调试用

      return new Promise((resolve, reject) => {
        uni.request({
          url: 'http://127.0.0.1:8000/api/accounts/projectCreate/', // 替换为你的后端接口地址
          method: 'POST',
          data: projectData, // 直接传递对象
          header: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}` // 确保 token 存在
          },
          success: (res) => {
            resolve(res);
          },
          fail: (err) => {
            reject(err);
          }
        });
      });
    },
    resetForm() {
      this.projectName = '';
      this.projectMembers = '';
      this.projectDescription = '';
      this.projectRequirements = '';
    }
  }
};
</script>

<style scoped>
.container {
  padding: 20px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input, textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

textarea {
  height: 100px;
}

.submit-button {
  height: 50px;
  width: 100%;
  background-color: #007AFF;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px;
}
</style>
