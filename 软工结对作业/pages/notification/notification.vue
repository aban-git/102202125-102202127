<template>
  <view class="notification-container">
    <view class="header">
      <text class="title">消息通知</text>
    </view>

    <view class="notification-section">
      <text class="section-title">申请通知</text>
      <view class="notification-list">
        <view v-for="(notification, index) in applicationNotifications" :key="index" class="notification-item">
          <view class="icon">
            <image :src="notification.icon" mode="aspectFill" />
          </view>
          <view class="details">
            <text class="notification-title">{{ notification.title }}</text>
            <text class="notification-time">{{ notification.time }}</text>
            <text class="notification-content">{{ notification.content }}</text>
          </view>
        </view>
      </view>
    </view>

    <view class="notification-section">
      <text class="section-title">邀请通知</text>
      <view class="notification-list">
        <view v-for="(notification, index) in invitationNotifications" :key="index" class="notification-item">
          <view class="icon">
            <image :src="notification.icon" mode="aspectFill" />
          </view>
          <view class="details">
            <text class="notification-title">{{ notification.title }}</text>
            <text class="notification-time">{{ notification.time }}</text>
            <text class="notification-content">{{ notification.content }}</text>
          </view>
        </view>
      </view>
    </view>

    <view class="notification-section">
      <text class="section-title">好友申请</text>
      <view class="notification-list">
        <view v-for="(notification, index) in friendRequests" :key="index" class="notification-item">
          <view class="icon">
            <image :src="notification.icon" mode="aspectFill" />
          </view>
          <view class="details">
            <text class="notification-title">{{ notification.title }}</text>
            <text class="notification-time">{{ notification.time }}</text>
            <text class="notification-content">{{ notification.content }}</text>
          </view>
        </view>
      </view>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      applicationNotifications: [
        {
          icon: 'https://example.com/app-icon1.png',
          title: '项目A的申请',
          time: '2024-10-09 10:00',
          content: '您提交的项目A申请已审核通过。'
        },
        {
          icon: 'https://example.com/app-icon2.png',
          title: '项目B的申请',
          time: '2024-10-08 15:30',
          content: '您的项目B申请被拒绝。'
        }
      ],
      invitationNotifications: [
        {
          icon: 'https://example.com/invite-icon1.png',
          title: '邀请您加入项目C',
          time: '2024-10-07 09:45',
          content: '李四邀请您加入项目C。'
        }
      ],
      friendRequests: [
        {
          icon: 'https://example.com/friend-icon1.png',
          title: '好友请求',
          time: '2024-10-06 12:30',
          content: '王五请求添加您为好友。'
        }
      ]
    };
  }
};
</script>

<style scoped>
.notification-container {
  padding: 20px;
  background-color: #f5f5f5;
  height: 100vh; /* 满屏高度 */
}

.header {
  margin-bottom: 20px;
}

.title {
  font-size: 24px;
  font-weight: bold;
}

.notification-section {
  margin-bottom: 20px;
}

.section-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
}

.notification-list {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.notification-item {
  display: flex;
  padding: 15px;
  border-bottom: 1px solid #eee;
}

.notification-item:last-child {
  border-bottom: none; /* 最后一项不显示下边框 */
}

.icon {
  margin-right: 10px;
}

.details {
  flex: 1;
}

.notification-title {
  font-weight: bold;
  font-size: 16px;
}

.notification-time {
  color: #999;
  font-size: 12px;
}

.notification-content {
  font-size: 14px;
  color: #555;
}
</style>
