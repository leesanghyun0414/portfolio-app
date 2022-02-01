<template>
  <li>
    <div>
      <p>
        {{ categoryItem.data.name }}
      </p>
    </div>
    
    <ul 
      v-if="categoryItem.children"
      class=" text-xl tracking-wide inline-grid"
    >
      <NavBarChildList
        v-for="childItem in categoryItem.children"
        :key="childItem.id"
        :child-category-item="childItem"
      />
    </ul>
  </li>
</template>

<script lang="ts">
import {defineComponent} from "vue"
import NavBarChildList from "./NavBarChildList.vue"



export default defineComponent({
  name: "NavBarList",
  components:{NavBarChildList},
  props: {
    categoryItem: {
      type: Object,
      required: true 
    }
  }
})
</script>


<style>


</style>