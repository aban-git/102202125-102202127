<template>
  <view class="container">
    <nav-bar :activeTab="2" /> <!-- 导航栏 -->

    <view class="task-input">
      <input 
        v-model="newTask" 
        placeholder="输入任务名称" 
        class="task-input-field" 
      />
      <button @click="addTask" class="add-task-button">添加任务</button>
    </view>

    <view class="task-list">
      <view 
        v-for="(task, index) in tasks" 
        :key="index" 
        class="task-item"
      >
        {{ task }}
        <button @click="removeTask(index)" class="remove-task-button">移除</button>
      </view>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      newTask: '',  // 存储新任务的名称
      tasks: []     // 存储任务列表
    };
  },
  methods: {
    addTask() {
      if (this.newTask.trim()) {  // 确保任务名称不为空
        this.tasks.push(this.newTask.trim()); // 将新任务添加到任务列表
        this.newTask = ''; // 清空输入框
      } else {
        uni.showToast({
          title: '请输入任务名称',
          icon: 'none'
        });
      }
    },
    removeTask(index) {
      this.tasks.splice(index, 1); // 从任务列表中移除指定任务
    }
  }
};
</script>

<style scoped>
.container {
  padding: 20px;
  padding-bottom: 60px; /* 留出底部导航栏的空间 */
}

.task-input {
  display: flex;
  margin-bottom: 20px;
}

.task-input-field {
  flex: 1;
  height: 40px;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 0 10px;
}

.add-task-button {
  height: 40px;
  margin-left: 10px;
  background-color: #007AFF;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px;
}

.task-list {
  display: flex;
  flex-direction: column;
}

.task-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 10px;
}

.remove-task-button {
  background-color: red;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 5px 10px;
}
</style>
