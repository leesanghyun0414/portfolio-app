<template>
  <router-view />

  <div class="grid gap-y-4 max-w-7xl text-regal-blue font-medium tracking-wider text-base md:text-2xl">
    <div class="hidden md:inline-block">
      <img
        src="../assets/coffeshop_top_imagepicture.jpg"
        alt="cofeeshoppicture"
      >
    </div>
    <div class="inline-grid grid-rows-2 ">
      <div class="inline-grid grid-rows-none md:grid-cols-2 gap-6 py-4 md:mx-10">
        <p class="md:my-auto md:mx-auto order-last my-10 mx-14 leading-loose font-semibold">
          {{ HOME_MESSAGES.concept }}
        </p>   
        <span>
          <img
            src="../assets/cafe_imege1.jpg"
            alt="cafeimage"
          >
        </span>
      </div>
      <div class="inline-grid grid-rows-none md:grid-cols-2 gap-6 py-4 md:mx-10">
        <img
          src="../assets/coffee_image2.jpg"
          alt="coffeeimage"
        >
        <p class="md:my-auto md:mx-auto md:order-first my-10 mx-14 leading-loose font-semibold">
          {{ HOME_MESSAGES.subConcept }}
        </p>
      </div>
    </div>
    <div class="inline-grid grid-rows-none grid-cols-5 m-10 gap-5 place-items-center">
      <img
        src="../assets/wifi.png"
        alt="wifi"
      >
      <img
        src="../assets/charge.png"
        alt="charge"
      >
      <img
        src="../assets/twitter.png"
        alt="twitter"
      >
      <img
        src="../assets/instagram.png"
        alt="instagram"
      >
      <img
        src="../assets/facebook.png"
        alt="facebook"
      >
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue"
import { HOME_MESSAGES } from "../constants/homeMessages"


export default defineComponent({
  name: "HomePage",


  setup() {

    return {
   HOME_MESSAGES
    }

    }
  

})
</script>

