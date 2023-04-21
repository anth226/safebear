<script>
	// import Nav from '../components/Nav.svelte';
	import { dev } from '$app/environment';
	import { page } from '$app/stores';

	const offline = typeof navigator !== 'undefined' && navigator.onLine === false;

	let message = offline ? 'Find the internet and try again' : $page.error?.message;

	let title = offline ? 'Offline' : $page.status;
	if ($page.status === 404) {
		title = 'Page non trouvée :(';
		message = 'Désolé! Si vous pensez que cette URL est cassée, veuillez nous en informer !';
	}
</script>

<svelte:head>
	<title>{title}</title>
</svelte:head>

<section class="container prose mx-auto p-16 dark:prose-invert bg-blue-2">
	<h1>{$page.status}: {title}</h1>
	<p class="font-lato">{message}</p>
	{#if dev && $page.error?.stack}
		<pre class="mono overflow-scroll bg-gray-800 p-8">{$page.error?.stack}</pre>
	{/if}
</section>

<style>
</style>
