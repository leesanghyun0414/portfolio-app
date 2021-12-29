import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router"
import PostPreview from "../pages/PostPreview.vue"
import HelloWorld from "../components/HelloWorld.vue"
// import PostDetail from "../pages/PostDetail.vue"
import MenuPage from "../pages/MenuPage.vue"
const routes: RouteRecordRaw[] = [

  
{
  path: "/menu",
  component: MenuPage,
  name: "MenuPage",
  props: false,
}
]

export const router = createRouter({
  history: createWebHashHistory(),
  routes,
})
