<template>
    
    <div class="grid grid-cols-8 gap-4 bg-white w-96" style="grid-template-rows: repeat(15, minmax(0, 1fr));">
        <!-- <div class="col-span-1 bg-gray-300 text-center"></div>
        <div class="col-span-1 bg-gray-300 text-center">週一</div>
        <div class="col-span-1 bg-gray-300 text-center">週二</div>
        <div class="col-span-1 bg-gray-300 text-center">週三</div>
        <div class="col-span-1 bg-gray-300 text-center">週四</div>
        <div class="col-span-1 bg-gray-300 text-center">週五</div>
        <div class="col-span-1 bg-gray-300 text-center">週六</div>
        <div class="col-span-1 bg-gray-300 text-center">週日</div>
        <div v-for="period in periods" :key="period" class="col-span-1 text-center">{{ period }}</div>
        <div v-for="period in periods" :key="period.period" class="row-span-1 text-center">{{ period.period }}</div>
        <div v-for="(table, index) in courses['table']" :key="index" class="col-span-1 text-center" :class="{ 'bg-gray-200': table.period !== index + 1 }">
            <div v-for="c in table.courses" :key="c.course_id" :style="{ backgroundColor: c.colorcode }">
                {{ c.title }} <br> {{ c.roomname }}
            </div>
        </div> -->
        <!-- <div v-for="(week, index) in table" :key="index" class="col-span-1 text-center">
            <div v-for="c in week" :key="c.course_id" :class="{ 'bg-gray-200': c.period !== index + 1 }" :style="{ backgroundColor: c.colorcode }">
                {{ c.title }} <br> {{ c.roomname }}
            </div>
        </div> -->

    </div>
</template>

<script lang="ts" setup>
    const { $baseUrl } = useNuxtApp()
    // const courses = ref(null)

    const { data: courses } = await useFetch($baseUrl + 'courses')


</script>