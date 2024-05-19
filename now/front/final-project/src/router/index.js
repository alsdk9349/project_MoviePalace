import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/HomeView.vue')
    },
    {
      path:'/recommend',
      name : 'recommend',
      component: () =>import('@/views/RecommendView.vue')
    },
    {
      path:'/search',
      name : 'search',
      component: () =>import('@/views/SearchView.vue')
    },
    {
      path:'/community',
      name : 'community',
      component: () =>import('@/views/CommunityView.vue')
    },
    {
      path:'/:movieId',
      name : 'detail',
      component: () =>import('@/views/ArticleDetailView.vue')
    },
    {
      path:'/community/:movieId',
      name : 'moviecommunity',
      component: () =>import('@/views/MovieCommunityView.vue')
    },

  ]
})

export default router
