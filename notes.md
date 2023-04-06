### python會有多個編譯環境
ENV PATH="$VIRTUAL_ENV/Scripts:$PATH"

### nuxt3 in docker的HMR問題，無限重新加載頁面
ports:
    - 24678:24678
vite: {
    server: {
        hmr: {
            protocol: 'ws'
        }
    }
}

### use HMR in docker
environment: 
    - CHOKIDAR_USEPOLLING=true

### 使用volumes時，雖然Dockerfile有npm install，但本地沒有node_modules，綁定掛載會使得container找不到node_modules而無法正常啟動伺服器
路徑發生衝突時，docker會以長的路徑為優先
volumes:
    - /app/frontend/node_modules

### nuxt/tailwindcss
modules: ['@nuxtjs/tailwindcss']

### nuxt路由無法訪問，權限問題，還有重新編譯
ENV HOST 0.0.0.0
environment:
    - HOST=0.0.0.0

### flask無法訪問，權限問題
app.run(host='0.0.0.0')

### pymongo in docker連線要使用container_name代替地址
client = MongoClient("mongodb://courseintegration-mongodb-1:27017/")

### server端渲染跟client端渲染
baseUrl: process.server ? 'http://courseintegration-backend-1:5000/api/' : 'http://localhost:5000/api/'

### useFetch not compatible with node18
instead node18 with node16

###  NuxtLink連接的頁面無法顯示
每個template只能有一個根，nuxt會把根等級的註釋也算做根

### pymongo 4.0後的刪除了Cursor object的count method
len(list(cursor))

### flask路由只能返回字串，其他型別都不行
str()

### package.json修改後沒有成功引入，container要刪掉不能留快取
docker-compose down

### Nitro不會自己關掉
docker-compose down

### CORS跨域問題可能是因為忘記加/api/
http://127.0.0.1:5000/api/

### 網頁控制台顯示有問題，不一定是跨域問題，後端沒處理好他一樣顯示跨域問題
看terminal日誌