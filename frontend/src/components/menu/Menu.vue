<template>
  <p v-if="!loading">
    {{ menuName }}
  </p>
  <p>{{ menus }}</p>
</template>

<script lang="ts">
import { defineComponent } from "vue"

import { GET_MENU_BY_CATEGORY_ID } from "../../api/graphql/querys"
import { useQuery, useResult } from "@vue/apollo-composable"

export default defineComponent({
  name: "Menu",
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
    console.log(props.categoryId)
    const {result, loading} = useQuery(GET_MENU_BY_CATEGORY_ID, { categoryId: props.categoryId })
    const menus = useResult(result, null, (data) => data.menuByCategoryId)
  return {
      loading,
      menus
  }
  }
})
</script>
