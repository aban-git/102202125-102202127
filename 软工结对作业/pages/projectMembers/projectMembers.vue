<template>
  <view class="container">
    <text class="title">项目成员</text>

    <view class="member-list">
      <view 
        v-for="(member, index) in members" 
        :key="index" 
        class="member-item"
      >
        <view class="member-info">
          <text class="member-name">{{ member.username }}</text> <!-- 假设成员对象有username字段 -->
          
        </view>
        <button @click="removeMember(index)" class="remove-member-button">移除</button>
      </view>
    </view>

    <button @click="inviteMember" class="invite-member-button">邀请成员</button>
  </view>
</template>

<script>
export default {
  data() {
    return {
      members: [] // 成员数据
    };
  },
  mounted() {
    this.fetchMembers();
  },
  methods: {
    fetchMembers() {
      // 这里替换为实际的API请求来获取成员信息
      uni.request({
        url: 'http://127.0.0.1:8000/api/accounts/projectCreate/', // 后端API路径
        method: 'GET',
        success: (res) => {
          if (res.statusCode === 200) {
            this.members = res.data; // 假设后端返回的数据结构与成员字段一致
          } else {
            uni.showToast({
              title: '获取成员信息失败',
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
    removeMember(index) {
      this.members.splice(index, 1); // 从成员列表中移除指定成员
    },
    inviteMember() {
      uni.showToast({
        title: '邀请功能待开发',
        icon: 'none'
      });
    }
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

.member-list {
  display: flex;
  flex-direction: column;
}

.member-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 10px;
}

.member-info {
  display: flex;
  flex-direction: column;
}

.member-name {
  font-size: 18px;
  font-weight: bold;
}

.member-role {
  font-size: 14px;
  color: gray;
}

.remove-member-button {
  background-color: red;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 5px 10px;
}

.invite-member-button {
  margin-top: 20px;
  height: 40px;
  background-color: #007AFF;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px;
}
</style>
