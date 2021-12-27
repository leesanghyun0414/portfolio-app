<template>
    


</template>




<script lang="ts">
import { defineComponent } from 'vue'
import { useQuery, useResult } from "@vue/apollo-composable"
import gql from "graphql-tag"
import { GET_ALLCATEGORY } from "../../../api/graphql/querys"
import { watch } from "vue"

export default defineComponent({
   name: "MenuNavBar",
   
// TODO: set up 追加
   setup() {

const { result } = useQuery(GET_ALLCATEGORY)

return { 
   result,
}

watch(result, value => {
      console.log(GET_ALLCATEGORY)
   
   
   }


</script>

