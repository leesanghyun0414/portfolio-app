<template>
  <AppHeader />
  <img
    alt="Vue logo"
    src="./assets/logo.png"
  >

  <router-view />
</template>

<script lang="ts">
import {defineComponent, provide, watch} from "vue"
import { DefaultApolloClient, useQuery } from "@vue/apollo-composable"
// import AppHeader from "./components/AppHeader.vue"
import { apolloClient } from "./api/graphql/client"
import { POST_BY_AUTHOR } from "./api/graphql/querys"



export default defineComponent({
  name: "App",

  components: {


    // AppHeader,

  },
setup () {
  provide(DefaultApolloClient, apolloClient)
  const { result, loading } = useQuery(POST_BY_AUTHOR, { variables: { username: "admin" } })

  watch(result,  (value: {value: never})  => {
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
#counter {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #464a4b;

}

img {
  display: inline !important;
}
</style>
