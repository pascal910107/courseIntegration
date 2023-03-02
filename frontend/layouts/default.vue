<template>
    <div class="bg-black_four text-white_one h-screen w-screen overflow-hidden drop-shadow-sm">
        <div class="relative">
            <NuxtLink to="/" class="absolute w-28 h-28 top-6 left-6 z-40 rounded-lg flex justify-center items-center text-xl font-semibold select-none hover:scale-110 hover:-skew-y-2 hover:translate-y-3 hover:translate-x-3 transition-transform duration-300" style="background:rgba(71 ,85 ,105, 0.9);">首頁</NuxtLink>
            <div class="absolute w-24 h-24 top-4 left-4 z-30 rounded-md" style="background:rgba(51 ,65 ,85, 0.8);"></div>
            <div class="absolute w-20 h-20 top-2 left-2 z-20 rounded" style="background:rgba(30 ,41 ,59, 0.8);"></div>
            <div class="absolute w-16 h-16 top-0 left-0 z-10 " style="background:rgba(15 ,23 ,42, 0.7);"></div>
        </div>
        <slot />
    </div>
</template>
