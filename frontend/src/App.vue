<template>
  <HomePage />
</template>

<script lang="ts">
import {defineComponent, provide, watch} from "vue"
import {DefaultApolloClient, useQuery} from "@vue/apollo-composable"
import {apolloClient} from "./api/graphql/client"
import {POST_BY_AUTHOR} from "./api/graphql/querys"

import HomePage from "./pages/HomePage.vue"


export default defineComponent({
  name: "App",
  components: {HomePage},


  setup() {
    provide(DefaultApolloClient, apolloClient)
    const {result, loading} = useQuery(POST_BY_AUTHOR, {variables: {username: "admin"}})

    watch(result, (value: { value: never }) => {
      console.log(value)
      console.log(Object.keys(value))

    })


    return {
      result, loading
    }
  }
})
</script>

<style>


img {
  display: inline !important;
}
</style>
