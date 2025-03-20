import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  resolve:{
    alias:{
      '@': '/src',
    }
  },
  build: {
    outDir: 'dist',
  },
  server: {
    port: 8080,  
    host: 'localhost'
  }
})
