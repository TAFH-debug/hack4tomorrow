export async function load ({ params, cookies, fetch }) {
    const token = btoa(cookies.get('username') + ":" + cookies.get("password"))

    const res = await fetch(
        "http://127.0.0.1:8000/dialog/get_messages/",
        {
            
            method: "POST",
            headers: {
                Authorization: `Basic ${token}`,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id: parseInt(params.num)
            })
        }
    ).then((res) => res.json());

    return {
        num: params.num,
        messages: res
    }
}