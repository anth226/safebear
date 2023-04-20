<script>
	import Button from '$lib/button.svelte';
	import Action from './main_area-action.svelte';
</script>

<section>
	<div class="block">
		<div class="row_one">
			Contenu labellisé comme : <Button name="Insultes" class="primary" />
		</div>
		<div class="message">
			<div class="message_label">Message :</div>
			<div>
				Dis donc sale **** tu réponds plus à mes messages ? T’as fait comme ton père c’est ça tu
				t’es barré ! Espèce de singe
			</div>
		</div>
		<div class="action_area">
			<Action type="yes" />
			<Action type="no" />
			<Action type="unknown" />
		</div>
	</div>
</section>

<style>
	section {
		display: flex;
		/* align-items: center; */
		justify-content: center;

		width: 100%;
	}

	.block {
		display: flex;
		flex-direction: column;
		max-width: 674px;
	}
	.row_one {
		display: flex;
		align-items: center;
		gap: 14px;

		border-radius: 14px;
		width: 100%;
		padding: 20px;
		background-color: rgba(167, 167, 167, 0.1);
		box-shadow: 0px 56px 37px -32px rgba(42, 74, 81, 0.18);
		backdrop-filter: blur(10px);

		font-weight: 500;
		font-size: 20px;
	}
	.message {
		margin-top: 18px;
		border: 2px solid #a7a7a7;
		border-radius: 23px;
		padding: 20px;
		width: 100%;
		max-width: 674px;
		height: 200px;
		background-color: #ffffff;
		box-shadow: 0px 56px 37px -32px rgba(42, 74, 81, 0.18);
		backdrop-filter: blur(10px);

		font-size: 18px;
	}
	.message_label {
		color: #a7a7a7;
		font-size: 16px;
	}
	.action_area {
		display: flex;
		justify-content: center;
		gap: 20px;

		margin-top: 50px;
	}
</style>
