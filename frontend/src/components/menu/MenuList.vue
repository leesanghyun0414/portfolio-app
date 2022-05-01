<template>
  <li
    v-for="menu in menus"
    :key="menu.menu_id"
  >
    <MenuItem :menu="menu" />
  </li>
</template>

<script lang="ts">
import { defineComponent } from "vue"
import MenuItem from "./MenuItem.vue"
import { setup } from "vue-class-component"

export default defineComponent({
  name: "MenuList",
  components: {
MenuItem
  },
  props: {
    menus: {
      type: Object,
      required: true,
    }
  },


})
</script>

<style scoped>

</style>