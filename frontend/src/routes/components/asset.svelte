<script>
    import { goto } from '$app/navigation';

    export let asset;
    export let username;
    export let password;
    export let slug;

    function del() {
        const token = btoa(username + ":" + password);
        document.getElementById("loading").style.display = "block";
        fetch(
            "http://198.211.109.211:8000/asset/delete",
            {
                
                method: "POST",
                headers: {
                    Authorization: `Basic ${token}`,
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    id: asset.id
                })
            }
        ).then((e) => {
            goto("/auth/projects/" + slug)
            document.getElementById("loading").style.display = "none";
        })
    }
</script>

<div href={"/auth/assets/" + asset.id} id={asset.id} class="asset">
    <img alt="" src={"http://198.211.109.211:8000/images/" + asset.path} />
    <div class="input_cont">
        <div class="asset_param">Character:</div>
        <div>{asset.entity_name}</div>
    </div>
    <button on:click={del}>Delete</button>
</div>

<style>
    @import url('https://fonts.googleapis.com/css?family=Poppins:400,500,600,700&display=swap');
    .asset {
        border: none;
        outline: none;
        font-family: Poppins, sans-serif;
        display: flex;
        flex-direction: column;
        justify-items: center;
        align-items: center;
        background-color: rgb(220, 220, 220);
        text-decoration: none;
        padding: 20px;
        margin: 15px;
        color: black;
        border-radius: 10px;
        transition: all 0.5s;
        height: 40vw;
        width: 30vw;
    }

    .asset:hover {
        color: rgb(39, 39, 39);
        background-color: rgb(195, 195, 195);
    }

    .asset_param {
        text-align: center;
        font-size: 15px;
    }

    .asset img {
        width: 80%;
        height: 50%;
        margin: 10px;
    }

    .asset button {
        background-color: rgb(80, 80, 196);
        border: none;
        border-radius: 5px;
        margin: 20px;
        padding: 10px;
        color: white;
    }

    .input_cont {
        margin: 10px;
    }
</style>