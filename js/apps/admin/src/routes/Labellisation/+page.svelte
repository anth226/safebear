<script lang="ts">
	import MultiSelect from '../../Components/MultiSelect/MultiSelect.svelte';
	// import SideBar from '../../Components/SideBar/SideBar.svelte';
	let value: any;
	function onKeyDown(e: any) {
		if (e.keyCode === 65) {
			console.log('A');
		} else if (e.keyCode === 88) {
			console.log('X');
		} else if (e.keyCode === 32) {
			console.log('Space');
		}
	}
	function labellisationAction(type: number) {
		if (type === 65) {
			console.log('A');
		} else if (type === 88) {
			console.log('X');
		} else if (type === 32) {
			console.log('Space');
		}
	}
</script>

<svelte:window on:keydown|preventDefault={onKeyDown} />
<!-- <SideBar /> -->

<div class="mt-[152px] ml-[40px] flex w-full flex-col">
	<img src="/Profile Avtar.svg" alt="" class="absolute top-[10%] left-[94%]" />
	<h1 class="text-2xl font-medium leading-9">Labellisation</h1>
	<div class="mt-[58px] flex">
		<div class="flex  h-[200px] w-[200px] flex-col  ">
			<span class="mb-[7px] text-lg"> Historique : </span>

			<MultiSelect id="lang" bind:value label="Toi tu vas voir...">
				<option value="menace">Menace</option>
				<option value="insultes">Insultes</option>
				<option value="racisme">Racisme</option>
			</MultiSelect>
			<MultiSelect id="lang" bind:value label="Espèce de ......">
				<option value="menace">Menace</option>
				<option value="insultes">Insultes</option>
				<option value="racisme">Racisme</option>
			</MultiSelect>
			<MultiSelect id="lang" bind:value label="Espèce de ......">
				<option value="racisme">Racisme</option>
			</MultiSelect>
			<MultiSelect id="lang" bind:value label="Espèce de ......">
				<option value="menace">Menace</option>
				<option value="insultes">Insultes</option>
				<option value="racisme">Racisme</option>
			</MultiSelect>
			<!-- {#if value && value.length}
				<ul>
					{#each value as val}
						<li>
							{val}
						</li>
					{/each}
				</ul>
			{:else}
				<div>Nothing selected</div>
			{/if} -->
		</div>
		<div class="flex w-full justify-center">
			<div class=" mr-[120px] ml-[120px] w-[674px]  flex-col ">
				<div
					class="mb-[18px] flex h-[82px] items-center rounded-2xl bg-[#a7a7a71a] pl-[27px]"
					style="box-shadow:0px 56px 37px -32px rgba(42, 74, 81, 0.18)"
				>
					Contenu labellisé comme :
				</div>
				<div
					class="mb-[75px] flex h-[200px] w-[674px] flex-col rounded-3xl border-2 border-solid border-[#A7A7A7] bg-white pt-[20px] pl-[27px] pb-[20px]"
					style="box-shadow: 0px 56px 37px -32px rgba(42, 74, 81, 0.18)"
				>
					<span class="text-base text-[#A7A7A7] "> Message: </span>
					<span class="text-lg">
						Dis donc sale **** tu réponds plus à mes messages ? T’as fait<br /> comme ton père c’est
						ça tu t’es barré ! Espèce de singe
					</span>
				</div>
				<div class="relative flex justify-center">
					<div class="flex flex-col items-center">
						<span class="mb-[8px]">Oui</span>
						<!-- svelte-ignore a11y-click-events-have-key-events -->
						<img
							src="/yes.svg"
							class="h-[190px] w-[130px] hover:cursor-pointer"
							alt=""
							on:click={() => {
								labellisationAction(65);
							}}
						/>
						<span
							class=" absolute bottom-[9%] flex h-[36px] w-[40px] items-center justify-center rounded-lg bg-[#a7a7a780] pl-[14px] pr-[14px]  text-base font-semibold text-[#2A4A51]"
							>A</span
						>
					</div>
					<div class="relative ml-[20px] mr-[20px] flex  flex-col items-center">
						<span class="mb-[8px]">Non</span>
						<!-- svelte-ignore a11y-click-events-have-key-events -->
						<div
							class="relative  hover:cursor-pointer"
							on:click={() => {
								labellisationAction(88);
							}}
						>
							<img src="/no.svg" class=" h-[190px] w-[130px] " alt="" />
							<img src="/red-cross.svg" class=" absolute top-[47px] left-[46px] h-[40px]" alt="" />
						</div>

						<span
							class=" absolute bottom-[9%] flex h-[36px] w-[40px] items-center justify-center rounded-lg bg-[#a7a7a780]  pl-[14px] pr-[14px] text-base font-semibold text-[#2A4A51]"
							>X</span
						>
					</div>
					<div class="relative flex flex-col items-center">
						<span class="mb-[8px]">Je ne sais pas</span>
						<!-- svelte-ignore a11y-click-events-have-key-events -->
						<div
							class="relative  hover:cursor-pointer"
							on:click={() => {
								labellisationAction(32);
							}}
						>
							<img src="/idw1.svg" class=" h-[190px] w-[130px]" alt="" />
							<img src="/idw2.svg" class=" absolute top-[40px] left-[39px] h-[53px]" alt="" />
							<img src="/idw3.svg" class=" absolute top-[46px] left-[49px] h-[38px]" alt="" />
						</div>

						<span
							class="absolute bottom-[9%] flex h-[36px] w-[80px] items-center justify-center rounded-lg bg-[#a7a7a780] pl-[14px] pr-[14px] text-base font-semibold text-[#2A4A51] "
							>Space</span
						>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
