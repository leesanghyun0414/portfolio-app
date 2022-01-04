<template>
  <ul>
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
    const { result } = useQuery(GET_ALLCATEGORY)
    const category = useResult(result, null, (data) => data.allCategory)

    return {
      result,
      category,
    }
  },
})
</script>
