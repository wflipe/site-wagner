/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./app.js"],
  theme: {
    extend: {
      colors: { 
        primary: "#00E5FF", 
        secondary: "#1DE9B6", 
        surface: "#050C0C", 
        surfaceAlt: "#0A1414",
        accent: "#006064", 
        border: "rgba(255, 255, 255, 0.1)", 
        textMain: "#FFFFFF", 
        textMuted: "#A1A1AA"
      },
      fontFamily: { 
        headline: ["'Space Grotesk'"], 
        body: ["'Manrope'"], 
        mono: ["'JetBrains Mono'"] 
      }
    }
  },
  plugins: [],
}
