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
            purple_one: "#382b4e",
            gray_one: "#282829",
            gray_two: "#333333",
            gray_three: "#3f3f3f",
            gray_four: "#a5a5a6",
            white_one: "#d2d2d4",
        },
      },
    },
    plugins: [],
};