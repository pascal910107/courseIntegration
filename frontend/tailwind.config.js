module.exports = {
    content: [
        './components/**/*.{vue,js,ts}',
        './layouts/**/*.vue',
        './pages/**/*.vue',
        './composables/**/*.{js,ts}',
        './plugins/**/*.{js,ts}',
        './app.{js,ts,vue}'
    ],
    theme: {
      extend: {
        colors: {
            black_one: "#282829",
            black_two: "#1e1e1f",
            black_three: "#1c1c1c",
            black_four: "#1d1d1d",
            black_five: "#1e1e1e",
            gray_one: "#282829",
            gray_two: "#333333",
            gray_three: "#3f3f3f",
            gray_four: "#a5a5a6",
            white_one: "#d2d2d4",
            blue_one: "#8FBCBB",
            blue_two: "#88C0D0",
            blue_three: "#81A1C1",
            blue_four: "#5E81AC",
            green_one: "#A3BE8C",
            red_one: "#BF616A",
            orange_one: "#D08770",
            yellow_one: "#EBCB8B",
            pink_one: "#B48EAD",
            purple_one: "#B48EAD",
        },
      },
    },
    plugins: [],
};