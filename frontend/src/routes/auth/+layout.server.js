import { redirect } from '@sveltejs/kit';
export async function load({ cookies, fetch }) {
    const username = cookies.get("username");
    const password = cookies.get("password");

    if (username === undefined || password === undefined) throw redirect(302, "/login");

    const res = await fetch("http://127.0.0.1:8000/auth/basic-auth/", {
        
        headers: {
            Authorization: `Basic ${btoa(username + ":" + password)}`
        }
    });

    if (!res.ok) throw redirect(302, "/login");

    return {
        username: username,
        password: password
    }
}