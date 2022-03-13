<template>
  <AppHeader />
  <router-view />
</template>

<script lang="ts">
import {defineComponent} from "vue"
import AppHeader from "./components/common/header/AppHeader.vue"

export default defineComponent({
  name: "App",
  components: { AppHeader },
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
