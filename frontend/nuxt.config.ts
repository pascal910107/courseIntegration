// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    vite: {
        server: {
          hmr: {
            protocol: 'ws'
          }
        }
    }, 
    modules: ['@nuxtjs/tailwindcss'],
    // Type checking can be performed during development
    typescript: {
      typeCheck: true
    },
    app: {
      pageTransition: { name: 'page', mode: 'out-in' },
      // layoutTransition: { name: 'layout', mode: 'out-in' }
    },
})
