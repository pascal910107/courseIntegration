<script setup lang="ts">
import * as THREE from 'three'

let renderer: THREE.WebGLRenderer
const table = ref<HTMLCanvasElement | null>(null)


// const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000)

const width = ref(600)
const height = ref(600)
const aspectRatio = computed(() => width.value / height.value)

const scene = new THREE.Scene()
const camera = new THREE.PerspectiveCamera(75, aspectRatio.value, 0.1, 1000) //FOV、寬高比、near、far
camera.position.set(0, 0, 5)
scene.add(camera)

const geometry = new THREE.BoxGeometry(2,2,2)
const material = new THREE.MeshBasicMaterial({color: 0x382b4e})
const cube = new THREE.Mesh(geometry, material)
scene.add(cube)


// const textGeometry = new THREE.TextGeometry('scheduleData', {
//     font: 'helvetiker',
//     size: 0.2,
//     height: 0.1,
// });
// const textMaterial = new THREE.MeshBasicMaterial({ color: 0x000000 })
// const textMesh = new THREE.Mesh(textGeometry, textMaterial)
// textMesh.position.set(0, 2.5, 2.5)
// cube.add(textMesh)

function updateCamera() {
  camera.aspect = aspectRatio.value
  camera.updateProjectionMatrix()
}
function updateRenderer() {
  renderer.setSize(width.value, height.value)
  renderer.render(scene, camera)
}
function setRenderer() {
  if (table.value) {
    renderer = new THREE.WebGLRenderer({ canvas: table.value })
    updateRenderer()
  }
}
watch(aspectRatio, () => {
  updateCamera()
  updateRenderer()
})
onMounted(() => {
  setRenderer()
  animate()
})
// 很像setInterval的函式。每一幀都會執行這個函式
const animate = () => {
	// 每一幀物體都會自轉
  cube.rotation.x += 0.01;
  cube.rotation.y += 0.01;
  updateRenderer()
	// 它每一幀執行animate()
	requestAnimationFrame( animate );
	// 每一幀，場景物件都會被鏡頭捕捉
	// renderer.render( scene, camera );
}

</script>
<template>
    <div>
        <canvas ref="table" />
    </div>


</template>