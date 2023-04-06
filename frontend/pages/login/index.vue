<template>
    <div class="relative">
        <div class="absolute inset-x-64">
            <div class="flex flex-col items-center py-48">
                <div class="flex items-center text-lg font-medium select-none">
                    學號<input type="text" v-model="id" class="focus:ring-0 focus:outline-none w-80 h-16 rounded-lg text-2xl p-4 m-4" style="background:rgba(56 , 53 , 78, 0.6);">
                </div>
                <div class="flex items-center text-lg font-medium relative select-none">
                    密碼<input v-bind:type="inputType" v-model="password" class="focus:ring-0 focus:outline-none w-80 h-16 rounded-lg text-2xl p-4 m-4" style="background:rgba(56 , 53 , 78, 0.6);">
                    <svg @click="inputType = inputType === 'password' ? 'text' : 'password'" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" class="w-6 h-6 absolute right-8 cursor-pointer">
                        <path v-if="inputType==='password'" strokeLinecap="round" strokeLinejoin="round" d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" />
                        <path v-if="inputType==='password'" strokeLinecap="round" strokeLinejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    
                        <path v-if="inputType==='text'" strokeLinecap="round" strokeLinejoin="round" d="M3.98 8.223A10.477 10.477 0 001.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.45 10.45 0 0112 4.5c4.756 0 8.773 3.162 10.065 7.498a10.523 10.523 0 01-4.293 5.774M6.228 6.228L3 3m3.228 3.228l3.65 3.65m7.894 7.894L21 21m-3.228-3.228l-3.65-3.65m0 0a3 3 0 10-4.243-4.243m4.242 4.242L9.88 9.88" />
                    </svg>
                </div>
                <div>
                    <button @click="login" class="focus:ring-0 focus:outline-none w-96 h-12 rounded-lg text-lg p-2 m-4 select-none hover:scale-105 ease-linear duration-150" style="background:rgba(56 , 53 , 78, 0.6);">登入</button>
                </div>
                <div v-if="error == 1" class="text-red-600">帳號或密碼輸入錯誤</div>
            </div>
        </div>
      <div v-for="i in 200" :key="i" class="snow"></div>
    </div>
    
</template>

<script lang="ts" setup>

    const inputType = ref("password")
    const id = ref("")
    const password = ref("")
    const { $baseUrl } = useNuxtApp()
    const result = reactive({}) as any
    const error = ref(0)

    const login = async () => {
      try {
        const { data: response }: any = await useFetch('login', {
          baseURL: $baseUrl,
          method: 'POST',
          body: {
            id: id.value,
            password: password.value
          }
        })
        result.value = response
        
        if (result.value == 'false') {
          error.value = 1
        } else if (result.value == null) {
          //後端沒開或有問題，檢查日誌
        } else{
          error.value = 0
          navigateTo('/')
        }
      } catch (error) {
        console.log(error)
      }
        
    }

    onMounted(() => {
      document.addEventListener('keydown', e => {
        if (e.code === 'Enter') {
          login()
        }
      })
    })

</script>
    

<style scoped>
.page-enter-active,
.page-leave-active {
  transition: all 0.4s;
}
.page-enter-from,
.page-leave-to {
  opacity: 0;
  filter: blur(1rem);
}

.snow {
  position: absolute;
  width: 10px;
  height: 10px;
  /* background: red; */
  /* border-radius: 50%; */
}
.snow:nth-child(even) {
    /* width: 6px;
    height: 24px;
    background: purple; */
    background: white;
    border-radius: 50%;
}
.snow:nth-child(odd) {
    background: white;
    border-radius: 50%;
}


.snow:nth-child(2) {
  opacity: 0.3202;
  transform: translate(73.3158vw, -10px) scale(0.046);
  animation: fall-2 10s -29s linear infinite;
}

@keyframes fall-2 {
  53.409% {
    transform: translate(72.7421vw, 53.409vh) scale(0.046);
  }
  to {
    transform: translate(73.02895vw, 100vh) scale(0.046);
  }
}

.snow:nth-child(3) {
  opacity: 0.8425;
  transform: translate(90.0112vw, -10px) scale(0.819);
  animation: fall-3 12s -30s linear infinite;
}

@keyframes fall-3 {
  38.973% {
    transform: translate(90.4238vw, 38.973vh) scale(0.819);
  }
  to {
    transform: translate(90.2175vw, 100vh) scale(0.819);
  }
}

.snow:nth-child(4) {
  opacity: 0.9593;
  transform: translate(10.5471vw, -10px) scale(0.9586);
  animation: fall-4 19s -23s linear infinite;
}

@keyframes fall-4 {
  41.712% {
    transform: translate(9.0839vw, 41.712vh) scale(0.9586);
  }
  to {
    transform: translate(9.8155vw, 100vh) scale(0.9586);
  }
}

.snow:nth-child(5) {
  opacity: 0.9665;
  transform: translate(74.2486vw, -10px) scale(0.891);
  animation: fall-5 10s -16s linear infinite;
}

@keyframes fall-5 {
  48.31% {
    transform: translate(70.5414vw, 48.31vh) scale(0.891);
  }
  to {
    transform: translate(72.395vw, 100vh) scale(0.891);
  }
}

.snow:nth-child(6) {
  opacity: 0.1916;
  transform: translate(20.8534vw, -10px) scale(0.5365);
  animation: fall-6 22s -8s linear infinite;
}

@keyframes fall-6 {
  74.714% {
    transform: translate(30.2779vw, 74.714vh) scale(0.5365);
  }
  to {
    transform: translate(25.56565vw, 100vh) scale(0.5365);
  }
}

.snow:nth-child(7) {
  opacity: 0.5055;
  transform: translate(81.422vw, -10px) scale(0.7444);
  animation: fall-7 29s -1s linear infinite;
}

@keyframes fall-7 {
  67.049% {
    transform: translate(82.3232vw, 67.049vh) scale(0.7444);
  }
  to {
    transform: translate(81.8726vw, 100vh) scale(0.7444);
  }
}

.snow:nth-child(8) {
  opacity: 0.7402;
  transform: translate(81.7983vw, -10px) scale(0.4301);
  animation: fall-8 12s -19s linear infinite;
}

@keyframes fall-8 {
  64.838% {
    transform: translate(81.5926vw, 64.838vh) scale(0.4301);
  }
  to {
    transform: translate(81.69545vw, 100vh) scale(0.4301);
  }
}

.snow:nth-child(9) {
  opacity: 0.1828;
  transform: translate(77.5765vw, -10px) scale(0.8537);
  animation: fall-9 20s -19s linear infinite;
}

@keyframes fall-9 {
  43.549% {
    transform: translate(71.3523vw, 43.549vh) scale(0.8537);
  }
  to {
    transform: translate(74.4644vw, 100vh) scale(0.8537);
  }
}

.snow:nth-child(10) {
  opacity: 0.3142;
  transform: translate(66.0916vw, -10px) scale(0.1918);
  animation: fall-10 30s -26s linear infinite;
}

@keyframes fall-10 {
  50.631% {
    transform: translate(76.0058vw, 50.631vh) scale(0.1918);
  }
  to {
    transform: translate(71.0487vw, 100vh) scale(0.1918);
  }
}

.snow:nth-child(11) {
  opacity: 0.94;
  transform: translate(27.6251vw, -10px) scale(0.6161);
  animation: fall-11 17s -6s linear infinite;
}

@keyframes fall-11 {
  64.226% {
    transform: translate(35.9643vw, 64.226vh) scale(0.6161);
  }
  to {
    transform: translate(31.7947vw, 100vh) scale(0.6161);
  }
}

.snow:nth-child(12) {
  opacity: 0.2997;
  transform: translate(31.3492vw, -10px) scale(0.0816);
  animation: fall-12 25s -11s linear infinite;
}

@keyframes fall-12 {
  37.949% {
    transform: translate(38.7887vw, 37.949vh) scale(0.0816);
  }
  to {
    transform: translate(35.06895vw, 100vh) scale(0.0816);
  }
}

.snow:nth-child(13) {
  opacity: 0.2539;
  transform: translate(83.7682vw, -10px) scale(0.5972);
  animation: fall-13 20s -4s linear infinite;
}

@keyframes fall-13 {
  38.69% {
    transform: translate(85.1085vw, 38.69vh) scale(0.5972);
  }
  to {
    transform: translate(84.43835vw, 100vh) scale(0.5972);
  }
}

.snow:nth-child(14) {
  opacity: 0.3296;
  transform: translate(16.0671vw, -10px) scale(0.205);
  animation: fall-14 26s -9s linear infinite;
}

@keyframes fall-14 {
  65.971% {
    transform: translate(20.3724vw, 65.971vh) scale(0.205);
  }
  to {
    transform: translate(18.21975vw, 100vh) scale(0.205);
  }
}

.snow:nth-child(15) {
  opacity: 0.0434;
  transform: translate(40.254vw, -10px) scale(0.9887);
  animation: fall-15 15s -5s linear infinite;
}

@keyframes fall-15 {
  50.763% {
    transform: translate(31.7445vw, 50.763vh) scale(0.9887);
  }
  to {
    transform: translate(35.99925vw, 100vh) scale(0.9887);
  }
}

.snow:nth-child(16) {
  opacity: 0.1601;
  transform: translate(74.0947vw, -10px) scale(0.2714);
  animation: fall-16 17s -24s linear infinite;
}

@keyframes fall-16 {
  63.125% {
    transform: translate(79.3153vw, 63.125vh) scale(0.2714);
  }
  to {
    transform: translate(76.705vw, 100vh) scale(0.2714);
  }
}

.snow:nth-child(17) {
  opacity: 0.3992;
  transform: translate(38.9481vw, -10px) scale(0.4717);
  animation: fall-17 30s -6s linear infinite;
}

@keyframes fall-17 {
  43.463% {
    transform: translate(33.7685vw, 43.463vh) scale(0.4717);
  }
  to {
    transform: translate(36.3583vw, 100vh) scale(0.4717);
  }
}

.snow:nth-child(18) {
  opacity: 0.9223;
  transform: translate(85.4519vw, -10px) scale(0.9145);
  animation: fall-18 29s -10s linear infinite;
}

@keyframes fall-18 {
  51.037% {
    transform: translate(82.252vw, 51.037vh) scale(0.9145);
  }
  to {
    transform: translate(83.85195vw, 100vh) scale(0.9145);
  }
}

.snow:nth-child(19) {
  opacity: 0.4808;
  transform: translate(72.3613vw, -10px) scale(0.5419);
  animation: fall-19 14s -6s linear infinite;
}

