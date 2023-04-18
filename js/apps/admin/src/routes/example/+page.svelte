<script context="module" lang="ts">
	import { GraphQLClient } from 'graphql-request';
	import {
		GetUsersDocument,
		type GetUsersQuery,
		type GetUsersQueryVariables,
		type User
	} from '../../lib/generated/graphql';

	// Load users data from the GraphQL API
	export const loadUsers = async () => {
		const client = new GraphQLClient('https://admin.preview.safebear.ai/graphql');

		const { users } = (await client.request<GetUsersQuery, GetUsersQueryVariables>(
			GetUsersDocument
		)) as { users: User[] };

		return { props: { users } };
	};
</script>

<script lang="ts">
	import { onMount } from 'svelte';

	export let users: User[] = [];

	onMount(async () => {
		const data = await loadUsers();
		users = data.props.users;
	});
</script>

<h1 class="text-3xl font-bold">Example Page - Users</h1>
<pre>{JSON.stringify(users, null, 2)}</pre>
