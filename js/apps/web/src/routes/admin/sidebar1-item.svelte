<script>
	import SVG from '$lib/svg.svelte';

	export let icon = '';
	export let active = false;
</script>

<button class:active>
	<div class="indicator" />
	{#if icon}
		<div class="svg">
			<SVG type={icon} />
		</div>
	{/if}
	<slot />
</button>

<style>
	button {
		display: flex;
		align-items: center;

		height: 40px;
		width: 100%;

		font-size: 16px;
		font-weight: 400;
		color: #131313;

		fill: #131313;
	}

	.indicator {
		margin-right: 37px;
		width: 3px;
		height: 100%;
		background-color: transparent;
	}
	.svg {
		margin-right: 20px;
	}

	.active {
		font-weight: 600;
		color: #007d82;

		fill: #007d82;
		stroke: #007d82;
		stroke-width: 1;
	}
	.active .indicator {
		background-color: #007d82;
	}
</style>
