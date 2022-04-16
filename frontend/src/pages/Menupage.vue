<template>
  <div class="flex flex-row md:gap-x-20">
<!--    <MenuNavBar />-->
    <router-view />
  </div>
</template>





<script lang="ts">

import {defineComponent} from "vue"

import MenuNavBar from "../components/common/NavBar/MenuNavBar.vue"

export default defineComponent({
  name: "MenuPage",
  components: {MenuNavBar}
  ,
})
</script>

