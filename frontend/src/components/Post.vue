<!--<template>-->
<!--  <div v-if="loading">-->
<!--    <p class="loading">-->
<!--      Loading...-->
<!--    </p>-->
<!--  </div>-->
<!--  <ul v-else>-->
<!--    <li-->
<!--      v-for="post in posts"-->
<!--      :key="post.author.user.id"-->
<!--    >-->
<!--      {{ post.author.user.username }}-->
<!--      <div>{{ users }}</div>-->
<!--    </li>-->
<!--  </ul>-->

<!--  <p>{{ result }}</p>-->
<!--  <p>{{ error }}</p>-->
<!--</template>-->

<!--<script lang="ts">-->
<!--import { defineComponent, computed, watch } from "vue"-->
<!--import { POST_BY_AUTHOR } from "../api/graphql/querys"-->
<!--import { useQuery, useResult } from "@vue/apollo-composable"-->

<!--export default defineComponent({-->
<!--  name: "Post",-->
<!--  setup () {-->
<!--    const { result, loading, error } = useQuery(POST_BY_AUTHOR,  { username: "admin" } )-->
<!--    const users = useResult(result, null, data => data.author)-->
<!--    const posts = useResult(result)-->
<!--    watch(result,  (value: {value: never})  => {-->
<!--      console.log(value)-->
<!--      console.log(Object.keys(value))-->

<!--    })-->
<!--    // watch(loading, (value: { value: never }) => {-->
<!--    //   console.log(value)-->
<!--    // })-->


<!--     return {-->
<!--      loading,-->
<!--       posts,-->
<!--       users,-->
<!--       result,-->
<!--       error-->
<!--     }-->
<!--  }-->

<!--})-->
<!--</script>-->

<!--<style scoped lang="sass">-->

<!--.loading-->
<!--  color: red-->

<!--</style>-->
