<template>
  <div class="flex mx-auto text-regal-blue gap-5 font-bold items-center uppercase  h-full">
    <div
      class="text-header-base lg:text-header-lg normal-case mr-auto"
    >
      <router-link
        :to="{name: 'HomePage'}"
      >
        CAFE SQUARE
      </router-link>
    </div>
    <div
      v-for="headerItem in Object.values(HeaderItems)"
      class=" text-lg hidden lg:text-xl sm:inline-flex text-indigo-900 "
    >
      <p
        class="cursor-pointer hover:opacity-50"
        @click="handleHeaderItemClick(headerItem)"
      >
        {{ headerItem }}
      </p>
    </div>
    <Menu
      as="div"
      class="sm:hidden inline-block relative"
    >
      <MenuButton class="w-10 h-10 inline-flex justify-center items-center ">
        <!--        <MenuIcon aria-hidden="true" />-->
      </MenuButton>
      <transition
        enter-active-class="transition duration-100 ease-out"
        enter-from-class="transform scale-95 opacity-0"
        enter-to-class="transform scale-100 opacity-100"
        leave-active-class="transition duration-75 ease-in"
        leave-from-class="transform scale-100 opacity-100"
        leave-to-class="transform scale-95 opacity-0"
      >
        <MenuItems
          class="flex flex-col gap-y-6 justify-items-end p-2 right-0 absolute  bg-white origin-top-right divide-y divide-gray-100 shadow-lg rounded-md ring-1 ring-black ring-opacity-5"
        >
          <MenuItem
            v-for="headerItem in Object.values(HeaderItems)"
            v-slot="{active}"
            class="rounded-md items-center text-2xl"
          >
            <p
              class="cursor-pointer"
              @click="handleHeaderItemClick(headerItem)"
            >
              {{ headerItem }}
            </p>
          </MenuItem>
        </MenuItems>
      </transition>
    </Menu>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue"
import {  HeaderItems } from "../../../constants/headerItems"
import { Menu, MenuButton, MenuItem, MenuItems } from "@headlessui/vue"
import { MenuIcon } from "@heroicons/vue/solid"
import { useRouter } from "vue-router"


export default defineComponent({
  name: "AppHeaderItem"
  ,
  components: { MenuButton, Menu, MenuItems, MenuItem, MenuIcon },
  setup() {
    const router = useRouter()

    function handleHeaderItemClick(headerItemName:string) {
      switch(headerItemName) {

        case HeaderItems.Menu:
          router.push({name:"MenuCategory"})
          break
        case HeaderItems.Map:
          router.push({name:"MapPage"})
          break
      }
    }

    return {
    handleHeaderItemClick: handleHeaderItemClick,HeaderItems, MenuIcon
    }
  }
})
</script>

<style scoped>

</style>
