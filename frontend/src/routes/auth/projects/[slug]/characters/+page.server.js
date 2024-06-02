export async function load({ fetch, cookies, params }) {
    const data = btoa(cookies.get('username') + ":" + cookies.get('password'));

    const res = await fetch("http://127.0.0.1:8000/character/get_all/", {
        
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            Authorization: `Basic ${data}`
        },
        body: JSON.stringify({
            id: parseInt(params.slug)
        })
    })
    .then((res) => res.json())

    return {
        characters: res
    }
}