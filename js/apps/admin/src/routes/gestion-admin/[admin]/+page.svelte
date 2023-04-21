<script>
	import { goto } from '$app/navigation';
	import toast from 'svelte-french-toast';
	import Input from '../../../components/Input.svelte';
	import { data as users } from '../data';

	let info = {
		fname: 'John',
		lname: 'Doe',
		email: 'janedoe@gmail.com'
	};
	export let data;

	const user = users.find((user) => user.id == data.adminId);

	function deleteData() {
		goto("/gestion-admin")
		toast.success('Supprimé avec succès');
	}

	function deactivateData() {
		goto("/gestion-admin")
		toast.success('Complété avec succès');
	}
</script>

<div class="flex flex-col gap-20">
	<div class="flex gap-3">
		<h1 class="text-2xl font-medium opacity-50">Utilisateurs</h1>
		<span class="pt-0.5 text-2xl font-medium opacity-50">></span>
		<h1 class="text-2xl font-medium">{user?.name || info.fname + '' + info.lname}</h1>
	</div>
	<div class="flex flex-col gap-14 rounded-[3px] bg-white px-8 py-8">
		<div class="flex gap-6">
			<h4 class="text-3xl">{user?.name || info.fname + '' + info.lname}</h4>
			<div class="flex gap-4 self-center">
				<button class="rounded bg-blue px-3 text-lg text-dark-green">Admin</button>
			</div>
		</div>
		<div class="flex flex-col gap-4 pr-10">
			<h3 class="text-2xl font-normal">Informations personnelles :</h3>
			<div class="flex flex-col justify-between gap-10 md:flex-row">
				<Input label={'Nom'} bind:value={info.fname} />
				<Input label={'Prénom'} bind:value={info.lname} />
				<Input label={'Mail'} bind:value={info.email} />
			</div>
		</div>

		<div class="flex flex-col gap-6">
			<h1 class="text-2xl">Informations Safebear :</h1>

			<div class="flex w-2/3 flex-col gap-5">
				<div class="flex justify-between gap-6">
					<div class="flex w-full gap-3 border-b border-blue-2 pb-4">
						<span class="font-semibold">Création du compte :</span>
						<span>23/09/2022</span>
					</div>
                    <div class="flex w-full gap-3 border-b border-blue-2 pb-4">
						<span class="font-semibold">ID :</span>
						<span>5367490900</span>
					</div>
				</div>

				<div class="flex justify-between gap-6 box-border">
					<div class="flex w-full gap-3 border-b border-blue-2 pb-4">
						<span class="font-semibold">Dernière connexion :</span>
						<span>10/03/2023</span>
					</div>
                    <div class="flex w-full gap-3 pb-4">
					</div>
				</div>
			</div>
		</div>
		<div class="flex justify-between">
			<div class="flex gap-4 self-center">
				<!-- svelte-ignore a11y-click-events-have-key-events -->
				<div class="flex cursor-pointer gap-2" on:click={deleteData}>
					<img src="/util/delete.svg" alt="" />
					<span class="font-medium text-blue-vert underline">Supprimer le compte</span>
				</div>
				<!-- svelte-ignore a11y-click-events-have-key-events -->
				<div class="flex cursor-pointer gap-2" on:click={deactivateData}>
					<img src="/util/deactivate.svg" alt="" />
					<span class="font-medium text-blue-vert underline">Désactiver le compte</span>
				</div>
			</div>
			<div>
				<button class="text-white px-8 py-3 rounded-[100px] bg-blue-vert font-lato">Valider les modifications </button>
			</div>
		</div>

	</div>
</div>
