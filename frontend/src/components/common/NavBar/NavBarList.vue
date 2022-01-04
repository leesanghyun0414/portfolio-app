<template>
  <li>
    <ul v-if="categoryItem.children">
      <NavBarChildList
        v-for="childItem in categoryItem"
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
  ,
  setup(props) {

    const arr = (Object.keys(props.categoryItem) as (keyof typeof props.categoryItem)[]).map((key) => {
      return { key, value: props.categoryItem[key]}


    })
    console.log(typeof arr)
    // console.log(props.categoryItem)
  }
})
</script>
