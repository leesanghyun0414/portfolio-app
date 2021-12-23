import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router"

import MapPage from "../pages/MapPage.vue"
import InformationPage from "../pages/InformationPage.vue"

const routes: RouteRecordRaw[] = [
  {
    path: "/map",
    component: MapPage,
    name: "MapPage",
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
