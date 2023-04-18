/** @type {import('tailwindcss').Config} */
module.exports = {
	content: [
		'./src/**/*.svelte',
		// may also want to include HTML files
		'./src/**/*.html'
	],
	darkMode: 'class',
	theme: {
		extend: {
			colors: {
				'silver':{
					DEFAULT: '#F8F8F8'
				}
			}
		}
	},
	variants: {},
	plugins: [
		require('@tailwindcss/typography')
	]
};
