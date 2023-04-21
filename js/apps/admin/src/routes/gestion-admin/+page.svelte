<script lang="ts">
	import { search as searchData } from '../../store/search';
	import { goto } from '$app/navigation';
	import toast from 'svelte-french-toast';
	import type { IAdmin } from '$lib/types';
	import { data } from './data';
	import { onMount } from 'svelte';

	const pageSize = 7,
		linkCount = 3;
	let users = data,
		search = '';
	let pageData: IAdmin[] = [];
	let links: number[] = [],
		linksCounter: number[][] = [];
	let currentPage = 1,
		currentLinkPage = 1;
	let selected: number[] = [];

	$: users = data.filter(
		(user) =>
			user.name.toLowerCase().includes(search.toLowerCase()) ||
			user.email.toLowerCase().includes(search.toLowerCase()) ||
			user.role.toLowerCase().includes(search.toLowerCase())
	);
	function changePage(pageNumber: number) {
		currentPage = pageNumber;
		selected = [];
		displayPage(pageNumber);
	}
	function changeLinkPage(number: number) {
		currentLinkPage = number;
		changePage(linksCounter[number - 1][0]);
	}
	function selectAll() {
		if (selected.length == pageData.length) {
			selected = [];
			return;
		}
		selected = pageData.map((user) => user.id);
	}
	function addToSelected(id: number) {
		if (selected.includes(id)) {
			selected = selected.filter((item) => item != id);
		} else {
			selected = [...selected, id];
		}
	}

	function deleteData() {
		users = users.filter((user) => !selected.includes(user.id));
		selected = [];
		toast.success('Supprimé avec succès');
	}

	function editAccount(id: number) {
		goto(`/gestion-admin/${id}`)
	}
    function createAccount() {
		goto(`/gestion-admin/new`)
	}

	function displayPage(pageNumber: number) {
		const startIndex = (pageNumber - 1) * pageSize;
		const endIndex = startIndex + pageSize;
		pageData = users.slice(startIndex, endIndex);
	}
	function generatePaginationLinks() {
		links = [];
		const totalPages = Math.ceil(users.length / pageSize);
		for (let i = 1; i <= totalPages; i++) {
			links = [...links, i];
		}
		linksCounter = [];
		const totalLinks = Math.ceil(links.length / linkCount);
		let numbers = 1;
		let array: number[] = [];
		for (let i = 1; i <= totalLinks; i++) {
			array = [];
			let stop = numbers + linkCount;
			for (let j = numbers; j < stop && j <= links.length; j++) {
				array = [...array, numbers];
				numbers++;
			}
			linksCounter = [...linksCounter, array];
		}
	}
	$: {
		if (users) {
			displayPage(currentPage);
			generatePaginationLinks();
		}
	}
	displayPage(1);
	generatePaginationLinks();

	onMount(() => {
		searchData.subscribe((value) => {
			search = value;
			currentLinkPage = 1;
			currentPage = 1;
		});
	});
</script>

<svelte:head>
	<title>Gestion des admins - Safebear</title>
</svelte:head>
<div class="flex justify-between">
	<h1 class="text-2xl">Gestion des admins</h1>
	
</div>

