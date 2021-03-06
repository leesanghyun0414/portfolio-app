import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router"
import MapPage from "../pages/MapPage.vue"
import HomePage from "../pages/HomePage.vue"
import MenuPage from "../pages/MenuPage.vue"
import MenuCategory from "../components/menu_category/MenuCategory.vue"
import Menu from "../components/menu/Menu.vue"
import MenuDetail from "../components/MenuDetail/MenuDetail.vue"

const routes: RouteRecordRaw[] = [
  { path: "/", component: HomePage, name: "HomePage" },
  {
    path: "/map",
    component: MapPage,
    name: "MapPage",
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
        path: "list/:menuName/:categoryId",
        component: Menu,
        props: true,
        name: "Menu",
      },
      {
        path:"menuDetail/:menuId",
        component: MenuDetail,
        props:true,
        name:"MenuDetail",

      },
    ],
    name: "MenuPage",
  },


]

export const router = createRouter({
  history: createWebHashHistory(),
  routes,
})
