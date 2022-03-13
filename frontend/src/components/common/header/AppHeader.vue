<template>
  <header class="mb-10 h-20">
    <nav class="h-full">
      <AppHeaderItem />
    </nav>
  </header>
</template>
<script lang="ts">
import { defineComponent } from "vue"
import AppHeaderItem from "./AppHeaderItem.vue"

export default defineComponent({
  name: "AppHeader",
  components: { AppHeaderItem }
})
</script>

<style scoped>

</style>
