

<template>
  <div class="grid gap-x-5 grid-rows-2 md:grid-cols-2  lg:grid-cols-2   grid-cols-none lg:grid-rows-none  lg:gap-x-10 mx-auto lg:mx-0 ">
    <div>
    <img class="w-full h-96 md:h-[26rem] lg:h-[29rem] min-h-40 "
    :src="ASSET_ROOT+menuInfo.image"
    />
    </div>
    <div class="inline-grid md:gap-5 text-regal-blue  mx-auto md:mx-0 text-center md:text-left place-items-center md:justify-items-start -mt-10 md:mt-0">
      <p class="md:font-extrabold font-bold lg:text-menu-name text-md-menuname md:text-md-menuname leading-[3.0rem]">
        {{ menuInfo.name }}
      </p>
      <p class="md:text-calorie md:text-navbar-base text-2xl opacity-[.65] leading-3 -mt-28 md:my-auto">
        {{ menuInfo.calorie }}cal
      </p>
      <div class="flex gap-x-5  text-center mx-auto  md:m-0 -mt-48">
        <p class="text-lg md:text-2xl font-bold border-solid border-2 border-regal-blue my-auto leading-3 md:leading-5 md:px-3 md:py-1 px-2 py-1">
          Hot
        </p>
        <p class="text-lg md:text-2xl font-bold border-solid border-2 border-regal-blue my-auto leading-3 md:leading-5 md:px-3 md:py-1 px-2 py-1">
          cold
        </p>
      </div>
      <p class="md:text-md-menuname text-md-price -mt-32 md:mt-auto">
        ￥{{ menuInfo.price }}
      </p>
    </div>
  </div>
</template>


<script lang="ts">
import { useQuery, useResult } from "@vue/apollo-composable"
import { defineComponent, watch } from "vue"
import { MENU_BY_ID } from "../../api/graphql/querys"
import { ASSET_ROOT } from "../../config/api_roots"

export default defineComponent({
name:"MenuDetail",
props:{
  menuId :{
   type:Number,
   required:true
  }
},

setup(props) {
  const {result, error} = useQuery(MENU_BY_ID,{menuId:props.menuId})
  const menuInfo = useResult(result,null, (data) => data.menuById)
  

return {
 menuInfo, 
 ASSET_ROOT
}
}

})
</script>
