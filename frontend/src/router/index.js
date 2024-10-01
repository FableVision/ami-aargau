import { createRouter, createWebHashHistory } from 'vue-router'
import GameView from '../views/MainScreen.vue'
import TitleView from '../views/TitleScreen.vue'
import AdminScreen from '../views/AdminScreen.vue'
import EndScreen from '../views/EndScreen.vue'

const router = createRouter({
  history: createWebHashHistory(),
  mode: 'hash',
  routes: [
    {
      path: '/game',
      name: 'game',
      component: GameView
    },
    {
      path: '/title',
      name: 'titlescreen',
      component: TitleView
    },
    {
      path: '/admin',
      name: 'adminscreen',
      component: AdminScreen
    },
    {
      path: '/end',
      name: 'end',
      component: EndScreen
    }
  ]
})

export default router
