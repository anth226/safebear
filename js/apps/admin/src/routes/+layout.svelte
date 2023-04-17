<script>
	import Sidebar from '../components/Sidebar.svelte';
	import '../tailwind.css';
</script>

<main class="bg-silver min-h-screen flex gap-0">
	<Sidebar/>
	<div class="flex-1 px-8">
		<div class="w-full flex justify-end">
			<img class="py-6 pr-3 pb-4" src="favicon.png" alt="">
		</div>
		<slot />
	</div>
</main>
