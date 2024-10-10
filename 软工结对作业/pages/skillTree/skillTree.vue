<template>
  <view class="container">

    <text class="title">技能树</text>
    
    <view class="skill-container">
      <!-- 使用 v-for 循环渲染每个技能输入框 -->
      <view class="skill-item" v-for="(skill, index) in skills" :key="index">
        <textarea
          placeholder="请输入技能名称"
          v-model="skill.name"
          class="skill-input"
        />
      </view>

      <!-- 添加技能按钮 -->
      <button class="add-skill" @click="addSkill">添加技能</button>
    </view>

    <!-- 提交按钮 -->
    <view class="button">
      <button type="primary" @click="submitSkills">提交</button>
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
      skills: [
        { name: '' } // 初始一个空的技能输入框
      ]
    };
  },
  methods: {
    addSkill() {
      // 添加一个新的技能输入框
      this.skills.push({ name: '' });
    },
    submitSkills() {
      // 检查所有输入框是否填写完整
      const allFilled = this.skills.every(skill => skill.name.trim() !== '');
      if (!allFilled) {
        uni.showToast({
          title: '请填写完整技能信息',
          icon: 'none'
        });
        return;
      }

      // 提交逻辑（可将数据发送到服务器）
      uni.showModal({
        title: '提交成功',
        content: '您的技能已成功提交',
        showCancel: false,
        success: (res) => {
          if (res.confirm) {
            console.log('用户点击确定');
            // 提交成功后可以清空技能输入框
            this.skills = [{ name: '' }];
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

.title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.skill-container {
  margin-bottom: 30px;
}

.skill-item {
  margin-bottom: 15px;
}

.skill-input {
  width: 100%; /* 宽度设为100% */
  height: 80px; /* 高度增大 */
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px; /* 增大字体 */
  box-sizing: border-box;
}

.add-skill {
  background-color: #007AFF;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 12px;
  font-size: 16px; /* 增大按钮字体 */
  cursor: pointer;
}

.button {
  margin-top: 20px;
}

button {
  width: 100%;
  height: 50px; /* 提交按钮高度增大 */
  background-color: #007AFF;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px; /* 提交按钮字体增大 */
}
</style>
