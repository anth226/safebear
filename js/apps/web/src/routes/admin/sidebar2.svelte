<script>
	import Item from './sidebar2-item.svelte';
</script>

<section class="sidebar">
	<div class="name one">Labellisation</div>
	<div class="name two">Historique :</div>
	<div class="block">
		<Item name="Toi tu vas voir..." icon="yes"/>
		<Item name="Espèce de ..." icon="unknown"/>
		<Item name="Espèce de ..." icon="unknown"/>
		<Item name="Espèce de ..." icon="no"/>
	</div>
</section>

<style>
	.sidebar {
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		flex-shrink: 0;

		width: 273px;
		padding: 40px;
		padding-top: 0;

	}

	.name {
		font-weight: 500;
		color: #2a4a51;
	}
	.one {
		font-size: 24px;
	}
	.two {
		margin-top: 60px;
	}

	.block {
		display: flex;
		flex-direction: column;
		gap: 16px;

		margin-top: 20px;
		width: 100%;
	}
</style>
