<template>
  <header>
    <nav
      class="grid grid-flow-col auto-cols-max gap-4 bg-green-500
      text-blue-50 max-h-96 min-h-0 h-16 py-4 text-header-base sm:text-header-sm xl:text-header-lg content-center pl-4 mb-5 font-bold"
    >
      <router-link to="/post">
        Post
      </router-link>
      <button @click="moveHome">
        Home
      </button>
    </nav>
  </header>
</template>

<script lang="ts">
import { defineComponent } from "vue"
import { useRouter } from "vue-router"

export default defineComponent({
  name: "AppHeader",
  setup() {
    const router = useRouter()
    const moveHome = () => {
      router.push({ name: "Root", params: { msg: "Hello Vue 3 + TypeScript + Vite" } })
    }

    return {
      moveHome
    }


  }

})
</script>

<style scoped>

</style>
