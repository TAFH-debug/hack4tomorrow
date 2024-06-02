<script>
    import { goto } from '$app/navigation';

    export let concept_art;
    export let username;
    export let password;
    export let slug;
    export let entity_name;

    function del() {
        const token = btoa(username + ":" + password);
        fetch(
            "http://165.227.130.2:8000/concept_art/delete",
            {
                
                method: "POST",
                headers: {
                    Authorization: `Basic ${token}`,
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    id: concept_art.id
                })
            }
        ).then((e) => {
            goto("/auth/projects/" + slug)
            document.getElementById("loading").style.display = "none";
        })
    }
</script>

<div href={"/auth/concept_arts/" + concept_art.id} id={concept_art.id} class="concept_art">
    <img alt="" src={"http://165.227.130.2:8000/images/" + concept_art.image} />
    <div class="input_cont">
        <div class="concept_art_param">Entity:</div>
        <div>{entity_name}</div>
    </div>
    <button on:click={del}>Delete</button>
</div>

<style>
    @import url('https://fonts.googleapis.com/css?family=Poppins:400,500,600,700&display=swap');
    .concept_art {
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

    .concept_art:hover {
        color: rgb(39, 39, 39);
        background-color: rgb(195, 195, 195);
    }

    .concept_art_param {
        text-align: center;
        font-size: 15px;
    }

    .concept_art img {
        width: 80%;
        height: 50%;
        margin: 10px;
    }

    .concept_art button {
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