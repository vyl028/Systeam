<template>
  <div class="container">
    <div class="form">
      <input v-model="username" placeholder="请输入用户名" class="input" />
      <input v-model="password" type="password" placeholder="请输入密码" class="input" />
      <input v-model="confirmPassword" type="password" placeholder="请确认密码" class="input" />
      <button @click="handleRegister" class="btn">注册</button>
      
      <div class="login-link">
        <router-link to="/login">已有账号？点击登录</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const userStore = useUserStore()
const username = ref('')
const password = ref('')
const confirmPassword = ref('')

const handleRegister = async () => {
  if (!username.value || !password.value || !confirmPassword.value) {
    showToast('请填写完整信息')
    return
  }

  if (password.value !== confirmPassword.value) {
    showToast('两次密码不一致')
    return
  }

  try {
    await userStore.register(username.value, password.value)
    showToast('注册成功')
    router.push('/login')
  } catch (error) {
    showToast('注册失败')
  }
}
</script>

<style scoped>
.container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f5f5f5;
  padding: 20px;
}

.form {
  width: 100%;
  max-width: 400px;
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.input {
  width: 100%;
  padding: 12px;
  margin-bottom: 15px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

.btn {
  width: 100%;
  padding: 12px;
  background: #007AFF;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
}

.login-link {
  margin-top: 15px;
  text-align: center;
}

.login-link a {
  color: #007AFF;
  text-decoration: none;
}
</style>
