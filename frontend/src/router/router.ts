import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router"
import MenuPage from "../pages/MenuPage.vue"

import MapPage from "../pages/MapPage.vue"
import InformationPage from "../pages/InformationPage.vue"
import Menu from "../components/menu/Menu.vue"
import MenuCategory from "../components/menu_category/MenuCategory.vue"
import HomePage from "../pages/HomePage.vue"

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
