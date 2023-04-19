<script>
	import '../../tailwind.css';
	import Labellisation_SVG from '../Svg/Labellisation_SVG.svelte';
	import Utilisateurs_SVG from '../Svg/Utilisateurs_SVG.svelte';
	import GestionAdmin_SVG from '../Svg/GestionAdmin_SVG.svelte';

	const items = [
		{
			label: 'Utilisateurs',
			icon: 'Labellisation_SVG',
			route: '/Utilisateurs'
		},
		{
			label: 'Labellisation',
			icon: 'Utilisateurs_SVG',
			route: '/Labellisation'
		},
		{
			label: 'Gestion admin',
			icon: 'GestionAdmin_SVG',
			route: '/GestionAdmin'
		}
	];
</script>

<main class=" left-0 top-0 flex h-[1149px] w-[240px] justify-center bg-white">
	<span
		class="font-poppins absolute top-14 left-10 h-16 w-44 text-2xl font-medium leading-9 text-[#2A4A51]"
	>
		Safebear<br /> Admin
	</span>

	<div class="absolute top-40 left-10  flex flex-col">
		{#each items as item, index}
			<div
				class=" Svg-Container group flex items-start hover:cursor-pointer hover:font-semibold hover:text-[#007D82]"
			>
				{#if item.icon === 'Labellisation_SVG'}
					<Labellisation_SVG classes="mr-[20px] group-hover:stroke-white" />
				{:else if item.icon === 'Utilisateurs_SVG'}
					<Utilisateurs_SVG classes="mr-[20px]" />
				{:else if item.icon === 'GestionAdmin_SVG'}
					<GestionAdmin_SVG classes="mr-[20px]" />
				{/if}

				<!-- svelte-ignore a11y-click-events-have-key-events -->
				<a href={item.route} class="mb-[41px] text-base leading-6 tracking-wide ">{item.label}</a>
			</div>
		{/each}
	</div>
</main>

<style>
	main {
		font-family: 'Poppins';
	}
	/* .Svg-Container :global(svg) {
		margin-right: 20px;
	}
	.Svg-Container :global(svg) {
		margin-right: 20px;
	} */
</style>
