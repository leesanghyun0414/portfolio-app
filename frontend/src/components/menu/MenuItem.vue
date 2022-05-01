<script setup lang="ts">
import { ASSET_ROOT } from "../../config/api_roots"
import { router } from "../../router/router"
function moveMenuDetail(menuId: number): void {
  router.push({name: "MenuDetail", params: {menuId: menuId}})
}
</script>


<template>
  <div
    class="text-center text-regal-blue font-bold cursor-pointer text-lg  lg:text-xl"
    @click="moveMenuDetail(menu.menuId)"
  >
    <div>
      <img
        :src="ASSET_ROOT + menu.image"
        alt="Image"
        class="w-full bg-cover "
      >
    </div>
    <div class="py-2">
      <p>
        {{ menu.name }}
      </p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue"

export default defineComponent({
  name: "MenuItem",
  props: {
    menu: {
      required: true,
      type: Object
    }
  },
  setup(props) {
    // localStorage.setItem("menu_name", props.menu.name)
    // localStorage.setItem("menu_image", props.menu.image)
  }
})
</script>

<style scoped>

</style>