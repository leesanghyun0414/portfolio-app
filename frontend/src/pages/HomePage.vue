<template>
  <AppHeader />
  <router-view />
</template>
<script lang="ts">
import { defineComponent } from "vue"
import AppHeader from "../components/common/header/AppHeader.vue"
// import { router } from "../router/router"

export default defineComponent({
  name: "HomePage",
  components: { AppHeader },
  // setup() {
  //   const clicked = (): void => {
  //     router.push({ name: "InformationPage" })
  //   }
  //   return {
  //     clicked
  //   }
  // }

})
</script>

<style scoped>

</style>
