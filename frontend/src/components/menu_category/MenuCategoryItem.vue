<script setup lang="ts">
import { ASSET_ROOT } from "../../config/api_roots"
import { router } from "../../router/router"

function moveMenuList(categoryId: string, menuName: string): void {
  menuName = menuName.replace(/\s+/g,"")
  router.push({name: "Menu", params: { categoryId: categoryId , menuName: menuName }})
}
</script>

<template>
  <div class="inline-grid gap-x-5 grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-y-5">
    <div
      v-for="child in children"
      :key="child.data.id"
      class="inline-grid text-regal-blue font-semibold items-center place-items-center text-xl md:text-2xl cursor-pointer"
      @click="moveMenuList(child.id, child.data.name)"
    >
      <div class="shadow-md">
        <a>
          <img
            :src="ASSET_ROOT + child.data.image"
            class="w-full  lg:h-96 md:h-80 h-60 aspect-square object-contain"
            alt="Menu Image"
          >
        </a>
      </div>
      <p>{{ child.data.name }}</p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue"
import { setup } from "vue-class-component"


export default defineComponent({
  name: "MenuCategoryItem"
  ,
  props: {
    children: {
      type: Object,
      required: false
    }

  }

})
</script>

<style scoped>

</style>