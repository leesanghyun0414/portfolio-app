<!--<template>-->
<!--  <div class="container px-3 max-w-full ">-->
<!--    <svg-->
<!--      v-if="loading"-->
<!--      class="animate-spin h-5 w-5 mr-3"-->
<!--      viewBox="0 0 24 24"-->
<!--    />-->
<!--    <ul-->
<!--      v-else-->
<!--      class="inline-grid md:grid-cols-3 lg:grid-cols-5"-->
<!--    >-->
<!--      <PostList-->
<!--        v-for="post in posts"-->
<!--        :key="post.id"-->
<!--        :post="post"-->
<!--      />-->
<!--    </ul>-->
<!--  </div>-->
<!--  <img-->
<!--    src="http://localhost:8080/media/images/menu/soft_drink/tropical_drink.png"-->
<!--    alt="drink"-->
<!--  >-->
<!--</template>-->

<!--<script lang="ts">-->
<!--import { defineComponent, watch } from "vue"-->
<!--import {  useQuery, useResult } from "@vue/apollo-composable"-->
<!--import { POST_BY_AUTHOR } from "../api/graphql/querys"-->
<!--import PostList from "../components/PostList.vue"-->
<!--export default defineComponent({-->
<!--  name: "PostPreview",-->
<!--  components: {-->
<!--    PostList-->
<!--  },-->
<!--  setup() {-->
<!--    const { result, loading, error } = useQuery(POST_BY_AUTHOR,  { username: "admin" })-->
<!--    const posts = useResult(result, null, data => data.postByAuthor)-->
<!--    watch(result,  (value: {value: never})  => {-->
<!--      console.log(value)-->
<!--      console.log(Object.keys(value))-->
<!--    })-->
<!--    return {-->
<!--      result, loading, error, posts-->
<!--    }-->
<!--  }-->
<!--})-->
<!--</script>-->

<!--<style scoped>-->

<!--</style>-->
