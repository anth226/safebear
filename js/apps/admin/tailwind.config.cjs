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
				silver:{
					200: '#131313',
					DEFAULT: '#F8F8F8'
				},
				blue:{
					DEFAULT: '#7CC0CE',
					vert:'#007D82',
					2: '#00979C'
				},
				'dark-green':{
					DEFAULT: '#2A4A51'
				}
			}
		}
	},
	variants: {},
	plugins: [
		require('@tailwindcss/typography')
	]
};
