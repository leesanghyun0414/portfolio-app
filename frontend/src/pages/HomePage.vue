<template>
  <AppHeader />
</template>
<script lang="ts">
import {defineComponent} from "vue"
import AppHeader from "../components/common/header/AppHeader.vue"

export default defineComponent({
  name: "HomePage",
  components: {AppHeader}
})
</script>

<style scoped>

</style>
