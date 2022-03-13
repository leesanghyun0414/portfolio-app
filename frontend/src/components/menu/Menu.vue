<script setup lang="ts">
import { useQuery, useResult } from "@vue/apollo-composable"
import { GET_MENU_BY_CATEGORY_ID } from "../../api/graphql/querys"

const menus = useQuery(GET_MENU_BY_CATEGORY_ID, )

</script>

<template>
  <p>{{ menuName }}</p>
</template>

<script lang="ts">
import { defineComponent } from "vue"

export default defineComponent({
  name: "Menu",
  props: {
    menuName :{
      type: String,
      required: true
    },
    categoryId : {
      type: Number,
      required: true
    }
  },
  setup(props) {
    console.log(props.menuName)
  }
})
</script>

<style scoped>

</style>