@keyframes fall-19 {
  65.818% {
    transform: translate(63.8391vw, 65.818vh) scale(0.5419);
  }
  to {
    transform: translate(68.1002vw, 100vh) scale(0.5419);
  }
}

.snow:nth-child(20) {
  opacity: 0.4216;
  transform: translate(91.323vw, -10px) scale(0.4435);
  animation: fall-20 10s -4s linear infinite;
}

@keyframes fall-20 {
  64.219% {
    transform: translate(93.9243vw, 64.219vh) scale(0.4435);
  }
  to {
    transform: translate(92.62365vw, 100vh) scale(0.4435);
  }
}

.snow:nth-child(21) {
  opacity: 0.5896;
  transform: translate(78.095vw, -10px) scale(0.7202);
  animation: fall-21 26s -23s linear infinite;
}

@keyframes fall-21 {
  43.823% {
    transform: translate(77.1973vw, 43.823vh) scale(0.7202);
  }
  to {
    transform: translate(77.64615vw, 100vh) scale(0.7202);
  }
}

.snow:nth-child(22) {
  opacity: 0.203;
  transform: translate(98.1589vw, -10px) scale(0.7949);
  animation: fall-22 22s -18s linear infinite;
}

@keyframes fall-22 {
  77.78% {
    transform: translate(94.8977vw, 77.78vh) scale(0.7949);
  }
  to {
    transform: translate(96.5283vw, 100vh) scale(0.7949);
  }
}

.snow:nth-child(23) {
  opacity: 0.2457;
  transform: translate(63.1482vw, -10px) scale(0.1139);
  animation: fall-23 18s -20s linear infinite;
}

@keyframes fall-23 {
  72.151% {
    transform: translate(60.6748vw, 72.151vh) scale(0.1139);
  }
  to {
    transform: translate(61.9115vw, 100vh) scale(0.1139);
  }
}

.snow:nth-child(24) {
  opacity: 0.2022;
  transform: translate(9.0828vw, -10px) scale(0.2845);
  animation: fall-24 23s -7s linear infinite;
}

@keyframes fall-24 {
  71.425% {
    transform: translate(9.0861vw, 71.425vh) scale(0.2845);
  }
  to {
    transform: translate(9.08445vw, 100vh) scale(0.2845);
  }
}

.snow:nth-child(25) {
  opacity: 0.2513;
  transform: translate(46.6443vw, -10px) scale(0.518);
  animation: fall-25 24s -8s linear infinite;
}

@keyframes fall-25 {
  73.171% {
    transform: translate(54.7336vw, 73.171vh) scale(0.518);
  }
  to {
    transform: translate(50.68895vw, 100vh) scale(0.518);
  }
}

.snow:nth-child(26) {
  opacity: 0.812;
  transform: translate(93.5341vw, -10px) scale(0.1345);
  animation: fall-26 30s -18s linear infinite;
}

@keyframes fall-26 {
  48.682% {
    transform: translate(85.4345vw, 48.682vh) scale(0.1345);
  }
  to {
    transform: translate(89.4843vw, 100vh) scale(0.1345);
  }
}

.snow:nth-child(27) {
  opacity: 0.1722;
  transform: translate(15.327vw, -10px) scale(0.9875);
  animation: fall-27 26s -21s linear infinite;
}

@keyframes fall-27 {
  51.947% {
    transform: translate(10.3644vw, 51.947vh) scale(0.9875);
  }
  to {
    transform: translate(12.8457vw, 100vh) scale(0.9875);
  }
}

.snow:nth-child(28) {
  opacity: 0.7511;
  transform: translate(77.1243vw, -10px) scale(0.5682);
  animation: fall-28 11s -28s linear infinite;
}

@keyframes fall-28 {
  58.939% {
    transform: translate(86.2125vw, 58.939vh) scale(0.5682);
  }
  to {
    transform: translate(81.6684vw, 100vh) scale(0.5682);
  }
}

.snow:nth-child(29) {
  opacity: 0.6558;
  transform: translate(95.6926vw, -10px) scale(0.1395);
  animation: fall-29 27s -27s linear infinite;
}

@keyframes fall-29 {
  53.599% {
    transform: translate(99.1234vw, 53.599vh) scale(0.1395);
  }
  to {
    transform: translate(97.408vw, 100vh) scale(0.1395);
  }
}

.snow:nth-child(30) {
  opacity: 0.4401;
  transform: translate(87.4329vw, -10px) scale(0.8945);
  animation: fall-30 23s -7s linear infinite;
}

@keyframes fall-30 {
  78.492% {
    transform: translate(93.6331vw, 78.492vh) scale(0.8945);
  }
  to {
    transform: translate(90.533vw, 100vh) scale(0.8945);
  }
}

.snow:nth-child(31) {
  opacity: 0.0633;
  transform: translate(25.9941vw, -10px) scale(0.5766);
  animation: fall-31 28s -24s linear infinite;
}

@keyframes fall-31 {
  57.666% {
    transform: translate(20.2035vw, 57.666vh) scale(0.5766);
  }
  to {
    transform: translate(23.0988vw, 100vh) scale(0.5766);
  }
}

.snow:nth-child(32) {
  opacity: 0.0371;
  transform: translate(92.443vw, -10px) scale(0.2059);
  animation: fall-32 14s -24s linear infinite;
}

@keyframes fall-32 {
  68.227% {
    transform: translate(91.7088vw, 68.227vh) scale(0.2059);
  }
  to {
    transform: translate(92.0759vw, 100vh) scale(0.2059);
  }
}

.snow:nth-child(33) {
  opacity: 0.2496;
  transform: translate(55.5002vw, -10px) scale(0.066);
  animation: fall-33 16s -28s linear infinite;
}

@keyframes fall-33 {
  75.54% {
    transform: translate(60.5617vw, 75.54vh) scale(0.066);
  }
  to {
    transform: translate(58.03095vw, 100vh) scale(0.066);
  }
}

.snow:nth-child(34) {
  opacity: 0.5574;
  transform: translate(24.9012vw, -10px) scale(0.452);
  animation: fall-34 21s -29s linear infinite;
}

@keyframes fall-34 {
  45.187% {
    transform: translate(29.5639vw, 45.187vh) scale(0.452);
  }
  to {
    transform: translate(27.23255vw, 100vh) scale(0.452);
  }
}

.snow:nth-child(35) {
  opacity: 0.9398;
  transform: translate(63.5651vw, -10px) scale(0.0297);
  animation: fall-35 14s -20s linear infinite;
}

@keyframes fall-35 {
  76.86% {
    transform: translate(69.4432vw, 76.86vh) scale(0.0297);
  }
  to {
    transform: translate(66.50415vw, 100vh) scale(0.0297);
  }
}

.snow:nth-child(36) {
  opacity: 0.7767;
  transform: translate(74.4689vw, -10px) scale(0.2407);
  animation: fall-36 20s -24s linear infinite;
}

@keyframes fall-36 {
  48.775% {
    transform: translate(70.998vw, 48.775vh) scale(0.2407);
  }
  to {
    transform: translate(72.73345vw, 100vh) scale(0.2407);
  }
}

.snow:nth-child(37) {
  opacity: 0.4609;
  transform: translate(39.1778vw, -10px) scale(0.4072);
  animation: fall-37 17s -8s linear infinite;
}

@keyframes fall-37 {
  66.615% {
    transform: translate(41.0314vw, 66.615vh) scale(0.4072);
  }
  to {
    transform: translate(40.1046vw, 100vh) scale(0.4072);
  }
}

.snow:nth-child(38) {
  opacity: 0.5816;
  transform: translate(64.4391vw, -10px) scale(0.1456);
  animation: fall-38 14s -21s linear infinite;
}

@keyframes fall-38 {
  79.909% {
    transform: translate(61.7355vw, 79.909vh) scale(0.1456);
  }
  to {
    transform: translate(63.0873vw, 100vh) scale(0.1456);
  }
}

.snow:nth-child(39) {
  opacity: 0.6221;
  transform: translate(50.5611vw, -10px) scale(0.7279);
  animation: fall-39 29s -2s linear infinite;
}

@keyframes fall-39 {
  61.534% {
    transform: translate(41.443vw, 61.534vh) scale(0.7279);
  }
  to {
    transform: translate(46.00205vw, 100vh) scale(0.7279);
  }
}

.snow:nth-child(40) {
  opacity: 0.2401;
  transform: translate(64.1131vw, -10px) scale(0.6505);
  animation: fall-40 15s -15s linear infinite;
}

@keyframes fall-40 {
  79.154% {
    transform: translate(56.131vw, 79.154vh) scale(0.6505);
  }
  to {
    transform: translate(60.12205vw, 100vh) scale(0.6505);
  }
}

.snow:nth-child(41) {
  opacity: 0.8434;
  transform: translate(68.9773vw, -10px) scale(0.4366);
  animation: fall-41 18s -23s linear infinite;
}

@keyframes fall-41 {
  44.33% {
    transform: translate(69.441vw, 44.33vh) scale(0.4366);
  }
  to {
    transform: translate(69.20915vw, 100vh) scale(0.4366);
  }
}

.snow:nth-child(42) {
  opacity: 0.8871;
  transform: translate(30.3671vw, -10px) scale(0.6224);
  animation: fall-42 21s -16s linear infinite;
}

@keyframes fall-42 {
  77.118% {
    transform: translate(27.2727vw, 77.118vh) scale(0.6224);
  }
  to {
    transform: translate(28.8199vw, 100vh) scale(0.6224);
  }
}

.snow:nth-child(43) {
  opacity: 0.406;
  transform: translate(25.9146vw, -10px) scale(0.3691);
  animation: fall-43 21s -17s linear infinite;
}

@keyframes fall-43 {
  74.543% {
    transform: translate(31.289vw, 74.543vh) scale(0.3691);
  }
  to {
    transform: translate(28.6018vw, 100vh) scale(0.3691);
  }
}

.snow:nth-child(44) {
  opacity: 0.5605;
  transform: translate(99.2295vw, -10px) scale(0.5779);
  animation: fall-44 11s -2s linear infinite;
}

@keyframes fall-44 {
  54.018% {
    transform: translate(107.815vw, 54.018vh) scale(0.5779);
  }
  to {
    transform: translate(103.52225vw, 100vh) scale(0.5779);
  }
}

.snow:nth-child(45) {
  opacity: 0.4851;
  transform: translate(57.5514vw, -10px) scale(0.2827);
  animation: fall-45 15s -11s linear infinite;
}

