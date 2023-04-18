import preprocess from 'svelte-preprocess';
import adapter from '@sveltejs/adapter-auto';


/** @type {import('@sveltejs/kit').Config} */
const config = {
	extensions: ['.svelte', '.html', '.svx'],
	preprocess: [
		preprocess({
			postcss: true
		})
	],

	// Docs: https://github.com/sveltejs/kit/blob/master/packages/adapter-netlify/README.md
	kit: {
		adapter: adapter({
			split: false,

			// nov 2022
			// if true, will create a Netlify Edge Function rather
			// than using standard Node-based functions. however, also uses esbuild, which as of nov 2022 has a bug on netlify
			// https://github.com/sveltejs/kit/issues/7839#issuecomment-1328605300

			// dec 2022 - moved back to true since we're using esbuild again
			edge: true,
		}),
		// https://kit.svelte.dev/docs/configuration#csp
		// csp: {
		// 	directives: {
		// 		'script-src': ['self']
		// 	},
		// 	reportOnly: {
		// 		'script-src': ['self']
		// 	}
		// }
	}
};

export default config;
