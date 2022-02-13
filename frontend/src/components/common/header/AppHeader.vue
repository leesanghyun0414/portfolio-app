<template>
  <AppHeaderItem />
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
