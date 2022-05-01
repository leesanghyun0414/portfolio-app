<script setup lang="ts">
import { useQuery, useResult } from "@vue/apollo-composable"
import { GET_ALLCATEGORY } from "../../api/graphql/querys"

const { result, loading } = useQuery(GET_ALLCATEGORY)
const categories = useResult(result, null, (data) => data.allCategory)


</script>

<template>
  <div
    v-if="loading"
    class="animate-pulse delay-150 rounded-0 shadow-lg bg-slate-200 grid animate-pulse  mx-auto text-sm lg:text-lg md:text-md lg:mx-0 grid-cols-none md:grid-cols-2 lg:grid-cols-3 auto-cols-fr gap-24"
  >
    <div class="w-screen h-screen" />
  </div>
  <div
    v-else
    class="px-4 grid grow gap-y-10"
  >
    <div
      v-for="category in categories"
      :key="category.id"
      class="grid gap-y-5"
    >
      <p class="text-header-base  md:text-header-lg  font-bold">
        {{ category.data.name }}
      </p>
      <MenuCategoryItem :children="category.children" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue"
import MenuCategoryItem from "./MenuCategoryItem.vue"

export default defineComponent({
  name: "MenuCategory",
  components: {
    MenuCategoryItem
  }
})
</script>

<style scoped>

</style>