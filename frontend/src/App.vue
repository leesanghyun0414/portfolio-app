<template>
  <div class="flex flex-col min-h-screen gap-y-10">
    <AppHeader />
    <router-view />
    <AppFooter />
  </div>
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

  margin-left: auto
  margin-right: auto
  max-width: 1536px

img
  display: inline !important

</style>
