<template>
  <div class="grid grid-cols-5 gap-4 px-2">
    <AppHeaderItem />
  </div>
</template>
<script lang="ts">
import {defineComponent} from "vue"
import AppHeaderItem from "./AppHeaderItem.vue"


export default defineComponent({
  name: "AppHeader",
  components: {AppHeaderItem},
})
</script>

<style scoped>

</style>
