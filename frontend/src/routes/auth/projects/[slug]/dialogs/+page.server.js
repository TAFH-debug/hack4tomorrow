export async function load({ fetch, cookies, params }) {
    const data = btoa(cookies.get('username') + ":" + cookies.get('password'));

    const res = await fetch("http://127.0.0.1:8000/dialog/get_all/", {
        
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

    const entities = await fetch("http://127.0.0.1:8000/character/get_all/", {
        
        method: "POST",
        headers: {
            Authorization: `Basic ${data}`,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id: parseInt(params.slug),
        })
    }).then((res) => res.json())

    res.forEach((i) => {
        i.character1 = entities.filter((val) => val.id == i.character1_id)[0].name;
        i.character2 = entities.filter((val) => val.id == i.character2_id)[0].name;
    });

    return {
        dialogs: res,
        entities: entities
    }
}