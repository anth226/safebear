<script lang="ts">
	import { each } from "svelte/internal";

    let history = [
        {
            message: "Toi tu vas voir...",
            labels: ["Menace", "Insultes", "Racisme"],
            status: "Yes"
        },
        {
            message: "Espèce de ...",
            labels: ["Menace", "Insultes", "Racisme"],
            status: "I don't know"
        },
        {
            message: "Espèce de ...",
            labels: ["Racisme"],
            status: "I don't know"
        },
        {
            message: "Espèce de ...",
            labels: ["Menace", "Insultes", "Racisme"],
            status: "No"
        },
    ]
    const setImg = (status:string) =>{
        if(status == "Yes"){
            return "labellisation/h-tick.svg"
        }else if(status == "No"){
            return "labellisation/h-cross.svg"
        }else{
            return "labellisation/h-idk.svg"
        }
    }
</script>

<svelte:head>
    <title>Labellisation</title>
</svelte:head>
<div class="flex flex-col gap-8">
    <h2 class="font-medium text-black text-2xl">Labellisation</h2>
    <div class="w-full flex gap-20">
        <div class="flex flex-col gap-2">
            <h4 class="font-medium text-black text-lg">Historique:</h4>
            <div class="flex flex-col gap-5">
                {#each history as item }
                <div class="flex flex-col gap-1">
                    <div class="flex justify-between">
                        <span class="text-lg text-dark-green">Toi tu vas voir...</span>
                        <div class="w-[26px] h-[26px] rounded-full border-[3px] border-dark-green flex items-center justify-center">
                            <img class=" self-center" src={setImg(item.status)} alt="">
                        </div>
                    </div>
                    <div class="flex gap-1">
                        {#each item.labels as label}
                        <p class={`px-3 pb-1  border rounded-[5px] ${label == "Menace" ? "border-orange bg-gradient-to-r from-primary to-primary" : "border-blue-less bg-blue-less bg-opacity-10"} `}>
                            <span class={`${ label == "Menace" ? "text-orange" : "text-blue-less"} text-[10px] font-semibold`}>{label}</span>
                        </p>
                        {/each}
                    </div>
                    <hr class="border-silver-hr mt-2">
                </div>
                {/each}
            </div>
        </div>
        <div class="flex flex-col gap-4">
            <div class="bg-silver-hr bg-opacity-10 py-6 px-4 rounded-[14px] min-w-[700px] shadow-label">
                <span class="text-black font-medium">Contenu labellisé comme :</span>
                <span class="px-6 py-2 text-blue-2 bg-blue-2 bg-opacity-30 rounded-lg">Insultes</span>
            </div>
            <div class="rounded-[14px] border-2 border-hr flex flex-col px-4 py-3 shadow-label bg-white">
                <span class="text-silver-hr">Message:</span>
                <textarea value="Dis donc sale **** tu réponds plus à mes messages ? T’as fait comme ton père c’est ça tu t’es barré ! Espèce de singe" class="focus:outline-none" name="" id="" cols="30" rows="6"></textarea>
            </div>
            <div class="flex items-center justify-center gap-4">
                <div class="flex flex-col gap-3">
                    <span class="self-center">Oui</span>
                    <img class="cursor-pointer" src="labellisation/tick.svg" alt="">
                    <span class="px-2  bg-silver-hr bg-opacity-50 text-center rounded-[10px] self-center -mt-16">A</span>
                </div>
                <div class="flex flex-col gap-3">
                    <span class="self-center">Oui</span>
                    <img class="cursor-pointer" src="labellisation/cross.svg" alt="">
                    <span class="px-2  bg-silver-hr bg-opacity-50 text-center rounded-[10px] self-center -mt-16">X</span>
                </div>
                <div class="flex flex-col gap-3">
                    <span class="self-center">Oui</span>
                    <img class="cursor-pointer" src="labellisation/idk.svg" alt="">
                    <span class="px-2  bg-silver-hr bg-opacity-50 text-center rounded-[10px] self-center -mt-16">Space</span>
                </div>
            </div>
        </div>
    </div>
</div>