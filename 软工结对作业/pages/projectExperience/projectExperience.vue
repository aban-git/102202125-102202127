<template>
  <view class="container">
     <!-- 导航栏 -->
    
    <view class="section">
      <text class="section-title">项目经历</text>
      <view class="input-item" v-for="(project, index) in projects" :key="index">
        <text>项目名称：</text>
        <input type="text" placeholder="请输入项目名称" v-model="project.name" />
      </view>
      <view class="input-item" v-for="(project, index) in projects" :key="'desc' + index">
        <text>项目描述：</text>
        <input type="text" placeholder="请输入项目描述" v-model="project.description" />
      </view>
      <button @click="addProject">添加项目</button>
    </view>

    <view class="section">
      <text class="section-title">获奖情况</text>
      <view class="input-item" v-for="(award, index) in awards" :key="index">
        <text>奖项名称：</text>
        <input type="text" placeholder="请输入奖项名称" v-model="award.name" />
      </view>
      <view class="input-item" v-for="(award, index) in awards" :key="'year' + index">
        <text>获奖年份：</text>
        <input type="text" placeholder="请输入获奖年份" v-model="award.year" />
      </view>
      <button @click="addAward">添加奖项</button>
    </view>

    <!-- 提交按钮 -->
    <view class="button">
      <button type="primary" @click="submitExperience">提交</button>
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
      projects: [
        { name: '', description: '' } // 默认项目
      ],
      awards: [
        { name: '', year: '' } // 默认奖项
      ]
    };
  },
  methods: {
    addProject() {
      this.projects.push({ name: '', description: '' }); // 添加新项目
    },
    addAward() {
      this.awards.push({ name: '', year: '' }); // 添加新奖项
    },
    submitExperience() {
      // 提交项目经历与获奖情况的逻辑
      const allFilled = this.projects.every(project => project.name && project.description) &&
                        this.awards.every(award => award.name && award.year);
      if (!allFilled) {
        uni.showToast({
          title: '请填写完整信息',
          icon: 'none'
        });
        return;
      }

      // 这里可以添加逻辑，比如将数据发送到服务器等
      uni.showModal({
        title: '成功',
        content: '您的项目经历与获奖情况已成功提交',
        showCancel: false,
        success: (res) => {
          if (res.confirm) {
            console.log('用户点击确定');
            // 清空输入框或执行其他操作
            this.projects = [{ name: '', description: '' }];
            this.awards = [{ name: '', year: '' }];
          }
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

.section {
  margin-bottom: 30px;
}

.section-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
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
