import { defineConfig } from "vite"
import vue from "@vitejs/plugin-vue"

// https://vitejs.dev/config/
export default defineConfig({
  root: "src",
  plugins: [vue()],

  server: {
    host: true,
    watch: {
      usePolling: true,
    },
    port: 3000,
  },
  resolve: {
    alias: { "@": "/src/", vue: "vue/dist/vue.esm-bundler.js" },
  },
})