<!-- svelte-ignore a11y-click-events-have-key-events -->
	<div class="flex w-full gap-5 rounded-[3px] px-6 py-4">
		<div class="flex cursor-pointer gap-2" on:click={createAccount}>
			<img src="/util/deactivate.svg" alt="" />
			<span class="font-medium text-blue-vert underline">Ajouter un utilisateur</span>
		</div>
        {#if selected.length > 0 && pageData.length != 0}
        <div class="flex cursor-pointer gap-2" on:click={deleteData}>
			<img src="/util/delete.svg" alt="" />
			<span class="font-medium text-blue-vert underline">Supprimer le compte</span>
		</div>
        {/if}
	</div>
<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="rounded-[3px] bg-white px-0.5 -mt-4">
	<div class="flex border-b border-[#F2F2F2] px-0.5 py-5">
		<div class="flex w-full gap-3 px-4">
			<div
				class="flex h-5 w-5 cursor-pointer items-center justify-center rounded-[7px] border"
				class:bg-blue-vert={selected.length == pageData.length && pageData.length != 0}
				class:border-blue-vert={selected.length == pageData.length && pageData.length != 0}
				class:border-silver-300={selected.length != pageData.length || pageData.length == 0}
				on:click={selectAll}
			>
				{#if selected.length == pageData.length}
					<img src="/util/tick.svg" alt="" />
				{/if}
			</div>
			<h4 class="self-center font-lato font-semibold">Nom</h4>
		</div>
		<div class="relative flex w-full gap-3 px-4">
			<h4 class="self-center font-lato font-semibold">Email</h4>
		</div>
		<div class="flex w-full gap-3 px-4">
			<h4 class="self-center font-lato font-semibold">Role</h4>
		</div>
		<div class="flex w-full gap-3 px-4">
		</div>
		<div class="flex w-full gap-3 px-4">
		</div>
	</div>
	{#each pageData as user}
		<div
			class="flex border-b border-[#F2F2F2] px-0.5 py-5"
		>
			<div class="flex w-full gap-3 px-4 self-center">
				<div
					class="flex h-5 w-5 cursor-pointer items-center justify-center rounded-[7px] border"
					class:bg-blue-vert={selected.includes(user.id)}
					class:border-blue-vert={selected.includes(user.id)}
					class:border-silver-300={!selected.includes(user.id)}
					on:click={() => {
						addToSelected(user.id);
					}}
				>
					{#if selected.includes(user.id)}
						<img src="util/tick.svg" alt="" />
					{/if}
				</div>
				<h4
					on:click={() => {
						goto(`/gestion-admin/${user.id}`);
					}}
					class="cursor-pointer self-center font-medium text-blue-vert underline"
				>
					{user.name}
				</h4>
			</div>
			<div class="flex w-full gap-3 px-4 self-center">
				<h4 class="self-center text-black opacity-[65%]">{user.email}</h4>
			</div>
			<div class="flex w-full gap-3 px-4 self-center">
				<h4 class="self-center text-black opacity-[65%]">{user.role}</h4>
			</div>
            
			<div class="flex w-full gap-3 px-4 self-start">
                {#if pageData.indexOf(user) == 0}
				<h4 class="text-blue-vert underline" on:click={()=>editAccount(user.id)}>{"Réinitialiser le mot de passe"}</h4>
                {/if}
			</div>
			<div class="flex w-full gap-3 px-4 self-start">
                {#if pageData.indexOf(user) == 0}
				<h4 class="text-blue-vert underline" on:click={()=>editAccount(user.id)}>
					{`Modifier le compte`}
				</h4>
                {/if}
			</div>
		</div>
	{/each}
</div>
{#if linksCounter.length >= 1}
	<div class="flex w-full justify-center gap-2">
		{#if currentLinkPage != 1}
			<button
				class="cursor-pointer px-1 py-0.5"
				on:click={() => {
					changeLinkPage(currentLinkPage - 1);
				}}
			>
				<img class="mt-0.5 -rotate-90 self-start" src="/util/arrow.svg" alt="" />
			</button>
			<button
				class="cursor-pointer px-1 py-0.5"
				on:click={() => {
					changeLinkPage(currentLinkPage - 1);
				}}>...</button
			>
		{/if}
		{#each linksCounter[currentLinkPage - 1] as link}
			<button
				class:text-blue-2={link == currentPage}
				class:underline={link == currentPage}
				class:font-semibold={link == currentPage}
				class="cursor-pointer px-1 py-0.5"
				on:click={() => {
					changePage(link);
				}}>{link}</button
			>
		{/each}
		{#if currentLinkPage < linksCounter.length}
			<button
				class="cursor-pointer px-1 py-0.5"
				on:click={() => {
					changeLinkPage(currentLinkPage + 1);
				}}>...</button
			>
			<button
				class="cursor-pointer px-1 py-0.5"
				on:click={() => {
					changeLinkPage(currentLinkPage + 1);
				}}
			>
				<img class="mt-0.5 rotate-90 self-start" src="/util/arrow.svg" alt="" />
			</button>
		{/if}
	</div>
{/if}
{#if users.length == 0}
	<div class="flex w-full justify-center bg-silver">
		<h4 class="self-center text-black opacity-[45%]">Aucune donnée disponible...</h4>
	</div>
{/if}
