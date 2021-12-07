import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router"
import PostPreview from "../pages/PostPreview.vue"
import HelloWorld from "../components/HelloWorld.vue"
// import PostDetail from "../pages/PostDetail.vue"

const routes: RouteRecordRaw[] = [
  { path: "/", component: HelloWorld, name: "HelloWorld" },
  {
    path: "/post",
    component: PostPreview,
    name: "Posts",
    props: true,
  },
  {
    path: "/hello",
    component: HelloWorld,
    name: "Root",
    props: true,
  },
  // {
  //   path: "/post/:postId",
  //   component: PostDetail,
  //   name: "PostDetail",
  //   props: true,
  // },
]

export const router = createRouter({
  history: createWebHashHistory(),
  routes,
})