@keyframes fall-45 {
  44.887% {
    transform: translate(50.748vw, 44.887vh) scale(0.2827);
  }
  to {
    transform: translate(54.1497vw, 100vh) scale(0.2827);
  }
}

.snow:nth-child(46) {
  opacity: 0.9649;
  transform: translate(94.3479vw, -10px) scale(0.2388);
  animation: fall-46 22s -23s linear infinite;
}

@keyframes fall-46 {
  43.222% {
    transform: translate(97.3386vw, 43.222vh) scale(0.2388);
  }
  to {
    transform: translate(95.84325vw, 100vh) scale(0.2388);
  }
}

.snow:nth-child(47) {
  opacity: 0.8839;
  transform: translate(97.7669vw, -10px) scale(0.6773);
  animation: fall-47 12s -21s linear infinite;
}

@keyframes fall-47 {
  66.223% {
    transform: translate(97.7242vw, 66.223vh) scale(0.6773);
  }
  to {
    transform: translate(97.74555vw, 100vh) scale(0.6773);
  }
}

.snow:nth-child(48) {
  opacity: 0.0357;
  transform: translate(91.3977vw, -10px) scale(0.2684);
  animation: fall-48 17s -11s linear infinite;
}

@keyframes fall-48 {
  41.583% {
    transform: translate(85.6361vw, 41.583vh) scale(0.2684);
  }
  to {
    transform: translate(88.5169vw, 100vh) scale(0.2684);
  }
}

.snow:nth-child(49) {
  opacity: 0.8807;
  transform: translate(96.5392vw, -10px) scale(0.5036);
  animation: fall-49 15s -15s linear infinite;
}

@keyframes fall-49 {
  72.191% {
    transform: translate(90.6253vw, 72.191vh) scale(0.5036);
  }
  to {
    transform: translate(93.58225vw, 100vh) scale(0.5036);
  }
}

.snow:nth-child(50) {
  opacity: 0.6397;
  transform: translate(44.8778vw, -10px) scale(0.3107);
  animation: fall-50 21s -27s linear infinite;
}

@keyframes fall-50 {
  38.015% {
    transform: translate(44.6663vw, 38.015vh) scale(0.3107);
  }
  to {
    transform: translate(44.77205vw, 100vh) scale(0.3107);
  }
}

.snow:nth-child(51) {
  opacity: 0.6735;
  transform: translate(95.2773vw, -10px) scale(0.9188);
  animation: fall-51 27s -4s linear infinite;
}

@keyframes fall-51 {
  65.295% {
    transform: translate(90.6297vw, 65.295vh) scale(0.9188);
  }
  to {
    transform: translate(92.9535vw, 100vh) scale(0.9188);
  }
}

.snow:nth-child(52) {
  opacity: 0.0231;
  transform: translate(38.8241vw, -10px) scale(0.3806);
  animation: fall-52 11s -12s linear infinite;
}

@keyframes fall-52 {
  62.989% {
    transform: translate(46.7781vw, 62.989vh) scale(0.3806);
  }
  to {
    transform: translate(42.8011vw, 100vh) scale(0.3806);
  }
}

.snow:nth-child(53) {
  opacity: 0.2411;
  transform: translate(5.8748vw, -10px) scale(0.054);
  animation: fall-53 13s -26s linear infinite;
}

@keyframes fall-53 {
  48.749% {
    transform: translate(10.4325vw, 48.749vh) scale(0.054);
  }
  to {
    transform: translate(8.15365vw, 100vh) scale(0.054);
  }
}

.snow:nth-child(54) {
  opacity: 0.6466;
  transform: translate(62.3058vw, -10px) scale(0.2937);
  animation: fall-54 27s -22s linear infinite;
}

@keyframes fall-54 {
  55.667% {
    transform: translate(55.8671vw, 55.667vh) scale(0.2937);
  }
  to {
    transform: translate(59.08645vw, 100vh) scale(0.2937);
  }
}

.snow:nth-child(55) {
  opacity: 0.1404;
  transform: translate(96.6435vw, -10px) scale(0.351);
  animation: fall-55 30s -23s linear infinite;
}

@keyframes fall-55 {
  69.546% {
    transform: translate(94.7523vw, 69.546vh) scale(0.351);
  }
  to {
    transform: translate(95.6979vw, 100vh) scale(0.351);
  }
}

.snow:nth-child(56) {
  opacity: 0.4631;
  transform: translate(28.1847vw, -10px) scale(0.2596);
  animation: fall-56 22s -11s linear infinite;
}

@keyframes fall-56 {
  31.138% {
    transform: translate(30.1533vw, 31.138vh) scale(0.2596);
  }
  to {
    transform: translate(29.169vw, 100vh) scale(0.2596);
  }
}

.snow:nth-child(57) {
  opacity: 0.5919;
  transform: translate(54.8185vw, -10px) scale(0.8184);
  animation: fall-57 24s -3s linear infinite;
}

@keyframes fall-57 {
  65.948% {
    transform: translate(57.8831vw, 65.948vh) scale(0.8184);
  }
  to {
    transform: translate(56.3508vw, 100vh) scale(0.8184);
  }
}

.snow:nth-child(58) {
  opacity: 0.1496;
  transform: translate(22.0583vw, -10px) scale(0.6614);
  animation: fall-58 20s -13s linear infinite;
}

@keyframes fall-58 {
  56.136% {
    transform: translate(24.957vw, 56.136vh) scale(0.6614);
  }
  to {
    transform: translate(23.50765vw, 100vh) scale(0.6614);
  }
}

.snow:nth-child(59) {
  opacity: 0.0744;
  transform: translate(36.5348vw, -10px) scale(0.2137);
  animation: fall-59 17s -14s linear infinite;
}

@keyframes fall-59 {
  61.919% {
    transform: translate(29.5679vw, 61.919vh) scale(0.2137);
  }
  to {
    transform: translate(33.05135vw, 100vh) scale(0.2137);
  }
}

.snow:nth-child(60) {
  opacity: 0.6198;
  transform: translate(32.2001vw, -10px) scale(0.3932);
  animation: fall-60 24s -14s linear infinite;
}

@keyframes fall-60 {
  50.453% {
    transform: translate(41.9565vw, 50.453vh) scale(0.3932);
  }
  to {
    transform: translate(37.0783vw, 100vh) scale(0.3932);
  }
}

.snow:nth-child(61) {
  opacity: 0.5846;
  transform: translate(73.0187vw, -10px) scale(0.8451);
  animation: fall-61 19s -14s linear infinite;
}

@keyframes fall-61 {
  57.354% {
    transform: translate(72.5707vw, 57.354vh) scale(0.8451);
  }
  to {
    transform: translate(72.7947vw, 100vh) scale(0.8451);
  }
}

.snow:nth-child(62) {
  opacity: 0.8818;
  transform: translate(39.1348vw, -10px) scale(0.5366);
  animation: fall-62 28s -21s linear infinite;
}

@keyframes fall-62 {
  75.504% {
    transform: translate(43.5932vw, 75.504vh) scale(0.5366);
  }
  to {
    transform: translate(41.364vw, 100vh) scale(0.5366);
  }
}

.snow:nth-child(63) {
  opacity: 0.0714;
  transform: translate(15.4199vw, -10px) scale(0.5065);
  animation: fall-63 18s -19s linear infinite;
}

@keyframes fall-63 {
  62.172% {
    transform: translate(20.8971vw, 62.172vh) scale(0.5065);
  }
  to {
    transform: translate(18.1585vw, 100vh) scale(0.5065);
  }
}

.snow:nth-child(64) {
  opacity: 0.7851;
  transform: translate(75.1477vw, -10px) scale(0.1015);
  animation: fall-64 13s -29s linear infinite;
}

@keyframes fall-64 {
  74.843% {
    transform: translate(78.8444vw, 74.843vh) scale(0.1015);
  }
  to {
    transform: translate(76.99605vw, 100vh) scale(0.1015);
  }
}

.snow:nth-child(65) {
  opacity: 0.1696;
  transform: translate(68.6432vw, -10px) scale(0.1245);
  animation: fall-65 17s -2s linear infinite;
}

@keyframes fall-65 {
  54.226% {
    transform: translate(64.1739vw, 54.226vh) scale(0.1245);
  }
  to {
    transform: translate(66.40855vw, 100vh) scale(0.1245);
  }
}

.snow:nth-child(66) {
  opacity: 0.6992;
  transform: translate(86.8832vw, -10px) scale(0.1511);
  animation: fall-66 25s -13s linear infinite;
}

@keyframes fall-66 {
  66.144% {
    transform: translate(82.0091vw, 66.144vh) scale(0.1511);
  }
  to {
    transform: translate(84.44615vw, 100vh) scale(0.1511);
  }
}

.snow:nth-child(67) {
  opacity: 0.8865;
  transform: translate(76.1898vw, -10px) scale(0.7454);
  animation: fall-67 14s -11s linear infinite;
}

@keyframes fall-67 {
  39.621% {
    transform: translate(70.5307vw, 39.621vh) scale(0.7454);
  }
  to {
    transform: translate(73.36025vw, 100vh) scale(0.7454);
  }
}

.snow:nth-child(68) {
  opacity: 0.413;
  transform: translate(67.1523vw, -10px) scale(0.5187);
  animation: fall-68 20s -22s linear infinite;
}

@keyframes fall-68 {
  36.966% {
    transform: translate(74.8486vw, 36.966vh) scale(0.5187);
  }
  to {
    transform: translate(71.00045vw, 100vh) scale(0.5187);
  }
}

.snow:nth-child(69) {
  opacity: 0.9265;
  transform: translate(23.0827vw, -10px) scale(0.3732);
  animation: fall-69 30s -14s linear infinite;
}

@keyframes fall-69 {
  59.254% {
    transform: translate(19.7263vw, 59.254vh) scale(0.3732);
  }
  to {
    transform: translate(21.4045vw, 100vh) scale(0.3732);
  }
}

.snow:nth-child(70) {
  opacity: 0.5778;
  transform: translate(58.1355vw, -10px) scale(0.0207);
  animation: fall-70 20s -20s linear infinite;
}

@keyframes fall-70 {
  76.253% {
    transform: translate(54.6822vw, 76.253vh) scale(0.0207);
  }
  to {
    transform: translate(56.40885vw, 100vh) scale(0.0207);
  }
}

.snow:nth-child(71) {
  opacity: 0.1577;
  transform: translate(27.0156vw, -10px) scale(0.8398);
  animation: fall-71 22s -21s linear infinite;
}

