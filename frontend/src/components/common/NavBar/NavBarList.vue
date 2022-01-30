<template>
  <li >
    <div>
      <p>
        {{ categoryItem.data.name }}
      </p>
    </div>
    
    <ul 
      v-if="categoryItem.children"
      class=" text-xl tracking-wide"
      :class="childCategoryDisplay"
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
import {data} from "autoprefixer"



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
setup() {
},

data(){
    return{
     childCategoryDisplay:{
       hidden:false,
       ["inline-grid"]:true
     }

     }


    },
methods:{
    toggleChildCategory(){
      this.childCategoryDisplay.hidden = !this.childCategoryDisplay.hidden
      this.childCategoryDisplay["inline-grid"] = !this.childCategoryDisplay["inline-grid"]
    }
}







  
})
</script>


<style>


</style>