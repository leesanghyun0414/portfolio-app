import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router"
import PostPreview from "../pages/PostPreview.vue"
import HelloWorld from "../components/HelloWorld.vue"
import MapPage from "../pages/MapPage.vue"
import InformationPage from "../pages/InformationPage.vue"

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
  {
    path: "/map",
    component: MapPage,
    name: "",
  },

  {
    path: "/information",
    component: InformationPage,
    name: "",
  },
]

export const router = createRouter({
  history: createWebHashHistory(),
  routes,
})
