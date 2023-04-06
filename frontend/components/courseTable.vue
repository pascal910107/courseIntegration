<template>
    

    <div class="ml-12 mr-12 mt-24">
        <table class="flex flex-col text-gray_four">
            <thead class="text-2xl">
                <tr class="flex justify-end pr-1.5">
                    <th class="m-1 mx-1.5" v-for="week in weeks" :key="week">{{ week }}</th>
                </tr>
            </thead>
            <tbody class="">
                <tr v-for="(time, index) in periods" :key="index" class="flex items-center h-14 border-t-2 justify-end pr-1 text-base leading-4 border-blue_one">
                    <td class="text-center" >{{ index + 1 }}<br>{{ time }}</td>
                    <td v-for="i in 7" class="flex flex-col border-l-2 border-blue_one w-full h-full relative" v-if="!(count = 0)">
                        <div v-if="userExist">
                            <div v-if="courses.value?.filter((p: { period: number }) => p.period === index + 1)[0]?.courses[count]?.week == i" class="">
                                {{ courses.value?.filter((p: { period: number }) => p.period === index + 1)[0]?.courses[count].title }}
                            </div>
                            <div v-if="courses.value?.filter((p: { period: number }) => p.period === index + 1)[0]?.courses[count]?.week == i" class="text-xs absolute right-0 bottom-0">
                                {{ courses.value?.filter((p: { period: number }) => p.period === index + 1)[0]?.courses[count++].roomname?.indexOf("(") === -1 ? courses.value?.filter((p: { period: number }) => p.period === index + 1)[0]?.courses[count - 1].roomname : courses.value?.filter((p: { period: number }) => p.period === index + 1)[0]?.courses[count - 1].roomname?.substring(0, courses.value?.filter((p: { period: number }) => p.period === index + 1)[0]?.courses[count - 1].roomname?.indexOf("(")) }}
                            </div>


                            <div v-else> 
                                
                            </div>
                        </div>
                        
                    </td>
                </tr>
            </tbody>
        </table>
        

    </div>
</template>

<script lang="ts" setup>

    const { $baseUrl } = useNuxtApp()
    const count = ref<number>(0)
    const weeks = reactive([
        '星期一',
        '星期二',
        '星期三',
        '星期四',
        '星期五',
        '星期六',
        '星期日',
    ])

    const periods = reactive([
        '08:10~09:00',
        '09:10~10:00',
        '10:10~11:00',
        '11:10~12:00',
        '12:10~13:00',
        '13:10~14:00',
        '14:10~15:00',
        '15:10~16:00',
        '16:10~17:00',
        '17:10~18:00',
        '18:30~19:20',
        '19:25~20:15',
        '20:25~21:15',
        '21:20~22:10',
    ])

    const selectedUserId = useState<string>('selected', () => '')
    const courses = reactive({}) as any
    const userExist = ref<boolean>(false)


    watch(selectedUserId, async() => {
        const { data, pending, error }: any = await useFetch(`courses/?id=${selectedUserId.value}&format=table`, {
            baseURL: $baseUrl
        })
        courses.value = data
        if (selectedUserId.value === '' || courses.value === 'id not found') {
            userExist.value = false
        } else if (courses.value == null) {
            // 後端有問題
        } else {
            userExist.value = true

            //先把值給鎖起來，因為selectedUserId是即時變更，所以可能fetch完變新的值
            const preLock = selectedUserId.value
            const { data, pending, error }: any = await useFetch(`courses/refresh/?id=${selectedUserId.value}&format=table`, {
                baseURL: $baseUrl
            })
            if (preLock === selectedUserId.value) {
                courses.value = data
            }
        }
    })

</script>