<script setup>
import { ref, computed } from 'vue'
import { RouterLink, useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const route = useRoute()

// 控制底部导航栏显示
const showBottomNav = computed(() => {
  // 在文章详情页隐藏底部导航
  return !route.path.includes('/article/detail')
})
</script>

<template>
  <div class="app">
    <RouterView />
    
    <!-- 底部导航栏 -->
    <div class="bottom-nav" v-if="showBottomNav">
      <router-link to="/home" class="nav-item">
        <span class="icon">🏠</span>
        <span>首页</span>
      </router-link>
      <router-link to="/plaza" class="nav-item">
        <span class="icon">🌎</span>
        <span>关注</span>
      </router-link>
      <router-link to="/post/create" class="nav-item">
        <div class="post-btn">+</div>
      </router-link>
      <router-link to="/message" class="nav-item">
        <span class="icon">💬</span>
        <span>消息</span>
      </router-link>
      <router-link to="/profile" class="nav-item">
        <span class="icon">👤</span>
        <span>我的</span>
      </router-link>
    </div>
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
    Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

.app {
  max-width: 600px;
  margin: 0 auto;
  min-height: 100vh;
  padding-bottom: 60px;
}

.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 50px;
  background: #fff;
  display: flex;
  justify-content: space-around;
  align-items: center;
  border-top: 1px solid #eee;
  max-width: 600px;
  margin: 0 auto;
}

.nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-decoration: none;
  color: #666;
  font-size: 12px;
}

.nav-item .icon {
  font-size: 20px;
  margin-bottom: 2px;
}

.post-btn {
  width: 35px;
  height: 35px;
  background: #000;
  color: #fff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  margin-bottom: -10px;
}

.router-link-active {
  color: #333;
}
</style>