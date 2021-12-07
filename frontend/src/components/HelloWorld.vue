<template>
  <h1>
    {{ msg }}
  </h1>
  <p>
    Recommended IDE setup:
    <a
      href="https://code.visualstudio.com/"
      target="_blank"
    >VSCode</a>
    +
    <a
      href="https://marketplace.visualstudio.com/items?itemName=octref.vetur"
      target="_blank"
    >
      Vetur
    </a>
    or
    <a
      href="https://github.com/johnsoncodehk/volar"
      target="_blank"
    >Volar</a>
    (if using
    <code>&lt;script setup&gt;</code>)
  </p>

  <p>See <code>README.md</code> for more information.</p>

  <p>
    <a
      href="https://vitejs.dev/guide/features.html"
      target="_blank"
    >
      Vite Docs
    </a>
    |
    <a
      href="https://v3.vuejs.org/"
      target="_blank"
    >Vue 3 Docs</a>
  </p>

  <button
    type="button"
    @click="count++"
  >
    count is: {{ count }}
  </button>
  <p>
    Edit
    <code>components/HelloWorld.vue</code> to test hot module replacement
  </p>
  <p
    v-if="result && result.allPosts"
  >
    {{ result.allPosts[0] }}
  </p>
</template>
<script lang="ts">
import { ref, defineComponent } from "vue"
import { useQuery } from "@vue/apollo-composable"
import gql from "graphql-tag"
import { ALL_POSTS } from "../api/graphql/querys"

export default defineComponent({
  name: "HelloWorld",
  props: {
    msg: {
      type: String,
      required: true
    }
  },
  setup: () => {
    const { result } = useQuery(ALL_POSTS)
    const count = ref(0)
    return { count, result }
  }
})
</script>
<style
  scoped
  lang="sass"
>
a
  color: #675950


label
  margin: 0 0.5em
  font-weight: bold


code
  background-color: #93bc8d
  padding: 2px 4px
  border-radius: 4px
  color: #304455
</style>

