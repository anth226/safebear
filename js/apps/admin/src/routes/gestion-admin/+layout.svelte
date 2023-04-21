<script lang="ts">
    import { search } from "../../store/search";
</script>
<svelte:head>
    <title>Gestion des admins - Safebear</title>
</svelte:head>
<div class="flex flex-col gap-6 -mt-12">
    <div class="relative w-1/3">
        <img class="absolute top-2 left-2" src="/util/search.svg" alt="">
        <input bind:value={$search} type="text" class="py-2 pl-10 w-full border border-silver-300 rounded-[3px] bg-white placeholder:text-silver-300 focus:outline-none" placeholder="Rechercher un utilisateur">
    </div>

    
    
    <slot />
</div>
