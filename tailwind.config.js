/** @type {import('tailwindcss').Config} */
const plugin = require('tailwindcss/plugin')
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      boxShadow: {
        'custom': '0 10px 15px 5px rgba(0, 0, 0, 0.6)',
      },
      fontFamily: {
        'sunrise': ['Waiting for the Sunrise', 'cursive'],
      }
    }
  },
  plugins: [
    
    
  ]
}