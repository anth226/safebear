<script>
	import Button from '$lib/button.svelte';
	import SVG from '$lib/svg.svelte';

	export let name = '';
	export let icon = '';
</script>

<section>
	<div class="row one">
		<div class="name">{name}</div>
		<div class="svg">
			<SVG type={icon} />
		</div>
	</div>
	<div class="row two">
		<Button name="Menace" class="wide threat" />
		<Button name="Insultes" class="wide" />
		<Button name="Racisme" class="wide" />
	</div>
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		gap: 4px;

		padding-bottom: 8px;
		border-bottom: 1px solid #a7a7a7;
	}

	.row {
		display: flex;
		align-items: center;
	}
	.one {
		justify-content: space-between;
	}
	.two {
		gap: 4px;
	}
</style>
