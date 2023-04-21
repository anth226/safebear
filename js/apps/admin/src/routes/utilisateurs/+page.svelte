<script lang="ts">
	import { search as searchData } from '../../store/search';
	import { goto } from '$app/navigation';
	import toast from 'svelte-french-toast';
	import type { IUser } from '$lib/types';
	import ClickOutside from 'svelte-click-outside';
	import { data } from './data';
	import { onMount } from 'svelte';

	const pageSize = 7,
		linkCount = 3;
	let users = data,
		search = '';
	let pageData: IUser[] = [];
	let links: number[] = [],
		linksCounter: number[][] = [];
	let currentPage = 1,
		currentLinkPage = 1;
	let selected: number[] = [];
	let isFilterOpen = false,
		isFolmuraFilterOpen = false,
		isStatusFilterOpen = false,
		isDateFilterOpen = false;

	$: users = data.filter(
		(user) =>
			user.name.toLowerCase().includes(search.toLowerCase()) ||
			user.date.includes(search) ||
			user.kyc.toLowerCase().includes(search.toLowerCase())
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

	function deactivateData() {
		users = users.map((user) => {
			if (selected.includes(user.id)) {
				return {
					...user,
					status: 'Désactivé'
				};
			}
			return user;
		});
		selected = [];
		toast.success('Complété avec succès');
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
	<title>Utilisateurs - Safebear</title>
</svelte:head>
<div class="flex justify-between">
	<h1 class="text-2xl">Utilisateurs</h1>
	<div class="flex gap-4">
		<!-- svelte-ignore a11y-click-events-have-key-events -->
		<div
			class="flex cursor-pointer gap-3 self-center rounded-lg bg-white px-3 py-2"
			class:opacity-40={isFilterOpen}
			on:click={() => (isFilterOpen = !isFilterOpen)}
		>
			<img class="cursor-pointer" src="util/filter.svg" alt="" />
			<span class="self-center text-sm font-medium">Filter</span>
		</div>
		{#if isFilterOpen}
			<ClickOutside on:clickoutside={() => (isFolmuraFilterOpen = false)}>
				<div
					class="relative flex w-[135px] flex-col gap-2 self-center bg-white px-3 py-2"
					class:pb-2={isFolmuraFilterOpen}
					class:rounded-tl-lg={isFolmuraFilterOpen}
					class:rounded-tr-lg={isFolmuraFilterOpen}
					class:rounded-lg={!isFolmuraFilterOpen}
					class:shadow-label={isFolmuraFilterOpen}
				>
					<!-- svelte-ignore a11y-click-events-have-key-events -->
					<div
						class="flex cursor-pointer gap-3"
						on:click={() => (isFolmuraFilterOpen = !isFolmuraFilterOpen)}
					>
						<span class="self-center text-sm font-medium">Par formule</span>
						<img
							class="w-[12px] self-center"
							class:rotate-180={!isFolmuraFilterOpen}
							class:mb-1={!isFolmuraFilterOpen}
							class:mt-1={isFolmuraFilterOpen}
							src="/util/arrow.svg"
							alt=""
						/>
					</div>
					{#if isFolmuraFilterOpen}
						<div
							class="absolute left-0 top-8 flex w-[135px] flex-col gap-1 rounded-bl-lg rounded-br-lg bg-white px-3 pb-2"
							class:shadow-label={isFolmuraFilterOpen}
						>
							<div class="flex cursor-pointer gap-2">
								<div class="h-[10px] w-[10px] self-center rounded-full border border-dark-green" />
								<span class="self-center text-xs font-medium">Safe</span>
							</div>
							<div class="flex cursor-pointer gap-2">
								<div class="h-[10px] w-[10px] self-center rounded-full border border-dark-green" />
								<span class="self-center text-xs font-medium">Safe Family</span>
							</div>
							<div class="flex cursor-pointer gap-2">
								<div class="h-[10px] w-[10px] self-center rounded-full border border-dark-green" />
								<span class="self-center text-xs font-medium">Basic</span>
							</div>
							<div class="flex cursor-pointer gap-2">
								<div class="h-[10px] w-[10px] self-center rounded-full border border-dark-green" />
								<span class="self-center text-xs font-medium">Basic Family</span>
							</div>
						</div>
					{/if}
				</div>
			</ClickOutside>
			<ClickOutside on:clickoutside={() => (isStatusFilterOpen = false)}>
				<div
					class="relative flex w-[135px] flex-col gap-2 self-center bg-white px-3 py-2"
					class:pb-2={isStatusFilterOpen}
					class:rounded-tl-lg={isStatusFilterOpen}
					class:rounded-tr-lg={isStatusFilterOpen}
					class:rounded-lg={!isStatusFilterOpen}
					class:shadow-label={isStatusFilterOpen}
				>
					<!-- svelte-ignore a11y-click-events-have-key-events -->
					<div
						class="flex cursor-pointer gap-3"
						on:click={() => (isStatusFilterOpen = !isStatusFilterOpen)}
					>
						<span class="self-center text-sm font-medium">Par statut</span>
						<img
							class="w-[12px] self-center"
							class:rotate-180={!isStatusFilterOpen}
							class:mb-1={!isStatusFilterOpen}
							class:mt-1={isStatusFilterOpen}
							src="/util/arrow.svg"
							alt=""
						/>
					</div>
					{#if isStatusFilterOpen}
						<div
							class="absolute left-0 top-8 flex w-[135px] flex-col gap-1 rounded-bl-lg rounded-br-lg bg-white px-3 pb-2"
							class:shadow-label={isStatusFilterOpen}
						>
							<div class="flex cursor-pointer gap-2">
								<div class="h-[10px] w-[10px] self-center rounded-full border border-dark-green" />
								<span class="self-center text-xs font-medium">Client -18 ans</span>
							</div>
							<div class="flex cursor-pointer gap-2">
								<div class="h-[10px] w-[10px] self-center rounded-full border border-dark-green" />
								<span class="self-center text-xs font-medium">Client +18 ans</span>
							</div>
							<div class="flex cursor-pointer gap-2">
								<div class="h-[10px] w-[10px] self-start rounded-full border border-dark-green" />
								<span class="self-center text-xs font-medium">Compte désactivé</span>
							</div>
						</div>
					{/if}
				</div>
			</ClickOutside>
		{/if}
	</div>
</div>
{#if selected.length > 0 && pageData.length != 0}
	<div class="flex w-full gap-5 rounded-[3px] bg-blue-vert bg-opacity-20 px-6 py-4">
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
{/if}
<div class="rounded-[3px] bg-white px-0.5" class:-mt-4={selected.length > 0}>
	<div class="flex border-b border-[#F2F2F2] px-0.5 py-5">
		<div class="flex w-full gap-3 px-4">
			<!-- svelte-ignore a11y-click-events-have-key-events -->
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
			<h4 class="self-center font-lato font-semibold">Utilisateur</h4>
		</div>
		<div class="relative flex w-full gap-3 px-4">
			<h4 class="self-center font-lato font-semibold">Date</h4>
			<div class="cursor-pointer rounded-[4px] px-1 py-1 shadow-out">
				<img src="/util/double-direction.svg" alt="" />
			</div>
		</div>
		<div class="flex w-full gap-3 px-4">
			<h4 class="self-center font-lato font-semibold">Statut</h4>
		</div>
		<div class="flex w-full gap-3 px-4">
			<h4 class="self-center font-lato font-semibold">Formule souscrite</h4>
		</div>
		<div class="flex w-full gap-3 px-4">
			<h4 class="self-center pl-10 font-lato font-semibold">KYC</h4>
		</div>
		<div class="flex w-full gap-3 px-4">
			<h4 class="self-center font-lato font-semibold">Compte lié</h4>
		</div>
	</div>
	{#each pageData as user}
		<div
			class="flex border-b border-[#F2F2F2] px-0.5 py-5"
			class:bg-inactive={user.status == 'Désactivé'}
			class:opacity-60={user.status == 'Désactivé'}
		>
			<div class="flex w-full gap-3 px-4">
				<!-- svelte-ignore a11y-click-events-have-key-events -->
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
				<!-- svelte-ignore a11y-click-events-have-key-events -->
				<h4
					on:click={() => {
						goto(`/utilisateurs/${user.id}`);
					}}
					class="cursor-pointer self-center font-medium text-blue-vert underline"
				>
					{user.name}
				</h4>
			</div>
			<div class="flex w-full gap-3 px-4">
				<h4 class="self-center text-black opacity-[65%]">{user.date}</h4>
			</div>
			<div class="flex w-full gap-3 px-4">
				<h4 class="self-center text-black opacity-[65%]">{user.status}</h4>
			</div>
			<div class="flex w-full gap-3 px-4">
				<h4 class="self-center text-black opacity-[65%]">{user.formula}</h4>
			</div>
			<div class="flex w-full gap-3 px-4">
				<div
					class="flex gap-2 rounded-[31px] px-1 py-0.5 pr-2"
					class:bg-[#33B35E]={user.kyc == 'Complété'}
					class:bg-[#F49817]={user.kyc == 'En attente'}
				>
					<img class:hidden={user.kyc != 'Complété'} src="/util/kyc-tick.svg" alt="" />
					<img class:hidden={user.kyc != 'En attente'} src="/util/kyc-dashed-circle.svg" alt="" />
					<h4 class="self-center text-white">{user.kyc}</h4>
				</div>
			</div>
			<div class="flex w-full gap-3 px-4">
				<h4 class="self-center">
					{`${user.linked_accounts} compte lié${user.linked_accounts > 1 ? 's' : ''}`}
				</h4>
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
