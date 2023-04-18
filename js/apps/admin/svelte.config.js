import preprocess from 'svelte-preprocess';
import adapter from '@sveltejs/adapter-vercel';


/** @type {import('@sveltejs/kit').Config} */
const config = {
	extensions: ['.svelte', '.html', '.svx'],
	preprocess: [
		preprocess({
			postcss: true
		})
	],
	kit: {
		adapter: adapter({
			
		}),
	}
};

export default config;
