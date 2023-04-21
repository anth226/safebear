/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
 
    return {
      adminId: params.admin,
    }
}