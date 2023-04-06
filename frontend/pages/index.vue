<template>
    
    <div class="flex">
        <div class="w-5/12">
            <CourseTable />
        </div>
        <div class="w-5/12">
            <div class="flex justify-center pl-8 pr-24 pt-36 pb-12">
                <div :class="{'bg-gray_two' : mode}" class="bg-gray_one rounded-l-lg drop-shadow-xl w-48 h-12 hover:bg-gray_two flex justify-center items-center cursor-pointer select-none" @click="mode = true">選課</div>
                <div :class="{'bg-gray_two' : !mode}" class="bg-gray_one rounded-r-lg drop-shadow-xl w-48 h-12 hover:bg-gray_two flex justify-center items-center cursor-pointer select-none" @click="mode = false">搶課</div>
            </div>
            <ScreeningCourse v-show="mode"/>
            <GrabbingCourse v-show="!mode" />
        </div>
        <div class="w-2/12">
            <ManageUsers />
        </div>
    </div>
    
</template>

<script lang="ts" setup>

    const login_page = ref<HTMLInputElement | null>(null)
    const mode = ref<boolean>(true)

</script>
    

<style scoped>


</style>