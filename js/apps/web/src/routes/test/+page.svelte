<script>
	import { request, gql } from 'graphql-request';
	import { onMount } from 'svelte';

	/**
	 * @type {{ countries: any; }}
	 */
	let data;
	const endpoint = 'https://countries.trevorblades.com/';
	const query = `
		{
			countries {
				name
				emoji
			}
		}
	`;

	onMount(async () => {
		// data = await request(endpoint, query);
		submit();
	});

	const submit = async () => {
		const resp = await fetch(endpoint, {
			method: 'post',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ query })
		});

		data = await resp.json();
		data = data.data;
	};
</script>

{#if data}
	<h1>result:</h1>
	<ul>
		{#each data.countries as c}
			<li>{c.name} - ({c.emoji})</li>
		{/each}
	</ul>
{:else}
	<p>Loading result...</p>
{/if}
