<template>
  <div class="grid grid-column-4 gap-4">
    <HeaderItem />
  </div>
</template>
<script lang="ts">
import {defineComponent} from "vue"
import HeaderItem from "./HeaderItem.vue"


export default defineComponent({
  name: "Header",
  components: {HeaderItem},
})
</script>

<style scoped>

</style>