@keyframes fall-71 {
  37.641% {
    transform: translate(20.7124vw, 37.641vh) scale(0.8398);
  }
  to {
    transform: translate(23.864vw, 100vh) scale(0.8398);
  }
}

.snow:nth-child(72) {
  opacity: 0.3474;
  transform: translate(1.9463vw, -10px) scale(0.2194);
  animation: fall-72 26s -10s linear infinite;
}

@keyframes fall-72 {
  43.343% {
    transform: translate(9.3291vw, 43.343vh) scale(0.2194);
  }
  to {
    transform: translate(5.6377vw, 100vh) scale(0.2194);
  }
}

.snow:nth-child(73) {
  opacity: 0.0454;
  transform: translate(81.4953vw, -10px) scale(0.5378);
  animation: fall-73 25s -7s linear infinite;
}

@keyframes fall-73 {
  66.933% {
    transform: translate(81.0792vw, 66.933vh) scale(0.5378);
  }
  to {
    transform: translate(81.28725vw, 100vh) scale(0.5378);
  }
}

.snow:nth-child(74) {
  opacity: 0.996;
  transform: translate(39.6585vw, -10px) scale(0.17);
  animation: fall-74 13s -15s linear infinite;
}

@keyframes fall-74 {
  56.369% {
    transform: translate(47.1193vw, 56.369vh) scale(0.17);
  }
  to {
    transform: translate(43.3889vw, 100vh) scale(0.17);
  }
}

.snow:nth-child(75) {
  opacity: 0.0143;
  transform: translate(60.2185vw, -10px) scale(0.791);
  animation: fall-75 18s -30s linear infinite;
}

@keyframes fall-75 {
  73.218% {
    transform: translate(67.9447vw, 73.218vh) scale(0.791);
  }
  to {
    transform: translate(64.0816vw, 100vh) scale(0.791);
  }
}

.snow:nth-child(76) {
  opacity: 0.7024;
  transform: translate(71.7743vw, -10px) scale(0.8368);
  animation: fall-76 22s -21s linear infinite;
}

@keyframes fall-76 {
  33.506% {
    transform: translate(67.5486vw, 33.506vh) scale(0.8368);
  }
  to {
    transform: translate(69.66145vw, 100vh) scale(0.8368);
  }
}

.snow:nth-child(77) {
  opacity: 0.4342;
  transform: translate(88.9102vw, -10px) scale(0.769);
  animation: fall-77 12s -16s linear infinite;
}

@keyframes fall-77 {
  79.273% {
    transform: translate(88.3696vw, 79.273vh) scale(0.769);
  }
  to {
    transform: translate(88.6399vw, 100vh) scale(0.769);
  }
}

.snow:nth-child(78) {
  opacity: 0.6814;
  transform: translate(88.2544vw, -10px) scale(0.2123);
  animation: fall-78 23s -3s linear infinite;
}

@keyframes fall-78 {
  69.612% {
    transform: translate(78.2829vw, 69.612vh) scale(0.2123);
  }
  to {
    transform: translate(83.26865vw, 100vh) scale(0.2123);
  }
}

.snow:nth-child(79) {
  opacity: 0.1705;
  transform: translate(70.0208vw, -10px) scale(0.7884);
  animation: fall-79 13s -16s linear infinite;
}

@keyframes fall-79 {
  47.254% {
    transform: translate(66.5639vw, 47.254vh) scale(0.7884);
  }
  to {
    transform: translate(68.29235vw, 100vh) scale(0.7884);
  }
}

.snow:nth-child(80) {
  opacity: 0.6031;
  transform: translate(67.2927vw, -10px) scale(0.6104);
  animation: fall-80 12s -28s linear infinite;
}

@keyframes fall-80 {
  58.484% {
    transform: translate(61.6041vw, 58.484vh) scale(0.6104);
  }
  to {
    transform: translate(64.4484vw, 100vh) scale(0.6104);
  }
}

.snow:nth-child(81) {
  opacity: 0.0841;
  transform: translate(76.6165vw, -10px) scale(0.1844);
  animation: fall-81 24s -26s linear infinite;
}

@keyframes fall-81 {
  44.135% {
    transform: translate(81.6971vw, 44.135vh) scale(0.1844);
  }
  to {
    transform: translate(79.1568vw, 100vh) scale(0.1844);
  }
}

.snow:nth-child(82) {
  opacity: 0.5337;
  transform: translate(7.9113vw, -10px) scale(0.3058);
  animation: fall-82 18s -29s linear infinite;
}

@keyframes fall-82 {
  66.523% {
    transform: translate(10.2769vw, 66.523vh) scale(0.3058);
  }
  to {
    transform: translate(9.0941vw, 100vh) scale(0.3058);
  }
}

.snow:nth-child(83) {
  opacity: 0.1049;
  transform: translate(6.2796vw, -10px) scale(0.0803);
  animation: fall-83 14s -19s linear infinite;
}

@keyframes fall-83 {
  30.415% {
    transform: translate(2.7165vw, 30.415vh) scale(0.0803);
  }
  to {
    transform: translate(4.49805vw, 100vh) scale(0.0803);
  }
}

.snow:nth-child(84) {
  opacity: 0.3704;
  transform: translate(33.864vw, -10px) scale(0.8929);
  animation: fall-84 23s -11s linear infinite;
}

@keyframes fall-84 {
  39.376% {
    transform: translate(40.1532vw, 39.376vh) scale(0.8929);
  }
  to {
    transform: translate(37.0086vw, 100vh) scale(0.8929);
  }
}

.snow:nth-child(85) {
  opacity: 0.5712;
  transform: translate(18.7134vw, -10px) scale(0.7693);
  animation: fall-85 26s -2s linear infinite;
}

@keyframes fall-85 {
  55.29% {
    transform: translate(25.0842vw, 55.29vh) scale(0.7693);
  }
  to {
    transform: translate(21.8988vw, 100vh) scale(0.7693);
  }
}

.snow:nth-child(86) {
  opacity: 0.5252;
  transform: translate(61.4402vw, -10px) scale(0.466);
  animation: fall-86 30s -15s linear infinite;
}

@keyframes fall-86 {
  34.042% {
    transform: translate(62.8934vw, 34.042vh) scale(0.466);
  }
  to {
    transform: translate(62.1668vw, 100vh) scale(0.466);
  }
}

.snow:nth-child(87) {
  opacity: 0.3569;
  transform: translate(59.5814vw, -10px) scale(0.0709);
  animation: fall-87 18s -20s linear infinite;
}

@keyframes fall-87 {
  78.129% {
    transform: translate(49.7594vw, 78.129vh) scale(0.0709);
  }
  to {
    transform: translate(54.6704vw, 100vh) scale(0.0709);
  }
}

.snow:nth-child(88) {
  opacity: 0.7184;
  transform: translate(62.7661vw, -10px) scale(0.663);
  animation: fall-88 18s -19s linear infinite;
}

@keyframes fall-88 {
  66.147% {
    transform: translate(61.8307vw, 66.147vh) scale(0.663);
  }
  to {
    transform: translate(62.2984vw, 100vh) scale(0.663);
  }
}

.snow:nth-child(89) {
  opacity: 0.1788;
  transform: translate(10.0498vw, -10px) scale(0.9103);
  animation: fall-89 25s -11s linear infinite;
}

@keyframes fall-89 {
  62.917% {
    transform: translate(16.2601vw, 62.917vh) scale(0.9103);
  }
  to {
    transform: translate(13.15495vw, 100vh) scale(0.9103);
  }
}

.snow:nth-child(90) {
  opacity: 0.0975;
  transform: translate(10.2986vw, -10px) scale(0.4348);
  animation: fall-90 19s -27s linear infinite;
}

@keyframes fall-90 {
  64.172% {
    transform: translate(17.896vw, 64.172vh) scale(0.4348);
  }
  to {
    transform: translate(14.0973vw, 100vh) scale(0.4348);
  }
}

.snow:nth-child(91) {
  opacity: 0.3737;
  transform: translate(99.658vw, -10px) scale(0.1164);
  animation: fall-91 19s -25s linear infinite;
}

@keyframes fall-91 {
  70.793% {
    transform: translate(102.6064vw, 70.793vh) scale(0.1164);
  }
  to {
    transform: translate(101.1322vw, 100vh) scale(0.1164);
  }
}

.snow:nth-child(92) {
  opacity: 0.104;
  transform: translate(86.7059vw, -10px) scale(0.3002);
  animation: fall-92 25s -11s linear infinite;
}

@keyframes fall-92 {
  39.114% {
    transform: translate(82.128vw, 39.114vh) scale(0.3002);
  }
  to {
    transform: translate(84.41695vw, 100vh) scale(0.3002);
  }
}

.snow:nth-child(93) {
  opacity: 0.5057;
  transform: translate(50.7716vw, -10px) scale(0.1901);
  animation: fall-93 28s -4s linear infinite;
}

@keyframes fall-93 {
  52.52% {
    transform: translate(60.3327vw, 52.52vh) scale(0.1901);
  }
  to {
    transform: translate(55.55215vw, 100vh) scale(0.1901);
  }
}

.snow:nth-child(94) {
  opacity: 0.8098;
  transform: translate(70.0962vw, -10px) scale(0.6367);
  animation: fall-94 26s -19s linear infinite;
}

@keyframes fall-94 {
  49.778% {
    transform: translate(61.2205vw, 49.778vh) scale(0.6367);
  }
  to {
    transform: translate(65.65835vw, 100vh) scale(0.6367);
  }
}

.snow:nth-child(95) {
  opacity: 0.5282;
  transform: translate(17.7108vw, -10px) scale(0.9511);
  animation: fall-95 24s -8s linear infinite;
}

@keyframes fall-95 {
  51.848% {
    transform: translate(21.882vw, 51.848vh) scale(0.9511);
  }
  to {
    transform: translate(19.7964vw, 100vh) scale(0.9511);
  }
}

.snow:nth-child(96) {
  opacity: 0.5748;
  transform: translate(50.0518vw, -10px) scale(0.9206);
  animation: fall-96 15s -3s linear infinite;
}

@keyframes fall-96 {
  54.18% {
    transform: translate(48.8608vw, 54.18vh) scale(0.9206);
  }
  to {
    transform: translate(49.4563vw, 100vh) scale(0.9206);
  }
}

.snow:nth-child(97) {
  opacity: 0.7027;
  transform: translate(2.5217vw, -10px) scale(0.8402);
  animation: fall-97 13s -26s linear infinite;
}

