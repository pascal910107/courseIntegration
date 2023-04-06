export default defineNuxtPlugin(nuxtApp => {
    return {
      provide: {
        test: (msg: string) => `test ${msg}!`,
        baseUrl: process.server ? 'http://courseintegration-backend-1:5000/api/' : 'http://localhost:5000/api/'
      }
    }
})