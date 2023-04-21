/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
 
    return {
      userId: params.utilisateur,
    }
}