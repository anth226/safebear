<script>
	import Sidebar from '../components/Sidebar.svelte';
	import '../tailwind.css';
</script>

<main class="bg-silver min-h-screen flex gap-0">
	<Sidebar/>
	<div class="flex-1">
	<slot />
	</div>
</main>