@keyframes fall-97 {
  60.28% {
    transform: translate(-2.3001vw, 60.28vh) scale(0.8402);
  }
  to {
    transform: translate(0.1108vw, 100vh) scale(0.8402);
  }
}

.snow:nth-child(98) {
  opacity: 0.0077;
  transform: translate(36.111vw, -10px) scale(0.1318);
  animation: fall-98 16s -25s linear infinite;
}

@keyframes fall-98 {
  36.95% {
    transform: translate(35.3133vw, 36.95vh) scale(0.1318);
  }
  to {
    transform: translate(35.71215vw, 100vh) scale(0.1318);
  }
}

.snow:nth-child(99) {
  opacity: 0.5995;
  transform: translate(62.1118vw, -10px) scale(0.8073);
  animation: fall-99 28s -25s linear infinite;
}

@keyframes fall-99 {
  34.643% {
    transform: translate(57.1413vw, 34.643vh) scale(0.8073);
  }
  to {
    transform: translate(59.62655vw, 100vh) scale(0.8073);
  }
}

.snow:nth-child(100) {
  opacity: 0.1884;
  transform: translate(10.974vw, -10px) scale(0.6027);
  animation: fall-100 15s -14s linear infinite;
}

@keyframes fall-100 {
  41.689% {
    transform: translate(20.1175vw, 41.689vh) scale(0.6027);
  }
  to {
    transform: translate(15.54575vw, 100vh) scale(0.6027);
  }
}

.snow:nth-child(101) {
  opacity: 0.1032;
  transform: translate(65.1039vw, -10px) scale(0.2215);
  animation: fall-101 26s -19s linear infinite;
}

@keyframes fall-101 {
  51.588% {
    transform: translate(72.7075vw, 51.588vh) scale(0.2215);
  }
  to {
    transform: translate(68.9057vw, 100vh) scale(0.2215);
  }
}

.snow:nth-child(102) {
  opacity: 0.0071;
  transform: translate(30.7195vw, -10px) scale(0.8275);
  animation: fall-102 22s -6s linear infinite;
}

@keyframes fall-102 {
  77.976% {
    transform: translate(30.78vw, 77.976vh) scale(0.8275);
  }
  to {
    transform: translate(30.74975vw, 100vh) scale(0.8275);
  }
}

.snow:nth-child(103) {
  opacity: 0.3412;
  transform: translate(84.9462vw, -10px) scale(0.3098);
  animation: fall-103 13s -21s linear infinite;
}

@keyframes fall-103 {
  35.867% {
    transform: translate(89.3392vw, 35.867vh) scale(0.3098);
  }
  to {
    transform: translate(87.1427vw, 100vh) scale(0.3098);
  }
}

.snow:nth-child(104) {
  opacity: 0.5894;
  transform: translate(20.1514vw, -10px) scale(0.3894);
  animation: fall-104 15s -26s linear infinite;
}

@keyframes fall-104 {
  66.265% {
    transform: translate(30.1366vw, 66.265vh) scale(0.3894);
  }
  to {
    transform: translate(25.144vw, 100vh) scale(0.3894);
  }
}

.snow:nth-child(105) {
  opacity: 0.6248;
  transform: translate(32.8659vw, -10px) scale(0.0765);
  animation: fall-105 28s -22s linear infinite;
}

@keyframes fall-105 {
  39.971% {
    transform: translate(40.9758vw, 39.971vh) scale(0.0765);
  }
  to {
    transform: translate(36.92085vw, 100vh) scale(0.0765);
  }
}

.snow:nth-child(106) {
  opacity: 0.7692;
  transform: translate(0.5097vw, -10px) scale(0.64);
  animation: fall-106 20s -6s linear infinite;
}

@keyframes fall-106 {
  65.73% {
    transform: translate(7.9616vw, 65.73vh) scale(0.64);
  }
  to {
    transform: translate(4.23565vw, 100vh) scale(0.64);
  }
}

.snow:nth-child(107) {
  opacity: 0.9274;
  transform: translate(0.7791vw, -10px) scale(0.1684);
  animation: fall-107 14s -16s linear infinite;
}

@keyframes fall-107 {
  73.053% {
    transform: translate(-2.7388vw, 73.053vh) scale(0.1684);
  }
  to {
    transform: translate(-0.97985vw, 100vh) scale(0.1684);
  }
}

.snow:nth-child(108) {
  opacity: 0.3137;
  transform: translate(2.6891vw, -10px) scale(0.3328);
  animation: fall-108 15s -11s linear infinite;
}

@keyframes fall-108 {
  61.752% {
    transform: translate(10.9352vw, 61.752vh) scale(0.3328);
  }
  to {
    transform: translate(6.81215vw, 100vh) scale(0.3328);
  }
}

.snow:nth-child(109) {
  opacity: 0.6786;
  transform: translate(64.6386vw, -10px) scale(0.91);
  animation: fall-109 10s -18s linear infinite;
}

@keyframes fall-109 {
  77.412% {
    transform: translate(55.9299vw, 77.412vh) scale(0.91);
  }
  to {
    transform: translate(60.28425vw, 100vh) scale(0.91);
  }
}

.snow:nth-child(110) {
  opacity: 0.8438;
  transform: translate(57.0459vw, -10px) scale(0.5205);
  animation: fall-110 29s -3s linear infinite;
}

@keyframes fall-110 {
  71.57% {
    transform: translate(56.3289vw, 71.57vh) scale(0.5205);
  }
  to {
    transform: translate(56.6874vw, 100vh) scale(0.5205);
  }
}

.snow:nth-child(111) {
  opacity: 0.6761;
  transform: translate(29.2213vw, -10px) scale(0.0455);
  animation: fall-111 21s -7s linear infinite;
}

@keyframes fall-111 {
  61.868% {
    transform: translate(33.9581vw, 61.868vh) scale(0.0455);
  }
  to {
    transform: translate(31.5897vw, 100vh) scale(0.0455);
  }
}

.snow:nth-child(112) {
  opacity: 0.7512;
  transform: translate(83.8535vw, -10px) scale(0.1898);
  animation: fall-112 28s -8s linear infinite;
}

@keyframes fall-112 {
  77.094% {
    transform: translate(84.7051vw, 77.094vh) scale(0.1898);
  }
  to {
    transform: translate(84.2793vw, 100vh) scale(0.1898);
  }
}

.snow:nth-child(113) {
  opacity: 0.2481;
  transform: translate(40.2495vw, -10px) scale(0.1404);
  animation: fall-113 11s -23s linear infinite;
}

@keyframes fall-113 {
  56.797% {
    transform: translate(49.1171vw, 56.797vh) scale(0.1404);
  }
  to {
    transform: translate(44.6833vw, 100vh) scale(0.1404);
  }
}

.snow:nth-child(114) {
  opacity: 0.8418;
  transform: translate(88.5325vw, -10px) scale(0.6673);
  animation: fall-114 12s -19s linear infinite;
}

@keyframes fall-114 {
  51.091% {
    transform: translate(93.8058vw, 51.091vh) scale(0.6673);
  }
  to {
    transform: translate(91.16915vw, 100vh) scale(0.6673);
  }
}

.snow:nth-child(115) {
  opacity: 0.1785;
  transform: translate(98.0879vw, -10px) scale(0.5226);
  animation: fall-115 11s -15s linear infinite;
}

@keyframes fall-115 {
  58.723% {
    transform: translate(106.6353vw, 58.723vh) scale(0.5226);
  }
  to {
    transform: translate(102.3616vw, 100vh) scale(0.5226);
  }
}

.snow:nth-child(116) {
  opacity: 0.7236;
  transform: translate(31.4221vw, -10px) scale(0.8912);
  animation: fall-116 20s -29s linear infinite;
}

@keyframes fall-116 {
  47.61% {
    transform: translate(23.5717vw, 47.61vh) scale(0.8912);
  }
  to {
    transform: translate(27.4969vw, 100vh) scale(0.8912);
  }
}

.snow:nth-child(117) {
  opacity: 0.7501;
  transform: translate(15.0566vw, -10px) scale(0.8518);
  animation: fall-117 21s -26s linear infinite;
}

@keyframes fall-117 {
  37.769% {
    transform: translate(15.2612vw, 37.769vh) scale(0.8518);
  }
  to {
    transform: translate(15.1589vw, 100vh) scale(0.8518);
  }
}

.snow:nth-child(118) {
  opacity: 0.2496;
  transform: translate(96.3781vw, -10px) scale(0.3584);
  animation: fall-118 28s -2s linear infinite;
}

@keyframes fall-118 {
  65.557% {
    transform: translate(106.108vw, 65.557vh) scale(0.3584);
  }
  to {
    transform: translate(101.24305vw, 100vh) scale(0.3584);
  }
}

.snow:nth-child(119) {
  opacity: 0.1696;
  transform: translate(41.7103vw, -10px) scale(0.9945);
  animation: fall-119 22s -9s linear infinite;
}

@keyframes fall-119 {
  65.46% {
    transform: translate(33.3324vw, 65.46vh) scale(0.9945);
  }
  to {
    transform: translate(37.52135vw, 100vh) scale(0.9945);
  }
}

.snow:nth-child(120) {
  opacity: 0.3258;
  transform: translate(44.9271vw, -10px) scale(0.5279);
  animation: fall-120 28s -22s linear infinite;
}

@keyframes fall-120 {
  56.626% {
    transform: translate(36.7572vw, 56.626vh) scale(0.5279);
  }
  to {
    transform: translate(40.84215vw, 100vh) scale(0.5279);
  }
}

.snow:nth-child(121) {
  opacity: 0.8755;
  transform: translate(15.4426vw, -10px) scale(0.8562);
  animation: fall-121 26s -8s linear infinite;
}

@keyframes fall-121 {
  59.779% {
    transform: translate(22.9567vw, 59.779vh) scale(0.8562);
  }
  to {
    transform: translate(19.19965vw, 100vh) scale(0.8562);
  }
}

.snow:nth-child(122) {
  opacity: 0.5855;
  transform: translate(67.0238vw, -10px) scale(0.0153);
  animation: fall-122 23s -21s linear infinite;
}

@keyframes fall-122 {
  77.419% {
    transform: translate(59.5382vw, 77.419vh) scale(0.0153);
  }
  to {
    transform: translate(63.281vw, 100vh) scale(0.0153);
  }
}

.snow:nth-child(123) {
  opacity: 0.3011;
  transform: translate(99.6191vw, -10px) scale(0.7602);
  animation: fall-123 23s -23s linear infinite;
}

