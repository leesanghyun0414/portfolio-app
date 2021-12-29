<template>
    <MenuNavBar />
        
</template>

<script lang="ts">
import { useQuery } from "@vue/apollo-composable"
import { defineComponent} from "vue"
import { GET_ALLCATEGORY } from "../api/graphql/querys"
import MenuNavBar from "../components/common/NavBar/MenuNavBar.vue"
export default defineComponent({
    name:"MenuPage",   
        components: {MenuNavBar}
,
setup() {
    const { result,error } = useQuery(GET_ALLCATEGORY)

return {result,error}
}
})
</script>

