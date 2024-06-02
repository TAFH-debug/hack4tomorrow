import { redirect } from '@sveltejs/kit';
export async function load({ params, cookies }) {
    const id = params.slug;

    const token = btoa(cookies.get('username') + ":" + cookies.get("password"));
    const res = await fetch("http://127.0.0.1:8000/project/get_by_id/", {
        
        method: "POST",
        headers: {
            Authorization: `Basic ${token}`,
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            id: id
        })
    })

    if(!res.ok) throw redirect(302, "/auth/dashboard");

    return await res.json()
}