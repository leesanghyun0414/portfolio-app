<template></template>

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
