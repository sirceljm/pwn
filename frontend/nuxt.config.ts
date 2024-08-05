// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  modules: ['@pinia/nuxt','@vesp/nuxt-fontawesome'],
  ssr: false,
  fontawesome: {
    icons: {
      solid: ['arrows-rotate'],
    }
  }
})
