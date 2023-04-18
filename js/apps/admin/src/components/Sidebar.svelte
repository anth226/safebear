<script lang="ts">
    import { page } from "$app/stores";
    console.log($page.route.id)

    const sidebarItems = [
        {
            name: "Utilisateurs",
            icon: "util.svg",
            route: "/utilisateurs"
        },
        {
            name: "Labellisation",
            icon: "label.svg",
            route: "/labellisation"
        },
        {
            name: "Gestion admin",
            icon: "gestion.svg",
            route: "/gestion-admin"
        }
    ]
</script>
<div class="bg-white w-[16%] flex flex-col justify-between pt-8 pb-2">
    <div class="flex flex-col gap-10">
        <h1 class="text-dark-green text-2xl pl-10 font-medium cursor-pointer"><a href="/">Safebear Admin</a></h1>
        <div class="flex flex-col gap-2 cursor-pointer">
            {#each sidebarItems as item}
            <a href={item.route} 
                class="flex gap-5 pl-10 py-3"
                class:border-l-2={item.route==$page.route.id}
                class:border-blue-vert={item.route==$page.route.id}
            >
                <img src={`sidebar/${item.route==$page.route.id ? 'a-' : ''}${item.icon}`} alt="">
                <span
                    class:text-silver-200={item.route!=$page.route.id}
                    class:text-blue-vert={item.route==$page.route.id}
                    class:font-semibold={item.route==$page.route.id}
                    >{item.name}</span>
            </a>
            {/each}
        </div>
    </div>
    <div class="pl-10 cursor-pointer flex gap-3">
        <img src="sidebar/aid.svg" alt="aide">
        <h5 class="text-silver-200">Aide</h5>
    </div>
</div>