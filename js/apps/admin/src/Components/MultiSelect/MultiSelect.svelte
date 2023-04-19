<script lang="ts">
	import { SvelteComponent, onMount } from 'svelte';
	import '../../tailwind.css';
	import { fly } from 'svelte/transition';
	import Icon from 'svelte-icons-pack/Icon.svelte';
	import FiXCircle from 'svelte-icons-pack/fi/FiXCircle';
	export let id = '';
	export let value: Array<Tobj> = [];
	export let label: string;
	export let readonly = false;
	export let placeholder = '';
	type Tobj = {
		value: any;
		name: any;
	};
	let input: HTMLInputElement,
		inputValue: string,
		options: Array<Tobj> = [],
		activeOption: Tobj | undefined,
		showOptions: Boolean = false,
		selected: any = {},
		first = true,
		slot: any;
	const iconClearPath =
		'M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z';

	onMount(() => {
		slot.querySelectorAll('option').forEach((o: any) => {
			o.selected && !value.includes(o.value) && (value = [...value, o.value]);
			options = [...options, { value: o.value, name: o.textContent }];
		});
		value &&
			(selected = options.reduce(
				(obj: any, op: any) => (value.includes(op.value) ? { ...obj, [op.value]: op } : obj),
				{}
			));
		first = false;
	});

	$: if (!first) value = Object.values(selected).map((o: any) => o.value);
	$: filtered = options.filter((o: Tobj) =>
		inputValue ? o.name.toLowerCase().includes(inputValue.toLowerCase()) : o
	);
	$: if ((activeOption && !filtered.includes(activeOption)) || (!activeOption && inputValue))
		activeOption = filtered[0];

	function add(token: Tobj) {
		if (!readonly) selected[token.value] = token;
	}

	function remove(value: string) {
		if (!readonly) {
			const { [value]: val, ...rest } = selected;
			selected = rest;
		}
	}

	function optionsVisibility(show: Boolean) {
		if (readonly) return;
		if (typeof show === 'boolean') {
			showOptions = show;
			show && input.focus();
		} else {
			showOptions = !showOptions;
		}
		if (!showOptions) {
			activeOption = undefined;
		}
	}

	function handleKeyup(e: any) {
		if (e.keyCode === 13) {
			if (activeOption)
				Object.keys(selected).includes(activeOption.value)
					? remove(activeOption.value)
					: add(activeOption);
			inputValue = '';
		}
		if ([38, 40].includes(e.keyCode)) {
			// up and down arrows
			const increment = e.keyCode === 38 ? -1 : 1;
			if (activeOption) {
				const calcIndex = filtered.indexOf(activeOption) + increment;
				activeOption =
					calcIndex < 0
						? filtered[filtered.length - 1]
						: calcIndex === filtered.length
						? filtered[0]
						: filtered[calcIndex];
			}
		}
	}

	function handleBlur(e: any) {
		optionsVisibility(false);
	}

	function handleTokenClick(e: any) {
		if (e.target.closest('.token-remove')) {
			e.stopPropagation();
			remove(e.target.closest('.token').dataset.id);
		} else if (e.target.closest('.remove-all')) {
			selected = [];
			inputValue = '';
		} else {
			optionsVisibility(true);
		}
	}

	function handleOptionMousedown(e: any) {
		const value = e.target.dataset.value;
		if (selected[value]) {
			remove(value);
		} else {
			add(options.filter((o: any) => o.value === value)[0]);
			input.focus();
		}
	}
</script>

