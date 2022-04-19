
<template>
  <li>
    <div>
      <router-link :to="{name:'Menu',params:{menuName:childCategoryItem.data.name.replace(/\s+/g, ''), categoryId:childCategoryItem.id}}">
        {{ childCategoryItem.data.name }}
      </router-link>
    </div>
  </li>
</template>
<script lang="ts">
import {defineComponent} from "vue"


export default defineComponent({
  name: "NavBarChildList",
  props: {
    childCategoryItem: {
      type:Object,
      required:true,
    }
  },




})
</script>

<style scoped>

</style>
