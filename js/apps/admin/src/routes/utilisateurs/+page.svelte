<script lang="ts">
	import { page } from "$app/stores";
	import type { IUser } from "$lib/types";
    import { data } from "./data";

    const pageSize = 7
    let users = data
    let pageData: IUser[] = []
    let links: number[] = []
    let currentPage = 1
    let selected: number[] = []
    let search = ""
    $: users = data.filter(user => user.name.toLowerCase().includes(search.toLowerCase()))
    function changePage(pageNumber: number){
        currentPage = pageNumber
        selected  = []
        displayPage(pageNumber)
    }
    function selectAll(){
        if(selected.length ==  pageData.length){
            selected = []
            return
        }
        selected = pageData.map(user => user.id)
    }
    function addToSelected(id: number){
        if(selected.includes(id)){
            selected = selected.filter(item => item != id)
        }else{
            selected = [...selected, id]
        }
    }

    function displayPage(pageNumber: number) {
        const startIndex = (pageNumber - 1) * pageSize;
        const endIndex = startIndex + pageSize;
        pageData = users.slice(startIndex, endIndex);
    }
    function generatePaginationLinks() {
        links=[]
        const totalPages = Math.ceil(users.length / pageSize)
        for (let i = 1; i <= totalPages; i++) {
            links = [...links, i]
        }
    }
    $: {
        if(users){
        displayPage(currentPage)
        generatePaginationLinks()
        console.log("changed")
    }
    }
    displayPage(1);
    generatePaginationLinks();
</script>
<svelte:head>
    <title>Utilisateurs - Safebear</title>
</svelte:head>
<div class="flex flex-col gap-6 -mt-12">
    <div class="relative w-1/3">
        <img class="absolute top-2 left-2" src="util/search.svg" alt="">
        <input bind:value={search} type="text" class="py-2 pl-10 w-full border border-silver-300 rounded-[3px] bg-white placeholder:text-silver-300 focus:outline-none" placeholder="Rechercher un utilisateur">
    </div>
    <div class="flex justify-between">
        <h1 class="text-2xl">Utilisateurs</h1>
        <div class="flex gap-3 bg-white px-3 rounded-lg cursor-pointer">
            <img class="cursor-pointer" src="util/filter.svg" alt="">
            <span class="font-medium text-sm self-center">Filter</span>
        </div>
    </div>
    {#if selected.length > 0 && pageData.length != 0}
    <div class="bg-blue-vert bg-opacity-20 py-4 rounded-[3px] w-full flex gap-5 px-6">
        <div class="flex gap-2 cursor-pointer">
            <img src="util/delete.svg" alt="">
            <span class="text-blue-vert font-medium underline">Supprimer le compte</span>
        </div>
        <div class="flex gap-2 cursor-pointer">
            <img src="util/deactivate.svg" alt="">
            <span class="text-blue-vert font-medium underline">Désactiver le compte</span>
        </div>
    </div>
    {/if}
    <div class="bg-white rounded-[3px] px-0.5" class:-mt-4={selected.length > 0}>
        <div class="flex border-b border-[#F2F2F2] py-5 px-0.5">
            <div class="flex w-full gap-3 px-4">
                <!-- svelte-ignore a11y-click-events-have-key-events -->
                <div 
                    class="w-5 h-5 cursor-pointer rounded-[7px] border flex items-center justify-center"
                    class:bg-blue-vert={selected.length==pageData.length && pageData.length != 0}
                    class:border-blue-vert={selected.length==pageData.length && pageData.length != 0}
                    class:border-silver-300={selected.length!=pageData.length || pageData.length == 0}
                    on:click={selectAll}
                >
                {#if selected.length==pageData.length}
                    <img src="util/tick.svg" alt="">
                {/if}
                </div>
                <h4 class="font-semibold self-center font-lato">Utilisateur</h4>
            </div>
            <div class="flex w-full gap-3 px-4"> 
                <h4 class="font-semibold self-center font-lato">Date</h4>
                <div class="py-1 px-1 shadow-out rounded-[4px] cursor-pointer">
                    <img src="util/double-direction.svg" alt="">
                </div>
            </div>
            <div class="flex w-full gap-3 px-4"> 
                <h4 class="font-semibold self-center font-lato">Statut</h4>
            </div>
            <div class="flex w-full gap-3 px-4"> 
                <h4 class="font-semibold self-center font-lato">Formule souscrite</h4>
            </div>
            <div class="flex w-full gap-3 px-4"> 
                <h4 class="font-semibold self-center font-lato pl-10">KYC</h4>
            </div>
            <div class="flex w-full gap-3 px-4"> 
                <h4 class="font-semibold self-center font-lato">Compte lié</h4>
            </div>
        </div>
        {#each pageData as user}
            <div class="flex border-b border-[#F2F2F2] py-5 px-0.5"
                class:bg-inactive={user.status=="Désactivé"}
                class:opacity-60={user.status=="Désactivé"}
                >
                <div class="flex w-full gap-3 px-4">
                    <!-- svelte-ignore a11y-click-events-have-key-events -->
                    <div 
                    class="w-5 h-5 cursor-pointer rounded-[7px] border flex items-center justify-center"
                    class:bg-blue-vert={selected.includes(user.id)}
                    class:border-blue-vert={selected.includes(user.id)}
                    class:border-silver-300={!selected.includes(user.id)}
                    on:click={()=>{addToSelected(user.id)}}
                    >
                    {#if selected.includes(user.id)}
                        <img src="util/tick.svg" alt="">
                    {/if}
                    </div>
                    <h4 class="self-center underline text-blue-vert font-medium">{user.name}</h4>
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
                    class="rounded-[31px] flex gap-2 px-1 pr-2 py-0.5"
                    class:bg-[#33B35E]={user.kyc=="Complété"}
                    class:bg-[#F49817]={user.kyc=="En attente"}
                    >
                        <img class:hidden={user.kyc!="Complété"} src="util/kyc-tick.svg" alt="">
                        <img class:hidden={user.kyc!="En attente"} src="util/kyc-dashed-circle.svg" alt="">
                        <h4 class="self-center text-white">{user.kyc}</h4>
                    </div>
                    
                </div>
                <div class="flex w-full gap-3 px-4"> 
                    <h4 class="self-center">{`${user.linked_accounts} compte lié${user.linked_accounts > 1 ? 's' : ''}`}</h4>
                </div>
            </div>
        {/each}
    </div>
    <div class="w-full flex justify-center gap-2">
        
        {#each links as link}
            <button class:text-blue-2={link==currentPage} class:underline={link==currentPage} class:font-semibold={link==currentPage} class="px-1 py-0.5 cursor-pointer" on:click={()=>{changePage(link)}}>{link}</button>
        {/each}
    </div>
</div>