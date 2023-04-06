<template>
    
    <div class="w-auto h-full">
       <form @submit.prevent="query" class="w-auto pl-8 pr-24 grid grid-cols-2 gap-x-16 gap-y-16">
            <div class="flex items-center w-10/12">
                <label>
                    <input type="checkbox" v-model="checkbox.codeCheckbox" class="w-4 h-4 rounded cursor-pointer accent-white_one">
                </label>
                <div class="relative z-0 w-full group ml-4">
                    <input type="text" name="code" id="code" oninput="value = value.length > 4 ? value.slice(0,4) : value" @focus="checkbox.codeCheckbox = true" class="block py-2.5 px-0 w-full text-xl text-white_one bg-transparent border-0 border-b-2 border-blue_three appearance-none focus:outline-none focus:ring-0 peer" placeholder=" " />
                    <label for="code" class="peer-focus:font-medium absolute text-md text-white_one duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue_three peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">選課代號</label>
                </div>
            </div>
            <div class="flex items-center text-white_one rounded-lg select-none">
                <label>
                    <input type="checkbox" v-model="checkbox.weekperiodCheckbox" class="w-4 h-4 rounded cursor-pointer accent-white_one">
                </label>
                <select name="week" id="week" @click="checkbox.weekperiodCheckbox = true" class="ml-4 focus:outline-none cursor-pointer w-16 h-full pl-1 bg-transparent border-b-2">
                    <option value="*" class="cursor-pointer text-black" selected>全部</option>
                    <option :value="index + 1" v-for="week,index in weeks" class="cursor-pointer text-black">{{week}}</option>
                </select>
                <select name="period" id="period" @click="checkbox.weekperiodCheckbox = true" class="focus:outline-none cursor-pointer w-44 h-full ml-2 pl-1 bg-transparent border-b-2">
                    <option value="*" class="cursor-pointer text-black" selected>全部</option>
                    <option :value="index + 1" v-for="period,index in periods" class="cursor-pointer text-black">{{ index + 1 }}（{{ period }}）</option>
                </select>
            </div>
            <div class="flex items-center w-10/12">
                <label>
                    <input type="checkbox" v-model="checkbox.courseCheckbox" class="w-4 h-4 rounded cursor-pointer accent-white_one">
                </label>
                <div class="relative z-0 w-full group ml-4">
                    <input type="text" name="course" id="course" @focus="checkbox.courseCheckbox = true" class="block py-2.5 px-0 w-full text-xl text-white_one bg-transparent border-0 border-b-2 border-blue_three appearance-none focus:outline-none focus:ring-0 peer" placeholder=" " />
                    <label for="course" class="peer-focus:font-medium absolute text-md text-white_one duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue_three peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">科目名稱</label>
                </div>
            </div>
            <div class="flex items-center w-10/12">
                <label>
                    <input type="checkbox" v-model="checkbox.teacherCheckbox" class="w-4 h-4 rounded cursor-pointer accent-white_one">
                </label>
                <div class="relative z-0 w-full group ml-4">
                    <input type="text" name="teacher" id="teacher" @focus="checkbox.teacherCheckbox = true" class="block py-2.5 px-0 w-full text-xl text-white_one bg-transparent border-0 border-b-2 border-blue_three appearance-none focus:outline-none focus:ring-0 peer" placeholder=" " />
                    <label for="teacher" class="peer-focus:font-medium absolute text-md text-white_one duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue_three peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">開課教師姓名</label>
                </div>
            </div>
            <div class="flex items-center w-10/12 text-white_one rounded-lg select-none">
                <label>
                    <input type="checkbox" v-model="checkbox.useLanguageCheckbox" class="w-4 h-4 rounded cursor-pointer accent-white_one">
                </label>
                <select name="useLanguage" id="useLanguage" @click="checkbox.useLanguageCheckbox = true" class="ml-4 focus:outline-none cursor-pointer w-24 h-12 pl-1 bg-transparent border-b-2">
                    <option :value="'0' + (index + 1)" v-for="language,index in languages" class="cursor-pointer text-black">{{language}}</option>
                </select>
            </div>
            <div class="flex items-center w-10/12 text-white_one rounded-lg select-none">
                <label>
                    <input type="checkbox" v-model="checkbox.specificSubjectCheckbox" class="w-4 h-4 rounded cursor-pointer accent-white_one">
                </label>
                <select name="specificSubject" id="specificSubject" @click="checkbox.specificSubjectCheckbox = true" class="ml-4 focus:outline-none cursor-pointer w-40 h-12 pl-1 bg-transparent border-b-2">
                    <option :value="index + 1" v-for="specificSubject,index in specificSubjects" class="cursor-pointer text-black">{{specificSubject}}</option>
                </select>
            </div>
            <div class="flex items-center w-10/12">
                <label>
                    <input type="checkbox" v-model="checkbox.courseDescriptionCheckbox" class="w-4 h-4 rounded cursor-pointer accent-white_one">
                </label>
                <div class="relative z-0 w-full group ml-4">
                    <input type="text" name="courseDescription" id="courseDescription" @focus="checkbox.courseDescriptionCheckbox = true" class="block py-2.5 px-0 w-full text-xl text-white_one bg-transparent border-0 border-b-2 border-blue_three appearance-none focus:outline-none focus:ring-0 peer" placeholder=" " />
                    <label for="courseDescription" class="peer-focus:font-medium absolute text-md text-white_one duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue_three peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">課程描述</label>
                </div>
            </div>
            <div class="col-start-1 col-span-2 flex justify-center">
                <button type="submit" class="bg-gray_one rounded-l-lg drop-shadow-xl w-28 h-12 hover:bg-gray_two">查詢</button>
                <button type="reset" class="bg-gray_one rounded-r-lg drop-shadow-xl w-28 h-12 hover:bg-gray_two" @click="reset">重設</button>
            </div>
        </form>

    </div>
    
