<template>
  <div v-if="loading">
    <p>Loading...</p>
  </div>

  <ul 
    v-else 
    class="hidden md:grid md:gap-y-7 md:text-navbar-base text-2xl text-regal-blue place-items-start text-left font-bold tracking-wider text-lg "
  >
    <NavBarList
      v-for="item in category"
      :key="item.id"
      :category-item="item"
    />
  </ul>
</template> 

<script lang="ts">
import { defineComponent } from "vue"
import { useQuery, useResult } from "@vue/apollo-composable"
import { GET_ALLCATEGORY } from "../../../api/graphql/querys"
import NavBarList from "./NavBarList.vue"

export default defineComponent({
  name: "MenuNavBar",

  components: { NavBarList },
  setup() {
    const { result, loading } = useQuery(GET_ALLCATEGORY)
    const category = useResult(result, null, (data) => data.allCategory)
  console.log(category)
    return {
      result,
      category,
      loading
    }
  },
})
</script>
