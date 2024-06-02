export async function load({ fetch, cookies }) {
    const data = btoa(cookies.get('username') + ":" + cookies.get('password'));

    const res = await fetch("http://127.0.0.1:8000/project/get_projects/", {
        
        headers: {
            Authorization: `Basic ${data}`
        }
    })
    .then((res) => res.json());

    return {
        projects: res
    }
}