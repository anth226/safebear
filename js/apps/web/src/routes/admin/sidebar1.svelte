<script>
	import Button from './sidebar1-item.svelte';
</script>

<section class="sidebar">
	<div class="name">Safebear Admin</div>
	<div class="block">
		<Button icon="report">Utilisateurs</Button>
		<Button icon="label" active>Labellisation</Button>
		<Button icon="setting">Gestion admin</Button>
		<div class="gap">
			<Button icon="question">Aide</Button>
		</div>
	</div>
</section>

<style>
	.sidebar {
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		flex-shrink: 0;

		width: 230px;
	}
	.name {
		padding: 40px;
		height: 132px;

		font-size: 24px;
		font-weight: 500;

		color: #2a4a51;
	}
	.block {
		display: flex;
		flex-direction: column;
		gap: 16px;
		
		padding-bottom: 40px;
		height: 100%;
	}
	.gap {
		margin-top: auto;
	}
</style>
