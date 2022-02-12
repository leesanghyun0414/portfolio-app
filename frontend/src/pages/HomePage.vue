<template>
  <AppHeader />
  <router-view />

  <div class="grid gap-y-4 max-w-7xl text-regal-blue font-medium tracking-wider text-base md:text-2xl">
    <div>
      <img
        src="../assets/coffeshop_top_imagepicture.jpg"
        alt="cofeeshoppicture"
      >
    </div>
    <div class="inline-grid grid-rows-2 ">
      <div class="inline-grid grid-rows-none md:grid-cols-2 gap-6 py-4 mx-4">
        <p class="pl-14 pr-10 py-10 order-last">
          {{ HOME_MESSAGES.concept }}
        </p>   
        <span>
          <img
            src="../assets/cafe_imege1.jpg"
            alt="cafeimage"
          >
        </span>
      </div>
      <div class="inline-grid grid-rows-none md:grid-cols-2 gap-6 py-4 ml-4 mr-4">
        <img
          src="../assets/coffee_image2.jpg"
          alt="coffeeimage"
        >
        <p class="p-10 md:order-first ">
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
        rc="../assets/charge.png"
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

