<template>
  <view class="container">
    <view class="form">
      <!-- 搜索用户部分 -->
      <view class="input-group">
        <text class="label">搜索成员用户名:</text>
        <input v-model="searchUsername" class="input" placeholder="请输入要搜索的用户名" />
        <button @click="searchUser" class="search-button">搜索</button>
      </view>

      <!-- 显示搜索结果 -->
      <view v-if="searchResult" class="search-result">
        <text class="result-label">搜索结果:</text>
        <view class="user-info">
          <view>
            <text class="username">{{ searchResult.username }}</text>
            <text class="email">{{ searchResult.email }}</text>
          </view>
          <button 
            @click="inviteMember(searchResult)" 
            :disabled="searchResult.has_project" 
            class="invite-button">
            {{ searchResult.has_project ? '已拥有项目' : '添加成员' }}
          </button>
        </view>
      </view>

      <!-- 已添加的成员列表 -->
      <view v-if="addedMembers.length" class="added-members">
        <text class="members-label">已添加成员:</text>
        <view v-for="member in addedMembers" :key="member.id" class="member-item">
          <text>{{ member.username }} ({{ member.email }})</text>
        </view>
      </view>
    </view>
  </view>
</template>

<script>
export default {
  props: {
    projectId: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      searchUsername: '',
      searchResult: null,
      addedMembers: []
    };
  },
  methods: {
    // 搜索用户方法
    async searchUser() {
      if (!this.searchUsername.trim()) {
        uni.showToast({
          title: '请输入用户名进行搜索',
          icon: 'none'
        });
        return;
      }
    
      try {
        const token = uni.getStorageSync('access');
        if (!token) {
          uni.showToast({
            title: '请先登录',
            icon: 'none'
          });
          return;
        }
    
        const response = await new Promise((resolve, reject) => {
          uni.request({
            url: `http://127.0.0.1:8000/api/accounts/searchUser/`,
            method: 'GET',
            data: { username: this.searchUsername },
            header: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${token}`
            },
            success: (res) => resolve(res),
            fail: (error) => reject(error)
          });
        });

        // 解构返回的结果
        const { statusCode, data } = response;

        if (statusCode === 200) {
          this.searchResult = data; // 存储搜索结果
        } else {
          this.searchResult = null; // 清空搜索结果
          uni.showToast({
            title: data.detail || '未找到用户',
            icon: 'none'
          });
        }
      } catch (error) {
        console.error('搜索用户失败:', error);
        uni.showToast({
          title: '搜索用户失败',
          icon: 'none'
        });
      }
    },

    // 邀请成员方法
    async inviteMember(user) {
      try {
        const token = uni.getStorageSync('access');
        if (!token) {
          uni.showToast({
            title: '请先登录',
            icon: 'none'
          });
          return;
        }

        const response = await new Promise((resolve, reject) => {
          uni.request({
            url: `http://127.0.0.1:8000/api/projects/${this.projectId}/addMember/`,
            method: 'POST',
            data: { user_id: user.id },
            header: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${token}`
            },
            success: (res) => resolve(res),
            fail: (error) => reject(error)
          });
        });

        const { statusCode, data } = response;

        if (statusCode === 200) {
          uni.showToast({
            title: '成员已添加',
            icon: 'success'
          });
          this.addedMembers.push(user);
          this.searchResult = null; // 清空搜索结果
          this.searchUsername = ''; // 清空搜索输入
        } else {
          uni.showToast({
            title: data.detail || '添加成员失败',
            icon: 'none'
          });
        }
      } catch (error) {
        console.error('添加成员失败:', error);
        uni.showToast({
          title: '添加成员失败',
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
  padding-bottom: 60px; /* 留出底部导航栏的空间 */
}

.form {
  display: flex;
  flex-direction: column;
}

.input-group {
  margin-bottom: 15px;
  display: flex;
  align-items: center;
}

.label {
  font-size: 16px;
  margin-right: 10px;
  width: 150px;
}

.input {
  flex: 1;
  height: 40px;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.search-button {
  margin-left: 10px;
  height: 40px;
  padding: 0 15px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 5px;
}

.search-result {
  margin-bottom: 20px;
}

.result-label {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 10px;
}

.user-info {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.username {
  font-size: 16px;
  font-weight: bold;
}

.email {
  font-size: 14px;
  color: #555;
  margin-right: 20px;
}

.invite-button {
  height: 35px;
  padding: 0 10px;
  background-color: #007AFF;
  color: white;
  border: none;
  border-radius: 5px;
}

.invite-button:disabled {
  background-color: #ccc;
}

.added-members {
  margin-top: 20px;
}

.members-label {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 10px;
}

.member-item {
  font-size: 14px;
  margin-bottom: 5px;
}
</style>
