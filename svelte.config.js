import adapter from '@sveltejs/adapter-auto';
import sveltePreprocess from 'svelte-preprocess';

/** @type {import('@sveltejs/kit').Config} */
const config = {
  kit: {
    adapter: adapter(),
  },

  preprocess: sveltePreprocess({
    scss: {
      additionalData: `@use 'src/styles/variables.scss' as *;`
    },
  }),
};

export default config;
