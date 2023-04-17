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
					hr: "#A7A7A7",
					DEFAULT: '#F8F8F8'
				},
				blue:{
					DEFAULT: '#7CC0CE',
					vert:'#007D82',
					2: '#00979C',
					less: "#82C3D0",
					gradient: ""
				},
				'dark-green':{
					DEFAULT: '#2A4A51'
				},
				orange:{
					DEFAULT: '#F7931F'
				},
				primary:{
					DEFAULT: 'rgba(247, 147, 31, 0.1)'
				}
			},
			boxShadow:{
				label:"0px 56px 37px -32px rgba(42, 74, 81, 0.18)",
			}
		}
	},
	variants: {},
	plugins: [
		require('@tailwindcss/typography')
	]
};
