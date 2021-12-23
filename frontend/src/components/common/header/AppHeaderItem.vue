<template>
  <div class="col-span-2 p-2">
    <p>Sq</p>
  </div>
  <div
    v-for="headerItem in headerItems"
    :key="headerItems.indexOf(headerItem)"
    class="p-2"
  >
    <p>{{ headerItem }}</p>
  </div>
</template>


<script lang="ts">
import {defineComponent} from "vue"

export default defineComponent({
  name: "AppHeaderItem"
  ,
  setup() {
    const headerItems = ["Menu","Info","Map"]

  return {
      headerItems
  }
  }
})
</script>

<style scoped>

</style>
