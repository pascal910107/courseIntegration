<template>
    <div class="relative">
        <ul class="absolute right-36 top-44 bg-gray_one pl-10 pr-6 pt-6 pb-3 rounded-lg text-gray_four text-xl overflow-y-scroll" style="max-height: 31.5rem;">
            
            <NuxtLink to="/login" class="bg-gray_two rounded-lg w-56 p-3 mb-4 flex justify-center cursor-pointer select-none hover:-translate-x-6 transition-transform duration-500 select hover:bg-gray_three">新增 +</NuxtLink>
            <li v-for="user in users" :key="user?._id?.$oid" :class="{ '-translate-x-6 bg-gray_three selectHover': user === selectedUser }" @click="selectUser(user)" class="bg-gray_two rounded-lg w-56 p-3 mb-4 flex justify-center cursor-pointer select-none hover:-translate-x-6 transition-transform duration-500 select hover:bg-gray_three">
                {{ user?.user?.detail?.id }} {{ user?.user?.detail?.name?.cht }}
            </li>
        </ul>
        
    </div>
</template>
<script lang="ts" setup>
    const { $baseUrl } = useNuxtApp()
    const selectedUser = ref(null)

    const { data: users } = await useFetch($baseUrl + 'users')
    
    const selectUser = (user: any) => {
        if (user === selectedUser.value) {
            selectedUser.value = null
        } else {
            selectedUser.value = user
        }
    }




</script>


<style scoped>
.select {
    position: relative;
}

.select::after,
.select::before {
    content: " ";
    width: 2px;
    height: 2px;
    position: absolute;
    border: 0px solid #fff;
    transition: all 1s;
    pointer-events: none;
}

.select::after {
    top: -1px;
    left: -1px;
    border-top: 2px solid rgba(148 ,163 ,184, 1);
    border-left: 2px solid rgba(148 ,163 ,184, 1);
}

.select::before {
    bottom: -1px;
    right: -1px;
    border-bottom: 2px solid rgba(148 ,163 ,184, 1);
    border-right: 2px solid rgba(148 ,163 ,184, 1);
}
.select select {
    transition: all 1s;
}
.select select:hover {
    border-top-right-radius: 0px;
    border-bottom-left-radius: 0px;
}
.select:hover::before,
.select:hover::after {
    width: 100%;
    height: 100%;
    border-radius: 0.5rem;
}

.selectHover {
    border-top-right-radius: 0px;
    border-bottom-left-radius: 0px;
}

.selectHover::before,
.selectHover::after {
    width: 100%;
    height: 100%;
    border-radius: 0.5rem;
}

/* custom scrollbar */
::-webkit-scrollbar {
  width: 20px;
}

::-webkit-scrollbar-track {
  background-color: transparent;
}

::-webkit-scrollbar-thumb {
  background-color: #333333;
  border-radius: 20px;
  border: 6px solid transparent;
  background-clip: content-box;
}

::-webkit-scrollbar-thumb:hover {
  background-color: #3f3f3f;
}

</style>