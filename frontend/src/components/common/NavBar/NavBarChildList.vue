
<script lang="ts">
import {defineComponent} from "vue"

// children要素が必要

export default defineComponent({
  name: "NavBarChildList",
  props: {
    childCategoryItem: {
      type:Object,
      required:true,
    }
  },

setup(props) {
    console.log(props.childCategoryItem)
}


})
</script>

<style scoped>

</style>
