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
					DEFAULT: '#F8F8F8',
					300: '#ADA7A7'
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
				},
				inactive:{
					DEFAULT: 'rgba(217, 217, 217, 0.52);'
				},
				hidden:{
					DEFAULT: 'rgba(255, 255, 255, 0.52)'
				}
			},
			fontFamily:{
				'lato': ['Lato', 'sans-serif'],
			},
			boxShadow:{
				label:"0px 56px 37px -32px rgba(42, 74, 81, 0.18)",
				out: "0px 2px 4px rgba(167, 167, 167, 0.46)"
			},
		}
	},
	variants: {},
	plugins: [
		require('@tailwindcss/typography')
	]
};
