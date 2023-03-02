<template>
  <NuxtLayout name="default">
    <NuxtPage />

  </NuxtLayout>
    
</template>

<script lang="ts" setup>


  // type Employee = {
  //   id?: number;
  //   name?: string;
  // };

  // const obj: Employee = {};

  // obj.id = 1;
  // obj.name = 'Alice';
  const year: string = '2022'
  const title: string = `${year} iThome 鐵人賽`
  // const count = ref(1)
  // const double = computed(() => count.value * 2)
  // const { data, refresh, pending } = await useAsyncData('/api/hello', () => $fetch('/api/hello'))http://127.0.0.1:5000/
</script>
<style>
.page-enter-active,
.page-leave-active {
  transition: all 0.4s;
}
.page-enter-from,
.page-leave-to {
  opacity: 0;
  filter: blur(1rem);
}

</style>












