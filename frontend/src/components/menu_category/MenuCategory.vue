<script setup lang="ts">
import { useQuery, useResult } from "@vue/apollo-composable"
import { GET_ALLCATEGORY } from "../../api/graphql/querys"

const { result, loading } = useQuery(GET_ALLCATEGORY)
const categories = useResult(result, null, (data) => data.allCategory)


</script>

<template>
  <div class="px-4 grid grow gap-y-10">
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