<span class="text-lg text-[#2A4A51]">{label}</span>
<div class="multiselect" class:readonly>
	<!-- svelte-ignore a11y-click-events-have-key-events -->
	<div class="tokens" class:showOptions on:click={handleTokenClick}>
		{#each Object.values(selected) as obj}
			<div class={obj.name === 'Menace' ? 'token2' : 'token'} data-id={obj.value}>
				<span class="text-xs">{obj.name}</span>
				<!-- {#if !readonly}
					<div class="token-remove" title="Remove {s.name}">
						<svg
							class="icon-clear"
							xmlns="http://www.w3.org/2000/svg"
							width="18"
							height="18"
							viewBox="0 0 24 24"
						>
							<path d={iconClearPath} />
						</svg>
					</div>
				{/if} -->
			</div>
		{/each}
		<div class="actions">
			<div class="remove-all" title="Remove All" class:hidden={!Object.keys(selected).length}>
				<Icon src={FiXCircle} className="text-[#2a4a51] h-[26px] w-[26px]" />
			</div>
			{#if !readonly}
				<input
					class="bg-transparent"
					{id}
					autocomplete="off"
					bind:value={inputValue}
					bind:this={input}
					on:keyup={handleKeyup}
					on:blur={handleBlur}
					{placeholder}
				/>
			{/if}
		</div>
	</div>

	<select bind:this={slot} multiple class="hidden"><slot /></select>

	{#if showOptions}
		<ul
			class="options"
			transition:fly={{ duration: 200, y: 5 }}
			on:mousedown|preventDefault={handleOptionMousedown}
		>
			{#each filtered as option}
				<li
					class:selected={selected[option.value]}
					class:active={activeOption === option}
					data-value={option.value}
				>
					{option.name}
				</li>
			{/each}
		</ul>
	{/if}
</div>

<style>
	.multiselect {
		/* background-color: white; */
		border-bottom: 1px solid hsl(0, 0%, 70%);
		position: relative;
		margin-bottom: 18px;
	}
	.multiselect:not(.readonly):hover {
		border-bottom-color: hsl(0, 0%, 50%);
	}

	.tokens {
		align-items: center;
		display: flex;
		/* flex-wrap: wrap; */
		position: relative;
		padding-bottom: 7px;
	}
	.tokens::after {
		background: none repeat scroll 0 0 transparent;
		bottom: -1px;
		content: '';
		display: block;
		height: 2px;
		left: 50%;
		position: absolute;
		background: hsl(45, 100%, 51%);
		transition: width 0.3s ease 0s, left 0.3s ease 0s;

		width: 0;
	}
	.tokens.showOptions::after {
		width: 100%;
		left: 0;
	}
	.token {
		align-items: center;
		background-color: linear-gradient(0deg, rgba(130, 195, 208, 0.1), rgba(130, 195, 208, 0.1)),
			#ffffff;
		display: flex;
		margin: 0.25rem 0.5rem 0.25rem 0;
		max-height: 1.3rem;
		padding: 0.25rem 0.5rem 0.25rem 0.5rem;
		transition: background-color 0.3s;
		white-space: nowrap;
		border-radius: 5px;

		border: 1px solid #82c3d0;
		color: #82c3d0;
	}
	.token2 {
		align-items: center;
		background-color: llinear-gradient(0deg, rgba(247, 147, 31, 0.1), rgba(247, 147, 31, 0.1)),
			#ffffff;
		display: flex;
		margin: 0.25rem 0.5rem 0.25rem 0;
		max-height: 1.3rem;
		padding: 0.25rem 0.5rem 0.25rem 0.5rem;
		transition: background-color 0.3s;
		white-space: nowrap;
		border-radius: 5px;
		border: 1px solid #f7931f;
		color: #f7931f;
	}
	.token:hover {
		background-color: hsl(214, 15%, 88%);
	}
	.readonly .token {
		color: hsl(0, 0%, 40%);
	}
	/* .token-remove, */
	.remove-all {
		position: absolute;
		bottom: 111%;
		left: 84%;
		color: #2a4a51;
		align-items: center;
		/* background-color: hsl(214, 15%, 55%); */
		border-radius: 50%;
		color: hsl(214, 17%, 92%);
		display: flex;
		justify-content: center;
		height: 1.25rem;
		margin-left: 0.25rem;
		min-width: 1.25rem;
	}
	/* .token-remove:hover, */

	.remove-all:hover {
		/* background-color: hsl(215, 21%, 43%); */
		color: #2a4a51;
		cursor: pointer;
	}

	.actions {
		align-items: center;
		display: flex;
		flex: 1;
		/* min-width: 15rem; */
	}

	input {
		border: none;
		font-size: 1.5rem;
		line-height: 1.5rem;
		margin: 0;
		outline: none;
		padding: 0;
		width: 100%;
	}

	/* .dropdown-arrow path {
		fill: hsl(0, 0%, 70%);
	}
	.multiselect:hover .dropdown-arrow path {
		fill: hsl(0, 0%, 50%);
	}

	.icon-clear path {
		fill: white;
	} */

	.options {
		box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1), 0px -2px 4px rgba(0, 0, 0, 0.1);

		left: 0;
		list-style: none;
		z-index: 999;
		margin-block-end: 0;
		margin-block-start: 0;
		max-height: 70vh;
		overflow: auto;
		padding-inline-start: 0;
		position: absolute;
		top: calc(100% + 1px);
		width: 100%;
	}
	li {
		background-color: white;
		cursor: pointer;
		padding: 0.5rem;
	}
	li:last-child {
		border-bottom-left-radius: 0.2rem;
		border-bottom-right-radius: 0.2rem;
	}
	li:not(.selected):hover {
		background-color: hsl(214, 17%, 92%);
	}
	li.selected {
		background-color: #82c3d0;
		color: white;
	}
	li[data-value='menace'].selected {
		background-color: #f7931f;
		color: white;
	}
	li.selected:nth-child(even) {
		background-color: #82c3d0;
		color: white;
	}
	li.active {
		background-color: hsl(214, 17%, 88%);
	}
	li.selected.active,
	li.selected:hover {
		background-color: #197182;
	}
	li[data-value='menace'].selected:hover {
		background-color: #f7931f;
	}

	.hidden {
		display: none;
	}
</style>