@keyframes fall-123 {
  78.988% {
    transform: translate(105.0933vw, 78.988vh) scale(0.7602);
  }
  to {
    transform: translate(102.3562vw, 100vh) scale(0.7602);
  }
}

.snow:nth-child(124) {
  opacity: 0.21;
  transform: translate(49.9926vw, -10px) scale(0.6693);
  animation: fall-124 29s -9s linear infinite;
}

@keyframes fall-124 {
  30.37% {
    transform: translate(54.3683vw, 30.37vh) scale(0.6693);
  }
  to {
    transform: translate(52.18045vw, 100vh) scale(0.6693);
  }
}

.snow:nth-child(125) {
  opacity: 0.2899;
  transform: translate(59.4507vw, -10px) scale(0.2821);
  animation: fall-125 17s -29s linear infinite;
}

@keyframes fall-125 {
  30.404% {
    transform: translate(58.4615vw, 30.404vh) scale(0.2821);
  }
  to {
    transform: translate(58.9561vw, 100vh) scale(0.2821);
  }
}

.snow:nth-child(126) {
  opacity: 0.4319;
  transform: translate(20.4901vw, -10px) scale(0.6941);
  animation: fall-126 25s -28s linear infinite;
}

@keyframes fall-126 {
  37.401% {
    transform: translate(10.8166vw, 37.401vh) scale(0.6941);
  }
  to {
    transform: translate(15.65335vw, 100vh) scale(0.6941);
  }
}

.snow:nth-child(127) {
  opacity: 0.4996;
  transform: translate(82.9972vw, -10px) scale(0.1008);
  animation: fall-127 21s -3s linear infinite;
}

@keyframes fall-127 {
  78.201% {
    transform: translate(77.9659vw, 78.201vh) scale(0.1008);
  }
  to {
    transform: translate(80.48155vw, 100vh) scale(0.1008);
  }
}

.snow:nth-child(128) {
  opacity: 0.0411;
  transform: translate(75.6205vw, -10px) scale(0.4767);
  animation: fall-128 12s -29s linear infinite;
}

@keyframes fall-128 {
  40.654% {
    transform: translate(68.6068vw, 40.654vh) scale(0.4767);
  }
  to {
    transform: translate(72.11365vw, 100vh) scale(0.4767);
  }
}

.snow:nth-child(129) {
  opacity: 0.1419;
  transform: translate(1.4319vw, -10px) scale(0.6248);
  animation: fall-129 29s -7s linear infinite;
}

@keyframes fall-129 {
  65.467% {
    transform: translate(-1.8227vw, 65.467vh) scale(0.6248);
  }
  to {
    transform: translate(-0.1954vw, 100vh) scale(0.6248);
  }
}

.snow:nth-child(130) {
  opacity: 0.4739;
  transform: translate(49.2206vw, -10px) scale(0.0267);
  animation: fall-130 22s -30s linear infinite;
}

@keyframes fall-130 {
  65.761% {
    transform: translate(58.6285vw, 65.761vh) scale(0.0267);
  }
  to {
    transform: translate(53.92455vw, 100vh) scale(0.0267);
  }
}

.snow:nth-child(131) {
  opacity: 0.3245;
  transform: translate(9.859vw, -10px) scale(0.1274);
  animation: fall-131 29s -30s linear infinite;
}

@keyframes fall-131 {
  59.372% {
    transform: translate(9.5047vw, 59.372vh) scale(0.1274);
  }
  to {
    transform: translate(9.68185vw, 100vh) scale(0.1274);
  }
}

.snow:nth-child(132) {
  opacity: 0.7018;
  transform: translate(95.3654vw, -10px) scale(0.5346);
  animation: fall-132 21s -6s linear infinite;
}

@keyframes fall-132 {
  73.707% {
    transform: translate(89.5764vw, 73.707vh) scale(0.5346);
  }
  to {
    transform: translate(92.4709vw, 100vh) scale(0.5346);
  }
}

.snow:nth-child(133) {
  opacity: 0.3785;
  transform: translate(74.9538vw, -10px) scale(0.9795);
  animation: fall-133 26s -10s linear infinite;
}

@keyframes fall-133 {
  51.745% {
    transform: translate(81.499vw, 51.745vh) scale(0.9795);
  }
  to {
    transform: translate(78.2264vw, 100vh) scale(0.9795);
  }
}

.snow:nth-child(134) {
  opacity: 0.819;
  transform: translate(19.5394vw, -10px) scale(0.9734);
  animation: fall-134 30s -21s linear infinite;
}

@keyframes fall-134 {
  34.341% {
    transform: translate(21.8859vw, 34.341vh) scale(0.9734);
  }
  to {
    transform: translate(20.71265vw, 100vh) scale(0.9734);
  }
}

.snow:nth-child(135) {
  opacity: 0.6801;
  transform: translate(22.8505vw, -10px) scale(0.7007);
  animation: fall-135 14s -12s linear infinite;
}

@keyframes fall-135 {
  76.164% {
    transform: translate(22.0253vw, 76.164vh) scale(0.7007);
  }
  to {
    transform: translate(22.4379vw, 100vh) scale(0.7007);
  }
}

.snow:nth-child(136) {
  opacity: 0.956;
  transform: translate(52.8151vw, -10px) scale(0.3086);
  animation: fall-136 13s -12s linear infinite;
}

@keyframes fall-136 {
  59.926% {
    transform: translate(52.7885vw, 59.926vh) scale(0.3086);
  }
  to {
    transform: translate(52.8018vw, 100vh) scale(0.3086);
  }
}

.snow:nth-child(137) {
  opacity: 0.4625;
  transform: translate(93.781vw, -10px) scale(0.9684);
  animation: fall-137 19s -29s linear infinite;
}

@keyframes fall-137 {
  44.81% {
    transform: translate(88.5508vw, 44.81vh) scale(0.9684);
  }
  to {
    transform: translate(91.1659vw, 100vh) scale(0.9684);
  }
}

.snow:nth-child(138) {
  opacity: 0.8095;
  transform: translate(67.9456vw, -10px) scale(0.9655);
  animation: fall-138 24s -6s linear infinite;
}

@keyframes fall-138 {
  67.902% {
    transform: translate(69.5261vw, 67.902vh) scale(0.9655);
  }
  to {
    transform: translate(68.73585vw, 100vh) scale(0.9655);
  }
}

.snow:nth-child(139) {
  opacity: 0.1952;
  transform: translate(64.8564vw, -10px) scale(0.1832);
  animation: fall-139 23s -20s linear infinite;
}

@keyframes fall-139 {
  38.819% {
    transform: translate(68.7641vw, 38.819vh) scale(0.1832);
  }
  to {
    transform: translate(66.81025vw, 100vh) scale(0.1832);
  }
}

.snow:nth-child(140) {
  opacity: 0.0274;
  transform: translate(25.9467vw, -10px) scale(0.3103);
  animation: fall-140 18s -14s linear infinite;
}

@keyframes fall-140 {
  72.334% {
    transform: translate(18.1545vw, 72.334vh) scale(0.3103);
  }
  to {
    transform: translate(22.0506vw, 100vh) scale(0.3103);
  }
}

.snow:nth-child(141) {
  opacity: 0.1734;
  transform: translate(16.7161vw, -10px) scale(0.3419);
  animation: fall-141 15s -26s linear infinite;
}

@keyframes fall-141 {
  75.259% {
    transform: translate(8.7218vw, 75.259vh) scale(0.3419);
  }
  to {
    transform: translate(12.71895vw, 100vh) scale(0.3419);
  }
}

.snow:nth-child(142) {
  opacity: 0.1811;
  transform: translate(96.0668vw, -10px) scale(1);
  animation: fall-142 19s -2s linear infinite;
}

@keyframes fall-142 {
  76.752% {
    transform: translate(100.279vw, 76.752vh) scale(1);
  }
  to {
    transform: translate(98.1729vw, 100vh) scale(1);
  }
}

.snow:nth-child(143) {
  opacity: 0.1459;
  transform: translate(40.876vw, -10px) scale(0.9079);
  animation: fall-143 25s -10s linear infinite;
}

@keyframes fall-143 {
  46.598% {
    transform: translate(50.6877vw, 46.598vh) scale(0.9079);
  }
  to {
    transform: translate(45.78185vw, 100vh) scale(0.9079);
  }
}

.snow:nth-child(144) {
  opacity: 0.0467;
  transform: translate(96.2652vw, -10px) scale(0.9263);
  animation: fall-144 21s -26s linear infinite;
}

@keyframes fall-144 {
  41.717% {
    transform: translate(90.7505vw, 41.717vh) scale(0.9263);
  }
  to {
    transform: translate(93.50785vw, 100vh) scale(0.9263);
  }
}

.snow:nth-child(145) {
  opacity: 0.7646;
  transform: translate(80.6242vw, -10px) scale(0.747);
  animation: fall-145 13s -26s linear infinite;
}

@keyframes fall-145 {
  45.397% {
    transform: translate(70.7027vw, 45.397vh) scale(0.747);
  }
  to {
    transform: translate(75.66345vw, 100vh) scale(0.747);
  }
}

.snow:nth-child(146) {
  opacity: 0.0586;
  transform: translate(42.4919vw, -10px) scale(0.1035);
  animation: fall-146 24s -6s linear infinite;
}

@keyframes fall-146 {
  43.443% {
    transform: translate(39.3104vw, 43.443vh) scale(0.1035);
  }
  to {
    transform: translate(40.90115vw, 100vh) scale(0.1035);
  }
}

.snow:nth-child(147) {
  opacity: 0.9094;
  transform: translate(20.4989vw, -10px) scale(0.8508);
  animation: fall-147 30s -2s linear infinite;
}

@keyframes fall-147 {
  51.144% {
    transform: translate(26.4737vw, 51.144vh) scale(0.8508);
  }
  to {
    transform: translate(23.4863vw, 100vh) scale(0.8508);
  }
}

.snow:nth-child(148) {
  opacity: 0.6408;
  transform: translate(84.4483vw, -10px) scale(0.8175);
  animation: fall-148 10s -16s linear infinite;
}

@keyframes fall-148 {
  62.263% {
    transform: translate(78.458vw, 62.263vh) scale(0.8175);
  }
  to {
    transform: translate(81.45315vw, 100vh) scale(0.8175);
  }
}

.snow:nth-child(149) {
  opacity: 0.6168;
  transform: translate(81.188vw, -10px) scale(0.9148);
  animation: fall-149 29s -22s linear infinite;
}

@keyframes fall-149 {
  72.419% {
    transform: translate(89.7904vw, 72.419vh) scale(0.9148);
  }
  to {
    transform: translate(85.4892vw, 100vh) scale(0.9148);
  }
}

