module.exports = {
  purge: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    fontSize: {
      "header-base": "1.5rem",
      "header-sm": "2.0rem",
      "header-lg": "2.5rem",
      xs: ".75rem",
      sm: ".875rem",
      base: "1rem",
      lg: "1.125rem",
      xl: "1.25rem",
      "2xl": "1.5rem",
      "navbar-base":"2.2rem",
      "md-menuname":"60px",
      "md-price":"50px",
      "menu-name":"5rem",
      "calorie":"45px",
    },
    extend: {
      colors: {
        "regal-blue": "#04043B",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [
    {
      tailwindcss: {},
      autoprefixer: {},
    },
  ],
}
