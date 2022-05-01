<template>
  <div
    v-if="loading"
    class="animate-pulse rounded-0 shadow-lg bg-slate-200 grid animate-pulse  mx-auto text-sm lg:text-lg md:text-md lg:mx-0 grid-cols-none md:grid-cols-2 lg:grid-cols-3 auto-cols-fr gap-24"
  >
    <div class="w-screen h-screen" />
  </div>
  <ul
    v-else
    class="grid mx-auto text-sm lg:text-lg md:text-md lg:mx-0 grid-cols-none md:grid-cols-2 lg:grid-cols-3 auto-cols-fr gap-24 "
  >
    <MenuList :menus="menus" />
  </ul>
</template>

<script lang="ts">
import { defineComponent, toRefs, watch } from "vue"

import { GET_MENU_BY_CATEGORY_ID } from "../../api/graphql/querys"
import { useQuery, useResult } from "@vue/apollo-composable"
import MenuList from "./MenuList.vue"


export default defineComponent({
  name: "Menu",
  components: {
    MenuList
  },
  props: {
    menuName: {
      type: String,
      required: true
    },
    categoryId: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const {result, loading, refetch } = useQuery(GET_MENU_BY_CATEGORY_ID, { categoryId: props.categoryId })
    let menus = useResult(result, null, (data) => data.menuByCategoryId)
    watch( () => props.categoryId, (newData) =>{
     refetch({categoryId: newData})
    })
  return {
      loading,
      menus,
  }
  }
})
</script>
