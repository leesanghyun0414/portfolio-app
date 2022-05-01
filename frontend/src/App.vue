<template>
  <AppHeader />
  <router-view />
  <AppFooter />
</template>

<script lang="ts">
import {defineComponent} from "vue"
import AppHeader from "./components/common/header/AppHeader.vue"
import AppFooter from "./components/common/footer/AppFooter.vue"

export default defineComponent({
  name: "App",
  components: { AppHeader, AppFooter },
  
})
</script>

<style lang="sass">

#counter
  padding-left: 1rem
  padding-right: 1rem
  //align-items: center
  //margin-left: auto
  //margin-right: auto
  //max-width: 1536px

img
  display: inline !important

</style>
