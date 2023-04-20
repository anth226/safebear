<script>
	export let name = '';

	let clas = '';
	export { clas as class };
</script>

<button class={clas}>
	{name}
</button>

<style>
	button {
		display: flex;
		align-items: center;
		justify-content: center;

		height: 22px;
		background: linear-gradient(0deg, rgba(130, 195, 208, 0.1), rgba(130, 195, 208, 0.1)), #ffffff;
		border: 1px solid #82c3d0;
		border-radius: 5px;

		font-weight: 600;
		font-size: 10px;
		color: #82c3d0;
	}

	.wide {
		width: 100%;
	}
	.threat {
		border-color: #f7931f;
		background: linear-gradient(0deg, rgba(247, 147, 31, 0.1), rgba(247, 147, 31, 0.1)), #ffffff;

		color: #f7931f;
	}

	.primary {
		display: flex;

		border: none;
		border-radius: 8px;
		padding: 22px 29px;
		background: linear-gradient(0deg, rgba(0, 151, 156, 0.3), rgba(0, 151, 156, 0.3)), #ffffff;

		font-weight: 600;
		font-size: 24px;
		color: #00979c;
	}
</style>