</template>


<script lang="ts" setup>

    const checkbox = reactive({ 
        codeCheckbox: <boolean>false,
        weekperiodCheckbox: <boolean>false,
        courseCheckbox: <boolean>false,
        teacherCheckbox: <boolean>false,
        useLanguageCheckbox: <boolean>false,
        specificSubjectCheckbox: <boolean>false,
        courseDescriptionCheckbox: <boolean>false,
    })

    const reset = () => {
        Object.keys(checkbox).forEach((key) => {
            checkbox[key] = false
        })
    }

    // const fields = reactive([
    //     { label: 'Field 1', name: 'field1', value: '', selected: false },
    //     { label: 'Field 2', name: 'field2', value: '', selected: false },
    //     { label: 'Field 3', name: 'field3', value: '', selected: false },
    // ])

    // const submitForm = () => {
    //   const formData = {}
    //   fields.forEach(field => {
    //     if (field.selected) {
    //       formData[field.name] = field.value
    //     }
    //   })
    //   console.log(formData) // do something with the form data
    // }
    const weeks = reactive([
        '一',
        '二',
        '三',
        '四',
        '五',
        '六',
        '日',
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

    const languages = reactive([
        '中文',
        '英語',
        '日語',
        '德語',
        '法語',
        '西班牙語',
        '其他',
        '中英'
    ])

    const specificSubjects = reactive([
        '通識課程',
        '體育選項課程',
        '大學國文',
        '中文思辨與表達',
        '全英語授課(EMI)'
    ])

    // const department = reactive({
    //     degree: [
    //         {degreeId: 1, degreeName: '大學部', dept: [
    //             {deptId: 'SX', deptName: '大學社會責任中心', unit:[
    //                 {unitId: 'SX01', unitName: '跨領域設計學院', class:[
    //                     {classId: 'SX01100', className: '跨領域設計學院綜合班'},
    //                 ]},
    //                 {unitId: 'SX02', unitName: '社會創新學院', class:[
    //                     {classId: 'SX02100', className: '社會創新學院綜合班'},
    //                 ]},
    //             ]},
    //             {deptId: 'CC', deptName: '創能學院', unit:[
    //                 {unitId: 'CC00', unitName: '創能學院', class:[
    //                     {classId: 'CC00100', className: '創能學院綜合班'},
    //                 ]},
    //                 {unitId: 'CC03', unitName: '人工智慧技術與應用學士學位', class:[
    //                     {classId: 'CC03110', className: '人工智慧一學位學程'},
    //                     {classId: 'CC03120', className: '人工智慧二學位學程'},
    //                 ]},
    //             ]},
    //             {deptId: 'GE', deptName: '通識中心'},
    //             {deptId: 'CA', deptName: '工程與科學學院'},
    //             {deptId: 'CB', deptName: '商學院'},
    //             {deptId: 'CH', deptName: '人社學院'},
    //             {deptId: 'CI', deptName: '資電學院'},
    //             {deptId: 'CD', deptName: '建設學院'},
    //             {deptId: 'CF', deptName: '金融學院'},
    //             {deptId: 'NM', deptName: '國際科技與管理學院'},
    //             {deptId: 'AS', deptName: '建築專業學院'},
    //             {deptId: 'PC', deptName: '學分學程'},
    //             {deptId: 'XA', deptName: '外語文'},
    //             {deptId: 'XC', deptName: '通識核心課'},
    //             {deptId: 'XD', deptName: '體育選項課'},
    //             {deptId: 'XE', deptName: '綜合班'},
    //             {deptId: 'XF', deptName: '統籌科目'},
    //             {deptId: 'XH', deptName: '軍訓'},
    //         ]},
    //         {degreeId: 3, degreeName: '碩士班', deptId: [
    //             {deptId: 'CA', deptName: '工程與科學學院'},
    //             {deptId: 'CB', deptName: '商學院'},
    //             {deptId: 'MB', deptName: '經管學院'},
    //             {deptId: 'CH', deptName: '人社學院'},
    //             {deptId: 'CI', deptName: '資電學院'},
    //             {deptId: 'CD', deptName: '建設學院'},
    //             {deptId: 'CF', deptName: '金融學院'},
    //             {deptId: 'AS', deptName: '建築專業學院'},
    //             {deptId: 'PC', deptName: '學分學程'},
    //         ]},
    //         {degreeId: 4, degreeName: '博士班', deptId: []},
    //         {degreeId: 5, degreeName: '進修學士班', deptId: []},
    //     ]
    // })

    const query = () => {
        console.log('query');
        
    }


</script>

<style scoped>


</style>