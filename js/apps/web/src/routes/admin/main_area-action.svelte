<script>
	import SVG from '$lib/svg.svelte';

	export let type = 'yes';
	let name = 'Oui';
	let shortcut = 'A';
	let color = '#007d82';

	if (type == 'no') {
		name = 'Non';
		shortcut = 'X';
		color = '#D96161';
	} else if (type == 'unknown') {
		name = 'Je ne sais pas';
		shortcut = 'Space';
		color = '#A7A7A7';
	}
</script>

<div class="action">
	<div class="name">{name}</div>
	<button class="svg" style:fill={color}>
		<SVG type="{type}_" size={130} />
	</button>
	<div class="shortcut">{shortcut}</div>
</div>

<style>
	.action {
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.name {
		font-size: 16px;
		color: #666262;
	}
	.svg {
		margin-top: 18px;
		box-shadow: 0px 56px 37px -32px rgba(42, 74, 81, 0.18);
		backdrop-filter: blur(10px);
	}

	.shortcut {
		display: flex;
		align-items: center;
		justify-content: center;

		margin-top: 8px;
		border-radius: 10px;
		padding: 6px 20px;
		background-color: rgba(167, 167, 167, 0.5);
		box-shadow: 0px 56px 37px -32px rgba(42, 74, 81, 0.18);
		backdrop-filter: blur(10px);

		color: #2a4a51;
		font-weight: 600;
		font-size: 24px;
	}
</style>
