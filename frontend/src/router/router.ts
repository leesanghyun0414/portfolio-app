import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router"
import MenuPage from "../pages/Menupage.vue"

import MapPage from "../pages/MapPage.vue"
import InformationPage from "../pages/InformationPage.vue"
import HomePage from "../pages/HomePage.vue"

const routes: RouteRecordRaw[] = [
  { path: "/", component: HomePage, name: "Home" },
  {
    path: "/map",
    component: MapPage,
    name: "Map",
  },
  {
    path: "/menu",
    component: MenuPage,
    name: "MenuPage",
    props: false,
  },
  {
    path: "/information",
    component: InformationPage,
    name: "Information",
  },
]

export const router = createRouter({
  history: createWebHashHistory(),
  routes,
})
