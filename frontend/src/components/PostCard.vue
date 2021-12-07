<!--<template>-->
<!--  <div-->
<!--    class="h-full rounded overflow-hidden shadow-lg  mb-5"-->
<!--    @click="movePostDetail"-->
<!--  >-->
<!--    <div class="px-6 py-4">-->
<!--      <div class="font-bold text-xl mb-4 text-left">-->
<!--        {{ post.title }}-->
<!--      </div>-->
<!--      <p class="text-gray-700 text-xs mb-1 md:text-sm lg:text-lg">-->
<!--        {{-->
<!--          post.subtitle-->
<!--        }}-->
<!--      </p>-->
<!--    </div>-->
<!--    <div class="px-6 pt-4 pb-2 text-right">-->
<!--      <span class="inline-block bg-gray-100 rounded-full px-3 py-1 text-sm font-semibold text-gray-700">{{-->
<!--        post.author.user.username-->
<!--      }}</span>-->
<!--    </div>-->
<!--  </div>-->
<!--  <div>{{ post.id }}</div>-->
<!--</template>-->

<!--<script>-->
<!--import { defineComponent, toRef, toRefs } from "vue"-->
<!--import { useRouter } from "vue-router"-->

<!--export default defineComponent({-->
<!--  name: "PostCard"-->
<!--  , props: {-->
<!--    post: {-->
<!--      type: Object,-->
<!--      required: true,-->

<!--    }-->
<!--  },-->
<!--  setup(props) {-->

<!--    const router = useRouter()-->
<!--    const movePostDetail = () => {-->
<!--      router.push({ name: "PostDetail", params: {postId: props.post.id, title : props.post.title  ,subTitle : props.post.subtitle} })-->
<!--    }-->

<!--    return {-->
<!--      movePostDetail-->
<!--    }-->
<!--  }-->

<!--})-->
<!--</script>-->

<!--<style scoped>-->

<!--</style>-->
