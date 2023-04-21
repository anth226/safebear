<script lang="ts">
    export let label = ""
    export let placeholder = ""
    export let value = ""
</script>

<div class="w-full flex flex-col">
    <span class="z-10 ml-4 bg-white -mb-4  pb-1 px-2 self-start">{label}</span>
    <input placeholder={placeholder} bind:value class="w-full py-2 pt-3 px-3 border border-[#B9B9B9] focus:outline-none rounded-[7px]" type="text">
</div>