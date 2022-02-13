import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router"
import MapPage from "../pages/MapPage.vue"
import HomePage from "../pages/HomePage.vue"
import MenuPage from "../pages/MenuPage.vue"
import MenuCategory from "../pages/MenuCategory.vue"
import Menu from "../components/menu/Menu.vue"
import InformationPage from "../pages/InformationPage.vue"

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
        path: "list/:menuName",
        component: Menu,
        props: true,
        name: "Menu",
      },
    ],
    name: "MenuPage",
  },
]

export const router = createRouter({
  history: createWebHashHistory(),
  routes,
})