.snow:nth-child(150) {
  opacity: 0.5502;
  transform: translate(40.0644vw, -10px) scale(0.3217);
  animation: fall-150 15s -4s linear infinite;
}

@keyframes fall-150 {
  42.2% {
    transform: translate(42.3636vw, 42.2vh) scale(0.3217);
  }
  to {
    transform: translate(41.214vw, 100vh) scale(0.3217);
  }
}

.snow:nth-child(151) {
  opacity: 0.3571;
  transform: translate(44.6394vw, -10px) scale(0.2336);
  animation: fall-151 21s -26s linear infinite;
}

@keyframes fall-151 {
  34.972% {
    transform: translate(51.5942vw, 34.972vh) scale(0.2336);
  }
  to {
    transform: translate(48.1168vw, 100vh) scale(0.2336);
  }
}

.snow:nth-child(152) {
  opacity: 0.0966;
  transform: translate(58.412vw, -10px) scale(0.3952);
  animation: fall-152 29s -25s linear infinite;
}

@keyframes fall-152 {
  72.593% {
    transform: translate(64.0153vw, 72.593vh) scale(0.3952);
  }
  to {
    transform: translate(61.21365vw, 100vh) scale(0.3952);
  }
}

.snow:nth-child(153) {
  opacity: 0.5873;
  transform: translate(41.1859vw, -10px) scale(0.1109);
  animation: fall-153 30s -27s linear infinite;
}

@keyframes fall-153 {
  41.921% {
    transform: translate(31.9089vw, 41.921vh) scale(0.1109);
  }
  to {
    transform: translate(36.5474vw, 100vh) scale(0.1109);
  }
}

.snow:nth-child(154) {
  opacity: 0.0538;
  transform: translate(83.7483vw, -10px) scale(0.9466);
  animation: fall-154 10s -22s linear infinite;
}

@keyframes fall-154 {
  61.767% {
    transform: translate(80.0036vw, 61.767vh) scale(0.9466);
  }
  to {
    transform: translate(81.87595vw, 100vh) scale(0.9466);
  }
}

.snow:nth-child(155) {
  opacity: 0.0017;
  transform: translate(0.0828vw, -10px) scale(0.134);
  animation: fall-155 12s -28s linear infinite;
}

@keyframes fall-155 {
  35.578% {
    transform: translate(9.2916vw, 35.578vh) scale(0.134);
  }
  to {
    transform: translate(4.6872vw, 100vh) scale(0.134);
  }
}

.snow:nth-child(156) {
  opacity: 0.1662;
  transform: translate(77.6334vw, -10px) scale(0.1233);
  animation: fall-156 15s -8s linear infinite;
}

@keyframes fall-156 {
  35.491% {
    transform: translate(79.3889vw, 35.491vh) scale(0.1233);
  }
  to {
    transform: translate(78.51115vw, 100vh) scale(0.1233);
  }
}

.snow:nth-child(157) {
  opacity: 0.297;
  transform: translate(26.9763vw, -10px) scale(0.5861);
  animation: fall-157 23s -23s linear infinite;
}

@keyframes fall-157 {
  44.355% {
    transform: translate(27.8091vw, 44.355vh) scale(0.5861);
  }
  to {
    transform: translate(27.3927vw, 100vh) scale(0.5861);
  }
}

.snow:nth-child(158) {
  opacity: 0.9166;
  transform: translate(99.78vw, -10px) scale(0.611);
  animation: fall-158 21s -16s linear infinite;
}

@keyframes fall-158 {
  68.38% {
    transform: translate(98.9115vw, 68.38vh) scale(0.611);
  }
  to {
    transform: translate(99.34575vw, 100vh) scale(0.611);
  }
}

.snow:nth-child(159) {
  opacity: 0.4495;
  transform: translate(48.6331vw, -10px) scale(0.2247);
  animation: fall-159 28s -24s linear infinite;
}

@keyframes fall-159 {
  38.865% {
    transform: translate(56.3253vw, 38.865vh) scale(0.2247);
  }
  to {
    transform: translate(52.4792vw, 100vh) scale(0.2247);
  }
}

.snow:nth-child(160) {
  opacity: 0.3695;
  transform: translate(20.7791vw, -10px) scale(0.972);
  animation: fall-160 30s -6s linear infinite;
}

@keyframes fall-160 {
  55.712% {
    transform: translate(15.9975vw, 55.712vh) scale(0.972);
  }
  to {
    transform: translate(18.3883vw, 100vh) scale(0.972);
  }
}

.snow:nth-child(161) {
  opacity: 0.6087;
  transform: translate(14.9672vw, -10px) scale(0.2158);
  animation: fall-161 24s -25s linear infinite;
}

@keyframes fall-161 {
  64.566% {
    transform: translate(8.278vw, 64.566vh) scale(0.2158);
  }
  to {
    transform: translate(11.6226vw, 100vh) scale(0.2158);
  }
}

.snow:nth-child(162) {
  opacity: 0.3896;
  transform: translate(50.1376vw, -10px) scale(0.9284);
  animation: fall-162 28s -11s linear infinite;
}

@keyframes fall-162 {
  62.561% {
    transform: translate(56.9732vw, 62.561vh) scale(0.9284);
  }
  to {
    transform: translate(53.5554vw, 100vh) scale(0.9284);
  }
}

.snow:nth-child(163) {
  opacity: 0.0212;
  transform: translate(85.9253vw, -10px) scale(0.7359);
  animation: fall-163 24s -24s linear infinite;
}

@keyframes fall-163 {
  73.314% {
    transform: translate(82.3423vw, 73.314vh) scale(0.7359);
  }
  to {
    transform: translate(84.1338vw, 100vh) scale(0.7359);
  }
}

.snow:nth-child(164) {
  opacity: 0.3433;
  transform: translate(1.1948vw, -10px) scale(0.1935);
  animation: fall-164 24s -30s linear infinite;
}

@keyframes fall-164 {
  47.168% {
    transform: translate(-4.932vw, 47.168vh) scale(0.1935);
  }
  to {
    transform: translate(-1.8686vw, 100vh) scale(0.1935);
  }
}

.snow:nth-child(165) {
  opacity: 0.5544;
  transform: translate(97.7648vw, -10px) scale(0.0441);
  animation: fall-165 24s -3s linear infinite;
}

@keyframes fall-165 {
  63.05% {
    transform: translate(105.2032vw, 63.05vh) scale(0.0441);
  }
  to {
    transform: translate(101.484vw, 100vh) scale(0.0441);
  }
}

.snow:nth-child(166) {
  opacity: 0.5652;
  transform: translate(60.731vw, -10px) scale(0.1045);
  animation: fall-166 25s -18s linear infinite;
}

@keyframes fall-166 {
  72.154% {
    transform: translate(64.1561vw, 72.154vh) scale(0.1045);
  }
  to {
    transform: translate(62.44355vw, 100vh) scale(0.1045);
  }
}

.snow:nth-child(167) {
  opacity: 0.9617;
  transform: translate(61.6842vw, -10px) scale(0.4757);
  animation: fall-167 17s -18s linear infinite;
}

@keyframes fall-167 {
  30.109% {
    transform: translate(52.1829vw, 30.109vh) scale(0.4757);
  }
  to {
    transform: translate(56.93355vw, 100vh) scale(0.4757);
  }
}

.snow:nth-child(168) {
  opacity: 0.8645;
  transform: translate(94.7055vw, -10px) scale(0.4308);
  animation: fall-168 12s -9s linear infinite;
}

@keyframes fall-168 {
  53.396% {
    transform: translate(94.1203vw, 53.396vh) scale(0.4308);
  }
  to {
    transform: translate(94.4129vw, 100vh) scale(0.4308);
  }
}

.snow:nth-child(169) {
  opacity: 0.8239;
  transform: translate(38.8273vw, -10px) scale(0.9923);
  animation: fall-169 23s -18s linear infinite;
}

@keyframes fall-169 {
  53.287% {
    transform: translate(36.5902vw, 53.287vh) scale(0.9923);
  }
  to {
    transform: translate(37.70875vw, 100vh) scale(0.9923);
  }
}

.snow:nth-child(170) {
  opacity: 0.7164;
  transform: translate(15.5489vw, -10px) scale(0.4147);
  animation: fall-170 23s -9s linear infinite;
}

@keyframes fall-170 {
  53.873% {
    transform: translate(9.5961vw, 53.873vh) scale(0.4147);
  }
  to {
    transform: translate(12.5725vw, 100vh) scale(0.4147);
  }
}

.snow:nth-child(171) {
  opacity: 0.704;
  transform: translate(87.7728vw, -10px) scale(0.0812);
  animation: fall-171 10s -19s linear infinite;
}

@keyframes fall-171 {
  38.817% {
    transform: translate(86.5772vw, 38.817vh) scale(0.0812);
  }
  to {
    transform: translate(87.175vw, 100vh) scale(0.0812);
  }
}

.snow:nth-child(172) {
  opacity: 0.4393;
  transform: translate(46.364vw, -10px) scale(0.073);
  animation: fall-172 14s -24s linear infinite;
}

@keyframes fall-172 {
  47.261% {
    transform: translate(51.8124vw, 47.261vh) scale(0.073);
  }
  to {
    transform: translate(49.0882vw, 100vh) scale(0.073);
  }
}

.snow:nth-child(173) {
  opacity: 0.9892;
  transform: translate(39.8802vw, -10px) scale(0.3623);
  animation: fall-173 26s -21s linear infinite;
}

@keyframes fall-173 {
  48.096% {
    transform: translate(48.3576vw, 48.096vh) scale(0.3623);
  }
  to {
    transform: translate(44.1189vw, 100vh) scale(0.3623);
  }
}

.snow:nth-child(174) {
  opacity: 0.2822;
  transform: translate(80.9743vw, -10px) scale(0.3873);
  animation: fall-174 14s -10s linear infinite;
}

@keyframes fall-174 {
  30.449% {
    transform: translate(79.7735vw, 30.449vh) scale(0.3873);
  }
  to {
    transform: translate(80.3739vw, 100vh) scale(0.3873);
  }
}

.snow:nth-child(175) {
  opacity: 0.7723;
  transform: translate(1.9147vw, -10px) scale(0.3985);
  animation: fall-175 10s -12s linear infinite;
}

@keyframes fall-175 {
  60.654% {
    transform: translate(11.3229vw, 60.654vh) scale(0.3985);
  }
  to {
    transform: translate(6.6188vw, 100vh) scale(0.3985);
  }
}

