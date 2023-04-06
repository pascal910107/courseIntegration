<template>
    <div class="relative">
        <div class="mt-48 -left-5 absolute">
            <div class="w-80 bg-gray_one pl-12 pr-6 pt-6 pb-3 rounded-lg drop-shadow-lg text-gray_four text-xl overflow-y-scroll" style="max-height: 31.5rem;">
                
                <NuxtLink to="/login" class="bg-gray_two rounded-lg drop-shadow-xl w-56 p-3 mb-4 flex justify-center cursor-pointer select-none hover:-translate-x-6 transition-transform duration-300 select hover:bg-gray_three">新增 +</NuxtLink>
                <div v-for="user in users" :key="user?._id?.$oid" class="relative">
                    <div  :class="{ '-translate-x-6 bg-gray_three selectHover': user.user.detail.id === selectedUserId }" @click="selectUser(user)" class="z-10 drop-shadow-xl bg-gray_two rounded-lg w-56 p-3 mb-4 flex justify-center cursor-pointer select-none hover:-translate-x-6 transition-transform duration-300 select hover:bg-gray_three">
                        {{ user?.user?.detail?.id }} {{ user?.user?.detail?.name?.cht }}
                    </div>
                    <div class="absolute right-0 top-3 -translate-x-0.5 cursor-pointer select-none" @click="deleteUser(user, $event)">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                        </svg>
    
                    </div>
                </div>
            </div>
            
        </div>
    </div>
</template>
<script lang="ts" setup>

    const { $baseUrl } = useNuxtApp()
    const selectedUserId = useState<string>('selected', () => '')


    interface User {
        _id: { $oid: string }
        // status: number
        user: {
            detail: {
                id: string
                name: { cht: string }
                // wishlist: {  }
            }
            // enableWishlist: boolean
            // isAnonymus: boolean
        }
    }

    const { data: users } = await useFetch<User[]>('users/', {
        baseURL: $baseUrl,
    })
    
    const selectUser = (user: User) => {
        if (user.user.detail.id === selectedUserId.value) {
            selectedUserId.value = ''
        } else {
            selectedUserId.value = user.user.detail.id
        }
    }

    const deleteUser = async (user: User, event:any) => {
        // console.log(event.currentTarget.parentNode)
        event.currentTarget.parentNode.remove()
        await useFetch($baseUrl + 'users/' + user.user.detail.id, {
            method: 'DELETE'
        })
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