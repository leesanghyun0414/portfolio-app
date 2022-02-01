import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router"
import PostPreview from "../pages/PostPreview.vue"
import HelloWorld from "../components/HelloWorld.vue"
// import PostDetail from "../pages/PostDetail.vue"

const routes: RouteRecordRaw[] = [
  {path: "/", component: HomePage, name:"Homepage"},
  {
    path: "/map",
    component: MapPage,
    name: "Map",
  },
  {
    path: "/menu",
    component: MenuPage,
    children: [
      {
        path: "",
        component: MenuCategory,
        name: "MenuCategory",
      },
      {
        path: "list/:menuName",
        component: Menu,
        props: true,
        name: "Menu",
      },
    ],
    name: "MenuPage",
  },
  {
    path: "/information",
    component: InformationPage,
    name: "InformationPage",
  },
]

export const router = createRouter({
  history: createWebHashHistory(),
  routes,
})
