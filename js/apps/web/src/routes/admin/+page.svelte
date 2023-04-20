<script>
	import Sidebar1 from './sidebar1.svelte';
	import Sidebar2 from './sidebar2.svelte';
	import MainArea from './main_area.svelte';

	import { request, GraphQLClient } from 'graphql-request';
	import { onMount } from 'svelte';

	// const client = new GraphQLClient('https://admin.preview.safebear.ai/data-model');
	onMount(async () => {
		// 	const query = `
		// 	{
		// 		users(id: "") {
		// 			releaseDate
		// 			actors {
		// 				name
		// 			}
		// 		}
		// 	}
		// `;
		// request('https://api.graph.cool/simple/v1/movies', query).then((data) => console.log(data));
		// const response = await client.request(query);
		// console.log(response);
		fetchData();
	});

	let data;

	async function fetchData() {
		const endpoint = 'https://admin.preview.safebear.ai/data-model';
		const query = `
      query {
        users {
          id
          name
          email
        }
      }
    `;
		const client = new GraphQLClient(endpoint);
		const result = await client.request(query);
		data = result.data;
		console.log(data);
	}
</script>

<section>
	<Sidebar1 />

	<div class="main_area">
		<div class="top">
			<img src="/logo.png" alt="logo" />
		</div>
		<div class="bottom">
			<Sidebar2 />
			<MainArea />
		</div>
	</div>
</section>

<style>
	section {
		display: flex;
		height: 100vh;
	}

	.main_area {
		display: flex;
		flex-direction: column;
		background-color: #f8f8f8;
		width: 100%;
	}
	.top {
		display: flex;
		justify-content: flex-end;

		height: 140px;
		padding: 40px;
	}
	img {
		width: 52px;
		height: 52px;
	}
	.bottom {
		display: flex;
		height: 100%;
	}
</style>
