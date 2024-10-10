<template> 
  <view class="container">
    <!-- 顶部搜索栏 -->
    <view class="search-bar">
      <input
        type="text"
        v-model="searchQuery"
        placeholder="搜索联系人"
        @input="filterContacts"
      />
    </view>

    <!-- 中间联系人列表 -->
    <scroll-view class="contact-list" scroll-y="true">
      <view
        v-if="filteredContacts.length === 0"
        class="no-results"
      >
        没有找到匹配的联系人
      </view>
      <view
        v-for="(contact, index) in filteredContacts"
        :key="index"
        class="contact-item"
        @click="goToChat(contact)"
      >
        {{ contact.name }}
      </view>
    </scroll-view>

    <!-- 底部导航栏，固定在页面底部 -->
    <NavBar :activeTab="3" />
      </view>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '',
      contacts: [
        { name: '联系人1' },
        { name: '联系人2' },
        { name: '联系人3' }
      ],
      filteredContacts: []
    };
  },
  methods: {
    filterContacts() {
      this.filteredContacts = this.contacts.filter(contact =>
        contact.name.includes(this.searchQuery)
      );
    },
    goToChat(contact) {
      uni.navigateTo({
        url: `/pages/chat/chat?contactName=${contact.name}`
      });
    },
    navigateTo(page) {
      let url = '';
      switch (page) {
        case 'main':
          url = '/pages/main/main';  // 跳转到主界面
          break;
        case 'project':
          url = '/pages/project/project';  // 跳转到项目详情
          break;
        case 'contact':
          url = '/pages/contact/contact';  // 跳转到联系人
          break;
        case 'profile':
          url = '/pages/profile/profile';  // 跳转到个人信息
          break;
      }
      uni.navigateTo({
        url: url
      });
    }
  },
  mounted() {
    this.filteredContacts = this.contacts; // 初始化联系人列表
  }
};
</script>

<style scoped>
/* 容器布局，确保底部导航栏固定在底部 */
.container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

/* 顶部搜索栏样式 */
.search-bar {
  padding: 10px;
  background-color: #f8f8f8;
  border-bottom: 1px solid #ddd;
}

.search-bar input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

/* 中间联系人列表样式，允许内容滚动 */
.contact-list {
  flex: 1;
  padding: 10px;
  padding-bottom: 60px;
  overflow-y: auto; /* 联系人过多时允许滚动 */
}

/* 没有匹配结果的提示样式 */
.no-results {
  padding: 15px;
  text-align: center;
  color: #999;
}

/* 每个联系人项的样式 */
.contact-item {
  padding: 15px;
  border-bottom: 1px solid #ddd;
  cursor: pointer;
}

/* 底部导航栏，固定在底部 */
.bottom-nav {
  display: flex;
  justify-content: space-around;
  padding: 10px;
  background-color: #fff;
  border-top: 1px solid #ddd;
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  z-index: 1000; /* 确保导航栏位于最顶层，不被覆盖 */
}

.bottom-nav view {
  flex: 1;
  text-align: center;
  padding: 10px 0;
  cursor: pointer;
}
</style>