.snow:nth-child(176) {
  opacity: 0.5566;
  transform: translate(89.8764vw, -10px) scale(0.146);
  animation: fall-176 27s -21s linear infinite;
}

@keyframes fall-176 {
  53.793% {
    transform: translate(98.5811vw, 53.793vh) scale(0.146);
  }
  to {
    transform: translate(94.22875vw, 100vh) scale(0.146);
  }
}

.snow:nth-child(177) {
  opacity: 0.8368;
  transform: translate(52.9129vw, -10px) scale(0.3415);
  animation: fall-177 22s -9s linear infinite;
}

@keyframes fall-177 {
  76.99% {
    transform: translate(52.3556vw, 76.99vh) scale(0.3415);
  }
  to {
    transform: translate(52.63425vw, 100vh) scale(0.3415);
  }
}

.snow:nth-child(178) {
  opacity: 0.2497;
  transform: translate(76.0406vw, -10px) scale(0.5371);
  animation: fall-178 11s -22s linear infinite;
}

@keyframes fall-178 {
  35.679% {
    transform: translate(75.7183vw, 35.679vh) scale(0.5371);
  }
  to {
    transform: translate(75.87945vw, 100vh) scale(0.5371);
  }
}

.snow:nth-child(179) {
  opacity: 0.6633;
  transform: translate(15.384vw, -10px) scale(0.7507);
  animation: fall-179 10s -18s linear infinite;
}

@keyframes fall-179 {
  31.964% {
    transform: translate(10.9304vw, 31.964vh) scale(0.7507);
  }
  to {
    transform: translate(13.1572vw, 100vh) scale(0.7507);
  }
}

.snow:nth-child(180) {
  opacity: 0.8701;
  transform: translate(64.6611vw, -10px) scale(0.4589);
  animation: fall-180 18s -28s linear infinite;
}

@keyframes fall-180 {
  72.294% {
    transform: translate(60.1595vw, 72.294vh) scale(0.4589);
  }
  to {
    transform: translate(62.4103vw, 100vh) scale(0.4589);
  }
}

.snow:nth-child(181) {
  opacity: 0.3228;
  transform: translate(24.7609vw, -10px) scale(0.6619);
  animation: fall-181 25s -9s linear infinite;
}

@keyframes fall-181 {
  34.716% {
    transform: translate(26.6009vw, 34.716vh) scale(0.6619);
  }
  to {
    transform: translate(25.6809vw, 100vh) scale(0.6619);
  }
}

.snow:nth-child(182) {
  opacity: 0.6258;
  transform: translate(22.6371vw, -10px) scale(0.095);
  animation: fall-182 16s -25s linear infinite;
}

@keyframes fall-182 {
  45.405% {
    transform: translate(29.6292vw, 45.405vh) scale(0.095);
  }
  to {
    transform: translate(26.13315vw, 100vh) scale(0.095);
  }
}

.snow:nth-child(183) {
  opacity: 0.7606;
  transform: translate(6.5241vw, -10px) scale(0.4102);
  animation: fall-183 19s -6s linear infinite;
}

@keyframes fall-183 {
  34.041% {
    transform: translate(2.4369vw, 34.041vh) scale(0.4102);
  }
  to {
    transform: translate(4.4805vw, 100vh) scale(0.4102);
  }
}

.snow:nth-child(184) {
  opacity: 0.6286;
  transform: translate(30.6704vw, -10px) scale(0.4584);
  animation: fall-184 27s -14s linear infinite;
}

@keyframes fall-184 {
  46.731% {
    transform: translate(24.2912vw, 46.731vh) scale(0.4584);
  }
  to {
    transform: translate(27.4808vw, 100vh) scale(0.4584);
  }
}

.snow:nth-child(185) {
  opacity: 0.9936;
  transform: translate(69.761vw, -10px) scale(0.2703);
  animation: fall-185 28s -9s linear infinite;
}

@keyframes fall-185 {
  69.145% {
    transform: translate(75.9677vw, 69.145vh) scale(0.2703);
  }
  to {
    transform: translate(72.86435vw, 100vh) scale(0.2703);
  }
}

.snow:nth-child(186) {
  opacity: 0.4337;
  transform: translate(99.5658vw, -10px) scale(0.0886);
  animation: fall-186 17s -3s linear infinite;
}

@keyframes fall-186 {
  56.838% {
    transform: translate(90.033vw, 56.838vh) scale(0.0886);
  }
  to {
    transform: translate(94.7994vw, 100vh) scale(0.0886);
  }
}

.snow:nth-child(187) {
  opacity: 0.3094;
  transform: translate(6.2547vw, -10px) scale(0.0036);
  animation: fall-187 14s -3s linear infinite;
}

@keyframes fall-187 {
  38.513% {
    transform: translate(5.8945vw, 38.513vh) scale(0.0036);
  }
  to {
    transform: translate(6.0746vw, 100vh) scale(0.0036);
  }
}

.snow:nth-child(188) {
  opacity: 0.2085;
  transform: translate(30.7611vw, -10px) scale(0.8817);
  animation: fall-188 21s -9s linear infinite;
}

@keyframes fall-188 {
  55.743% {
    transform: translate(22.3001vw, 55.743vh) scale(0.8817);
  }
  to {
    transform: translate(26.5306vw, 100vh) scale(0.8817);
  }
}

.snow:nth-child(189) {
  opacity: 0.0514;
  transform: translate(15.1538vw, -10px) scale(0.4164);
  animation: fall-189 25s -16s linear infinite;
}

@keyframes fall-189 {
  69.502% {
    transform: translate(14.2157vw, 69.502vh) scale(0.4164);
  }
  to {
    transform: translate(14.68475vw, 100vh) scale(0.4164);
  }
}

.snow:nth-child(190) {
  opacity: 0.6061;
  transform: translate(4.1665vw, -10px) scale(0.041);
  animation: fall-190 29s -28s linear infinite;
}

@keyframes fall-190 {
  63.49% {
    transform: translate(2.1207vw, 63.49vh) scale(0.041);
  }
  to {
    transform: translate(3.1436vw, 100vh) scale(0.041);
  }
}

.snow:nth-child(191) {
  opacity: 0.9133;
  transform: translate(6.7345vw, -10px) scale(0.9738);
  animation: fall-191 23s -10s linear infinite;
}

@keyframes fall-191 {
  63.607% {
    transform: translate(16.4731vw, 63.607vh) scale(0.9738);
  }
  to {
    transform: translate(11.6038vw, 100vh) scale(0.9738);
  }
}

.snow:nth-child(192) {
  opacity: 0.2883;
  transform: translate(64.067vw, -10px) scale(0.015);
  animation: fall-192 14s -30s linear infinite;
}

@keyframes fall-192 {
  32.354% {
    transform: translate(62.5984vw, 32.354vh) scale(0.015);
  }
  to {
    transform: translate(63.3327vw, 100vh) scale(0.015);
  }
}

.snow:nth-child(193) {
  opacity: 0.8738;
  transform: translate(5.5917vw, -10px) scale(0.0985);
  animation: fall-193 18s -24s linear infinite;
}

@keyframes fall-193 {
  44.87% {
    transform: translate(-1.9043vw, 44.87vh) scale(0.0985);
  }
  to {
    transform: translate(1.8437vw, 100vh) scale(0.0985);
  }
}

.snow:nth-child(194) {
  opacity: 0.4295;
  transform: translate(18.4634vw, -10px) scale(0.9168);
  animation: fall-194 12s -4s linear infinite;
}

@keyframes fall-194 {
  76.591% {
    transform: translate(23.2959vw, 76.591vh) scale(0.9168);
  }
  to {
    transform: translate(20.87965vw, 100vh) scale(0.9168);
  }
}

.snow:nth-child(195) {
  opacity: 0.6755;
  transform: translate(27.0638vw, -10px) scale(0.8905);
  animation: fall-195 29s -21s linear infinite;
}

@keyframes fall-195 {
  32.333% {
    transform: translate(17.7663vw, 32.333vh) scale(0.8905);
  }
  to {
    transform: translate(22.41505vw, 100vh) scale(0.8905);
  }
}

.snow:nth-child(196) {
  opacity: 0.2883;
  transform: translate(91.3651vw, -10px) scale(0.003);
  animation: fall-196 18s -10s linear infinite;
}

@keyframes fall-196 {
  47.456% {
    transform: translate(92.3919vw, 47.456vh) scale(0.003);
  }
  to {
    transform: translate(91.8785vw, 100vh) scale(0.003);
  }
}

.snow:nth-child(197) {
  opacity: 0.4085;
  transform: translate(73.996vw, -10px) scale(0.6547);
  animation: fall-197 12s -12s linear infinite;
}

@keyframes fall-197 {
  69.455% {
    transform: translate(78.5787vw, 69.455vh) scale(0.6547);
  }
  to {
    transform: translate(76.28735vw, 100vh) scale(0.6547);
  }
}

.snow:nth-child(198) {
  opacity: 0.8895;
  transform: translate(57.4172vw, -10px) scale(0.4981);
  animation: fall-198 26s -5s linear infinite;
}

@keyframes fall-198 {
  51.353% {
    transform: translate(61.2321vw, 51.353vh) scale(0.4981);
  }
  to {
    transform: translate(59.32465vw, 100vh) scale(0.4981);
  }
}

.snow:nth-child(199) {
  opacity: 0.3423;
  transform: translate(18.7495vw, -10px) scale(0.02);
  animation: fall-199 25s -4s linear infinite;
}

@keyframes fall-199 {
  35.801% {
    transform: translate(25.5673vw, 35.801vh) scale(0.02);
  }
  to {
    transform: translate(22.1584vw, 100vh) scale(0.02);
  }
}

.snow:nth-child(200) {
  opacity: 0.1802;
  transform: translate(18.8488vw, -10px) scale(0.9668);
  animation: fall-200 12s -30s linear infinite;
}

@keyframes fall-200 {
  57.989% {
    transform: translate(23.4096vw, 57.989vh) scale(0.9668);
  }
  to {
    transform: translate(21.1292vw, 100vh) scale(0.9668);
  }
}

.snow:nth-child(201) {
  opacity: 0.8976;
  transform: translate(75.1861vw, -10px) scale(0.1711);
  animation: fall-1 30s -21s linear infinite;
}

@keyframes fall-201 {
  30.162% {
    transform: translate(71.2496vw, 30.162vh) scale(0.1711);
  }
  to {
    transform: translate(73.21785vw, 100vh) scale(0.1711);
  }
}


</style>